import imaplib
import email
from email.header import decode_header

def decode_mime_words(s):
    """Decode MIME encoded words in email headers."""
    decoded_words = email.header.decode_header(s)
    return ''.join([str(t[0], t[1] or 'utf-8') if isinstance(t[0], bytes) else t[0] for t in decoded_words])

def extract_emails(email_user, email_pass):
    """Extract 'From' and 'To' email addresses from the inbox."""
    from_emails = []
    to_emails = []
    
    try:
        # Connect to the server
        print("Connecting to the server...")
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        print("Connected to the server.")
        
        # Login to the account
        print("Logging in...")
        mail.login(email_user, email_pass)
        print("Logged in.")
        
        # Select the mailbox you want to check
        print("Selecting mailbox...")
        mail.select("inbox")
        print("Mailbox selected.")
        
        # Search for all emails in the mailbox
        print("Searching for emails...")
        result, data = mail.search(None, "ALL")
        
        if result != 'OK':
            print(f"Error searching inbox: {result}")
            return from_emails, to_emails
        
        # List of email IDs
        email_ids = data[0].split()
        print(f"Found {len(email_ids)} email(s).")
        
        for e_id in email_ids:
            try:
                # Fetch the email by ID
                result, msg_data = mail.fetch(e_id, "(RFC822)")
                
                if result != 'OK':
                    print(f"Error fetching email ID {e_id.decode()}: {result}")
                    continue
                
                # Extract the email content
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)
                
                # Decode and append 'From' email address
                from_email = decode_mime_words(msg.get("From"))
                from_emails.append(from_email)
                
                # Decode and append 'To' email addresses
                to_email = decode_mime_words(msg.get("To"))
                if to_email:
                    to_emails.extend(to_email.split(','))
            
            except Exception as e:
                print(f"Error processing email ID {e_id.decode()}: {e}")
    
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return from_emails, to_emails

def main():
    # Replace with your Gmail credentials
    email_user = 'arjun@trestle.co.in'
    email_pass = '0103T@Kjun'
    
    from_emails, to_emails = extract_emails(email_user, email_pass)
    
    print("Extracted From Emails:")
    for email in from_emails:
        print(email)
    
    print("Extracted To Emails:")
    for email in to_emails:
        print(email)

if __name__ == '__main__':
    main()
