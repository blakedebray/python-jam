#Creating a mad libs game

#Asks the user questions and sets them to variables
#Makes sure the answers are lowercase, except for friend
adjective1 = input('Enter an adjective: ').lower()
game = input('Enter the name of an outdoor game: ').lower()
adjective2 = input('Enter another adjective: ').lower()
friend = input('Enter the name of a friend: ').capitalize()
verb = input('Enter a verb ending in \'ing\': ').lower()
adjective3 = input('Enter one more adjective: ').lower()

#Creates the story using our variables
story = (f"""
         It was a {adjective1} summer day at the beach. 
         My friends and I were in the water playing {game}. 
         As a {adjective2} wave came closer, my friend {friend} yelled, 
         \"Look! There\'s a jellyfish {verb}!\" As we got closer, 
         we saw that the jellyfish was indeed {verb}! 
         {friend} ran out of the water and onto the sand. 
         {friend} was afraid of {verb} jellyfish. 
         The rest of us stayed in the water playing {game} because 
         {verb} jellyfish are {adjective3}.""")

print(story + '\n')