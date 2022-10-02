from unicodedata import category
from gameData import *
from Linkedlist import LinkedList

#Create a linkedList of game categories
def get_categories(game_data):
    list_of_categories = LinkedList()
    categories = []
    for game in game_data:
        for cat in game[2]:
            if cat not in categories:
                categories.append(cat)
                list_of_categories.insert_beggining(cat)
    return categories
#Generate a list of game platforms
def get_platform_list(game_data):
    platforms = []
    for game in game_data:
        for platform in game[1]:
            if platform not in platforms:
                platforms.append(platform)
    return platforms

#Create a linkedList data structure with all games
def get_games(game_data):
    list_of_games = LinkedList()
    categories = get_categories(game_data)
    for cat in categories:
        list_of_games_by_cat = LinkedList()
        for game in game_data:
            for game_cat in game[2]:
                if game_cat == cat:
                    list_of_games_by_cat.insert_beggining(game)
        list_of_games.insert_beggining(list_of_games_by_cat)
    return list_of_games


game_list = get_games(game_data)
cat_list = get_categories(game_data)
platform_list = get_platform_list(game_data)


game_list_head = game_list.get_head_node()


game_sublist_head = game_list_head.get_value().get_head_node()

#Print Welcome Message
print("******")
print("WELCOME TO THE GAME LIBRARY")
print("SEARCH FOR GAMES USING CATEGORY SEARCH, OR PLATFORM SEARCH")
print("*****")

#Take user input for choosing category search or platform search
user_search_choice = input("Type \"cat\" if you want to search by category or \"plat\" if you want to search by platform: ")
search_by_list = ""
while search_by_list == "":
    if user_search_choice == "cat":
        search_by_list = cat_list
    elif user_search_choice == "plat":
        search_by_list = platform_list
    else:
        user_search_choice = input("Wrong type of input, Type \"cat\" if you want to search by category or \"plat\" if you want to search by platform: ")

#Define a function to find matching search types from user choice and displaying them
def choices_search(search_by_list):
    for choice in search_by_list:
        print(choice)
    user_category_choice = str(input("Choose a category by typing the beginning of the category: "))
    matching_choices = []
    for cat in search_by_list:
        if str(cat).startswith(user_category_choice.upper()):
            matching_choices.append(cat)
    return matching_choices

matching_choices = choices_search(search_by_list)
print(matching_choices)

if len(matching_choices) == 1:
    print("We have found one search choice: {0}".format(matching_choices[0]))
    user_continue = input("Would you like to continue with this choice (y/n): ")
    if user_continue == "y":
        selected_search = matching_choices[0]
else:
    print("We have found multiple search choices: ")
    for choice in matching_choices:
        print(choice)
    user_continue = input("Would you like to continue with this choice (y/n): ")

if user_continue == "y":
    while game_list_head.get_next_node() is not None:
        sublist_head = game_list_head.get_value().get_head_node()
        while sublist_head.get_next_node() is not None:
            if selected_search in sublist_head.get_value()[2]:
                print("*****")
                print("Name: " , sublist_head.get_value()[0])
                print("Platform: " , sublist_head.get_value()[1])
                print("Category: " , sublist_head.get_value()[2])
                print("Member Rating: " , sublist_head.get_value()[3])
                print("Critic Rating: " , sublist_head.get_value()[4])
                print("******\n")
            sublist_head = sublist_head.get_next_node()
        game_list_head = game_list_head.get_next_node()