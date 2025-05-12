import reflex as rx
from app.components.emojis import db


# Obtener las categorías únicas
emojis_categories = sorted(set(item["group"] for item in db))


class CategoryState(rx.State):
    selected_category: str = "Activities"

    def set_category(self, category: str):
        self.selected_category = category

    @rx.var
    def filtered_emojis(self) -> list[dict]:
        if not self.selected_category:
            return []
        return [
            emoji
            for emoji in db
            if emoji["group"] == self.selected_category
        ]


def categories():
    return rx.box(
        rx.center(
            rx.divider(
                size="4",
                width="90%",
            ),
        ),
        rx.heading(
            "Categories",
            size="9",
            color_scheme="crimson",
            margin_top="35px",
            align="center",
        ),
        rx.center(
            rx.grid(
                rx.foreach(
                    emojis_categories,
                    lambda category: rx.button(
                        category.capitalize(),
                        variant=rx.cond(
                            CategoryState.selected_category == category,
                            "solid",
                            "outline",
                        ),
                        height="8vh",
                        width="100%",
                        color_scheme="teal",
                        on_click=lambda c=category: CategoryState.set_category(c),
                        transition="all 0.5s",
                        size="4",
                        cursor="pointer",
                    ),
                ),
                columns="5",
                spacing="4",
                width="100%",
                max_width="1000px",
            ),
            padding="50px",
            padding_top="40px",
        ),
        rx.center(
            rx.grid(
                rx.foreach(
                    CategoryState.filtered_emojis,
                    lambda emoji: rx.button(
                        rx.vstack(  
                            rx.text(emoji["char"], size='9'),  
                            #rx.text(emoji["name"], size='2'), #to see the emojis names on the cards
                            align='center' 
                        ),
                        padding="40px",
                        radius="large",
                        cursor="pointer",
                        on_click=lambda e=emoji: [
                            rx.set_clipboard(e["char"]),  
                            rx.toast(f"Emoji {e['char']} copied!")  
                        ],
                        _hover={"background_color": "#c4cccc"},
                        transition="background-color 0.5s",
                        style={"background-color": "#85929e"}
                    ),
                ),
                columns="10",
                spacing="4",
                width="100%",
                max_width="1000px",
            )
        ),
        margin_top="50px",
    )
