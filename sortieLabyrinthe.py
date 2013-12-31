#!/bin/python3

print("Algorithme de sortie du labyrinthe")
print("Merci d'entrer le labyrinthe ligne par ligne : x = mur et o ou [espace] = couloir")
print("Entrez 'q' pour terminer")
line = ""
lineLenght = 0
lines = []
while line.lower() != "q":
	line = input(">")
	if lineLenght == 0:
		if len(line) < 3:
			print("Longueur de ligne non acceptée : trop courte")
		else:
			lineLenght = len(line)
			print("La longueur d'une ligne a été définie à : "+str(lineLenght))
			lines.append(line)
	else:
		if len(line) == lineLenght:
			lines.append(line)
		elif line.lower() != "q":
			print("La longueur de la ligne n'est pas conforme.")

print("Voici le labyrinthe entré :")
for key,l in enumerate(lines):
	print(str(key)+" > "+l)

print("Position de l'entrée du labyrinthe : ")
print("(La première case est la 0,0)")
saisieEnt = True
		

entree = {"x":0,"y":0}
sortie = {"x":0,"y":0}
			
while saisieEnt:
	x = input("x :")
	y = input("y :")
	try:
		x = int(x)
		y = int(y)
		assert x > -1 and x < lineLenght and y > -1 and y < len(lines)
	except AssertionError:
		print("Erreur : coordonnées trop grandes ou trop petites")
	except:
		print("Erreur : coordonnées invalides")
	else:
		saisieEnt = False
		entree["x"] = x
		entree["y"] = y

print("Bien. Entrez maintenant les coordonnées de la sortie.")

saisieSort = True
while saisieSort:
	x = input("x :")
	y = input("y :")
	try:
		x = int(x)
		y = int(y)
		assert x > -1 and x < lineLenght and y > -1 and y < len(lines)
	except AssertionError:
		print("Erreur : coordonnées trop grandes ou trop petites")
	except:
		print("Erreur : coordonnées invalides")
	else:
		saisieSort = False
		sortie["x"] = x
		sortie["y"] = y


laby = lines
coordsPassees = []
parcourus = []

def trouverSortie(coords, dest, fromCoords):
	global laby
	global parcourus
	# Pour trouver la sortie :
	# On envoie un explorateur dans toutes les directions
	# Si toutes les réponses sont "false" on returne false.

	if compareCoords(coords, dest):
		return True

	
	if (coords["x"], coords["y"]) in parcourus:
		print("Arghlllll ! Chemin deja vu")
		print("INFO : Le labyrinthe a probablement plusieurs chemins vers la sortie car nos robots explorateurs sont tombes sur un chemin deja vu. Le chemin donné n'est pas forcément le plus court")
		return False

	parcourus.append((coords["x"],coords["y"]))
	currentLine = laby[coords["y"]]
	topCase = "x"
	bottomCase = "x"
	leftCase = "x"
	rightCase = "x"	
	bottomCoords = {"x":coords["x"],"y":coords["y"]+1}
	topCoords = {"x":coords["x"],"y":coords["y"]-1}
	leftCoords = {"x":coords["x"]-1,"y":coords["y"]}
	rightCoords = {"x":coords["x"]+1,"y":coords["y"]}	
	
	if coords["y"] > 0:
		topCase = laby[coords["y"]-1][coords["x"]]
	if coords["y"]+1 < len(laby):
		bottomCase = laby[coords["y"]+1][coords["x"]]
	if leftCoords["x"] >= 0:
		leftCase = currentLine[leftCoords["x"]]
	if rightCoords["x"] < len(currentLine):
		rightCase = currentLine[rightCoords["x"]]

	
	ansBottom = False
	ansTop = False
	ansLeft = False
	ansRight = False

	if isVoid(bottomCase) and not compareCoords(fromCoords, bottomCoords):
		ansBottom = trouverSortie(bottomCoords, dest, coords)
	if isVoid(topCase) and not compareCoords(fromCoords, topCoords):
		ansTop = trouverSortie(topCoords, dest, coords)
	if isVoid(leftCase) and not compareCoords(fromCoords, leftCoords):
		ansLeft = trouverSortie(leftCoords, dest, coords)
	if isVoid(rightCase) and not compareCoords(fromCoords, rightCoords):
		ansRight = trouverSortie(rightCoords, dest, coords)


	if ansBottom or ansTop or ansLeft or ansRight:
		coordsPassees.append((coords["x"],coords["y"]))
		return True
	if not (ansBottom or ansTop or ansLeft or ansRight):
		return False

	
	
def compareCoords(coord1, coord2):
	if coord1["x"] == coord2["x"] and coord2["y"] == coord1 ["y"]:
		return True
	return False

def isVoid(case):
	if case == "o" or case == " ":
		return True
	return False

if trouverSortie(entree, sortie, entree):
	print("Affichage de la sortie :")
	coordsPassees.append((sortie["x"], sortie["y"]))
	for x,y in coordsPassees:
		if y > -1 and y < len(laby):
			if x > -1 and x < len(laby[y]):
				laby[y] = laby[y][:x]+"."+laby[y][x+1:]

	for l in laby:
		print(l)
else:
	print("Sorry...")
	print("L'algo' ne trouve pas le moyen d'aller a la sortie.")

