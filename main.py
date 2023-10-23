from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText

# Set the URL and headers (Change the amazon-url to a product you want to follow)
url = "https://www.amazon.se/dp/B073PD6YRQ"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,sv-SE;q=0.8,sv;q=0.7"
}

# Send the HTTP request
response = requests.get(url, headers=headers)

# Check for a valid response
if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.text, "lxml")
    
    # Locate the price tag
    price_tag_whole = soup.find('span', {'class': 'a-price-whole'})
    price_tag_fraction = soup.find('span', {'class': 'a-price-fraction'})

    if price_tag_whole and price_tag_fraction:
        # Extracting the text and removing any non-breaking space characters or commas
        price_whole = price_tag_whole.text.replace('\xa0', '').replace(',', '')
        price_fraction = price_tag_fraction.text
        
        # Combining the whole and fractional parts, then converting to a float
        price = float(f"{price_whole}.{price_fraction}")
        print(f"The price is SEK {price}")
    else:
        print("Price tags not found.")
else:
    print(f"Failed to retrieve the page. HTTP Status Code: {response.status_code}")

# Assuming the product title can be fetched like so:
title_tag = soup.find('span', {'id': 'productTitle'})
title = title_tag.text.strip() if title_tag else 'Unknown Product'

# Check if the price is below the target
target_price = 400
if price and price < target_price:
    # Set up the SMTP client
    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server details
    smtp.starttls()
    smtp.login('x@gmail.com', '*********')  # Use your email login details
    
    # Create the email content
    subject = f"Price Drop Alert: {title}"
    body = f"The price of {title} has dropped to SEK {price}.\nBuy now: https://www.amazon.se/dp/B073PD6YRQ"
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = 'x@gmail.com'
    msg['To'] = 'x@gmail.com'
    
    # Send the email
    smtp.sendmail('x@gmail.com', 'x@gmail.com', msg.as_string())
    smtp.quit()
    print(f"Price alert email sent for {title}!")
else:
    print(f"No price drop detected for {title}.")
