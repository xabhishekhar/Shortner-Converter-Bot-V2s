# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28077048"))
API_HASH = os.environ.get("API_HASH", "3fbbfeab258fffc79a79c9ae678f2a6b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6683114977:AAGQAuE1PBSXcQrnGJHyhWeVGC9drUUEz8M")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6650073089")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kiranu:kirankabot@cluster0.k5tx2bb.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6650073089")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001928382490")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "popcornpanda") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
