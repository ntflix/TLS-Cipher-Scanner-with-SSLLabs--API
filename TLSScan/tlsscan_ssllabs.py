import socket
from ssllabs.api import Endpoint, Analyze
from ssllabs.data.host import HostData
from ssllabs.data.endpoint import EndpointData


def get_ip_from_host(host: str) -> str:
    ip = socket.gethostbyname(host)
    return ip


async def get_endpoint(target: str) -> EndpointData:
    api = Endpoint()
    endpoint: EndpointData = await api.get(
        host=target,
        s=get_ip_from_host(target),
        fromCache=True,
        # all=True,
    )
    return endpoint


async def analyze(target: str) -> HostData:
    api = Analyze()
    host: HostData = await api.get(
        host=target,
        fromCache=True,
        all="on",
        maxAge=168,
    )
    return host
