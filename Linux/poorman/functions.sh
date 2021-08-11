#!/bin/bash

function call_cmd(){
	xte "str $1"
	sleep 0.5
	xte "key Return"
}

function ctrl(){
	xte "keydown Control_L" "key $1" "keyup Control_L"
}

function hide_guake(){
	xte "keydown F12" "key Return" "key Return" "keyup F12"
	sleep 0.5
}

function alt_tab(){
	xte "keydown Alt_L" "keydown Tab" "keyup Alt_L" "keyup Tab"
	sleep 0.5
}


# Added variables so stablize_shell.sh will work with ohmyzsh
COLS=$(tput cols)
ROWS=$(tput lines)
