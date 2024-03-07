#!/usr/bin/env python3

from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib
import json
import sys
import os

# GMAIL API (On My Todo): https://mailtrap.io/blog/python-send-email-gmail/#How-to-send-an-email-with-Python-via-Gmail-API

#  Get directory of script directory
current_directory = os.path.dirname(os.path.realpath(__file__))


def main(): #  Prcocess command arguments & Commands
    
    """
    Main() - Process functions by looking at arguments in CMD
    Trriggers certain functions based on first argument
    """

    for arguemnts in sys.argv[1:]: # Iterates through commands --> Arguements
        #print(f"Arugment: {arguemnts}")
        if arguemnts.lower() == "-absent":
            send_email(sys.argv[2])

        elif arguemnts.lower() == "-process":
            process_list()
            sys.exit()
         
        elif arguemnts.lower() == "-help":
            help()
            sys.exit()

        else: #  If none are true | If commands don't match with arguement
            print("\033[91m {}\033[00m" .format("[X] Inccorrect Syntax | Try -help"))

# Gmail App Password as 'less secure apps' no longer function 
# https://stackoverflow.com/questions/73026671/how-do-i-now-since-june-2022-send-an-email-via-gmail-using-a-python-script

def email_text(date): # Template text, for emails
    
    """
    Param: Date | Dates absent | Example: 2/12-2/23
    This function serves as a place to use template emails
    """
    name = os.getenv("Name")

    blank_date = f"""I will not be able to attend school through {date}. I will make sure to catch up on any missed work and assignments. Thank you for your understanding.

    Sincerely,
    {name}"""

    return blank_date

def send_email(date): #  Sends email with {date} variable sent as days abent
    #  https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0

    """
    Param: Date | Dates absent | Example: 2/12-2/23
    Will send emails to all emails within info/Emails.json using the template text in email_text()
    """

    print("\033[92m {}\033[00m" .format("[!]Starting Process"))

    # Places all emails within a list
    with open(f"{current_directory}/info/Emails.json", "r+") as email_json:
        cached_json = json.load(email_json)
        email_to_list = []
        for index in cached_json.values():
            email_to_list.append(index)

    load_dotenv(f"{current_directory}/info/index.env")
    password = os.getenv("Password")
    from_email = os.getenv("Email")
    
    text_1 = email_text(date)
    msg = MIMEText(text_1)

    msg['Subject'] = f'Will be Absent {date}'
    msg['From'] = from_email
    msg['To'] = email_to_list

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.ehlo()
        server.starttls() # TLS Encryption
        server.ehlo()
        server.login(from_email, password) # User | Password
        server.send_message(msg)

        print("\033[92m {}\033[00m" .format("[!]Confirmation: Emails Sent!"))
        server.quit()

    sys.exit() # Cancels terminal

def process_list(): #  Prints list of emails saved in .json file

    """
    Prints all emails values in info/Emails.json 
    """

    try:
        with open(f"{current_directory}/info/Emails.json", "r+") as indexed_file: #  Opens .json file
            cached_json = json.load(indexed_file) # .json to dict

            for index in cached_json.values():
                print(index)
            exit # Ensures code doesn't continue to check for other commands

    except FileNotFoundError:
        print("Error, cannot access file")


def help(): # Prints help command

    """
    Prints list of all commands
    """

    print(""" 
    -Absent [date] |Example: -Absent 1/10-1/23 | Sends emails to all saved in Emails.json
          
    -Process |Example: -Process | Prints all saved emails
          
    -help |  Example: -help     | Prints list of all avaliable commands""")


main()