import reflex as rx
import greenheart_reflex.styles.styles as styles


def title(text: str) -> rx.component:
    return rx.heading(
        text,
        size="lg",
        style=styles.title_style

    )
