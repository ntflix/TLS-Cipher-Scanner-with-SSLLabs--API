import re


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
