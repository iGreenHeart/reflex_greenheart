import reflex as rx
import datetime
from greenheart_reflex.styles.styles import Size as Size
from greenheart_reflex.styles.colors import TextColor as TextColor
import greenheart_reflex.constants as const


def footer() -> rx.Component:
    return rx.vstack(
        rx.responsive_grid(rx.image(
            src="logo.jpg",
            height=Size.VERYBIG.value,
            width=Size.VERYBIG.value,
            border_radius="50%",
            alt="Logotipo de GreenHeart"
        ),
            rx.image(
            src="Logo_UNSAM.ico",
            height=Size.VERYBIG.value,
            bg="White",
            alt="Logotipo de UNSAM",
        ), spacing=Size.BIG.value,
            columns=[1, 2]


        ),

        rx.text(
            f"@2022 - {datetime.date.today().year} hecho por Juan Cruz Bogado V0.1",
            font_size=Size.MEDIUM.value
        ),
        rx.text("Coding with love from Argentina",
                font_size=Size.MEDIUM.value,
                margin_top=Size.ZERO.value
                ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value



    )
