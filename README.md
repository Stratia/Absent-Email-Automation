# Email-Automation

Place Credentials in index.env within the info folder

Create a Google APP Password: https://support.google.com/accounts/answer/185833?hl=en
 - Place App password in index.env within the info folder (password=App Password)

```
Run in script directory: python setup.py develop

Allows script to be used in CMD globally

Command-List:
-Absent [date] |Example: -Absent 1/10-1/23 | Sends emails to all saved in Emails.json
          
-Process |Example: -Process | Prints all saved emails
          
-help |  Example: -help     | Prints list of all available commands
```

**Example**
![alt text](AbsentExample.png)

