import flet as ft

def main(page: ft.Page):
    # Función para manejar el cambio de pestañas
    def on_tab_change(e):
        print(f"Current tab: {tabs.value}")

    # Definir el contenido de cada panel
    explorer_panel = ft.Text("Explorador de archivos")
    settings_panel = ft.Text("Configuraciones")
    saved_panel = ft.Text("Elementos guardados")

    # Crear las pestañas
    tabs = ft.Tabs(
        selected_index=0,
        on_change=on_tab_change,
        tabs=[
            ft.Tab(text="Explorador", content=explorer_panel),
            ft.Tab(text="Configuraciones", content=settings_panel),
            ft.Tab(text="Guardados", content=saved_panel),
        ],
        expand=1,
    )

    # Añadir las pestañas a la página
    page.add(ft.SafeArea(tabs))

ft.app(target=main)
