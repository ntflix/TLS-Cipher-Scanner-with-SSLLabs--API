import asyncio
from TLSScan import scan_with_ssllabs
from TLSScan.helpers import get_hosts

OUTPUT_FILENAME = "Output/tlsscan.csv"


def get_list_of_hosts():
    hosts_filename = "masterurl.csv"
    return get_hosts(hosts_filename)


def run_scan():
    hosts = get_list_of_hosts()
    asyncio.run(
        scan_with_ssllabs.scan_and_output(hosts, output_filename=OUTPUT_FILENAME)
    )


if __name__ == "__main__":
    run_scan()
