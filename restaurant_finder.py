

from restaurantData import *
from node import Node
from linkedlist import LinkedList
#from hashmap import HashMap

##############
# TO DO LIST #
##############

# Maybe find a way to use Hash Maps

# Maybe make a better banner function that takes in a message
# and makes a banner of the appropriate size

# Opening title banner
def banner():
   print()
   print('+------------------------------+')
   print('|                              |')
   print('| Welcome to Restaurant Finder |')
   print('|                              |')
   print('+------------------------------+')
   print()
   print('Type exit at anytime to end program')

# Create a LinkedList with the food types
# from the list - types in restaurantData.py
def make_food_type_list():
   food_types = LinkedList()
   for food_type in types:
      food_types.add_node(food_type)
   return food_types

# Create a LinkedList of LinkedLists with the data
# from the list  - restaurant_data in restaurantData.py
def make_restaurant_list():
   restaurants_list = LinkedList()
   for food_type in types:
      restaurants_sublist = LinkedList()
      for restaurant in restaurant_data:
         if restaurant[0] == food_type:
            restaurants_sublist.add_node(restaurant)
      restaurants_list.add_node(restaurants_sublist)
   return restaurants_list

# Finds food types that begin with choice and
# returns a list of all food types that match
def get_matches(choice, food_type_list):
   matches = []
   food_type_head = food_type_list.get_head_node()
   while food_type_head is not None:
      current_food_type = str(food_type_head.get_value())
      if current_food_type.startswith(choice):
         matches.append(current_food_type)
      food_type_head = food_type_head.get_next_node()
   return matches

# uses the food type list as an argument
# returns the food type the user would like
# to find restaurants for or exit if the user wishes
# to quit
def get_food_type(food_type_list):
   while True:
      # get beginning of food type
      choice = str(input('Enter the beginning of the type of food you would like: ')).lower()

      #checks if user wants to end program
      if choice == 'exit':
         return choice

      # find matching food types
      matches = get_matches(choice, food_type_list)

      # if no matches try again
      if len(matches) == 0:
         print(f'There are no food types that begin with {choice} in your area. Try again.')
         continue

      # print matching food types
      for match in matches:
         print(match)

      # User confirms food type choice once narrowed down to just one option
      if len(matches) == 1:
         print(f'{matches[0]} is the only food type that matches.')
         print(f'Would you like to see all the {matches[0]} restaurants in the area?')
         confirm_choice = str(input('Enter y for yes and n for no: ')).lower()

         # Prints restaurants with that food type if y
         if confirm_choice == 'y':
            print(f'You have chosen {matches[0]} food.')
            return matches[0]
         # or exit program
         elif confirm_choice == 'exit':
            return confirm_choice

# Takes in food_type and restaurant list and displays restaurants
# of that food type
def display_food_type_restaurants(food_type, restaurant_list):
   restaurant_head = restaurant_list.get_head_node()
   while restaurant_head.get_next_node() is not None:
      sub_restaurant_head = restaurant_head.get_value().get_head_node()
      if sub_restaurant_head.get_value()[0] == food_type:
         while sub_restaurant_head.get_next_node() is not None:
            print()
            print(f'Name: {sub_restaurant_head.get_value()[1]}')
            print(f'Price: {sub_restaurant_head.get_value()[2]}/5')
            print(f'Rating: {sub_restaurant_head.get_value()[3]}/5')
            print(f'Address: {sub_restaurant_head.get_value()[4]}')
            print()
            sub_restaurant_head = sub_restaurant_head.get_next_node()
      restaurant_head = restaurant_head.get_next_node()

# Finds out if user wants to find another restaurant or quit
def get_restart():
   print('Would you like to find another restaurant?')
   restart = str(input('Enter y for yes and n for no: ')).lower()
   return restart

# Main Function
def main():
   #Load data into LinkedLists
   food_type_list = make_food_type_list()
   restaurant_list = make_restaurant_list()

   # display opening banner
   banner()

   while True:
      # get food type
      food_type = get_food_type(food_type_list)

      # exit check
      if food_type == 'exit':
         print('Thank you for using Restaurant Finder.')
         break

      #display retaurants of food type
      display_food_type_restaurants(food_type, restaurant_list)

      restart = get_restart()
      if restart in ['n', 'exit']:
         print('Thank you for using Restaurant Finder.')
         break

##### MAIN LINE #####

main()

##### END #####
