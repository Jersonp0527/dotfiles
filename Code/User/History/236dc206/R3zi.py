import flet as ft

def main(page: ft.Page):

    # Función para manejar la selección de destino
    def on_nav_change(e):
        if page.navigation_bar.selected_index == 0:
            page.views.clear()
            page.add(ft.Text("Guardados"))
        elif page.navigation_bar.selected_index == 1:
            page.views.clear()
            page.add(ft.Text("Explorar"))
        elif page.navigation_bar.selected_index == 2:
            page.views.clear()
            page.add(ft.Text("Configuraciones"))

    # Configuramos el título de la página
    page.title = "NavigationBar Example"
    
    # Creamos la barra de navegación
    page.navigation_bar = ft.NavigationBar(
        selected_index=1,  # Comenzamos con la pestaña de "Explorar"
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="Guardados"),
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configuraciones"),
        ]
    )
    
    # Mostramos la vista inicial (Explorar)
    page.add(ft.Text("Explorar"))

ft.app(main)
