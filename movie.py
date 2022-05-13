import os
# Chemin du dossier my-cinema-club
CUR_DIR = os.path.dirname(__file__)
# Chemin du fichier moovies.json
DATA_FILE = os.path.join(CUR_DIR, "data","moovies.json")

class Movie:
    def __init__(self, title : str):
        self.title = title
    
    def __str__(self):
        """
        Affiche et Formate l'affichage de l'instance créer 

        Returns:
            str : convertion la première lettre de chaque mot en majuscule, retourne le titre
        """
        return f"{self.title.title()}\n"

    def _get_movies(self):
        """
        Méthode pour Ouvrir et lire le fichier moovies.jsson
        """
        pass

    def _write_movies(self):
        """
        Méthode pour Ouvrir et Ecrire dans le fichier moovies.json
        """
        pass


if __name__ == "__main__":
    m = Movie("harry potter")
    print(m)