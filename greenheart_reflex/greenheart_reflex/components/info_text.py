import reflex as rx
import greenheart_reflex.styles.styles as styles
from greenheart_reflex.styles.styles import Size as Size
from greenheart_reflex.styles.colors import TextColor as TextColor
from greenheart_reflex.styles.colors import Color as Color
from greenheart_reflex.styles.fonts import Font, FontWeight


def info_text(title: str, body: str) -> rx.component:
    return rx.box(
        rx.span(
            title,
            color=Color.TERCIARY.value,
            font_family=Font.TITLE.value,
            font_weight=FontWeight.MEDIUM.value
        ),
        f" {body}",
        font_size=Size.DEFAULT.value,
        color=TextColor.BODY.value,
        font_family=Font.DEFAULT.value,
        font_weight=FontWeight.EXTRA_LIGHT.value
    )
