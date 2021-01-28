# Multiple email sender with attachment

Code for automatically emailing, with or without attachment, a list of contacts.

### Run

For running the code, make sure 1) you have the destination names and email addresses written in contacts.txt separated by blank space, and 2) you are happy with the message written in message.txt.

Then, on the command line, run:
```sh
$ python3 send_emails.py -a <True> -t <email_subject>
```
  - "-a" stands for "attachment". If it is 'True', each email will contain one attachment named equally as the destination. Make sure the file that will be attached is in the same directory as send_email.py. 
  - "-t" stands for the email subject. If the email subject is not passed as an argument, the email will be sent without any Subject.
  
Obs: This code results from shamelessly copies and pastes from [this one] and [this other one] tutorials, with minor modifications.

[this one]: https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/
[this other one]: https://www.tutorialspoint.com/send-mail-with-attachment-from-your-gmail-account-using-python
