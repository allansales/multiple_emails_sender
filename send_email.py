import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import argparse

MY_ADDRESS = "sender_email'
PASSWORD = 'email_password'
 
# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--attachment", help = "'True' for attachment on the email")
parser.add_argument("-t", "--subject", help = "The email subject")
args = parser.parse_args()

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('contacts.txt') # read contacts
    message_template = read_template('message.txt') # import message

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart() # create a message

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']=args.subject

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())
        print(message)
        
        #The subject line
        #The body for the mail
        msg.attach(MIMEText(message, 'plain'))
        
        if args.attachment == "True":
	        #The attachment for the mail
        	attach_file_name = name+'.pdf'
	        attach_file = open(attach_file_name, "rb") # Open the file as binary mode
        	payload = MIMEBase('application', 'octate-stream')
	        payload.set_payload(attach_file.read())
	        encoders.encode_base64(payload) #encode the attachment
        
	        #add payload header with filename
	        payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
	        msg.attach(payload)
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
