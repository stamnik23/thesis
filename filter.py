import pandas as pd

#top100 names to keep
last_names_to_keep = [
    "Sinner", "Alcaraz", "Djokovic", "Zverev", "Medvedev", "Rublev", "Ruud", "Hurkacz",
    "de Minaur", "Dimitrov", "Tsitsipas", "Fritz", "Paul", "Shelton", "Rune", "Humbert",
    "Bublik", "Auger-Aliassime", "Baez", "Jarry", "Mannarino", "Khachanov", "Griekspoor",
    "Tabilo", "Lehecka", "Korda", "Cerundolo", "Tiafoe", "Navone", "Musetti", "Etcheverry",
    "Davidovich Fokina", "Machac", "Arnaldi", "Struff", "Monfils", "Thompson", "Fils",
    "Norrie", "Draper", "Darderi", "Marozsan", "Safiullin", "Zhang", "Eubanks", "Djere",
    "Martinez", "Borges", "Popyrin", "Cobolli", "Kotov", "Ofner", "Kecmanovic", "Giron",
    "Fucsovics", "Moutet", "Lajovic", "Sonego", "Shevchenko", "Munar", "Michelsen", "Evans",
    "Carballes Baena", "Diaz Acosta", "Koepfer", "Mpetshi Perricard", "Rinderknech",
    "O'Connell", "Coria", "Nakashima", "Seyboth Wild", "Ruusuvuori", "Nardi", "McDonald",
    "Cazaux", "Monteiro", "Nagal", "Muller", "Mensik", "Hijikata", "Bergs", "Gaston",
    "Kovacevic", "Daniel", "Bautista Agut", "Marterer", "Vukic", "Coric", "Altmaier",
    "Lestienne", "Hanfmann", "Karatsev", "Wawrinka", "Kokkinakis", "Berrettini", "Shang",
    "Murray", "Harris", "van de Zandschulp", "Purcell"
]


df = pd.read_excel("raw_followers_data.xlsx")


def contains_last_name(full_name, last_names):
    return any(last_name in full_name for last_name in last_names)


filtered_df = df[df['Follower'].apply(lambda x: contains_last_name(x, last_names_to_keep)) & df['Following'].apply(lambda x: contains_last_name(x, last_names_to_keep))]


filtered_df.to_excel("filtered_followers_data.xlsx", index=False)

print("end of process")
