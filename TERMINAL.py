import cmd
import os 

import queue
import threading, time, random

from cmd import Cmd

class Prompt(Cmd):
	prompt = 'FAI/SYSTEM> '	
	intro = "Welcome! Type ? to list commands"

	def do_help(self, line):
		print('\n')
		print('exec: Execute tous les scripts dans lordre.')

	def do_exit(self, inp):
		print('Closing')
		return True

	def do_EOF(self, line):
		return True

	def do_get(self, line):
		print('Executing first script...')
		import LINKCHECK
		print('Next command : second')

	def do_second(self, line):
		print('Executing second script...')
		import SCRAPPER
		print('Next command : third')

	def do_third(self, line):
		print('Executing third script...')
		import NETTOYEUR
		print('Next command : fourth')

	def do_fourth(self, line):
		print('Executing fourth script...')
		import TRANSLATING
		print('Next command : fourth')

	def do_fifth(self, line):
		print('Executing fifth script...')
		import COMPAR
		print('Next command : wordclass')

	def do_wordclass(self, line):
		print('Soon(tm)')
		return True

#delall commands ---------------------

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
