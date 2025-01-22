from ssllabs.data.endpoint import EndpointData
from ssllabs.data.protocol_suites import ProtocolSuitesData

from TLSScan.protocol_names import ProtocolNames
import TLSScan.suite_strength_checker as suite_strength_checker


class EndpointProtocolSuitesData:
    host: str
    serverName: str
    protocolSuites: list[ProtocolSuitesData]

    def __init__(
        self, host: str, serverName: str, protocolSuites: list[ProtocolSuitesData]
    ):
        self.host = host
        self.serverName = serverName
        self.protocolSuites = protocolSuites

    @staticmethod
    def from_endpoint(endpoint: EndpointData) -> "EndpointProtocolSuitesData":
        if endpoint.statusMessage != "Ready":
            raise ValueError("Endpoint is not ready")
        assert endpoint.details
        assert endpoint

        if not endpoint.serverName:
            endpoint.serverName = ""

        assert endpoint.details.suites

        return EndpointProtocolSuitesData(
            host=endpoint.ipAddress,
            serverName=endpoint.serverName,
            protocolSuites=endpoint.details.suites,
        )

    def csv(self) -> list[list[str]]:
        lines: list[list[str]] = []
        for protocolSuite in self.protocolSuites:
            for suite in protocolSuite.list:
                lines.append(
                    [
                        self.host,
                        self.serverName,
                        str(ProtocolNames().get_protocol_name(protocolSuite.protocol)),
                        str(protocolSuite.protocol),
                        str(suite.id),
                        suite.name,
                        str(suite.cipherStrength),
                        "INSECURE" if suite.q == 0 else "WEAK" if suite.q == 1 else "",
                        suite_strength_checker.get_cipher_strength(suite.name),
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
            "Suite RFC ID",
            "Suite Name",
            "Suite Strength",
            "SSLLabs Flags",
            "Cipher Recommendedness",
        ]
