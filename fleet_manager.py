def main():
    TNG_ranks = ["Crewman","Cadet","Ensign","Lieutenant Junior Grade","Lieutenant","Lieutenant Commander","Commander","Captain","Rear Admiral","Vice Admiral","Admiral","Fleet Admiral"]
    
    def init_database():
        names = ["Picard", "Riker", "Worf", "Data", "Troi"]
        ranks = ["Captain", "Commander", "Lieutenant", "Lieutenant Commander", "Lieutenant Commander"]
        divs  = ["Command", "Command", "Security", "Operations", "Counselor"]
        IDs = ["PC-1701-D", "RI-1701-D", "WORF-201", "D-4C-6F", "TR-1701-D"]
        return names, ranks, divs, IDs 
    names, ranks, divs, IDs = init_database()

    def add_member():
        while True:
            member_rank = input("--------------------------------------\nRank: ")
            if member_rank not in TNG_ranks:
                print("*error*\nNot a valid rank, try again...")
                continue
            member_ID = input("ID: ")
            if member_ID in IDs:
                print("*error*\nID already belongs to someone, try again...")
                continue        
            member_name = input("Name: ")
            member_div = input("Division: ")
            ranks.append(member_rank)
            IDs.append(member_ID)
            names.append(member_name)
            divs.append(member_div)
            break

    def remove_member():
        while True:
            ID_remove = input("--------------------------------------\nID: ")
            if ID_remove in IDs:
                a = IDs.index(ID_remove)
                names.pop(a)
                ranks.pop(a)
                divs.pop(a)
                IDs.pop(a)
                break
            else:
                print("*error*\nMember not found...")
                continue

    def update_rank():
        while True:
            ID_update = input("--------------------------------------\nID: ")
            if ID_update in IDs:
                b = IDs.index(ID_update)
                c = input("New rank: ")
                if c in TNG_ranks:
                    ranks[b] = c
                    break
                else:
                    print("Not a valid rank, try again...")
                    continue
            else:
                print("Member not found, try again...")
                continue

    def display_roster():
        print("-"*50)
        print(f"{"names":<10} {"ranks":<20} {"divs":<10} {"IDs":<10}")
        print("-"*50)
        for i in range(len(names)):
            print(f"{names[i]:<10} {ranks[i]:<20} {divs[i]:<10} {IDs[i]:<10}")

    def search_crew():
        while True:
            search_choice = input("--------------------------------------\nSearch by...\n\n(1) Name (2) Rank (3) Division (4) ID\n--------------------------------------\nChoose an option: ")
            if not search_choice.isdigit():
                print("not an option try again")
                continue
            search_choice = int(search_choice)
            if search_choice == 1:
                name_search = input("--------------------------------------\nName: ")
                if name_search in names:
                    d = names.index(name_search)
                    break
                else:
                    print("Member not found, try again...")
                    continue
            elif search_choice == 2:
                rank_search = input("--------------------------------------\nRank: ")
                if rank_search in ranks:
                    d = ranks.index(rank_search)
                    break
                else:
                    print("Member not found, try again...")
                    continue
            elif search_choice == 3:
                div_search = input("--------------------------------------\nDivision: ")
                if div_search in divs:
                    d = divs.index(div_search)
                    break
                else:
                    print("Member not found, try again...")
                    continue
            elif search_choice == 4:
                ID_search = input("--------------------------------------\nID: ")
                if ID_search in IDs:
                    d = IDs.index(ID_search)
                    break
                else:
                    print("Member not found, try again...")
                    continue
            else:
                print("Not an option, try again...")
                continue
        print(f"--------------------------------------\n\n--- Name: {names[d]} --- Rank: {ranks[d]} --- Division: {divs[d]} --- ID: {IDs[d]} ---")
    
    def filter_by_division():
        div_list = list(set(divs))
        print("--------------------------------------\nFilter by...\n")
        for i, e in enumerate(div_list, start=1):
            print(f"({i}) {e}")
        while True:
            filter_choice = input("--------------------------------------\nChoose an option: ")
            if not filter_choice.isdigit() or 1 > int(filter_choice) or int(filter_choice)> len(div_list):
                print("Not an option, try again...")
                continue
            div = div_list[int(filter_choice)-1]
            print("-"*50)
            print(f"{"names":<10} {"ranks":<20} {"divs":<10} {"IDs":<10}")
            print("-"*50)
            for i in range(len(divs)):
                if divs[i] == div:
                    print(f"{names[i]:<10} {ranks[i]:<20} {divs[i]:<10} {IDs[i]:<10}")
            break
    
    def calculate_payroll():
        def get_pay(rank):
            if rank in ["Captain","Rear Admiral","Vice Admiral","Admiral","Fleet Admiral"]:
                return 200000
            elif rank in ["Commander", "Lieutenant Commander"]:
                return 90000
            elif rank in ["Lieutenant","Lieutenant Junior Grade"]:
                return 50000
            elif rank in ["Crewman","Ensign","Cadet"]:
                return 35000
            else: 
                return 30000

        total_pay = sum(get_pay(rank) for rank in ranks)
        print(f"--------------------------------------\nTotal crew payroll: {total_pay} credits")

    def count_officers():
        f = 0
        for rank in ranks:
            if rank == "Captain" or rank == "Commander":
                f = f + 1
        print(f"--------------------------------------\nTotal officers: {f}")        

    def display_menu():
        print("--------------------------------------\nStudent logged in:", user_name.title())
        try:
            x = int(input("--------------------------------------\n(1) Add member (2) Remove member (3) Update rank\n(4) Display roster (5) Search crew member (6) Filter by division\n(7) Calculate payroll (8) Count Officers (9) Exit\n--------------------------------------\nChoose an option: "))
            if x == 1:
                add_member()
            elif x == 2:
                remove_member()
            elif x == 3:
                update_rank()
            elif x == 4:
                display_roster()
            elif x == 5:
                search_crew()
            elif x == 6:
                filter_by_division()
            elif x == 7:
                calculate_payroll()
            elif x == 8:
                count_officers()
            elif x == 9:
                exit()
        except ValueError:
            print("not an option, try again...")
    user_name = input("What is your full name?...")        
    while True:
        1==1
        display_menu()

main()