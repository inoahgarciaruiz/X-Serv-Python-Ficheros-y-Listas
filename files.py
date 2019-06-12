#!/usr/bin/python3

"""

   Make a Python script that:
      1. Opens file /etc/passwd and saves each line in a list
      2. Displays every username and its associated shell
      3. Counts the number of users in the list

Author: Ainhoa Garcia-Ruiz Fuentes.       Date: 12/06/2019
Course: Servicios y Aplicaciones en Redes de Ordenadores.

"""

# Open, read and close the file
f = open("/etc/passwd", "r")
users = f.readlines()
f.close()

# Displays users and associated shell
for user in users:
    name = user.split(":")[0]
    shell = user.split(":")[-1]
    print("User: " + name + "\t Shell: " + shell)

print("Number of users: ", len(users))
