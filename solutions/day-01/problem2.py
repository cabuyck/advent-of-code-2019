INPUT_FILENAME = 'problem2_input.txt'


def sum_fuel_requirements():
    fuel_requirements = []
    masses_of_modules = create_list_from_input_file()
    for mass in masses_of_modules:
        fuel_requirement = calculate_fuel_requirements(mass)
        fuel_requirement += calculate_fuel_requirements_for_fuel(fuel_requirement)
        fuel_requirements.append(fuel_requirement)
    return sum(fuel_requirements)


def create_list_from_input_file():
    masses_of_modules = []
    with open(INPUT_FILENAME, 'r') as inputFile:
        for line in inputFile.readlines():
            masses_of_modules.append(int(line))
    return masses_of_modules


def calculate_fuel_requirements(mass):
    return (mass // 3) - 2


def calculate_fuel_requirements_for_fuel(mass_of_fuel):
    fuel_for_fuel = 0
    while calculate_fuel_requirements(mass_of_fuel) > 0:
        mass_of_fuel = calculate_fuel_requirements(mass_of_fuel)
        fuel_for_fuel += mass_of_fuel
    return fuel_for_fuel


print(sum_fuel_requirements())

# doing calculating fuel-for-fuel requirements at the end overshoots the answer because the instructions state
# that they should be handled at a per-module level. The extra is coming from the floor()ing that isn't done per module.
