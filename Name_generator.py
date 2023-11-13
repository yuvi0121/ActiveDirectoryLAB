from faker import Faker

faker = Faker()

# Generate 1005 random first and last names
names_list = [(faker.first_name(), faker.last_name()) for _ in range(1005)]

# Print the list
for first_name, last_name in names_list:
    print(f"{first_name} {last_name}")
