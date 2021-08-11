#!/bin/bash

source "/home/porro/Documents/Scripts/poorman/functions.sh"

COLS=137
ROWS=55

hide_guake
call_cmd "script /dev/null -c bash"
#call_cmd "python -c 'import pty; pty.spawn(\"/bin/bash\")'"
ctrl Z
call_cmd "stty raw -echo"
call_cmd "fg"
call_cmd "export TERM=xterm"
call_cmd "stty rows $ROWS columns $COLS"
call_cmd "alias ll='ls -ltra'"
call_cmd "reset"
