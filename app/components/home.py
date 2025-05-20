import reflex as rx

def home():
    return rx.box(
        rx.vstack(
            rx.heading(
                "EmojiBox📦",
                font_size="100px",
                color_scheme="yellow"
            ),
            rx.text(
                "Discover a world of emojis categorized by activities, objects, and more. Find the perfect emoji for every moment and express yourself in style!",
                max_width="550px",
                text_align="center",
                margin_top="50px"
            ),
            align="center"
        ),
        margin_top="100px",
    )