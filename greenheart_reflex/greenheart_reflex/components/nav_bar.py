import reflex as rx
import greenheart_reflex.styles.styles as styles
from greenheart_reflex.styles.styles import Size as Size
from greenheart_reflex.styles.colors import TextColor as TextColor
from greenheart_reflex.styles.colors import Color as Color
import greenheart_reflex.styles.styles as styles


def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("i", color="white"),
            rx.span("Green", color=Color.TERCIARY.value),
            rx.span("Heart", color="white"),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
