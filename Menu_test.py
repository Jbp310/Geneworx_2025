from pybricks.tools import hub_menu
from example_file import example_func()

#make a menu to choose letters/numbers
seleted = hub_menu("H", "S", "L")



#based on selection, run a program
if selected == "H":
	example_func()
