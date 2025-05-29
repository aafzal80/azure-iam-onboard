import os
import pandas as pd
from msal import ConfidentialClientApplication
import requests

CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
if not CLIENT_SECRET:
    raise Exception("Please set AZURE_CLIENT_SECRET in your environment")

df = pd.read_csv("users.csv")

app = ConfidentialClientApplication(
    client_id="c42e4a9a-adc9-404a-99b1-e9cf53757280",
    authority="https://login.microsoftonline.com/90d0af64-5dd1-46bb-91db-e1f490d8299f",
    client_credential="cce5ccd8-8602-412f-b635-69e76c0a1aa9"
)

for _, row in df.iterrows():
    token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    headers = {"Authorization": "Bearer " + token["access_token"],
               "Content-Type": "application/json"}
    user_data = {
        "accountEnabled": True,
        "displayName": row["name"],
        "mailNickname": row["name"].lower(),
        "userPrincipalName": row["email"],
        "passwordProfile": {
          "forceChangePasswordNextSignIn": True,
          "password": "TempP@ssw0rd"
        }
    }
    r = requests.post("https://graph.microsoft.com/v1.0/users", json=user_data, headers=headers)
    print(f'Created {row["name"]}:', r.status_code)
