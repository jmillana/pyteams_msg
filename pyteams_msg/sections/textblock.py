
# ==== IMPORTS SECTION ========================================================


# PYTHON

# LOCAL
from pyteams_msg.sections.section import Section

# ==== CONSTANTS DEFINITIONS ==================================================


# ==== CLASS DEFINITION =======================================================
class TextBlock(Section):

    # ==== ATTRIBUTES =========================================================
    # SIZE
    SIZE_SMALL = "Small"
    SIZE_DEFAULT = "Default"
    SIZE_MEDIUM = "Medium"
    SIZE_LARGE = "Large"
    SIZE_EXTRA_LARGE = "ExtraLarge"
    # WEIGHT
    WEIGHT_LIGHT = "Lighter"
    WEIGHT_DEFAULT = "Default"
    WEIGHT_BOLD = "Bolder"
    # COLOR
    COLOR_DEFAULT = "Default"  # Automatically set the propper color for dark/light theme  # noqa: E501
    COLOR_DARK = "Dark"  # White
    COLOR_LIGHT = "Light"  # Gray
    COLOR_ACCENT = "Accent"  # purple
    COLOR_GOOD = "Good"  # green
    COLOR_WARNING = "Warning"  # yellow
    COLOR_ATTENTION = "Attention"  # red

    def __init__(self, text: str, size: int = None, weight: str = None,
                 color: str = None):

        # Type of block
        self._type = "TextBlock"
        # Text block
        self.text = text
        # Layout
        self.spacing = None
        self.separator = False
        self.horizontal_alignment = None
        self.height = None
        self.wrap = True
        # Style
        self.font_type = None
        self.size = size
        self.weight = weight
        self.color = color
        self.is_subtle = False

    def get_payload(self):
        payload = {
            "type": self._type,
            "text": self.text
        }
        if self.spacing is not None:
            payload["spacing"] = self.spacing
        if self.separator is not None:
            payload["separator"] = self.separator
        if self.horizontal_alignment is not None:
            payload["horizontalAlignment"] = self.horizontal_alignment
        if self.height is not None:
            payload["height"] = self.height
        if self.wrap is not None:
            payload["wrap"] = self.wrap
        if self.font_type is not None:
            payload["fontType"] = self.font_type
        if self.size is not None:
            payload["size"] = self.size
        if self.weight is not None:
            payload["weight"] = self.weight
        if self.color is not None:
            payload["color"] = self.color
        if self.is_subtle is not None:
            payload["isSubtle"] = self.is_subtle
        return payload
