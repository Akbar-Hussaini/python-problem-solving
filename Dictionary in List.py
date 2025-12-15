travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgard"]
    }
]

def add_new_country(country, visits, cities):
    new_dictionary = {
        "country" : country,
        "visits" : visits,
        "cities" : cities
    }
    travel_log.append(new_dictionary)

add_new_country("Russia", 2, ["Moscow", "City A", "City B"])
print(travel_log)