# ANIMIKH AICH & AKHILESH V

import aiml


k = aiml.Kernel()

k.bootstrap(learnFiles="aiml_dir.xml", commands="load aiml")
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print("Hello User\nWelcome to shopping.com \nI'm Casey! Your Shopping Assistant\nWhat is your name?")
while True:
    user_input = (input(">>"))
    if user_input.lower() == "bye":
        break
    else:
        print(k.respond(user_input))

print("Okay! Goodbye! Thank You for shopping with us :)")
