import cmd
import os 

import queue
import threading, time, random

from cmd import Cmd

class Prompt(Cmd):
	prompt = 'FAI/SYSTEM> '	
	intro = "Welcome! Type ? to list commands"

	def do_help(self, line):
		print('hello')

	def do_exit(self, inp):
		print('Closing')
		return True

	def do_EOF(self, line):
		return True

	def do_delall(self, line):
		print('Deleting all data files.')

		if os.path.exists("complex.csv"):
			os.remove("complex.csv")
		else:
			print("The file(s) does not exist")
			pass
		
		if os.path.exists("reservations.csv"):
			os.remove("reservations.csv")
		else:
			print("The file(s) does not exist")
			pass

		if os.path.exists("nottranslated.csv"):
			os.remove("nottranslated.csv")
		else:
			print("The file(s) does not exist")
			pass

		if os.path.exists("not_translated_final.csv"):
			os.remove("not_translated_final.csv")
		else:
			print("The file(s) does not exist")
			pass

		if os.path.exists("final_reservations.csv"):
			os.remove("final_reservations.csv")
		else:
			print("The file(s) does not exist")
			pass

		if os.path.exists("final_complex.csv"):
			os.remove("final_complex.csv")
		else:
			print("The file(s) does not exist")
			pass

	def default(self, inp):
		if inp == 'exit' or inp == 'quit' or inp =='x':
			return self.do_exit(inp)

if __name__ == '__main__':
    Prompt().cmdloop()



