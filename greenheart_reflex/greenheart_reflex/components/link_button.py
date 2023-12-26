import reflex as rx
import greenheart_reflex.styles.styles as styles
from greenheart_reflex.styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    margin=styles.Size.ZERO.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )
