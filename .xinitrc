#! /bin/bash
#Enable Colors and Config
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources &
#Create Deamon process for Urxvt
urxvtd -q -o -f
#exec xmonad
exec awesome
