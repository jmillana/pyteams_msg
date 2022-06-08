
# ==== IMPORTS SECTION ========================================================


# PYTHON
import requests

# LOCAL

# ==== CONSTANTS DEFINITIONS ==================================================


# ==== CLASS DEFINITION =======================================================

class TeamsMessage():

    # _________________________________________________________________________
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        self.payload = {
            "type": "message",
            "attachments": [],
        }

    # _________________________________________________________________________
    def add_card(self, card):
        self.payload["attachments"].append(card.payload)

    # _________________________________________________________________________
    def send(self):
        headers = {'Content-Type': 'application/json'}
        requests.post(self.webhook_url, json=self.payload, headers=headers)
