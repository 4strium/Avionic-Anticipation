# Avionic-Anticipation
 Un algorithme simple pour pilote de ligne afin d'anticiper une descente de l'aéronef à 3°

## Calcul de l’altitude grâce à la [pression statique](https://fr.wikipedia.org/wiki/Pression_statique)
Donc imaginons que nous mesurons une pression de **177 millibars/hectopascals** via la sonde positionnée au niveau de la cabine, nous cherchons donc à déterminer l’altitude de notre aéronef en pied grâce à cette constatation.

On utilise la formule suivante → **Altitude (en [ft.](https://fr.wikipedia.org/wiki/Pied_(unit%C3%A9)))** :
![Formule permettant de convertir une pression statique mesurée en une altitude](https://romainmellaza.fr/img/autonomous-landing/static-pressure-equation.png)

En y injectant notre valeur de 177 millibars, on obtient une altitude d’environ **41 000 pieds.** Le pied et le mile nautique sont les unités internationales de longueurs utilisées dans le secteur aéronautique, mais pour simplifier la compréhension de cette présentation **nous utiliserons le mètre à partir de maintenant.**

On doit donc convertir notre résultat de **41 000 pieds en m, en multipliant cette valeur par 0.3048, ce qui nous permet d’obtenir une altitude d’environ 12 500 mètres !**

## Anticipation de l'approche
En modélisant une approche constante et alignée avec la piste, il est possible de connaître précisément à quelle distance de notre point de toucher l’avion doit initier sa descente.

Pour cela il faut représenter **un triangle rectangle où, tout d’abord, notre angle Alpha sera l’angle de descente, c’est-à-dire 3° ici** (*comme préconisé par l’[Organisation de l'aviation civile internationale](https://fr.wikipedia.org/wiki/Organisation_de_l%27aviation_civile_internationale)*). **Et donc par rapport à cet angle nous aurons le côté qui y est opposé, autrement dit l'altitude que nous venons de calculer, et le côté adjacent à l’angle alpha qui est donc la longueur que l’on cherche à calculer.**

En utilisant une relation trigonométrique, on calcule la distance recherchée via la formule suivante :
![Formule permettant d’obtenir la distance (au niveau du sol) entre l’aéronef et son point de toucher](https://romainmellaza.fr/img/autonomous-landing/distance-GPS-altitude.png)

**En l'occurrence, avec notre altitude de 12 500 m calculé, on peut estimer que notre Airbus A350 doit entamer sa descente lorsqu’il se situera à 238 514 m de son point de toucher sur la piste.**