import util

class Studente:
    def __init__(self, name, cognome, anno_nascita):
        self.name = name
        self.cognome = cognome
        self.anno_nascita = anno_nascita
        self.voti = []

    def eta(self):
        return 2025 - self.anno_nascita

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def media(self):
        return util.media(self.voti) if self.voti else 0

    def scheda(self):
        media_voti = util.media(self.voti) if self.voti else 0
        print(f"Lo studente si chiama {self.name} {self.cognome}, ha {self.eta()} anni e la sua media scolastica è {media_voti}")
