import reflex as rx
from app.components.emojis import db

# Obtener las categorías únicas
emojis_categories = list(set(item["category"] for item in db))


class CategoryState(rx.State):
    selected_category: str = ""

    def set_category(self, category: str):
        self.selected_category = category

    @rx.var
    def filtered_emojis(self) -> list[str]:
        return [
            emoji["htmlCode"][0]
            for emoji in db
            if emoji["category"] == self.selected_category
        ]


def categories():
    return rx.box(
        rx.center(
            rx.divider(
                size='4',
                width="90%",
            ),
        ),
        rx.heading(
            "Categories",
            size="9",
            color_scheme="crimson",
            margin_top="35px",
            align="center"
        ),
        rx.center(
            rx.grid(
                rx.foreach(
                    emojis_categories,
                    lambda category: rx.button(
                        category.capitalize(),
                        variant=rx.cond(
                            CategoryState.selected_category == category,
                            "solid",  # seleccionado
                            "outline"  # no seleccionado
                        ),
                        height="5vh",
                        width="100%",
                        color_scheme="teal",
                        on_click=lambda c=category: CategoryState.set_category(c),
                        transition="all 0.5s",
                        size='4',
                        cursor="pointer"
                    ),
                ),
                columns="4",
                spacing="4",
                width="100%",
                max_width="1000px",
            ),
            padding="50px",
            padding_top="40px",
        ),
        # Aquí mostramos los emojis filtrados según la categoría
        rx.center(
            rx.grid(
                rx.foreach(
                    CategoryState.filtered_emojis.to(list[str]),
                    lambda emoji: rx.box(
                        rx.text(emoji["htmlCode"][0], font_size="40px"),
                        rx.text(emoji["name"], size="2", align="center"),
                        padding="10px",
                        border="1px solid #e0e0e0",
                        border_radius="10px",
                        text_align="center"
                    ),
                ),
                columns="6",
                spacing="4",
                width="100%",
                max_width="1000px",
                margin_top="30px"
            )
        ),
        margin_top="50px",
    )
