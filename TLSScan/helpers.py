import re
import requests
import json
import ipaddress


SVCXPLORE_BASE_URL = "http://10.244.69.163/api/interfaces"


def get_hosts_from_svcxplore():
    domains: list[str] = []

    response = requests.get(SVCXPLORE_BASE_URL)
    if response.status_code == 200:
        interfaces = json.loads(response.text)
        for interface in interfaces:
            interface: str
            try:
                interface: str = interface["url"]  # type: ignore
            except KeyError:
                pass
            domains.append(interface)
    else:
        print(f"Failed to get hosts from svcxplore: {response.text}")

    domains = [get_domain_only(domain) for domain in domains]
    domains = list(set(domains))  # Remove duplicates
    domains = [domain for domain in domains if not is_ip(domain)]  # Remove IPs

    return domains


def is_ip(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def get_domain_only(host: str) -> str:
    # remove protocol, ://, any path, and any port
    host = host.strip()
    host = re.sub(r"https?://", "", host)
    host = re.sub(r"/.*", "", host)
    host = re.sub(r":\d+", "", host)
    return host


def get_hosts(from_path: str) -> list[str]:
    with open(from_path) as f:
        hosts = f.readlines()
    hosts: list[str] = [host for host in hosts if host.startswith("#") is False]
    hosts = [get_domain_only(host) for host in hosts]
    hosts = list(set(hosts))  # Remove duplicates
    return hosts
