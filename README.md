# SMTPFury

SMTPFury is a Python written application that can handle a large list of emails and send messages using a SMTP connection. The code and part of the design is inspired by a very old project that was a simple commandline script. SMTPFury is designed to look simple, be simple to use and be efficient.

Operation is extremely easy. Modify the files provided containing the SMTP details and provide the program with a list of emails.

# Gallery

![alt text](https://ibb.co/qMHQVSv)

![alt text](https://gyazo.com/bcbae9aa196d61753ca68c9be032187d)

The application uses a config structure that goes as follows:

1) Name of the file containing the emails, make sure each one is on a separate line, the script will take care of the rest.
2) Title of the email itself.
3) Name of the HTML file that will act as the body of the email being sent.
4) SMTP host name 
5) Your SMTP username (or email address)
6) SMTP password
7) SMTP port

All of these settings can ofcourse be manually inputed inside the program and you can save them inside a config. A functioning config should look something like:

![alt text](https://ibb.co/Dt2Yw4d)


