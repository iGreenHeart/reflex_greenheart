import reflex as rx
from greenheart_reflex.components.link_icon import link_icon
from greenheart_reflex.components.info_text import info_text
from greenheart_reflex.styles.styles import Size as Size
from greenheart_reflex.styles.fonts import Font, FontWeight
from greenheart_reflex.styles.colors import Color as Color
from greenheart_reflex.styles.colors import TextColor as TextColor
import greenheart_reflex.constants as const


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Green Heart",
                src="logo.jpg",
                size="xl",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.TERCIARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Juan Cruz Bogado",
                    size="xl"
                ),
                rx.text(
                    "iGreenHeart",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value,
                    font_size=Size.DEFAULT.value,
                    font_family=Font.DEFAULT.value,
                    font_weight=FontWeight.EXTRA_LIGHT.value

                ),
                rx.hstack(
                    link_icon("icons/instagram.svg",
                              const.LINK_IG,
                              "Instagram"
                              ),
                    link_icon("icons/github.svg",
                              const.LINK_GITHUB,
                              "Github"
                              ),
                    link_icon("icons/ketoivy.png",
                              const.LINK_KETOIVY,
                              "Keto Ivy"
                              ),
                    color=Color.TERCIARY.value,
                ),
                align_items="start",
                spacing=Size.SMALL.value

            ),
            spacing=Size.DEFAULT.value
        ),

        rx.flex(
            rx.box(
                rx.link(
                    "CARRERA",
                    font_weight="bold",
                    color=Color.TERCIARY.value,
                    href=const.LINK_TPI
                ),
                rx.link(" TPI UNSAM",
                        font_size=Size.DEFAULT.value,
                        color=TextColor.BODY.value,
                        href=const.LINK_TPI),
            ),
            rx.spacer(),
            info_text("LENGUAJES", "Python"),
            rx.spacer(),
            info_text("DB", "MongoDB, SQL"),
            width="100%"
        ),


        rx.text(
            """Hola! Soy Juan, argentino actualmente estudiando una tecnicatura en programación informática
            en la Universidad Nacional de San Martín (UNSAM). Esta web está hecha con python puro y Reflex. Como objetivo,
            quiero como programador Backend utilizando mis habilidades y mi amor por codear para contribuir en proyectos de
            desarrollo en software.
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start",
        width="100%"

    )
