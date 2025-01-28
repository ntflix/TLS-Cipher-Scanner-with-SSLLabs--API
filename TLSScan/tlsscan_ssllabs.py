import socket
from httpx import HTTPStatusError
import httpx
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

    while True:
        try:
            endpoint = await api.get(
                host=target,
                s=get_ip_from_host(target),
                fromCache="on",
                # all="done",
            )
            break
        except HTTPStatusError as e:
            # if 429, wait for 10 seconds and retry
            if e.response.status_code == 429:
                await asyncio.sleep(10)
            else:
                raise e

    assert endpoint is not None
    return endpoint


async def analyze(target: str) -> HostData:
    api = Analyze()
    host: HostData | None = None

    while True:
        try:
            host = await api.get(
                host=target,
                fromCache="on",
                all="done",
                maxAge=96,
            )
            break
        except HTTPStatusError as e:
            # if 429, wait for 10 seconds and retry
            if e.response.status_code == 429:
                await asyncio.sleep(10)
            else:
                raise e
        except httpx.ReadTimeout as readTimeout:
            print(f"ReadTimeout: {readTimeout}. Sleeping 60 seconds.")
            await asyncio.sleep(60)
        except httpx.ConnectTimeout as connectTimeout:
            print(f"ConnectTimeout: {connectTimeout}. Sleeping 60 seconds.")
            await asyncio.sleep(60)
    assert host is not None
    return host
