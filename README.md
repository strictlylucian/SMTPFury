# SMTPFury

SMTPFury is a Python written application that can handle a large list of emails and send messages using a SMTP connection. The code and part of the design is inspired by a very old project that was a simple commandline script. SMTPFury is designed to look relatively minimalistic, be simple to use and be efficient.

Operation is extremely easy. Modify the files provided containing the SMTP details and provide the program with a list of emails then just press the "Start" button.

# Gallery

![alt text](https://i.ibb.co/FbQTCrF/mainui.png)

![alt text](https://i.ibb.co/h7tfTvH/logging.png)

The application uses a config structure that goes as follows:

1) Name of the file containing the emails, make sure each one is on a separate line, the script will take care of the rest.
2) Title of the email itself.
3) Name of the HTML file that will act as the body of the email being sent.
4) SMTP host name 
5) Your SMTP username (or email address)
6) SMTP password
7) SMTP port

All of these settings can ofcourse be manually inputed inside the program and you can save them inside a config. A functioning config should look something like:

![alt text](https://i.ibb.co/s2YCsj7/config.png)


Thanks to hoffstadt for making his dearpygui project available which I relied on when developing this project.

His GitHub: https://github.com/hoffstadt
DearPyGui: https://github.com/hoffstadt/DearPyGui
