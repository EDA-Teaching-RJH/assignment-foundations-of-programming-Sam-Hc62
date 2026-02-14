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
            member_rank = input("Rank:")
            if member_rank not in TNG_ranks:
                print("Not ID_update valid rank...")
                continue
            member_ID = input("ID:")
            if member_ID in IDs:
                print("ID already belongs to someone...")
                continue        
            member_name = input("Name:")
            member_div = input("Division:")
            ranks.append(member_rank)
            IDs.append(member_ID)
            names.append(member_name)
            divs.append(member_div)
            break

    def remove_member():
        while True:
            ID_remove = input("ID:")
            if ID_remove in IDs:
                y = IDs.index(ID_remove)
                names.pop(y)
                ranks.pop(y)
                divs.pop(y)
                IDs.pop(y)
                break
            else:
                print("Member not found...")
                continue
    def update_rank():
        while True:
            ID_update = input("ID:")
            if ID_update in IDs:
                z = IDs.index(ID_update)
                a = input("New rank:")
                if a in TNG_ranks:
                    ranks[z] = a
                    break
                else:
                    print("Not a valid rank...")
                    continue
            else:
                print("Member not found...")
                continue
    def display_menu():
        user_name = input("What is your full name?...")
        print("Student logged in:", user_name.title())
        try:
            x = int(input("(1) Add member (2) Remove member (3) Update rank\n(4) Display roster (5) Search crew member (6) Filter by division\n(7) Calculate payroll (8) Count Officers\nChoose an option:\n"))
            if x == 1:
                add_member()
            elif x == 2:
                remove_member()
            elif x == 3:
                update_rank()
        except ValueError:
            print("not an option, try again...")
    display_menu()

main()