#!/usr/local/bin/python3

import sys
import os
import os.path
import shutil
import traceback

from git import Repo
from git import Git

def list_directory(directory):
	if directory == "parent":
		folder = os.path.dirname(os.getcwd())
	elif directory == "self":
		folder = os.getcwd()
	print("+ Listing directory: " + folder)
	for item in os.listdir(folder):
		print(" - " + item)

def delete_directory(directory):
	if os.path.isdir(directory):
		shutil.rmtree(directory)
		print("\n-- Deleted '%s' directory successfully" % directory)

if __name__ == '__main__':
	if len(sys.argv) > 2:
		action = sys.argv[1]
		if action == "list_directory":
			list_directory(sys.argv[2])
		else:
			print("Action not valid")
