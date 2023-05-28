import requests

proxies = {
    "http": "http://customer-rcodewithharry-cc-us:UCl3NtE2jXcf@pr.oxylabs.io:7777",
    "https": "http://customer-rcodewithharry-cc-us:UCl3NtE2jXcf@pr.oxylabs.io:7777"
}

r = requests.get("http://api64.ipify.org?format=json", proxies=proxies)
print(r.json())