#!/bin/sh
tmux new-session -d 'python ~/PycharmProjects/vk-to-mpd/main.py'
tmux split-window -h 'ncmpc'
tmux select-pane -t :.+
tmux -2 attach-session -d
