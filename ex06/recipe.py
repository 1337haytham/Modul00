

cookbook = {
	"Sandwich":{"ingredients":["ham","bread","cheese","tomatoes"],"meal":"lunch","prep_time":10},
	"Cake":{"ingredients":["flour","sugar","eggs"],"meal":"dessert","prep_time":60},
	"Salad":{"ingredients":["avocado","arugula","tomatoes","spinach"],"meal":"lunch","prep_time":15}
}

def recipe_name():
	print("Available recipe are:")
	for k,i in cookbook.items():
		print(k)

def recipe_details(name):
	print("Recipe for {0}:".format(name))
	print(" Ingredients list: ",end='')
	print(cookbook[name]["ingredients"])
	print(" To be eaten for {0}.".format(cookbook[name]["meal"]))
	print(" Takes {0} minutes of cooking.".format(cookbook[name]["prep_time"]))

def recipe_delete(name):
	cookbook.pop(name)

def recipe_add():
	ing = []
	name = input("Enter the recipe name:\n")
	i = input("Enter the ingrediens: (empty to stop)\n")
	while i:
		ing.append(i)
		i = input("")
	meal = input("Enter the meal type:\n")
	while 1:
		try:
			time = int(input("Enter preparation time:\n"))
			if time > 0:
				break
			print("Please enter a valide time!")
		except:
			print("Please enter a valide time!")
	cookbook.update({name:{"ingredients":ing,"meal":meal,"prep_time":time}})

print("Welcome to the Python Cookbook !")
while 1:
	i = input("""
List of available option:
  1: Add a recipe
  2: Delete a recipe
  3: Print a recipe
  4: Print the cookbook
  5: Quit

Please select an option:
""")
	if i == '1':
		recipe_add()
	elif i == '2':
		recipe = input("Enter the recipe name to delete:\n")
		try:
			recipe_delete(recipe)
		except:
			print("This recipe does not exist")
	elif i == '3':
		recipe = input("Enter recipe name to get details:\n")
		try:
			recipe_details(recipe)
		except:
			print("This recipe does not exist")
	elif i == '4':
		recipe_name()
	elif i == '5':
		print("Cookbook closed. Goodbye !")
		break
	else:
		print("Sorry, this option does not exist.")
