def main():
    def init_database():
        names = ["Picard", "Spock", "Worf", "Data", "Sisko"]
        ranks = ["Captain", "Commander", "Lieutenant", "Lieutenant Commander", "Captain"]
        divs  = ["Command", "Science", "Security", "Operations", "Command"]
        IDs = ["SP-937-215","S179-276SP","WORF-201","D-4C-6F","FS-326-758"]
        return names, ranks, divs, IDs
    init_database()
    def display_menu():
        user_name = input("What is your full name?")
        print("Student logged in:", user_name.title())
        x = input("Choose an option:\n1: Add member\n2: Remove member\n3: Update rank\n4: Display roster\n5:Search crew member\n6: Filter by division\n7: Calculate payroll\n8: Count Officers\n")
        try:
            if x == 1:
                return 1
            elif x == 2:
                return 2
            elif x == 3:
                return 3
            elif x == 4:
                return 4
            elif x == 5:
                return 5
            elif x == 6:
                return 6
            elif x == 7:
                return 7
            elif x == 8:
                return 8
        except ValueError:
            print("not an option, try again")
    display_menu()
main()