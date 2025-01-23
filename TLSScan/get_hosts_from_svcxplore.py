import requests
import json


SVCXPLORE_BASE_URL = "http://10.244.69.163/api/interfaces"


def get_hosts_from_svcxplore():
    domains: list[str] = []

    response = requests.get(SVCXPLORE_BASE_URL)
    if response.status_code == 200:
        interfaces = json.loads(response.text)
        for interface in interfaces:
            interface: str
            try:
                interface: str = interface["url"]
            except KeyError:
                pass
            domains.append(interface)
    else:
        print(f"Failed to get hosts from svcxplore: {response.text}")

    return domains
