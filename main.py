#GUI

from dearpygui.core import *
from dearpygui.simple import *

# SMTP

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# other functions

from main_functions import path_to_aray, clear_that_file
import json
import sys

#functions for misc stuff


def save_config(sender, data):
    with window("SMTPFury"):
        clear_that_file('config.txt') # clearning the previous config
        with open('config.txt', 'w') as data:
            data.write(get_value("Path") + '\n')
            data.write(get_value("email_header") + '\n')
            data.write(get_value("HTMLPath") + '\n')
            data.write(get_value("Host") + '\n')
            data.write(get_value("Username") + '\n')
            data.write(get_value("Password") + '\n')
            data.write(get_value("Port"))
            log_info(logger="email_logging", message="Config saved")


def load_config(sender, data):
    with window("SMTPFury"):
        x = open('config.txt')
        lines = x.readlines()
        set_value("Path", lines[0].rstrip("\n"))
        set_value("email_header", lines[1].rstrip("\n"))
        set_value("HTMLPath", lines[2].rstrip("\n"))
        set_value("Host", lines[3].rstrip("\n"))
        set_value("Username", lines[4].rstrip("\n"))
        set_value("Password", lines[5].rstrip("\n"))
        set_value("Port", lines[6].rstrip("\n"))
        log_info(logger="email_logging", message="Config loaded")


def clear_all_fields(sender, data):
    with window("SMTPFury"):
        set_value("Path", "")
        set_value("email_header", "")
        set_value("HTMLPath", "")
        set_value("Host", "")
        set_value("Username", "")
        set_value("Password", "")
        set_value("Port", "")
        log_warning(logger="email_logging", message="Cleared fields")


def send_emails(sender, data):
    with window("SMTPFury"):
        array_of_emails = path_to_aray(get_value("Path"))
        length = len(array_of_emails)
        for i in range(length):
            X = array_of_emails[i]
            receiver_email= X
            log_debug(logger="email_logging", message=receiver_email)
            message = MIMEMultipart()

            set_value("Progress", value=0.1)

            message['From'] = get_value("Username")
            message['To'] = receiver_email
            message['Subject'] = get_value("email_header")
            email_html = open(get_value("HTMLPath"))
            mail_content = email_html.read()

            set_value("Progress", value=0.3)

            message.attach(MIMEText(mail_content, 'html'))
            s = smtplib.SMTP(get_value("Host"), get_value("Port"))
            s.starttls()

            set_value("Progress", value=0.6)

            s.login(get_value("Username"),get_value("Password"))
            text = message.as_string()

            set_value("Progress", value=0.8)

            s.sendmail(get_value("Username"), receiver_email, text)
            s.quit()

            set_value("Progress", value=1)
            log_info(logger="email_logging", message="Mail sent")
            set_value("Progress", value=0)


def set_JSON_path(sender, data):
    with window("SMTPFury"):
        if get_value("Path") == "":
            log_error(logger="email_logging", message="Empty path")

        else:
            log_info(logger="email_logging", message="Selected path:")
            log_info(logger="email_logging", message=get_value("Path"))

def set_HTML_path(sender, data):
    with window("SMTPFury"):
        if get_value("email_header") == "":
            log_warning(logger="email_logging", message="Empty header")

        if get_value("email_html_path") == "":
            log_warning(logger="email_logging", message="Empty HTML path")

        if get_value("email_header") == "" and get_value("email_logging") == "":
            log_error(logger="email_logging", message="Missing email info")

        if get_value("email_header") != "" and get_value("email_logging") != "":
            log_info(logger="email_logging", message="Header:")
            log_info(logger="email_logging", message=get_value("email_header"))
            log_info(logger="email_logging", message="HTML path:")
            log_info(logger="email_logging", message=get_value("HTMLPath"))

def set_SMTP_data(sender, data):
    with window("SMTPFury"):
        if get_value("Host") == "" and get_value("Username") == "" and get_value("Port") == "" and get_value("Password") == "":
            log_error(logger="email_logging", message="Fill in the SMTP information")
        else:
            log_info(logger="email_logging", message="SMTP data:")
            log_info(logger="email_logging", message=get_value("Host")+","+get_value("Username")+","+get_value("Port")+","+get_value("Password"))


# global settings
set_main_window_size(800,800)
set_global_font_scale(1.10)
set_theme("Dark")
set_main_window_title("SMTPFury")
set_main_window_resizable(False)

with window("SMTPFury", width=780, height=755, no_resize=True , no_move=True, no_close=True, no_collapse=True):
    set_window_pos("SMTPFury", 0, 0)

    # getting the path for the list of emails

    add_child(width=390, height=250, name="path_selection")
    add_text("Email list",
    color=[255,255,255])
    add_separator()
    add_spacing(count=10)
    add_separator()
    add_text("Enter the name of the .txt file containing your",
    color=[255,255,255])
    add_text("list of emails.",
    color=[255,255,255])
    add_spacing(count=10)
    add_input_text("Path", width=300, default_value="")
    add_spacing(count=10)
    add_button("Set path", callback=set_JSON_path)
    end()

    # we use this as a logger for the emails we send

    add_same_line() # putting the 2 elements on the same add_same_line
    add_child(width=390, height=250, name="logging_section")
    add_text("Logging section",
    color=[255,255,255])
    add_separator()
    add_spacing(count=10)
    add_separator()
    add_logger(name="email_logging", width=355, height=130, clear_button=True, auto_scroll_button=False)
    end()

    # letting the user formulate the email, should maybe add a path for a HTML file aswell

    add_child(width=390, height=350, name="email_body")
    add_text("Email body",
    color=[255,255,255])
    add_separator()
    add_spacing(count=10)
    add_separator()
    add_spacing(count=10)
    add_input_text("email_header", width=300,label="Header", default_value="")
    add_spacing(count=10)
    add_text("Type the HTML file name for the body below",
    color=[255,255,255])
    add_spacing(count=10)
    add_input_text("HTMLPath", width=300, label="HTML File", default_value="")
    add_spacing(count=10)
    add_button("Set HTML path", callback=set_HTML_path)
    end()

    add_same_line()

    add_child(width=390, height=350, name="smtp_settings")
    add_text("SMTP settings",
    color=[255,255,255])
    add_separator()
    add_spacing(count=10)
    add_separator()
    add_spacing(count=10)
    add_input_text("Host", width=300, default_value="")
    add_spacing(count=5)
    add_input_text("Username", width=270, default_value="")
    add_spacing(count=5)
    add_input_text("Password", width=270, password=True, default_value="")
    add_spacing(count=5)
    add_input_text("Port", width=300, default_value="")
    add_spacing(count=5)
    add_button("Set SMTP settings", callback=set_SMTP_data)
    end()

# google SMTP reports, maybe replace this with values pinging a certain website

    add_child(width=390, height=110, name="network_histrogram", no_scrollbar=True)
    add_text("Google SMTP Reports(x100)",
    color=[255,255,255])
    add_simple_plot("", value=(0.14, 0.1, 0.12, 0.06, 0.09, 0.11, 0.2), height=80,width=370, histogram=True, minscale=0.00)
    end()

    add_same_line()
    add_child(width=390, height=110, name="important_bottons")
    add_spacing(count=5)
    add_button("Start", callback=send_emails)
    add_same_line()
    add_button("Save config", callback=save_config)
    add_same_line()
    add_button("Load config", callback=load_config)
    add_same_line()
    add_button("Clear fields", callback=clear_all_fields)
    add_separator()
    add_spacing(count=5)
    add_progress_bar("Progress",width=370, height=20,tip="The progrss bar shows the stage of each email being sent")
    end()
start_dearpygui()
