n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

 #unnecessary code

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading = loading +1

        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #'==' fixed from '='
            print("Current Crew List:")
            
            for i in range(len(n)): #actual list range
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank) #appending other list
            d.append(new_div) #appending other list
            print("Crew member added.")
            
        elif opt == "3":
            while True:
                rem = input("Name to remove: ")
                try: #wrapped index remove in a try loop so typos dont crash programme 
                    idx = n.index(rem)
                    n.pop(idx)
                    r.pop(idx)
                    d.pop(idx)
                    print("Removed.")
                    break
                except ValueError:
                    print("error typing name")
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": #needed another 'rank ==' after the 'or'
                    count = count + 1
            print("High ranking officers: ", count) #',' instead of '+'
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        elif len(n) == 0: 
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith() #brackets added to call the function
