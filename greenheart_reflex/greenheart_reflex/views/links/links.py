import reflex as rx
from greenheart_reflex.components.link_button import link_button
from greenheart_reflex.components.title import title
from greenheart_reflex.styles.styles import Size as Size
import greenheart_reflex.constants as const


def links() -> rx.Component:
    return rx.vstack(
        title("Proyectos"),
        link_button(
            "typing_game_asm",
            "Proyecto Final de Sistemas de Procesamiento de Datos",
            "icons/unsamlogo.png",
            const.LINK_TYPING_GAME),
        title("Contacto"),
        link_button(
            "Email",
            "juancbogadoo@gmail.com",
            "icons/envelope-solid.svg",
            f"mailto:juancbogadoo@gmail.com"
        ),
        link_button(
            "Linkedin",
            "Curriculum y mensajeria",
            "icons/linkedin.svg",
            const.LINK_LINKEDIN
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )
