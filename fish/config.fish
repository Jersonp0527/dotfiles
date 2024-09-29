if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Deactivate greeting
set fish_greeting

# Init Zoxide
zoxide init fish | source

# Init Oh-My-Posh
# oh-my-posh init fish --config ~/.config/Oh-my-posh-themes/themes/avit.omp.json | source

# Created by `pipx` on 2024-08-15 14:58:55
set PATH $PATH /home/exodus/.local/bin

# Init Starship
starship init fish | source

# Create enviroment variables
set -x RSPOTIFY_CLIENT_ID b3b32d8696ba48ec8abb887d7a2b0a24
set -x RSPOTIFY_CLIENT_SECRET c664d7c0afc047dca18f086de3db625c
