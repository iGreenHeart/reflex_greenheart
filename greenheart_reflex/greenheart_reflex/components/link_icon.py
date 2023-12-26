import reflex as rx
import greenheart_reflex.styles.styles as styles
from greenheart_reflex.styles.styles import Size as Size


def link_icon(image: str, url: str, alt: str) -> rx.component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.BIG.value,
            alt=alt
        ),
        href=url,
        is_external=True,
    )
