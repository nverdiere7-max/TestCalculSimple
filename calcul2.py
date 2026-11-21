def multiplier_par_deux(valeur):
    """Retourne le double de la valeur fournie."""
    return valeur * 3


if __name__ == "__main__":
    saisie = input("Entrez un nombre : ")
    nombre = float(saisie.replace(",", "."))
    resultat = multiplier_par_deux(nombre)
    print(f"Le double de {nombre} est {resultat}")