import os, json

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

        Returns:
            liste: contenu du fichier moovies.json
        """
        with open(DATA_FILE, "r") as file:
            movie = json.load(file)
        return movie

    def _write_movies(self, movies):
        """
        Méthode pour Ouvrir et Ecrire dans le fichier moovies.json

        Args:
            movies (list[str]): liste de films
        """
        with open(DATA_FILE, "a") as file:
            json.dump(movies,file, indent=4)


if __name__ == "__main__":
    m = Movie("harry potter")
    print(m)