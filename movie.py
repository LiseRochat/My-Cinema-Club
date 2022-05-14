import os, json, logging


logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s : %(message)s")
# Chemin du dossier my-cinema-club
CUR_DIR = os.path.dirname(__file__)
# Chemin du fichier movies.json
DATA_FILE = os.path.join(CUR_DIR, "data","movies.json")

def get_movies():
        """
        Récupère tous les films présent dans le fichier movies.json sous forme d'instance de Movie
        """
        movies_instance = []
        with open(DATA_FILE, "r") as file:
            movies = json.load(file)
        for movie in movies:
            new_movie = Movie(movie)
            movies.append(new_movie)
        return movies_instance

class Movie:
    def __init__(self, title : str):
        self.title = title.title()
    
    def __str__(self):
        """
        Affiche et Formate l'affichage de l'instance créer 

        Returns:
            str :  retourne le titre
        """
        return f"{self.title}\n"
    
    def _get_movies(self):
        """
        Méthode pour Ouvrir et lire le fichier movies.jsson

        Returns:
            liste: contenu du fichier movies.json
        """
        with open(DATA_FILE, "r") as file:
            movie = json.load(file)
            return movie

    def _write_movies(self, movies):
        """
        Méthode pour Ouvrir et Ecrire dans le fichier movies.json

        Args:
            movies (list[str]): liste de films
        """
        with open(DATA_FILE, "w") as file:
            json.dump(movies, file, indent=4)
    
    def add_to_movies(self):
        """
        Récupère la liste des films.
        Vérifie que le film n'est pas déjà dans la liste. Si ce n'est pas le cas on l'ajoute dans la liste. 
        Sinon on affiche un message pour indiquer que le film est déjà dans la liste.

        Returns:
            booléen: Vrais si le film est ajouté, Faux : message indiquant que le film existe déjà 
        """
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True

        else:
            logging.warning(f"Le film {self.title} est déjà enregistré.")
            return False

    def remove_from_movies(self):
        """
        Récupère la liste des films.
        Si c'est le cas on le supprime
        """
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
        
            
    
if __name__ == "__main__":
    m = Movie("lili")
    m.add_to_movies()