country_code = {
    'United States': 224,
    'United Kingdom': 45,
    'Nigeria': 234,
    'Germany': 24,
    'Canada': [221, 209, 236]
}


print(country_code['United States'])

for country in country_code:
    print(country, country_code[country])


for key, value in country_code.items():
    print(key, value)
