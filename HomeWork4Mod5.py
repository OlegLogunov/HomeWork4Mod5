class Building:
    total = 0

    def __init__(self):
        Building.total += 1

street = []
for build in range(40):
    new_build = Building()
    print(f"Создано строение класса Building № {build+1}")
    street.append(new_build)

print(40 * "-")
print(f"Итого на улице {Building.total} строений")
