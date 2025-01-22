SUITE_STRENGTH_FILENAME = "cipher_strengths.csv"


def read_suite_strengths() -> dict[str, str]:
    suite_strengths: dict[str, str] = {}
    with open(SUITE_STRENGTH_FILENAME, "r") as file:
        for line in file:
            split_line = line.strip().split(",")
            strength = split_line[0]
            suite = split_line[1]
            suite_strengths[suite] = strength

    return suite_strengths


suite_strengths = read_suite_strengths()


def get_cipher_strength(for_cipher: str) -> str:
    return suite_strengths.get(for_cipher, "UNKNOWN")
