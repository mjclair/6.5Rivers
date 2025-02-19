rivers = {
    'nile': 'egypt',
    'frenchbroad': 'asheville',
    'mississipiriver': 'mississippi'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country.title())
