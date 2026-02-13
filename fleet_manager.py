def main():
    def init_database():
        names = ["Picard", "Riker", "Worf", "Data", "Troi"]
        ranks = ["Captain", "Commander", "Lieutenant", "Lieutenant Commander", "Lieutenant Commander"]
        divs  = ["Command", "Command", "Security", "Operations", "Counselor"]
        IDs = ["PC-1701-D", "RI-1701-D", "WORF-201", "D-4C-6F", "TR-1701-D"]
        return names, ranks, divs, IDs 
    names, ranks, divs, IDs = init_database()
    def display_menu():
        user_name = input("What is your full name?")
        print("Student logged in:", user_name.title())
        x = int(input("Choose an option:\n1: Add member\n2: Remove member\n3: Update rank\n4: Display roster\n5:Search crew member\n6: Filter by division\n7: Calculate payroll\n8: Count Officers\n"))
        try:
            if 1 <= x <= 8:
                return x
        except ValueError:
            print("not an option, try again")
    display_menu()
    def add_member():
        TNG_ranks = ["Crewman","Cadet","Ensign","Lieutenant Junior Grade","Lieutenant","Lieutenant Commander","Commander","Captain","Rear Admiral","Vice Admiral","Admiral","Fleet Admiral"]
        while True:
            member_rank = input("Rank:")
            if member_rank not in TNG_ranks:
                print("Not a valid rank")
                continue
            member_ID = input("ID:")
            if member_ID in IDs:
                print("ID already belongs to someone")
                continue        
            member_name = input("Name:")
            member_div = input("Division:")
            ranks.append(member_rank)
            IDs.append(member_ID)
            names.append(member_name)
            divs.append(member_div)
            break
    add_member()
    def remove_member():
        while True:
            y = input("ID:")
            if y in IDs:
                z = IDs.index(y)
                names.pop(z)
                ranks.pop(z)
                divs.pop(z)
                IDs.pop(z)
                break
            else:
                print("Member not found")
                continue
    remove_member()
main()