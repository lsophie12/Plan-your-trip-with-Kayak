import scrapy
import os
import sys
import logging
from scrapy.crawler import CrawlerProcess

class BookingSpider(scrapy.Spider):
    name = "booking"
    
    # Liste des destinations
    if len(sys.argv) > 1:
        destinations = sys.argv[1].split(";")   
    else:
        destinations = ["Paris"]
    
    # URL de départ pour chaque destination 
    # avec sélection des hôtels avec notes des commentaires supérieur à 8 
    # et trier par le plus de commentaires positifs
    start_urls = [f"https://www.booking.com/searchresults.fr.html?ss={destination}&order=bayesian_review_score&nflt=review_score%3D90%3Bht_id%3D204%3Breview_score%3D80" 
                  for destination in destinations]

    def parse(self, response):
        # XPath pour sélectionner les hôtels
        hotels = response.xpath('//div[@data-testid="property-card"]')

        for hotel in hotels:
            nom = hotel.xpath('.//div[@data-testid="title"]/text()').get()
            #experience = hotel.xpath('.//div[@class="abf093bdfe f45d8e4c32 d935416c47"]/text()').get()
            #experience = int(experience[0:-19].replace(" ",""))
            score = hotel.xpath('.//div[@class="a3b8729ab1 d86cee9b25"]/text()').get()
            url = hotel.xpath('.//h3[@class="aab71f8e4e"]/a/@href').get()
            description = hotel.xpath('.//div[@class="abf093bdfe"]/text()').get()

            # Effectuer une nouvelle requête pour la page de l'hôtel afin de récupérer les coordonnées
            yield scrapy.Request(
                url,
                callback=self.parse_hotel_coordinates,
                meta={
                    'destination': response.url.split('=')[1].replace('&order','').replace('%',' '),
                    'nom': nom,
                    'score': score,
                    'url': url,
                    'description': description
                }
            )

    def parse_hotel_coordinates(self, response):
        coordinates = response.xpath('//a[@data-atlas-latlng]/@data-atlas-latlng').get()
        latitude, longitude = coordinates.split(',')

        # Récupérer les données envoyées avec 'meta'
        destination = response.meta['destination']
        nom = response.meta['nom']
        url = response.meta['url']
        score = response.meta['score']
        description = response.meta['description']

        yield {
            'destination' : destination,
            'nom': nom,
            'score': score,
            'latitude' : latitude,
            'longitude' : longitude,
            'url': url,
            'description': description
        }


# Configuration et exécution du crawler
BASE_DIR = './src'
filename = "best_hotels.json"
filepath = os.path.join(BASE_DIR, filename)

# Supprimer l'ancien fichier s'il existe
if os.path.exists(filepath):
    os.remove(filepath)

# Lancer le processus Scrapy
process = CrawlerProcess(settings={
    'USER_AGENT': 'Chrome/130.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {filepath: {"format": "json"}}
})

process.crawl(BookingSpider)
process.start()

