from typing import AsyncGenerator
from TLSScan.tlsscan_ssllabs import analyze
from ssllabs.data.host import HostData
import asyncio


async def scan_host(host: str) -> HostData:
    ready = False
    results: HostData | None = None
    total_sleep = 0

    while not ready:
        results = await analyze(host)
        status = results.status
        await asyncio.sleep(5)
        if status == "READY":
            ready = True
            print(f"Scan complete for {host}.")
        else:
            if total_sleep >= 500:
                raise TimeoutError(
                    (
                        f"Timeout after {total_sleep} seconds on {host}"
                        f"Status of the scan is {status}"
                    )
                )
            elif total_sleep == 0:
                print(f"Began scanning {host}. Waiting for results...")
            elif status == "ERROR":
                print(f"Scan on {host} encountered an error.")
                # cancel the scan
                raise Exception(f"Scan on {host} encountered an error.")
            elif status == "IN_PROGRESS":
                print(f"Status of scan on {host} is {status}. Waiting for results...")
            elif status == "DNS":
                print(f"Status of scan on {host} is {status}. Waiting for results...")
            else:
                print(f"Status of scan on {host} is unknown - {status}.")
                raise Exception(f"Status of scan on {host} is unknown - {status}.")
            total_sleep += 5
            await asyncio.sleep(5)

    assert results is not None
    assert results.status == "READY"
    return results


async def scan_hosts(hosts: list[str]) -> AsyncGenerator[tuple[HostData, str], None]:
    results: list[HostData] = []
    for host in hosts:
        try:
            result: HostData = await scan_host(host)
            yield (result, host)
            results.append(result)
        except TimeoutError:
            print(f"Timeout error scanning {host}")
        except Exception as e:
            print(f"Error scanning {host}: {e}")
