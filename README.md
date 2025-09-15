# Dotfiles de Jersonp0527

Este repositorio contiene mis archivos de configuración (dotfiles) para diversas aplicaciones y entornos en Linux y Windows. Los dotfiles permiten personalizar y versionar la configuración de tu entorno de desarrollo y usuario.

## Estructura del repositorio

- **fish/**: Configuración del shell Fish (archivos, funciones, temas y plugins).
- **hypr/**: Configuración de Hyprland (gestor de ventanas dinámico para Wayland).
- **kitty/**: Configuración del emulador de terminal Kitty.
- **ookla/**: Configuración y resultados de Speedtest CLI.
- **tmux/**: Configuración y plugins de tmux (multiplexor de terminal).
- **transmission/**: Configuración de Transmission (cliente BitTorrent).
- **waybar/**: Configuración y estilos de Waybar (barra de estado para Wayland).
- **wofi/**: Estilos para Wofi (launcher para Wayland).
- **QtProject.conf**: Configuración global de proyectos Qt.
- **starship.toml**: Configuración de Starship (prompt universal).

## Instalación

Puedes clonar este repositorio y enlazar los archivos de configuración a tu directorio home usando enlaces simbólicos. Ejemplo:

```sh
# En Linux
ln -s /ruta/a/dotfiles/fish ~/.config/fish
ln -s /ruta/a/dotfiles/kitty ~/.config/kitty
# ...
```

En Windows, puedes usar `mklink` para crear enlaces simbólicos.

## Recomendaciones
- Revisa cada archivo antes de usarlo para adaptarlo a tus necesidades.
- Algunos archivos pueden requerir software adicional (Hyprland, Fish, Kitty, etc.).

## Licencia

Estos dotfiles están bajo la licencia MIT. Úsalos y modifícalos libremente.
