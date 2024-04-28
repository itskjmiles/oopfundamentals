class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        
    def update_owner(self, new_owner):
        self.owner = new_owner

vehicle1 = Vehicle("ABC123", "Car", "John")
vehicle2 = Vehicle("XYZ789", "Truck", "Alice")

print("Original owners:")
print("Vehicle 1:", vehicle1.owner)
print("Vehicle 2:", vehicle2.owner)

vehicle1.update_owner("Bob")
vehicle2.update_owner("Eve")

print("\nUpdated owners:")
print("Vehicle 1:", vehicle1.owner)
print("Vehicle 2:", vehicle2.owner)

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
        
    def add_participant(self):
        self.participant_count += 1
        
    def get_participant_count(self):
        return self.participant_count

event1 = Event("Birthday Party", "2023-05-15")
event2 = Event("Concert", "2023-06-20")

print("Initial participant counts:")
print("Event 1:", event1.get_participant_count())
print("Event 2:", event2.get_participant_count())

event1.add_participant()
event1.add_participant()
event2.add_participant()

print("\nUpdated participant counts:")
print("Event 1:", event1.get_participant_count())
print("Event 2:", event2.get_participant_count())
