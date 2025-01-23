import asyncio
from TLSScan import scan_with_ssllabs
from TLSScan.helpers import get_hosts, get_hosts_from_svcxplore

OUTPUT_FILENAME = "Output/tlsscan_new.csv"


def get_list_of_hosts():
    hosts_filename = "masterurl.csv"

    hosts_from_file: list[str] = get_hosts(hosts_filename)
    # disable if you don't have access to svcxplore:
    hosts_from_svcxplore: list[str] = get_hosts_from_svcxplore()

    hosts = hosts_from_file + hosts_from_svcxplore

    return hosts


def run_scan():
    hosts = get_list_of_hosts()
    asyncio.run(
        scan_with_ssllabs.scan_and_output(hosts, output_filename=OUTPUT_FILENAME)
    )


if __name__ == "__main__":
    run_scan()
