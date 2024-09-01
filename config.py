import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26541830"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ee2c107f1d4a1fdb2d1852d72f6a5c79")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Demo-yt:<db_1k8GNAZn4EBOVdHB>@demon.w0z8k.mongodb.net/?retryWrites=true&w=majority&appName=Demon")
