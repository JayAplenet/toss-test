import requests
import json

tenant_region_api_server = 'pa-sg01.api.prismaaccess.com'
url = f'https://{tenant_region_api_server}/api/sase/v2.0/resource/custom/query/gp_mobileusers/connected_user_count'

tsg_id = '1126238331'
jwt_token = 'eyJ0eXAiOiJKV1QiLCJraWQiOiJyc2Etc2lnbi1wa2NzMS0yMDQ4LXNoYTI1Ni8xIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI0ZDAxOTY0Zi02ZWZlLTQxYTQtODUyYi1mNDdjOWE5MmQ0OWYiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXVkaXRUcmFja2luZ0lkIjoiMWUzODFjNTktMjI1NC00MjI2LTg4YTctZTk4YTNjMDIwNTNmLTE1MzY1NjA4Iiwic3VibmFtZSI6IjRkMDE5NjRmLTZlZmUtNDFhNC04NTJiLWY0N2M5YTkyZDQ5ZiIsImlzcyI6Imh0dHBzOi8vYXV0aC5hcHBzLnBhbG9hbHRvbmV0d29ya3MuY29tOjQ0My9hbS9vYXV0aDIiLCJ0b2tlbk5hbWUiOiJhY2Nlc3NfdG9rZW4iLCJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiYXV0aEdyYW50SWQiOiJ0MExNNUJ2R2VoeVVSM0ZzZTBKUkxiRFl0SDgiLCJhdWQiOiJBcGxlbmV0QDExMjYyMzgzMzEuaWFtLnBhbnNlcnZpY2VhY2NvdW50LmNvbSIsIm5iZiI6MTcyMTg3MjY5MywiZ3JhbnRfdHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsInNjb3BlIjpbInByb2ZpbGUiLCJlbWFpbCIsInRzZ19pZDpub25lIl0sImF1dGhfdGltZSI6MTcyMTg3MjY5MywicmVhbG0iOiIvIiwiZXhwIjoxNzIxODczNTkzLCJpYXQiOjE3MjE4NzI2OTMsImV4cGlyZXNfaW4iOjkwMCwianRpIjoiWW5XdUV1YjdjdkVxU2tUTzQ4YWpheGoyakFZIiwidHNnX2lkIjoibm9uZSIsImFjY2VzcyI6eyJwcm46bm9uZTo6OjoiOlsic3VwZXJ1c2VyIl19fQ.E420Cy3MxNwVqwQ9rdtU6oRH2MeP5u56N-xub9NL3t0ksU7xdvChdUUBIBN3ZK_7PpzVS_w_5tl2JgNpe8Dwvj1S2R_LGDi1n246Kbvb8putftKxyVLFFGVbFDnxWV3A8QQiH2xmsc_-O1fqi7WcM6p0T8dLVZOgD0Zl_qqRM60L0nUwGPxNt_lTGNMWXp9gpCf-An90efCMrk7WQwjfOTbz6nnzZ660CNy-nt9K4Wzin8J7cqxjGnoLJi7sR024foCwYu-lR2EJnvwrVxeBaf2pOJjtnB2RVJd3YFpuHaz9k1JBcE1gpE6mibe6PZrgIHCf-4ZeeN7iyKY6rfKnDg'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {jwt_token}',
    'Prisma-Tenant': tsg_id
}

response = requests.post(url, headers=headers)

print(f'Status Code: {response.status_code}')

if response.status_code == 200:
    try:
        response_data = response.json()
        print(json.dumps(response_data, indent=4))
    except ValueError:
        print("Response is not in JSON format")
        print("Response Text:", response.text)
else:
    print("Failed to retrieve data")
    print("Response Text:", response.text)






