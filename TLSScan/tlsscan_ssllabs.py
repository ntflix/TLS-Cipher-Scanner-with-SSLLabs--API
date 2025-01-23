import socket
from httpx import HTTPStatusError
from ssllabs.api import Endpoint, Analyze
from ssllabs.data.host import HostData
from ssllabs.data.endpoint import EndpointData
import asyncio


def get_ip_from_host(host: str) -> str:
    ip = socket.gethostbyname(host)
    return ip


async def get_endpoint(target: str) -> EndpointData:
    api = Endpoint()
    endpoint: EndpointData | None = None
    try_again: bool = False

    while try_again:
        try_again = False
        try:
            endpoint = await api.get(
                host=target,
                s=get_ip_from_host(target),
                fromCache=True,
                # all=True,
            )
        except HTTPStatusError as e:
            # if 429, wait for 10 seconds and retry
            if e.response.status_code == 429:
                try_again = True
                await asyncio.sleep(10)
            else:
                raise e

    assert endpoint is not None
    return endpoint


async def analyze(target: str) -> HostData:
    api = Analyze()
    host: HostData | None = None
    try_again: bool = False

    while try_again:
        try_again = False
        try:
            host = await api.get(
                host=target,
                fromCache=True,
                all="on",
                maxAge=168,
            )
        except HTTPStatusError as e:
            # if 429, wait for 10 seconds and retry
            if e.response.status_code == 429:
                try_again = True
                await asyncio.sleep(10)
            else:
                raise e

    assert host is not None
    return host
