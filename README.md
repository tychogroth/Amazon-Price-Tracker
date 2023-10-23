# Amazon Price Tracker

This project is designed to track the price of a specific product on Amazon. When the price of the product drops below a set target price, an email alert is sent to notify you of the price drop.

## Dependencies

- BeautifulSoup
- requests
- smtplib
- email

You can install the required modules using pip:

```bash
pip install beautifulsoup4 requests
```

## How to Use

1. Update the `url` variable with the Amazon URL of the product you want to track.
2. Set the `target_price` to the price you're willing to pay for the product.
3. Update the SMTP client setup with your email server details, login credentials, and recipient email address.
4. Run the script to start tracking the price.

## Code Overview

The script does the following:

1. Sends an HTTP request to the Amazon product page.
2. Parses the HTML of the page to extract the current price and product title.
3. Checks if the price is below the target price.
4. If the price is below the target, it sets up an SMTP client.
5. Creates an email with the product details and sends the email to the specified recipient.

## Notes

- Be sure to use your email server and login details for the SMTP client setup.
- The script prints the status to the console, whether it's a price drop alert or no price drop detected.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
