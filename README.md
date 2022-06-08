# PyTeams-Msg
This module allows to build and send custom messages to Microsoft Teams Webhooks.

## Message Types
For the time being only the *message* type container has been implemented.

### AdaptiveCards
Adaptive cards are platform-agnostic snippets of UI, authored in JSON.

### Card Elements
The following are the currently implemented card elements that can be added to the AdaptiveCard sections.
- **TextBlock**: Displays texts, allowing control over font sizes, weight and color
- **Image**: Displays an image. Acceptable formats are PNG, JPEG, and GIF. The URL field allows data URI since v1.2+ 

For further information on all the available snipets and it's format check: https://adaptivecards.io/explorer/
## Sample Usage

```python
from pyteams_msg.teamsmessage import TeamsMessage
from pyteams_msg.adaptivecard import AdaptiveCard
from pyteams_msg.sections import TextBlock, Image
    
my_msg = TeamsMessage(webhook=os.environ["TEAMS_WEBHOOK"])
card = AdaptiveCard()
title_section = TextBlock(
    "Some cool clickbait",
    size=TextBlock.SIZE_EXTRA_LARGE
    color=TextBlock.COLOR_ACCENT
)
body_section = TextBlock("Beer Ipsum... yada yada")
image_from_url = Image("https://cdn.pixabay.com/photo/2016/11/21/15/48/dog-1846066_960_720.jpg")
image_from_file = Image()
image_from_file.add_image("path/to/some/file")
card.add_section(title_section)
card.add_section(body_section)
card.add_section(image_from_url)
card.add_section(image_from_file)
my_msg.add_card(card)
my_msg.send()
```
