class Boisson:
    def __init__(self, volume, peremption) -> None:
        self.volume = volume
        self.peremption = peremption

    def __str__(self):
        return f"Volume : {self.volume} ml\nPeremption : dans {self.peremption} jour(s)"

    def prochain_jour(self):
        self.peremption -= 1

