import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()
CLIENT_ID = "e18698933cb347c9a343c8d25ec9616f"
CLIENT_SECRET ="995e3dc1447f4236869c280c18049390"

client_id = os.environ.get("e18698933cb347c9a343c8d25ec9616f")
client_secret = os.environ.get("447f4236869c280c18049390")