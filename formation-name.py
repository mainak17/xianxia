import random as rd

# Create a list of cultivation beast special attributes
attributes = ["Heavenly", "Divine", "Spiritual", "Demonic","Ancestral","Primordial","Grand"]

# Create a list of cultivation beast element
element = ["Frost","Ice", "Flaming","Jade","Void", "Lightning", "Earth","Stone", "Tempest", "Toxic", "Venom",  "Wood", "Light","Shadow",
            "Poison","Chaos","Iron"]

beasts = ["Dragon", "Phoenix", "Tiger", "Lion", "Serpent", "Bear", "Fox","Slug","Spider","Cicada"]

types = ["Killing","Protective","Imprisoning","Illusory","Sealing","Soul-Devouring","Sacrificial","Qi Gathering","Devouring"]


def get_formation_names(n):
    formation_names = []
    for i in range(n):
        formation_names.append(rd.choice(attributes) + " " +rd.choice(element) + " " +rd.choice(beasts)+" " +rd.choice(types)+" Formation")

    return formation_names

formation_list= get_formation_names(1000) #1000 is to generate 1000 formation names. change it accordingly

# for i in range(21):
#     print(rd.choice(attributes) + " " +rd.choice(element) + " " +rd.choice(beasts)+" " +rd.choice(types)+" Formation")

import pandas as pd 

formation = pd.DataFrame(formation_list)

# print(formation.head(20))
formation.to_csv('formation-list-1.csv')
# Demonic Tempest Serpent,Divine Shadow Phoenix
