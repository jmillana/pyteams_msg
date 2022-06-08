
# ==== IMPORTS SECTION ========================================================


# PYTHON
import base64

# LOCAL
from pyteams_msg.sections.section import Section

# ==== CONSTANTS DEFINITIONS ==================================================
MAX_IMAGE_SIZE = 1024 * 28  # 28Kb


# ==== CLASS DEFINITION =======================================================
class Image(Section):

    def __init__(self, url: str = None, size: int = None,
                 alt_text: str = None):
        # Type of block
        self._type = "Image"
        # Image block
        self.url = url
        self.alt_text = alt_text
        # Layout
        self.spacing = None
        self.separator = False
        self.horizontal_alignment = None
        self.size = size
        self.px_width = None
        self.px_height = None
        # Style
        self.person = False
        self.bg_color = None

    def get_payload(self):
        payload = {
            "type": self._type,
            "url": self.url,
        }
        if self.alt_text is not None:
            payload["altText"] = self.alt_text
        if self.spacing is not None:
            payload["spacing"] = self.spacing
        if self.separator:
            payload["separator"] = self.separator
        if self.horizontal_alignment is not None:
            payload["horizontalAlignment"] = self.horizontal_alignment
        if self.size is not None:
            payload["size"] = self.size
        if self.px_width is not None:
            payload["width"] = self.px_width
        if self.px_height is not None:
            payload["height"] = self.px_height
        if self.person:
            payload["person"] = self.person
        if self.bg_color is not None:
            payload["backgroundColor"] = self.bg_color
        return payload

    def add_url(self, url):
        self.url = url

    def add_image(self, image_path):
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        decoded_image = base64.b64encode(image_data).decode("utf-8")
        if len(decoded_image) > MAX_IMAGE_SIZE:
            raise Exception("Image is too big")
        self.url = f"data:image/png;base64,{decoded_image}"
