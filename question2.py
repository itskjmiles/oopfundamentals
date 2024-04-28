class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        
    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.name},{self.floors}\n")
    
    @staticmethod
    def load_from_file(filename):
        buildings = []
        with open(filename, 'r') as file:
            for line in file:
                name, floors = line.strip().split(',')
                building = Building(name, int(floors))
                buildings.append(building)
        return buildings

building1 = Building("Skyscraper", 50)
building2 = Building("Office Building", 20)

building1.save_to_file("buildings.txt")
building2.save_to_file("buildings.txt")

loaded_buildings = Building.load_from_file("buildings.txt")
for building in loaded_buildings:
    print(f"Name: {building.name}, Floors: {building.floors}")
