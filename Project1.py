# Import required modules: requests, BeautifulSoup, smtplib, schedule, time, pandas (optional)
import requests 
from bs4 import BeautifulSoup 
import time
import schedule
import smtplib 
from email.message import EmailMessage


# Define email credentials and settings (sender, app password, recipient, SMTP server)
Sender_email = input('Enter Your Eamil: ')
Sender_password = input('Enter Your App Passwored: ')
Receiver_email = input('Enter the rveiver email: ')
smtp_code = 'smtp.gmail.com'
smtp_port = 465 

# Create a function to fetch news headlines and summaries from a trusted source (BBC/sports)
def get_content():
    request = 'https://www.bbc.com/sport'
    response = requests.get(request)
    soup = BeautifulSoup(response.content, 'html.parser')
        
    # Extract article titles and links using CSS selectors or .find()/.find_all()
    Headlines = []
    for h3 in soup.find_all('h3'):
        text = h3.text.strip()
        Headlines.append(text)
    return Headlines

    Headlines = Headlines[:5]
    # Store results in a pandas DataFrame for clean formatting
    df = pd.DataFrame(Headlines, columns=['Headlines'])
    return df

# start make the function for the html the DateFrame
def html_dateframe(df):
    if df.empty:
        return 'Not Found News Today'
    body = '<h2>News Tody From BBC Is Deffrant</h2>'
    for headline in df['Headlines']:
        body += f"<p>{headline}</p>"
    return body

# Store results in a pandas DataFrame for clean formatting
def send_email(body):
    msg = EmailMessage()
    msg['from'] = Sender_email
    msg['to'] = Receiver_email
    msg['subject'] = 'News Today From BBC'
    
    # connect the SMTP server and send the email
    with smtplib.SMTP_SSL(smtp_code, smtp_port) as server:
        server.login(Sender_email, Sender_password)
        server.send_message(msg)
    print('Email Send Successfully')     

# function for that function all
def jop():
    df = get_content()
    body = html_dateframe(df)
    send_email(body)

# start make the schedule to send the email specific time
schedule.every(10).minutes.do(jop)

while True:
    schedule.run_pending()
    time.sleep(10)