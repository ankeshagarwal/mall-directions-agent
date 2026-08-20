import os
from dotenv import load_dotenv

load_dotenv()

# Flask Configuration
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
DEBUG = FLASK_ENV == 'development'
PORT = int(os.getenv('PORT', 5000))

# Mall Configuration
MALL_NAME = "Premium Shopping Mall"
MALL_LOCATION = "Downtown District"
MALL_PHONE = "1-800-MALL-HELP"
MALL_WEBSITE = "https://www.premiumshoppingmall.com"

# Operating Hours
OPERATING_HOURS = {
    "monday_to_friday": "10:00 AM - 10:00 PM",
    "saturday_sunday": "9:00 AM - 11:00 PM",
    "public_holidays": "9:00 AM - 10:00 PM"
}

# Agent Settings
AGENT_NAME = "Mall Guide Assistant"
AGENT_GREETING = "Welcome to the Premium Shopping Mall! I'm your personal shopping guide. How can I help you today?"
