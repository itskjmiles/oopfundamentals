from transportation import Bus

bus1 = Bus(101, 50)
bus2 = Bus(102, 40)

print(f"City Name: {Bus.city_name}")
print(f"Base Fare: ${Bus.base_fare}")

print(f"Bus 1 Route Number: {bus1.route_number}")
print(f"Bus 1 Passenger Capacity: {bus1.passenger_capacity}")
print(f"Bus 2 Route Number: {bus2.route_number}")
print(f"Bus 2 Passenger Capacity: {bus2.passenger_capacity}")
