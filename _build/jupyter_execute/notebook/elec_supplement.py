La page ci-présente existe en version notebook téléchargeable grâce au bouton ![Bouton](./images/bouton_tl.png) (choisir le format `.ipynb`). On rappelle qu'l faut ensuite l'enregistrer dans un répertoire adéquat sur votre ordinateur (`tp3` par exemple dans votre répertoire personnel) puis lancer Jupyter Notebook depuis Anaconda pour accéder au notebook, le modifier et exécutez les cellules de code adéquates.


Cette partie n'est à faire qu'après avoir bien compris les premières parties. 3 études sont proposées. Les deux premières reprennent des idées des séances précédentes et vous propose de les réinvestier sans guide ni étude préliminaire :
* réfléchir aux problèmes de terre et temps caractéristiques pour observer les régimes transitoires successifs d'un système d'ordre 2.
* dimensionner un filtre passe-bande d'ordre 2 et automatiser sont étude fréquentielle.

Le dernier propose d'apprendre à utiliser un microcontrolleur (Arduino) pour étudier un système électrique lent.

```{margin}
Vous n'aurez probablement pas le temps de faire les trois manipulations (compter 2h par manipulations). Il est conseillé de faire l'une des deux premières et celle utilisant un microcontrolleur.
```

# Etude du régime transitoire (Ordre 2)
On veut :
1. obtenir l'évolution temporelle de la tension aux bornes d'un condensateur dans un RLC série avec FOXY en régime pseudo-périodique et utiliser ce tracé pour obtenir la pseudo pulsation etle décrément logarithmique puis la pulsation propre et le facteur de qualité. On comparera alors ces valeurs aux valeurs attendues.
2. obtenir le portrait de phase du condensateur en régime libre et en échelon de tension à l'__oscilloscope__. On commentera alors l'allure du portrait de phase en fonction de la valeur de la résistance $R$.

Dans les deux cas, on utilisera des charges et décharges successives grâce à un créneau. On prend $L = 100mH$ (bobine bleue) et $C = 100nF$.

## Régime pseudo-périodique
````{admonition} Dimensionnement
:class: tip
1. En tenant compte de la résistance de sortie du GBF, quelle condition doit-on imposer à la résistance $R$ du RLC ?
2. Estimer un ordre de grandeur de la fréquence du créneau pour observer plusieurs pseudo-périodes en régime pseudo-périodique faiblement amorti.
````

````{admonition} Réalisation
:class: tip
1. Proposer un montage et le réaliser. Régler correctement le GBF et les paramètres d'acquisition sur FOXY (__on travaillera en acquisition continue__).
2. Vérifier que vous obtenez bien un régime pseudo-périodique et modifier R de manière à obtenir une dizaine de période.
3. Une fois le tracé utilisable, passer sur une acquisition unique pour faire les mesures. Vous devrez :
	1. Réfléchir aux mesures à réaliser pour obtenir la pseudo-période et le décrément logarithmique. Ce dernier devra être mesurée comme une moyenne sur au moins 5 mesures.
	2. Réaliser les mesures nécessaires en pensant aux incertitudes puis utiliser la cellule de code ci-dessous pour estimer (avec leurs incertitudes) : la pseudo-période, le décrément logarithmique puis la pulsation propre et le facteur de qualité.
	3. Comparer les valeurs attendues (avec les incertitudes sur les composants) pour $\omega_0$ et $Q$ aux valeurs expérimentales.
````

"""Il y aura sans doute beaucoup à coder. Servez-vous de ce que vous avez fait précédemment."""



## Portrait de phase

````{admonition} Réalisation
:class: tip
1. Proposer un montage permettant d'observer __à l'oscilloscope__ le portrait de phase du condensateur (à un coefficient près pour l'intensité) en utilisant un GBF pour réaliser des charges et décharges successives.
2. Réaliser le montage et jouer sur la valeur de $R$ pour observer les trois régimes.
````


# Etude d'un filtre passe-bande
On veut :
1. dimensionner expérimentalement un filtre passe-bande RLC série en choisissant les valeur de R et C ($L = 100mH$ (boite bleue)) pour obtenir une fréquence de résonance de $5kHz$ et une bande passante de $1kHz$.
2. Réaliser une étude fréquentielle automatiser en réalisant un balayage en fréquence entre $f_{min} = 500Hz$ et $f_{max} = 50kHz$.

## Dimensionnement du filtre
````{admonition} Dimensionnement
:class: tip
1. Proposer un protocole de réglage des composants R et C pour répondre aux attentes.
2. Réaliser alors le dimensionnement et rendre compte des valeurs choisies pour R et C avec leurs incertitudes. Calculer les valeurs attendues de R et C (en fonction du cahier des charges et de L) et leurs incertitudes au moyen de la cellule ci-dessous. Utilisez aussi cette cellule pour tester la cohérence entre les valeurs attendues de R et C et les valeurs obtenues lors du dimensionnement.
````

"""Utilisez cette cellule pour faire vos calculs."""



## Etude fréquentielle
On gardera les valeurs de R et C trouvées précédemment. Le but est d'obtenir directement à l'oscilloscope l'amplitude $s_m(f)$ comme une fonctione de la fréquence d'entrée. On utilisera le Balayage en fréquence permis par le GBF (`Sweep`). La sortie `main` enverra alors un signal sinusoïdal mais dont la fréquence varie de $f_{min}$ à $f_{max}$. Si la variation de $f$ est suffisamment lente, on peut considérer qu'on est à chaque fois en régime sinusoïdal forcé. Les caractéristiques du balayage en fréquence sont :
* Bouton `start` : affiche la fréquence $f_{min}$ qui est réglable avec la molette de réglage de la fréquence
* Bouton `stop` : affiche la fréquence $f_{max}$ qui est réglable avec la molette de réglage `Stop`
* Vitesse de balayage en fréquence : réglable avec la molette `Rate`. Pour savoir le temps mis pour passer de $f_{min}$ à $f_{max}$, vous pouvez visualiser une tension proportionnelle à la fréquence instantanée avec la borne `Sweep In/Out` (très utile pour synchroniser le signal).
* Bouton `Log/Lin` : permet un balayage logarithmique (pour un diagramme de Bode par exemple) ou linéaire.

````{admonition} Etude du filtre
:class: tip
1. Activer le balayage en fréquence et le régler en fonction du balayage en fréquence demandé plus haut. Observer alors le signal en sortie du filtre.
2. Proposer un montage à brancher après le filtre pour visualiser l'amplitude du signal de sortie. Faut-il intercaler un suiveur entre ce montage et le filtre ?
3. Réaliser le montage complet en adaptant les valeurs des composants et observer la réponse fréquentielle du filtre. Vérifier qu'on retrouve les caractéristiques imposées par le cahier des charges (utiliser la sortie `Sweep In/Oui` pour mesurer des fréquences).
````


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