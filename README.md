# Azure IAM Onboard 🚀  
![Python](https://img.shields.io/badge/python-3.10-blue)

## Overview  
Automates bulk user onboarding in Azure AD with Microsoft Graph API, MSAL, and Python.

## Motivation  
Manually creating users in Azure AD is repetitive and error-prone. This script speeds up onboarding, ensures consistency, and frees up IT time.

## Skills Demonstrated  
- Azure AD app registration & permission granting  
- MSAL OAuth2 client credentials flow  
- Microsoft Graph API calls to create users  
- Python scripting & CSV file handling  

## Prerequisites  
1. An Azure free account  
2. Python 3.7+ installed  
3. In your terminal:  
   ```bash
   pip install msal pandas requests
   ```

## Repository Contents  
- `users.csv` – sample list of users to onboard  
- `onboard.py`  – Python script that reads `users.csv` and calls Graph API  
- `README.md`   – this file  
- `.gitignore`  – ignores secrets files (e.g. `.env`)

## Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/YourUsername/azure-iam-onboard.git
   cd azure-iam-onboard
   ```

2. **Register your Azure AD app**  
   - In Azure Portal → **Azure Active Directory** → **App registrations** → **New registration**  
   - Name: `MyRobotHelper`  
   - Supported account types: **Accounts in this organizational directory only**  
   - Redirect URI: leave blank → **Register**

3. **Grant Microsoft Graph permissions**  
   - Under your app → **API permissions** → **Add a permission** → **Microsoft Graph** → **Application permissions**  
   - Select **User.ReadWrite.All** and **Group.ReadWrite.All** → **Add permissions**  
   - Click **Grant admin consent** for your tenant

4. **Create a client secret**  
   - Under **Certificates & secrets** → **New client secret** → add description & expiry → **Add**  
   - Copy the **Value** (you’ll need it in step 6)

5. **Configure your environment**  
   - Create a file named `.env` in the repo root:  
     ```bash
     AZURE_CLIENT_SECRET=your-newly-generated-secret-value
     ```  
   - Add `.env` to `.gitignore` so it stays out of Git.

6. **Edit `onboard.py`**  
   - Replace the placeholders for `client_id` and `tenant_id` with your App (client) ID and Directory (tenant) ID.  
   - The script already reads `AZURE_CLIENT_SECRET` from the environment.

7. **Run the onboarding script**  
   ```bash
   python onboard.py
   ```
   You should see output like:
   ```
   Created Alice: 201
   Created Bob:   201
   ```

8. **Verify in Azure**  
   Go to **Azure Active Directory → Users** and confirm that your sample users (Alice, Bob) have been created.

## Usage Example  
```bash
python onboard.py
# → Created Alice: 201  
# → Created Bob:   201
```

## Next-Steps & Enhancements  
- Send email or Teams notifications on completion  
- Generate strong, randomized passwords  
- Add retry logic and error handling  
- Integrate with a secrets-management service  

## Contact  
- LinkedIn: https://linkedin.com/in/ahmadsafzal  
- GitHub:   https://github.com/aafzal80  
