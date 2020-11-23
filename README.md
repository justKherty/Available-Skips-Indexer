# Foundation Non Reserved Non Translated Articles Indexer
# Shortened as : Foundation Articles Indexer (FAI)

----

Les scripts FAI permettent de : 

-> Indexer les articles non traduits de la branche originale 

-> Récupérer et indexer les articles réservés par la branche française

-> Comparer les deux listes pour lister les articles non-réservés, et pas encore traduits

Les scripts FAi ne **permettent pas** pour l'instant : 

-> D'avoir une interface graphique

-> De donner les liens hypertextes (soon)

-> Être utilisé pour les besoins des autres branches

-> De supprimer automatiquement les fichiers .csv (very soon)


FAI ne donne que les numéros des articles correspondant aux deux critères précedent (non traduits, non réservés). L'objectif principal de FAI est de vérifier plus rapidement si les articles pas encore traduits n'ont pas encore été réservés auparavent, et donne une liste d'articles 

# Fonctionnement

Il faut exécuter le script SCRAPPER.py pour construire la liste d'articles réservés.
Ensuite, il faut exécuter le script TRANSLATING.py pour construire la liste d'articles par encore traduits. (est très long pour l'instant !) Puis finalement, exécuter le script COMPFIN.py pour comparer les deux listes, et intégrer cette liste dans le fichier de données FAINDEXED.csv.

# Dépendances

FAI nécessite:

> BeautifulSoup (bs4)

> urllib3
