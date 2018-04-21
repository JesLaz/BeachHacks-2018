from __future__ import print_function
from telesign.messaging import MessagingClient

customer_id = ""
api_key = "nsDVlYZ0/L8cbD9OJHZqrzRONb1JFujQztb/Wi6qXWRcZLyRna3CiMW+F3NFbJ0zlIggNb9hQaSqDZj+hwb9wQ=="

phone_number = "**********"
message = "You're scheduled for a dentist appointment at 2:30PM."
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)
response = messaging.message(phone_number, message, message_type)
  
