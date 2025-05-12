import reflex as rx

def search():
    return rx.box(
        rx.vstack(
            rx.input(
                placeholder="Search...",
                color_scheme="yellow",
                margin_top="25px",
            ),
            align="center",
            text_align="center",
        )
    )