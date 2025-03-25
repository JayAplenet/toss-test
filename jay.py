import requests
import json

# API URL ??
tenant_region_api_server = 'pa-us01.api.prismaaccess.com'
url = f'https://{tenant_region_api_server}/api/sase/v2.0/resource/custom/query/gp_mobileusers/current_connected_user_list'

# ???? ??
payload = {
    "filter": {
        "rules": [
            {
                "property": "edge_location_display_name",
                "operator": "equals",
                "values": ["US Central"]
            }
        ]
    }
}

access_token = 'eyJ0eXAiOiJKV1QiLCJraWQiOiJyc2Etc2lnbi1wa2NzMS0yMDQ4LXNoYTI1Ni8xIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI0ZDAxOTY0Zi02ZWZlLTQxYTQtODUyYi1mNDdjOWE5MmQ0OWYiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXVkaXRUcmFja2luZ0lkIjoiZGFiNmM5NGMtYTA2ZC00OGI1LTk5N2QtYWZjMTI3ZDMyZGEyLTY2NTM4MzYiLCJzdWJuYW1lIjoiNGQwMTk2NGYtNmVmZS00MWE0LTg1MmItZjQ3YzlhOTJkNDlmIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmFwcHMucGFsb2FsdG9uZXR3b3Jrcy5jb206NDQzL2FtL29hdXRoMiIsInRva2VuTmFtZSI6ImFjY2Vzc190b2tlbiIsInRva2VuX3R5cGUiOiJCZWFyZXIiLCJhdXRoR3JhbnRJZCI6Ik9zUVRyamRuTnJmUktlUHNNcndVNDBCdWs2USIsImF1ZCI6IkFwbGVuZXRAMTEyNjIzODMzMS5pYW0ucGFuc2VydmljZWFjY291bnQuY29tIiwibmJmIjoxNzIxNjEyNzEzLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwic2NvcGUiOlsidHNnX2lkOjExMjYyMzgzMzEiLCJwcm9maWxlIiwiZW1haWwiXSwiYXV0aF90aW1lIjoxNzIxNjEyNzEzLCJyZWFsbSI6Ii8iLCJleHAiOjE3MjE2MTM2MTMsImlhdCI6MTcyMTYxMjcxMywiZXhwaXJlc19pbiI6OTAwLCJqdGkiOiJDRDRMYXdLM2VhczFZWWYzakZ0bmhKaFdJeHMiLCJ0c2dfaWQiOiIxMTI2MjM4MzMxIiwiYWNjZXNzIjp7InBybjoxMTI2MjM4MzMxOjo6OiI6WyJzdXBlcnVzZXIiXX19.DZA5RtwjREg6hQXWS1RQULb374H5L14IhU5VdeBQWvH50Dtr1KVAlAw4817gmrm52KVp6NzjD2zE9uainN9k-LkavjHvaz7ZuS2Jn0mdIlgVCyvJWB9X6Kq2snm7XNWVlnVW4eaNLTAlwzCplN7R3EiH5lUSU46xOVlGxfLdHGbiwBBAKuXaVIQKcHRIBg_2c-QlNFS882xQlcxiqn_yElNY2jgPd8GRJbuAqODwi4hB9gti5kUYeHd3eiVxNWGAM_WBzrzcbnm6MkeUpdS2wEgOQHDfTmdO7YNB4A4CrhWSNHBqDCb7Sjjw0vX7_W0B2EZHtJYEZ3XeBGTotvqpPQ' 

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

# ?? ?? ??
print(f'Status Code: {response.status_code}')

# ?? ??? ??
try:
    response_data = response.json()
    print(json.dumps(response_data, indent=4))  # ??? ??
except ValueError:
    print("Response is not in JSON format")