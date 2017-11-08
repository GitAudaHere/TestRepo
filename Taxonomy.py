class Kingdom:
    kingdoms = [
        'Animalia',
        'Archaebacteria',
        'Eubacteria',
        'Fungi',
        'Plantae',
        'Protista'
    ]

    def __init__(self, kingdom):
        self.kingdom = kingdom

    def __str__(self):
        return f'The kingdom of {self.kingdom}.'

    def get_kingdom(self):
        return self.kingdom


class Phylum(Kingdom):
    animal_phyla = [
        'Anthropoda',
        'Annelida',
        'Chordata',
        'Cnidaria',
        'Echinodermata',
        'Mollusca',
        'Nematoda',
        'Platyhelminthes',
        'Porifera'
    ]

    archael_phyla = [
        'Crenarchaeota',
        'Euryarchaeota',
        'Korarchaeota',
        'Nanoarchaeota',
        'Thaumarchaeota'
    ]

    bacterial_phyla = [
        'Acidobacteria',
        'Actinobacteria',
        'Aquificae',
        'Armatimonadetes',
        'Bacteroidetes',
        'Caldiserica',
        'Chlamydiae',
        'Chlorobi',
        'Chloroflexi',
        'Chrysiogenetes',
        'Cyanobacteria',
        'Deferribacteres',
        'Deinococcus-Thermus',
        'Dictyoglomi',
        'Elusimicrobia',
        'Fibrobacteres',
        'Firmicutes',
        'Fusobacteria',
        'Gemmatimonadetes',
        'Lentisphaerae',
        'Nitrospira',
        'Planctomycetes',
        'Proteobacteria',
        'Spirocaetes',
        'Synergistetes',
        'Tenericutes',
        'Thermodesulfobacteria',
        'Thermotogae',
        'Verrucomicrobia'
    ]

    fungal_phyla = [
        'Ascomycota',
        'Basidioycota',
        'Blastocladiomycota',
        'Chytridiomycota',
        'Glomeromycota',
        'Microsporidia',
        'Neocallimastigomycota',
        'Zygomycota'
    ]

    plant_phyla = [
        'Anthocerotophyta',
        'Bryophyta',
        'Charophyta',
        'Chlorophyta',
        'Cycadophyta',
        'Ginkophyta',
        'Glaucophyta',
        'Gnetophyta',
        'Lycopodiophyta',
        'Magnoliophyta',
        'Marchantiophyta',
        'Pinophyta',
        'Pteridophyta'
    ]

    protista_phyla = [
        'Amoebozoa',
        'Bigyra',
        'Cerccozoa',
        'Choanozoa',
        'Ciliophora',
        'Cryptista',
        'Euglenozoa',
        'Foraminifera',
        'Haptophyta',
        'Loukozoa',
        'Metamonada',
        'Myzozoa',
        'Mycetozoa',
        'Ochrophyta',
        'Oomycota',
        'Percolozoa',
        'Radiozoa',
        'Sarcomastigophora',
        'Sulcozoa'
    ]

    phyla = {
        'Animalia': animal_phyla,
        'Archaebacteria': archael_phyla,
        'Eubacteria': bacterial_phyla,
        'Fungi': fungal_phyla,
        'Plantae': plant_phyla,
        'Protista': protista_phyla
    }

    def __init__(self, phylum):
        self.phylum = phylum
        for kingdom, phyla in self.phyla.items():
            for the_phylum in phyla:
                if the_phylum == self.phylum:
                    super().__init__(kingdom)

    def __str__(self):
        return f'The phylum of {self.phylum} ' \
               f'of the kingdom {self.get_kingdom()}.'

    def get_phylum(self):
        return self.phylum


# TODO: Complete the Class class
class Class(Phylum):
    pass


# TODO: Complete the Order class
class Order(Class):
    pass


# TODO: Complete the Family class
class Family(Order):
    pass


# TODO: Complete the Genus class
class Genus(Family):
    pass


# TODO: Complete the Species class
class Species(Family):
    pass

chordata = Phylum('Chlorophyta')
print(chordata)
