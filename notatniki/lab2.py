# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 🌸 Programowanie obiektowe

# %% [markdown]
# ### ~ Wstęp ~

# %% [markdown]
# **Obiekt:** konkretny egzemplarz klasy, np. ksiazka1 = Ksiazka("Red Rising", "Pierce Brown"). <br>
# **Atrybut:** informacja przechowywana w obiekcie, np. tytul, autor. <br>
# **Metoda:** funkcja zdefiniowana wewnątrz klasy, która określa, co obiekt może robić, np. pokaz_autora().

# %%
class Ksiazka:  # klasa
    def __init__(self, tytul, autor):  # konstruktor
        self.tytul = tytul  # atrybut
        self.autor = autor  # atrybut

    def podaj_autora(self):  # metoda
        print(f"autor to {self.autor}")


# %%
ksiazka1 = Ksiazka('red rising', 'pierce brown')  # obiekt
ksiazka2 = Ksiazka('tog','sjm')

# %%
print(ksiazka1.tytul)

# %%
ksiazka2.podaj_autora()


# %% [markdown]
# ### ~ Dziedziczenie ~

# %%
class KsiazkaSciFi(Ksiazka):
    def __init__(self, tytul, autor, gatunek):
        super().__init__(tytul, autor)  # pozwala wywołać metodę klasy, po której dziedziczymy
        self.gatunek = gatunek
    
    def jest_scifi(self):
        if self.gatunek == 'sci-fi':
            print(f"{self.tytul} jest scifi")
        else:
            print(f"{self.tytul} nie jest scifi")


# %%
ksiazka3 = KsiazkaSciFi('mistborn','brandon sanderson','fantasy')

# %%
ksiazka3.jest_scifi()
