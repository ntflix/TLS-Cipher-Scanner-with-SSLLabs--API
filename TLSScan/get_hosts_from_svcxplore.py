import requests
import json


SVCXPLORE_BASE_URL = "http://localhost:8080/interfaces"

"""
[
	{
		"interfaceType": "publicIP",
		"ipVersion": "v4",
		"updatedAt": "2024-07-01T09:48:21Z",
		"createdAt": "2024-07-01T09:48:21Z",
		"ip": "92.197.203.0",
		"url": "edexcelonline.pearson.com",
		"id": "6D87BB4C-E398-49F1-BC3B-AED6D9B7BEA8",
		"serviceInstance": {
			"comment": null,
			"updatedAt": "2024-06-30T21:29:21Z",
			"id": "6E8D7E03-F4B0-4369-947B-94A2A08676BB",
			"vpc": {
				"id": null
			},
			"createdAt": "2024-06-30T21:29:21Z",
			"environmentType": "production",
			"service": {
				"id": "104331AC-17C0-42BF-A81A-410B762F5250"
			}
		}
	},
	{
		"ip": "faca:a1fc:1b43:cf7d:12d3:4dda:f52e:49ae",
		"serviceInstance": {
			"service": {
				"id": "104331AC-17C0-42BF-A81A-410B762F5250"
			},
			"createdAt": "2024-06-30T21:29:21Z",
			"updatedAt": "2024-06-30T21:29:21Z",
			"comment": null,
			"vpc": {
				"id": null
			},
			"id": "6E8D7E03-F4B0-4369-947B-94A2A08676BB",
			"environmentType": "production"
		},
		"createdAt": "2024-07-01T10:09:10Z",
		"updatedAt": "2024-07-01T10:09:10Z",
		"ipVersion": "v6",
		"url": "edexcelonline.pearson.com",
		"interfaceType": "publicIP",
		"id": "677DA6F5-B3E0-4255-B4C8-A5152D94A712"
	}
]"""


def get_hosts_from_svcxplore():
    domains: list[str] = []

    response = requests.get(SVCXPLORE_BASE_URL)
    if response.status_code == 200:
        interfaces = json.loads(response.text)
        for interface in interfaces:
            interface: str
            try:
                interface: str = interface["url"]
            except KeyError:
                pass
            domains.append(interface)
    else:
        print(f"Failed to get hosts from svcxplore: {response.text}")

    return domains
