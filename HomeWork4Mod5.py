class Building:
    total = 0

    def __init__(self):
        Building.total += 1

for build in range(40):
    print(f"Строение № {build+1}")
    Building()

print(f"Итого на улице {Building.total} строений")
