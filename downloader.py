#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Liste des pages à télécharger et analyser :
pages = [
"https://www.frenchweb.fr/e-sante-lefficacite-de-lintelligence-artificielle-mise-a-rude-epreuve-par-le-coronavirus/394689",
"https://www.frenchweb.fr/pourquoi-ce-ou-cette-developpeuse-ne-veut-pas-rejoindre-votre-start-up/310798",
"https://www.frenchweb.fr/intelligence-artificielle-et-la-creativite-dans-tout-ca/334210",
"https://www.frenchweb.fr/le-leadership-effectual-ou-les-5-principes-de-la-transformation-2-agir-en-perte-acceptable/324186",
"https://www.frenchweb.fr/le-management-ce-nest-pas-choisir-des-options-cest-definir-des-priorites/376702",
"https://www.frenchweb.fr/faut-il-plus-de-scientifiques-et-dingenieurs-en-politique/383048",
"https://www.frenchweb.fr/ia-et-ethique-le-contresens-navrant-de-cedric-villani/321805",
"https://www.frenchweb.fr/fw-radar-heuritech-la-start-up-qui-utilise-le-deep-learning-pour-anticiper-les-tendances-retail/323723",
"https://www.frenchweb.fr/numbers-combien-toyota-investit-il-dans-la-voiture-autonome/279360",
"https://www.frenchweb.fr/marissa-mayer-nommee-pdg-de-yahoo-13986/71442",
"https://www.frenchweb.fr/pourquoi-il-faut-creer-une-science-de-lartificiel/374573",
"https://www.frenchweb.fr/salon-qs-world-grad-school-tour-paris-2/282694",
"https://www.frenchweb.fr/faut-il-avoir-peur-du-plan-de-la-chine-pour-dominer-lintelligence-artificielle/393793",
"https://www.frenchweb.fr/un-monde-de-ruptures-le-grand-soir-des-modeles-mentaux/355552",
"https://www.frenchweb.fr/transformation-tirer-parti-des-surprises-pour-faire-bouger-nos-modeles-mentaux/363952",
"https://www.frenchweb.fr/vive-lidiotie-principe-de-vie-a-lusage-des-entrepreneurs-et-des-managers/327869",
"https://www.frenchweb.fr/made-in-grenoble-zoom-sur-digitalps-et-rencontre-avec-eric-gaussier-coordinateur-de-miaigrenoble-alpes/348958",
"https://www.frenchweb.fr/piles-a-biocarburant-comment-befc-peut-appliquer-sa-technologie-aux-dispositifs-medicaux/392969",
"https://www.frenchweb.fr/mener-un-projet-informatique-sans-la-dsi/318983",
"https://www.frenchweb.fr/unleash18-jour-1-mon-resume/339382",
"https://www.frenchweb.fr/la-vision-comme-modele-mental-ce-nest-pas-la-marche-au-hasard/349669",
"https://www.frenchweb.fr/derives-du-management-les-managers-manquent-ils-de-courage/339875",
]

# On crée un fichier output.csv dans le même dossier, dans lequel on va écrire les données extraites
outputFile = open("output.csv","w",encoding="utf8")

# On ajoute une ligne de titres de colonnes dans ce fichier
outputFile.writelines('"url","titre","sous-titre","date","contenu"\n')

# On lance Firefox
driver = webdriver.Firefox()

# Pour toute page de la liste des pages ci-dessus
for page in pages:

   # On visite la page :
   driver.get(page)
   print("Page visitée : "+page)

   # On récupère le titre dans l'élément ayant la classe CSS post-title
   titleE = driver.find_element_by_css_selector('.post-title')
   title = format(titleE.text)

   # On récupère le sous-titre éventuel dans l'élément ayant la classe CSS entry-sub-title
   subtitle = ""
   try:
      subtitleE = driver.find_element_by_css_selector('.entry-sub-title')
      subtitle = format(subtitleE.text)
   except:
      pass

   # On récupère la date dans l'élément ayant la classe CSS date situé dans l'élément ayant la classe post-meta
   dateE = driver.find_element_by_css_selector('.post-meta .date')
   date = format(dateE.text)

   # On récupère les éléments dans les balises p et h2 à l'intérieur de l'élément ayant la classe CSS entry
   contentE = driver.find_elements_by_css_selector('.entry p,h2')
   # Pour tout élément trouvé, on l'ajoute au texte, en mettant un | à la fin.
   texte = ""
   for element in contentE :
      texte += format(element.text)+" | "
   
   # On ajoute une ligne avec toutes les informations extraites au fichier output.csv
   outputFile.writelines('"'+page+'","'+title.replace('"',"''")+'","'+subtitle.replace('"',"''")+'","'+date.replace('"',"''")+'","'+texte.replace('"',"''")+'"\n')
   
   # On attend 5 secondes avant de passer à la page suivante
   time.sleep(5)

# On ferme le fichier output.csv
outputFile.close