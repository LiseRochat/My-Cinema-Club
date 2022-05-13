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



if __name__ == "__main__":
    m = Movie("harry potter")
    print(m)