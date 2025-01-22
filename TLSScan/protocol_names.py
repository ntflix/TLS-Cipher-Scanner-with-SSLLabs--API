class ProtocolNames:
    @staticmethod
    def get_protocol_name(for_id: int) -> str:
        """
        TLS 1.2	0x0303	771 decimal
        TLS 1.1	0x0302	770 decimal
        TLS 1.0	0x0301	769 decimal
        TLS 1.3	0x0304	772 decimal
        SSL 3.0	0x0300	768 decimal
        SSL 2.0	0x0002	2 decimal

        https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA14u0000008UgRCAU
        """

        versions: dict[int, str] = {
            771: "TLS 1.2",
            770: "TLS 1.1",
            769: "TLS 1.0",
            772: "TLS 1.3",
            768: "SSL 3.0",
            2: "SSL 2.0",
        }
        return versions.get(for_id, f"Unknown Protocol ID: {for_id}")
