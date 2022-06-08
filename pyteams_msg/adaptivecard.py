
# ==== IMPORTS SECTION ========================================================


# PYTHON

# LOCAL
from pyteams_msg.sections.section import Section

# ==== CONSTANTS DEFINITIONS ==================================================
CARD_VERSION = "1.0"
ADAPTIVE_CARD_SCHEMA = "http://adaptivecards.io/schemas/adaptive-card.json"


# ==== CLASS DEFINITION =======================================================
class AdaptiveCard():

    def __init__(self):
        self.payload = {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "contentUrl": None,
            "content": {
                "$schema": ADAPTIVE_CARD_SCHEMA,
                "type": "AdaptiveCard",
                "version": CARD_VERSION,
                "body": [],
                "padding": None
            }
        }

    def add_section(self, section: Section):
        self.payload["content"]["body"].append(section.get_payload())
