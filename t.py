import re


def search_contacts(filename):
    # Define regular expressions for phone numbers and email addresses
    phone_regex = re.compile(r'\+91\d{10}')
    email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    # Initialize lists to store found phone numbers and emails
    phone_numbers = []
    emails = []

    # Open the file and search each line
    with open(filename, 'r') as file:
        for line in file:
            # Find all matches in the current line
            found_phones = phone_regex.findall(line)
            found_emails = email_regex.findall(line)

            # Add found items to respective lists
            phone_numbers.extend(found_phones)
            emails.extend(found_emails)

            # Display results

    if phone_numbers:
        print("📞 Phone Numbers found:")
        for phone in phone_numbers:
            print(phone)
    else:
        print("No phone numbers found.")

    if emails:
        print("\n📧 Email Addresses found:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")


# Specify the file to search
filename = 'contacts.txt'  # Replace with the path to your file

# Call the search function
search_contacts(filename)
