# SMS_Alert_Project
## Contents of File
- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [Usage](#Usage)

## Introduction
The SMS_Alert_Project project is a simple Python script that is responsible for sending scheduled alert sms messages to recipient(s).  
This script utilizes the schedule module for executing scheduled tasks and the Twilio Cloud Communications Platform API for sending  
SMS messages. The purpose of this project is to have the ability to send out reminders and alerts as SMS to recipient(s).

## Requirements
Just to make aware, this script was executed on the Linux operating system. In order to be successfully execute this program, there are  
a few components that will needed. The following components are:
- Python 3
- Schedule Python Module 
- Twilio Cloud Communications Platform Account (Account SID and Authentication Token) which can be created by visiting  
[Twilio Sign Up](https://www.twilio.com/try-twilio)
- Twilio Cloud Communications Platform Phone Number
- Twilio Cloud Communications Platform Command Line Interface (CLI)

## Installation
**Python 3**  
Instructions for installing Python 3 can be found at:  
[Python Install](https://wiki.python.org/moin/BeginnersGuide/Download)

**Schedule Module**  
Instructions for installing the schedule module can be found at:  
[Schedule Module](https://pypi.org/project/schedule/)

**Twilio Cloud Communications Platform Command Line Interface (CLI)**  
Instructions for installing the Twilio Cloud Communications Platform Command Line Interface (CLI) can be found at:  
[Twilio CLI Instructions](https://www.twilio.com/docs/sms/quickstart/python).

## Configuration
This step involves configuring the neccessary components in order for the sms_alert.py script to execute. After you have created  
your Twilio Cloud Communications Platform account you will be presented with a your [Twilio Dashboard](https://console.twilio.com/). From the dashboard,  
you will need to obtain the your accounts account's sid, authentication token, and phone number.  

Following that, open the sms_alert.py file and edit the following:  
<code>
26. twilio_number = 'TWILIO_PHONE_NUMBER'   
29. recipient = 'RECIPENT(S)_PHONE_NUMBER' 
</code>  
where 'TWILIO_PHONE_NUMBER' is the your twilio account phone number and 'RECIPENT(S)_PHONE_NUMBER' is the phone   
number of the recipient. Note, all numbers must start with the country code. Ex: '+19876543210'. 

You may adjust the time according to you preference displayed below:  
<code>48. schedule.every().day.at("13:00").do(sendMessage)</code>


## Usage
In oder to execute this program all you will have to do is open up command line session. Following that, migrate to the directory  
with the sms_alert.py file. First, the twilio account's sid and authentication token must be loaded in to the environment variables.  
This can be accomplished by entering the following:  
<code>
export TWILIO_ACCOUNT_SID='twilio_account_sid'  
export TWILIO_AUTH_TOKEN='twilio_auth_token'
</code>  

Following that, to execute the sms_alert.py file enter the command below:  
<code>python3 sms_alert.py</code>  
If successful, the script will return a status code.
