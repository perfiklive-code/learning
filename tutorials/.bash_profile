
# Setting PATH for Python 3.12
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:${PATH}"
export PATH
# Add Homebrew's executable directory to the front of the PATH
export PATH=/usr/local/bin:$PATH

##
# Your previous /Users/viktor/.bash_profile file was backed up as /Users/viktor/.bash_profile.macports-saved_2024-01-14_at_10:56:10
##

# MacPorts Installer addition on 2024-01-14_at_10:56:10: adding an appropriate PATH variable for use with MacPorts.
export PATH="/opt/local/bin:/opt/local/sbin:$PATH"
# Finished adapting your PATH environment variable for use with MacPorts.

#

alias codepy='tmux new -s python -d
tmux split-window -h -t python:0.0
tmux resize-pane -R 30
tmux send-keys -t python:0.0 "cd Documents/python/" Enter
tmux send-keys -t python:0.0 "vim ~/new.py"  Enter
tmux select-pane -L -t python
tmux a -t python'
