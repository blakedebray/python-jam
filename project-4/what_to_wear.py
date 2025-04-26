#if the temperature is 80 degrees or warmer, wear shorts and sunglases
#if the temperature is 60 - 79 degrees, wear a light jacket
#if the temperature is 59 degrees or cooler, wear a coat, hat, and gloves

#get the current temperature
temperature = int(input('What is the current temperature? '))

#checks whenever the temperature is 80 degrees or warmer 
if temperature >= 80:
    outfit = 'shorts and pack sunglasses'
    #create an else if statement
elif temperature <= 79 and temperature > 60:
    outfit = 'a light jacket'
else:
    outfit = 'a coat in addition to a hat, gloves, and a scarf' 
    
advice = (f'Today you should wear {outfit}.')
print(advice)