import reflex as rx

def footer() -> rx.Component:
    return rx.el.footer(
        rx.center(
            rx.link(
                rx.text(
                    "☄️ Created by HavertzZ ☂️",
                    size="5",
                    weight="medium",
                    align="center",  
                    color_scheme='yellow'
                ),
                href="https://havertzz.netlify.app/",
                is_external=True,  # abre en nueva pestaña
                style={"text_decoration": "none"},  # opcional: quita el subrayado
            ),
        ),
        margin_top="5px",
        padding="30px",
    )
