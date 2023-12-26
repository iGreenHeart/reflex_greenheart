from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font, FontWeight

# Constantes
MAX_WIDTH = "600px"

# Tamaños
# 1 em = 16px
STYLE_SHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@700:200&display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa&display=swap"
]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERYBIG = "4em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.EXTRA_LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.Heading: {
        "size": "lg",
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.BOLD.value,

    },

    rx.Button: {
        # "font_weight": "normal",
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_aling": "start",

        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}

    }
}
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)
title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    size="lg"
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.BOLD.value,
    font_size=Size.LARGE.value,
    color=TextColor.HEADER.value
)
button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.EXTRA_LIGHT.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.BODY.value
)
