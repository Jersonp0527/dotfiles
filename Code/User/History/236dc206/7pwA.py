import flet as ft
from explore import explore_view  # Importa la vista de "Explorar"
from saved import saved_view      # Importa la vista de "Guardados"
from settings import settings_view # Importa la vista de "Configuraciones"

def main(page: ft.Page):
    # Contenedor para el contenido que cambiará
    content = ft.Column([explore_view()])  # Por defecto, muestra la vista "Explorar"

    # Función para manejar el cambio de pestaña
    def on_nav_change(e):
        """on_nav_change permite cambiar entre pestaña de la barra de navegación

        Args:
            e (_type_): variable de retorno de flet
        """
        # Cambia el contenido de la vista según la pestaña seleccionada
        if page.navigation_bar.selected_index == 0:
            content.controls = [saved_view()]
        elif page.navigation_bar.selected_index == 1:
            content.controls = [explore_view()]
        elif page.navigation_bar.selected_index == 2:
            content.controls = [settings_view()]
        page.update()  # Actualiza la página para reflejar el nuevo contenido

    # Configuración del título de la página
    page.title = "NavigationBar Example"

    # Configura la barra de navegación
    page.navigation_bar = ft.NavigationBar(
        selected_index=1,  # Pestaña "Explorar" seleccionada por defecto
        on_change=on_nav_change,  # Llama a la función cuando cambie la pestaña
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="Guardados"),
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configuraciones"),
        ]
    )

    # Añade el contenedor del contenido dinámico a la página
    page.add(content)

# Inicia la aplicación llamando a la función principal
ft.app(main)
