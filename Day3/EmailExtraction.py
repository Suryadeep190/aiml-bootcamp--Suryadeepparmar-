import re
from collections import Counter

text = '''
asha.sharma@codetrade.io wrote to ravi_k99@gmail.com
meera.p+work@company.co.in, phone 022-2555-1234
dev@sub.domain.example.org and +91 98765 43210
not.an.email@ nor @nothing.com -- watch these
'''

email_pattern = r'(?<![\w.+-])([A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*)@((?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,})(?![\w.-])'

email_parts = re.findall(email_pattern, text)

emails = [username + "@" + domain for username, domain in email_parts]

print("--- Extracted Emails ---")

for email in emails:
    print(email)


phone_pattern = r'(?<!\d)(?:\+91[\s-]?\d{5}[\s-]?\d{5}|0\d{2,4}[-\s]?\d{6,8}|\d{5}[\s-]?\d{5})(?!\d)'

phones = re.findall(phone_pattern, text)

print("\n--- Extracted Phone Numbers ---")

for phone in phones:
    print(phone)


print("\n--- Username and Domain ---")

for username, domain in email_parts:
    print(f"Username: {username} | Domain: {domain}")


domain_count = Counter(domain for username, domain in email_parts)

print("\n--- Email Count by Domain ---")

for domain, count in domain_count.items():
    print(f"{domain}: {count}")


print("\n--- Summary ---")
print("Total emails:", len(emails))
print("Total phone numbers:", len(phones))
print("Unique domains:", len(domain_count))
