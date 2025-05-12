import reflex as rx

from app.components.home import home
#from app.components.search import search
from app.components.categories import categories
from app.components.emojis import db

def index():
    return rx.box(
        home(),
        categories(),
    )

app = rx.App()
app.add_page(index, route="/")