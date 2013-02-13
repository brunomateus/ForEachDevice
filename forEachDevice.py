#!/usr/bin/python

# forEachDevice - A helper shell script to execute adb commands in every device connected automatically
#
# Copyright (C) <2012>  
# Author: androidzin@blogspot.com
# Contact: androizinblog@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import sys

if len(sys.argv) <= 1:
	print "forEachDevice version 1.0"
	print "You should use one of adb commands. Use adb --help to see these commands"
	print "Ex:"
	print "forEachDevice install path_to_apk_file	  -To install a apk file on each connected device use"
	sys.exit(2)

#Creting string with the command and options 
options = ""
for option in sys.argv[1:]:
	options = options + " " + option
print options	

#Creating auxiliary text file with the connected device's id
os.system("adb devices | grep -v devices > tmp.txt")
os.system("awk '{print ($1) >> \"tmp2.txt\" ;}END{}' tmp.txt")

if os.path.exists("tmp.txt"):
	os.remove("tmp.txt")

f = open("tmp2.txt", "r")

#Execute a command for each connected device
for line in f:
	if line != "\n" :
		command = "adb -s %s" % (line)
		command = command.replace("\n", "")
		command +=  " " + options
		print command
		os.system(command)
f.close()

if os.path.exists("tmp2.txt"):
	os.remove("tmp2.txt")
