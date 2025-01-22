from enum import Enum
from ssllabs.data.endpoint import EndpointDetailsData


class EndpointVulnerability(Enum):
    vulnBeast = ("BEAST", "vulnBeast")
    renegSupport = ("Renegotiation Support", "renegSupport")
    sessionResumption = ("Session Resumption", "sessionResumption")
    hstsPolicy = ("HSTS Policy", "hstsPolicy")
    heartbleed = ("Heartbleed", "heartbleed")
    poodle = ("POODLE", "poodle")
    poodleTls = ("POODLE TLS", "poodleTls")
    bleichenbacher = ("Bleichenbacher", "bleichenbacher")
    ticketbleed = ("Ticketbleed", "ticketbleed")
    drownVulnerable = ("DROWN Vulnerable", "drownVulnerable")
    rc4 = ("RC4", "supportsRc4")
    aead = ("AEAD", "supportsAead")
    cbc = ("CBC", "supportsCBC")
    openSslCcs = ("OpenSSL CCS", "openSslCcs")
    openSSLLuckyMinus20 = ("OpenSSL LuckyMinus20", "openSSLLuckyMinus20")
    zombiePoodle = ("Zombie POODLE", "zombiePoodle")
    goldenDoodle = ("GOLDENDOODLE", "goldenDoodle")
    zeroLengthPaddingOracle = ("0-Length Padding Oracle", "zeroLengthPaddingOracle")
    sleepingPoodle = ("Sleeping POODLE", "sleepingPoodle")
    freak = ("FREAK", "freak")

    @staticmethod
    def from_name(name: str) -> "EndpointVulnerability":
        for vulnerability in EndpointVulnerability:
            if vulnerability.name == name:
                return vulnerability
        raise ValueError(f"No vulnerability with name {name}")

    @staticmethod
    def from_endpoint_details(
        details: EndpointDetailsData,
    ) -> dict["EndpointVulnerability", bool | str | int | None]:
        assert details.hstsPolicy

        return {
            EndpointVulnerability.vulnBeast: details.vulnBeast,
            EndpointVulnerability.renegSupport: details.renegSupport,
            EndpointVulnerability.sessionResumption: details.sessionResumption,
            EndpointVulnerability.hstsPolicy: details.hstsPolicy.status,
            EndpointVulnerability.heartbleed: details.heartbleed,
            EndpointVulnerability.poodle: details.poodle,
            EndpointVulnerability.poodleTls: details.poodleTls,
            EndpointVulnerability.bleichenbacher: details.bleichenbacher,
            EndpointVulnerability.ticketbleed: details.ticketbleed,
            EndpointVulnerability.drownVulnerable: details.drownVulnerable,
            EndpointVulnerability.rc4: details.supportsRc4,
            EndpointVulnerability.aead: details.supportsAead,
            EndpointVulnerability.cbc: details.supportsCBC,
            EndpointVulnerability.openSslCcs: details.openSslCcs,
            EndpointVulnerability.openSSLLuckyMinus20: details.openSSLLuckyMinus20,
            EndpointVulnerability.zombiePoodle: details.zombiePoodle,
            EndpointVulnerability.goldenDoodle: details.goldenDoodle,
            EndpointVulnerability.zeroLengthPaddingOracle: details.zeroLengthPaddingOracle,
            EndpointVulnerability.sleepingPoodle: details.sleepingPoodle,
            EndpointVulnerability.freak: details.freak,
        }
