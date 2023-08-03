# Nesting
capitals = {
    "Bangladesh": "Dhaka",
    "India": "New Delhi",
    "China": "Hong Kong"
}

# Nesting a list in dictionary
travel_log = {
    "Bangladesh": ["Dhaka", "Chittagong", "Rajshahi", "Jashore", "Khulna"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "France": {"cities_visited": ["Paris", "Lili", "Dijon"], "total_visits": 12}
}

# nesting dictionary in list
travel_log_dictionary = [
    {
        "country": "Bangladesh",
        "cities_visited": ["Dhaka", "Chittagong", "Rajshahi", "Jashore", "Khulna"],
        "total_visits": 15
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
    {
        "country": "France",
        "cities_visited": ["Paris", "Lili", "Dijon"],
        "total_visits": 12
    }
]
