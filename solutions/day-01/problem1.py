INPUT_FILENAME = 'problem1_input.txt'


def sum_fuel_requirements():
    fuel_requirements = []
    masses_of_modules = create_list_from_input_file()
    for mass in masses_of_modules:
        fuel_requirement = calculate_fuel_requirements(mass)
        fuel_requirements.append(fuel_requirement)
    return sum(fuel_requirements)


def create_list_from_input_file():
    masses_of_modules = []
    with open(INPUT_FILENAME, 'r') as inputFile:
        for line in inputFile.readlines():
            masses_of_modules.append(int(line))
    return masses_of_modules


def calculate_fuel_requirements(mass):
    return (mass//3) - 2


print(sum_fuel_requirements())