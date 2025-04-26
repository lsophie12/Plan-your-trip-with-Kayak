# Plan-your-trip-with-Kayak

Kayak est un moteur de recherche de voyages qui aide les utilisateurs à planifier leur prochain voyage au meilleur prix.

L'entreprise a été fondée en 2004 par Steve Hafner et Paul M. English. Après plusieurs levées de fonds, Kayak a été rachetée par Booking Holdings , qui détient désormais :

Booking.com
Kayak
Priceline
Agoda
Location de voitures
OpenTable

Avec plus de 300 millions de dollars de revenus par an, Kayak opère dans presque tous les pays et toutes les langues pour aider ses utilisateurs à réserver des voyages à travers le monde.

Projet 🚧
L'équipe marketing a besoin d'aide pour un nouveau projet. Après une étude utilisateur, l'équipe a découvert que 70 % de ses utilisateurs préparant un voyage aimeraient avoir plus d'informations sur leur destination .

De plus, les recherches auprès des utilisateurs montrent que les gens ont tendance à se méfier des informations qu'ils lisent s'ils ne connaissent pas la marque qui a produit le contenu.

L'équipe marketing de Kayak souhaite donc créer une application qui recommandera des destinations de vacances. Cette application s'appuiera sur des données réelles concernant :

Météo
Hôtels dans la région
L'application devrait alors être en mesure de recommander les meilleures destinations et hôtels en fonction des variables ci-dessus à tout moment.

Objectifs 🎯
Le projet venant de démarrer, votre équipe ne dispose d'aucune donnée permettant de créer cette application. Votre mission consistera donc à :

Extraire les données des destinations
Obtenez des données météorologiques pour chaque destination
Obtenez des informations sur les hôtels pour chaque destination
Stockez toutes les informations ci-dessus dans un lac de données
Extraire, transformer et charger les données nettoyées de votre lac de données vers un entrepôt de données

Portée de ce projet 🖼️
L'équipe marketing souhaite d'abord se concentrer sur les meilleures villes de France. Selon One Week In.com, voici le top 35 des villes à visiter en France :

["Mont Saint Michel",
"St Malo",
"Bayeux",
"Le Havre",
"Rouen",
"Paris",
"Amiens",
"Lille",
"Strasbourg",
"Chateau du Haut Koenigsbourg",
"Colmar",
"Eguisheim",
"Besancon",
"Dijon",
"Annecy",
"Grenoble",
"Lyon",
"Gorges du Verdon",
"Bormes les Mimosas",
"Cassis",
"Marseille",
"Aix en Provence",
"Avignon",
"Uzes",
"Nimes",
"Aigues Mortes",
"Saintes Maries de la mer",
"Collioure",
"Carcassonne",
"Ariege",
"Toulouse",
"Montauban",
"Biarritz",
"Bayonne",
"La Rochelle"]

Votre équipe doit se concentrer uniquement sur les villes ci-dessus pour votre projet .

Aides 🦮
Pour vous aider à réaliser ce projet, voici quelques conseils qui devraient vous aider

Obtenez des données météorologiques avec une API
Utilisez https://nominatim.org/ pour obtenir les coordonnées GPS de toutes les villes (aucun abonnement requis) Documentation : https://nominatim.org/release-docs/develop/api/Search/

Utilisez https://openweathermap.org/appid (vous devez vous abonner pour obtenir une clé API gratuite) et https://openweathermap.org/api/one-call-api pour obtenir des informations sur la météo des 35 villes et les placer dans un DataFrame

Déterminez la liste des villes où le temps sera le plus agréable dans les 7 prochains jours Par exemple, vous pouvez utiliser les valeurs de daily.pop et daily.rain pour calculer le volume de pluie attendu dans les 7 prochains jours... Mais ce n'est qu'un exemple, en fait vous pouvez avoir des opinions différentes sur ce à quoi ressemblerait un beau temps 😎 Peut-être que le critère le plus important pour vous est la température ou l'humidité, alors n'hésitez pas à changer les règles !

Enregistrez tous les résultats dans un .csvfichier ; vous pourrez l'utiliser plus tard ! 😉 Vous pouvez enregistrer toutes les informations qui vous semblent importantes ! N'oubliez pas d'enregistrer le nom des villes et de créer une colonne contenant un identifiant unique (id) pour chaque ville (important pour la suite du projet).

Utilisez plotly pour afficher les meilleures destinations sur une carte

Scrape Booking.com
Étant donné que BookingHoldings ne dispose pas de bases de données agrégées, il sera beaucoup plus rapide d'extraire les données directement de booking.com.

Vous pouvez extraire autant d'informations que vous le souhaitez, mais nous vous suggérons d'obtenir au moins :

nom de l'hôtel,
URL vers sa page booking.com,
Ses coordonnées : latitude et longitude
Note attribuée par les utilisateurs du site
Description textuelle de l'hôtel

Créez votre lac de données avec S3
Une fois que vous avez réussi à créer votre ensemble de données, vous devez le stocker dans S3 sous forme de fichier csv.

ETL
Une fois vos données chargées sur S3, il sera plus judicieux pour la prochaine équipe d'analyse d'extraire les données propres directement depuis un entrepôt de données. Créez donc une base de données SQL avec AWS RDS, extrayez vos données de S3 et stockez-les dans votre nouvelle base de données.

Livrable 📬
Pour mener à bien ce projet, votre équipe doit fournir :

Un .csvfichier dans un bucket S3 contenant des informations enrichies sur la météo et les hôtels pour chaque ville française

Une base de données SQL où nous devrions pouvoir obtenir les mêmes données nettoyées à partir de S3

Deux cartes contenant un top 5 des destinations et un top 20 des hôtels de la région. Vous pouvez utiliser Plotly ou une autre bibliothèque pour cela. 
