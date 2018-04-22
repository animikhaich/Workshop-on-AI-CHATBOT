import random, time, datetime, pickle


text = '''Hello! How are you doing?
I am doing great!
Who are you?
My name is Animikh
Oh! What are you up-to?
I am teaching Python
Cool!'''


file1 = open('Database/Elon_Musk.txt', 'r')
print(file1.read())
file1.close()

file2 = open('Database/FileText1.txt', 'w')
file2.write('This is the first line' + '\n\n')
file2.write(text)
file2.write('\n\n' + 'This is the last line')
file2.close()

for i in range(100):
    file3 = open('Database/FileText2.txt', 'a')
    file3.write(str(i)+'\t')
    file3.close()

file3 = open('Database/FileText2.txt', 'a')
file3.write('\n\n')
file3.close()

for i in range(100):
    with open('Database/FileText2.txt', 'a') as file4:
        file4.write(str(i*10)+'\t')

# Datetime Module
today = datetime.date.today()
print("Today's date:", today)
print("Today's Day: {} Month: {} Year: {}".format(today.day, today.month, today.year))
print("Today's Weekday Number:", today.weekday() + 1)
print("Current Date and Time down to microsecond accuracy:", datetime.datetime.now())

# Time Module
print("Current Date and Time:", time.ctime())
print("Current Time Zone:", time.tzname)
print("Number of ticks since 12:00am, January 1, 1970:", time.time())   # 12:00am, January 1, 1970 is called Unix Time
print("Sum of the system and user CPU time of the current process:", time.process_time())
# time.sleep(5)   # No operation for 5 seconds

# Random Module
random_numbers_1 = [random.random() for i in range(5)]
print("Random Numbers Set 1:", random_numbers_1)
random_numbers_2 = [random.random() for i in range(5)]
print("Random Numbers Set 1:", random_numbers_2)

random.seed(10)
new_random_numbers_1 = [random.random() for i in range(5)]
print("Random Numbers Set 1:", new_random_numbers_1)
random.seed(10)
new_random_numbers_2 = [random.random() for i in range(5)]
print("Random Numbers Set 2:", new_random_numbers_2)

names = ['Animikh', 'Akhilesh', 'Akshay', 'Aishwarya', 'Akshaya', 'Harshitha']
# Completely Random
for i in range(10):
    print(random.choice(names))
print()

# Random but same series every time
random.seed(10)
for i in range(10):
    print(random.choice(names))
print()

# Same name every time
for i in range(10):
    random.seed(10)
    print(random.choice(names))
print()


# Pickling of objects
new_random_list = new_random_numbers_1 + new_random_numbers_2 + random_numbers_1 + random_numbers_2
print("Generated New Random List:", new_random_list)

# Save the object, or pickle the object
pickle_out_file = open("Database/random_list.pkl", 'wb')
pickle.dump(obj=new_random_list, file=pickle_out_file)
pickle_out_file.close()

# Retrieve the Pickled Object
pickle_in_file = open("Database/random_list.pkl", 'rb')
example_list = pickle.load(pickle_in_file)
pickle_in_file.close()

print("List Opened form Pickle File", example_list)
