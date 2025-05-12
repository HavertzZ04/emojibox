import reflex as rx

from app.components.home import home
from app.components.categories import categories
from app.components.emojis import db
from app.components.footer import footer

def index():
    return rx.box(
        home(),
        categories(),
        footer()
    )

app = rx.App()
app.add_page(index, route="/", title='EmojiBox')