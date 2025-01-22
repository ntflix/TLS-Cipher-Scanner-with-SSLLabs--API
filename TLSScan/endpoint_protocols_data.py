from ssllabs.data.endpoint import EndpointData
from ssllabs.data.protocol import ProtocolData


class EndpointProtocolsData:
    host: str
    serverName: str
    protocols: list[ProtocolData]

    def __init__(self, host: str, serverName: str, protocols: list[ProtocolData]):
        self.host = host
        self.serverName = serverName
        self.protocols = protocols

    @staticmethod
    def from_endpoint(endpoint: EndpointData) -> "EndpointProtocolsData":
        if endpoint.statusMessage != "Ready":
            raise ValueError("Endpoint is not ready")
        assert endpoint.details
        assert endpoint

        if not endpoint.serverName:
            endpoint.serverName = ""

        return EndpointProtocolsData(
            host=endpoint.ipAddress,
            serverName=endpoint.serverName,
            protocols=endpoint.details.protocols,
        )

    @staticmethod
    def transform_protocols_data(protocols: list[ProtocolData]) -> list[str]:
        protocols_transformed: list[str] = []

        for protocol in protocols:
            insecure_flag = " [INSECURE]" if protocol.q == 0 else ""

            protocols_transformed.append(
                f"{protocol.name} {protocol.version}{insecure_flag}"
            )

        return protocols_transformed

    @staticmethod
    def get_sorted_protocols(protocols: list[ProtocolData]) -> list[ProtocolData]:
        sorted_protcols = sorted(protocols, key=lambda protocol: protocol.id)
        return sorted_protcols

    def __str__(self) -> str:
        return f"Host: {self.host}\n" f"Server Name: {self.serverName}\n" + "\n".join(
            f"{protocol.name} {protocol.version}" for protocol in self.protocols
        )

    def csv(self) -> list[list[str]]:
        lines: list[list[str]] = []
        for protocol in self.protocols:
            lines.append(
                [
                    self.host,
                    self.serverName,
                    protocol.name,
                    protocol.version,
                    str(protocol.id),
                ]
            )

        return lines

    @staticmethod
    def csv_headers() -> list[str]:
        return [
            "Host",
            "Server Name",
            "Protocol Name",
            "Protocol Version",
            "Protocol ID",
        ]
