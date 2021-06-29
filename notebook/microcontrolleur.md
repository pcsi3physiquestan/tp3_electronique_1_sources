---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,md:myst
  split_at_heading: true
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Automatisation de l'étude d'un RC.
Le but de cette manipulation est d'utiliser un microcontrolleur pour automatiser l'étude d'un circuit RC et mesurer un grand nombre de fois sa constante de temps.

Pour comprendre l'utilisation du microcontrolleur Arduino. Commencez par lire [cette présentation](microcon).

## Réalisation du montage.
Le microcontrolleur Arduino étant relativement lent (fréquence de mesure analogique faible), on va devoir travailler sur un RC avec une grande constante de temps et utiliser un condensateur chimique. Ce dernier est __polarisé et ne doit surtout pas être branché sur une tension négative__. On fera donc bien attention au sens de branchement du système.

On va réaliser le montage suivant.

````{admonition} Montage
:class: tip
1. Réaliser le montage et repérer bien la broche d'Arduino à laquelle est reliée la résistance. Ce sera l'alimentation du RC pour passer d'un échelon de tension à un régime libre. Repérer aussi la borne de mesure (A0), elle permettra de mesure la tension entre le point de branchement et la masse. On pourra vérifier qu'on mesurer effectivement $u_C$.
````


## Programmation du microcontrolleur.

Le programme a été partiellement écrit. Télécharger le fichier ici et l'ouvrier dans le logiciel Arduino. Il n'est pas nécessaire de comprendre le langage C, il suffit de bien lire les commentaires pour comprendre le programme.

````{admonition} Modification du programme
:class: tip
1. Trouver la ligne qui définit le PIN d'alimentation de la cellule RC et entrer le numéro de la broche choisie.
2. Trouver la ligne qui définit la durée d'une charge et d'une décharge et choisir une durée permettant d'atteindre le régime permanent à chaque fois.
3. Trouver la ligne qui définit le nombre de mesures à réaliser et choisir 1000 mesures.
4. Téléverser le programme dans la carte Arduino. Celle-ci est maintenant prête à lancer les mesures.
````

## Acquisition des mesures.
Pour récupérer et traiter les données plus facilement, nous allons utiliser un script Python qui va se charger de déclencher le début de la mesure puis récupérer les mesures et les enregistrer dans un fichier. Télécharger le fichier ici et l'ouvrir avec Pyzo.

````{admonition} Lancement de l'acquisition
:class: tip
1. Vérifier que le nom du branchement correspondant à Arduino est correct puis lancer l'acquisition en exécutant le programme. Un fichier `data_rc.dat` sera créé avec les données de mesures.
````

## Traitement des données.
Télécharger et ouvrir avec Pyzo le script prévu pour l'analyse des données. Vous trouverez simplement quelques lignes qui charges les mesures des temps tau dans un vecteur numpy. A vous d'écrire la suite du programme pour :
1. Tracer l'histogramme des valeurs de $\tau$ et vérifier qu'il n'y a pas de mesure aberrantes. Si c'est le cas, il faudra une série d'instructions pour les supprimer.
2. Obtenir la moyenne et l'écart-type des mesures puis la comparer avec la valeur attendues connaissant les valeurs de R et C.



(microcon)=
# (Complément) Fonctionnement d'un microcontrolleur

Nous allons présenter (sommairement) le fonctionnement et l'utilsation d'un microcontrolleur (ici Arduino).