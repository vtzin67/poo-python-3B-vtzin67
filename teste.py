class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(f"{self.titulo} ({self.genero})")


class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(f"Filme: {self.titulo} | {self.genero} | {self.duracao} min")


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"Série: {self.titulo} | {self.genero} | {self.temporadas} temporadas")


class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(f"Documentário: {self.titulo} | {self.genero} | Tema: {self.tema}")


class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
        print(f"Podcast: {self.titulo} | {self.genero} | {self.episodios} episódios")


# Missão 1
catalogo = [
    Filme("Interestelar", "Ficcao", 169),
    Filme("Shrek", "Animacao", 90),
    Serie("Stranger Things", "Ficcao", 4),
    Serie("Round 6", "Suspense", 2),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem"),
]

# Missão 3
catalogo.append(Podcast("Nerdcast", "Humor", 900))

print()
for item in catalogo:      # o mesmo laço, sem nenhuma mudança
    item.exibir_info()