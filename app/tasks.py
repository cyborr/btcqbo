import time
from app import qbo as qbo

def repeat_refresh():
    while True:
        time.sleep(3000)
        qbo.refresh_stored_tokens()
