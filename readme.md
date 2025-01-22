# TLS Cipher Scanner with SSLLabs' API

Consumes [SSLLabs' API](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md) to scan a list of domains and return the results in a CSV file.

Only focuses on TLS ciphers and protocols, matching against a given list of recommended, secure, weak, and insecure ciphers (`cipher_strengths.csv`).

Put domains to scan in `masterurl.csv`.

Outputs to CSV - sample:

| Original Host | Host    | Server Name              | Protocol Name | Protocol Version | Suite RFC ID | Suite Name                    | Suite Strength | SSLLabs Flags | Cipher Recommendedness |
| ------------- | ------- | ------------------------ | ------------- | ---------------- | ------------ | ----------------------------- | -------------- | ------------- | ---------------------- |
| my.domain.com | 1.1.1.1 | something.in.a.cloud.com | TLS 1.0       | 769              | 53           | TLS_RSA_WITH_AES_256_CBC_SHA  | 256            | WEAK          | Weak                   |
| my.domain.com | 1.1.1.1 | something.in.a.cloud.com | TLS 1.0       | 769              | 47           | TLS_RSA_WITH_AES_128_CBC_SHA  | 128            | WEAK          | Weak                   |
| my.domain.com | 1.1.1.1 | something.in.a.cloud.com | TLS 1.0       | 769              | 10           | TLS_RSA_WITH_3DES_EDE_CBC_SHA | 112            | WEAK          | Weak                   |
