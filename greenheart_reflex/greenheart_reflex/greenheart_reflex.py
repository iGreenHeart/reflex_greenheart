import reflex as rx
from greenheart_reflex.components.nav_bar import nav_bar
from greenheart_reflex.components.footer import footer
from greenheart_reflex.views.headers.header import header
from greenheart_reflex.views.links.links import links
import greenheart_reflex.styles.styles as styles
from greenheart_reflex.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:

    return rx.box(
        nav_bar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLE_SHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="GreenHeart's Page",
    description="Hola! Soy GreenHeart, Futuro técnico en programación y programador en backend.",
    image="logo.jpg"
)
app.compile()
