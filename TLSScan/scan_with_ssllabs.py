from typing import Coroutine
from TLSScan.endpoint_suites_data import EndpointProtocolSuitesData
from TLSScan.scanner_framework import scan_host
from ssllabs.data.host import HostData
import asyncio


async def scan_and_output(hosts: list[str], output_filename: str) -> None:
    semaphore = asyncio.Semaphore(2)
    write_csv_headers(output_filename)

    async def sem_scan_host(host: str):
        async with semaphore:
            result = await scan_host(host)
            assert result.host
            output_csv(result, host, output_filename)
            await asyncio.sleep(1)  # Add a 1-second delay between starting each task

    tasks: list[Coroutine[None, None, None]] = []
    for host in hosts:
        tasks.append(sem_scan_host(host))
        # await asyncio.sleep(1)  # Add a 1-second delay between starting each task

    await asyncio.gather(*tasks)
    print(
        (
            f"CSV output to {output_filename} complete. "
            "See https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#endpointdetails "
            "for more information on the headers and their meanings."
        )
    )


def output_csv(result: HostData, original_hostname: str, output_filename: str) -> None:
    assert result.endpoints
    endpointsProtocolSuitesData: list[EndpointProtocolSuitesData] = []

    for endpoint in result.endpoints:
        endpointProtocolSuitesData: EndpointProtocolSuitesData | None = None

        try:
            endpointProtocolSuitesData = EndpointProtocolSuitesData.from_endpoint(
                endpoint
            )
        except ValueError:
            print(
                f"Error parsing endpoint {endpoint.ipAddress} - {endpoint.statusMessage} - {endpoint.statusDetailsMessage}"
            )
            continue
        if endpointProtocolSuitesData:
            endpointsProtocolSuitesData.append(endpointProtocolSuitesData)

    with open(output_filename, "a") as f:
        for i, endpointProtocolSuitesData in enumerate(endpointsProtocolSuitesData):
            csv_lines = endpointProtocolSuitesData.csv()
            for line in csv_lines:
                line = [original_hostname] + line
                # add the actual host name from result to the csv_lines
                f.write(",".join(line) + "\n")
            print(
                f"Wrote {result.endpoints[i].serverName} results to `{output_filename}` for {result.host}"
            )


def write_csv_headers(output_filename: str) -> None:
    with open(output_filename, "w") as f:
        headers = EndpointProtocolSuitesData.csv_headers()
        headers = ["Original Host"] + headers
        f.write(",".join(headers) + "\n")
