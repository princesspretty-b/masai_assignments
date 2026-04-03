Task 1 — Classify and Handle PII Fields:

a. full_name:
    Type: Direct PII 
    Action: Drop or Pseudonymize
    Reason: Directly identifies an individual. If not essential for analysis, drop it. If linkage across records is needed, replace with a hashed ID.

b. email:
    Type: Direct PII 
    Action: Drop
    Reason: Emails are very personal and unique. Not needed for research, so remove it completely.

c. date_of_birth:
    Type: Indirect PII 
    Action: Mask
    Reason: Exact birth date can help identify someone. Just use age or age group instead.

d. zip_code:
    Type: Indirect PII 
    Action: Mask
    Reason: Full zip code can point to a small area. Keep only part of it (like first 3 digits).

e. job_title:
    Type: Indirect PII 
    Action: Keep
    Reason: Usually safe but can become identifying in rare cases (e.g., “CEO of small company”)

f. diagnosis_notes:
    Type: Indirect PII 
    Action: Mask(Clean or remove)
    Reason: Notes might accidentally include names or places. Remove those before sharing.

Task 2 — Audit the API Script for Ethical Compliance:

Problem 1: API key is exposed

The key is like a password. Keeping it in code is risky because anyone who sees the code can misuse it.

Fix: Store it secretly (in environment variables) instead of writing it directly.

Problem 2: Collecting and storing too much raw personal data

a. Pulling 100 pages may violate APi rate limits and Fair usage policy. 
b. Saves personal patient details as is without cleaning.

Fix:

a. Add rate limiting and respect API usage
b. De-identify data before storage
c. Avoid storing unnecessary raw PII

Python code after fixing the issues:

'''
import os
import time
import requests

API_URL = "https://healthstats-api.example.com/records"
API_KEY = os.getenv("HEALTH_API_KEY")

def deidentify(record):
    return {
        "patient_id": hash(record["full_name"] + record["email"]),
        "age": 2026 - int(record["date_of_birth"][:4]),
        "zip_prefix": record["zip_code"][:3],
        "job_category": record["job_title"],
        "diagnosis_notes": redact_text(record["diagnosis_notes"])
    }

records = []
for page in range(1, 101):
    response = requests.get(API_URL, params={"page": page, "key": API_KEY})
    
    if response.status_code != 200:
        break  # stop if API signals an issue
    
    data = response.json()
    
    # De-identify before storing
    cleaned = [deidentify(r) for r in data["results"]]
    records.extend(cleaned)
    
    time.sleep(0.5)  # respect rate limits

# Store only de-identified data
save_to_database(records)
'''