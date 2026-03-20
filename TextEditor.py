import flet as ft

class TextApp:
    def __init__(self):
        self.words_text = ft.Text("Words 0", size=16)
        self.characters_text = ft.Text("Characters 0", size=16)
        self.text_field = None

    def update_text(self, e):
        text = self.text_field.value
        self.words_text.value = f"Words {len(text.split())}"
        self.characters_text.value = f"Characters {len(text)}"
        e.page.update()

    def clear_text(self, e):
        self.text_field.value = ""
        self.words_text.value = "Words 0"
        self.characters_text.value = "Characters 0"
        e.page.update()

    def main(self, page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.text_field = ft.TextField(
            multiline=True,
            on_change=lambda e: self.update_text(e),
            width=400,
            text_align=ft.TextAlign.CENTER
        )
        
        metrics_row = ft.Row(
            [self.words_text, self.characters_text],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
        
        clear_button = ft.ElevatedButton(
            "Clear",
            on_click=lambda e: self.clear_text(e),
            width=150
        )
        
        page.add(
            self.text_field,
            metrics_row,
            clear_button
        )

app = TextApp()
ft.app(target=app.main)