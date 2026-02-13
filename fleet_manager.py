def main():
    def init_database():
        names = ["Picard", "Spock", "Worf", "Data", "Sisko"]
        species = ["Human", "Vulcan/Half-Human", "Klingon", "Android", "Human/Celestial"]
        ranks = ["Captain", "Commander", "Lieutenant", "Lieutenant Commander", "Captain"]
        episodes = [176, 80, 172, 174, 173]
        return names, species, ranks, episodes
    init_database()
main()