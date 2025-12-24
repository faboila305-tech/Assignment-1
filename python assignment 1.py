#List with pastrami appearing at least three times
sandwich_orders = [
     'pastrami','tuna','pastrami',
     'chicken', 'pastrami', 'beef'
]
finished_sandwiches =[]
#Inform users that pastrami is unavailable
print("sorry,the deli has run out of pastrami.\n")
#Remove all pastrami is sandwiches
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
 #Make remaining sandwiches
while sandwich_orders:
    current_sandwich =sandwich_orders.pop(0)
    print(f"I made ypur{current_sandwich} sandwich.")
    finished_sandwiches .append(current_sandwich)
    #Display finished sandwiches
    print("\nSandwiches made:")
    for sandwich in finished_sandwiches:
        print(sandwich)




