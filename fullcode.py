import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


df_players = pd.read_excel("twitter_data_clear.xlsx", sheet_name="Players")
df_follows = pd.read_excel("twitter_data_clear.xlsx", sheet_name="Follows")

G_real = nx.Graph()


for _, row in df_players.iterrows():
    G_real.add_node(row['Player'], nationality=row['Nationality'], titles=row['ATP Titles'])

# add follow edges
for _, row in df_follows.iterrows():
    G_real.add_edge(row['Follower'], row['Following'])

# calculate metrics for real graph
if nx.is_connected(G_real):
    real_radius = nx.radius(G_real)
    real_diameter = nx.diameter(G_real)
else:
    real_radius = float('inf')
    real_diameter = float('inf')

real_density = nx.density(G_real)
real_clustering_coefficient = nx.average_clustering(G_real)

print("Real Graph")
print("Radius:", real_radius)
print("Diameter:", real_diameter)
print("Density:", real_density)
print("Clustering Coeff:", real_clustering_coefficient)

# Erdos Renyi graph
n = len(G_real.nodes)  # αριθμός κόμβων ίσος με τον πραγματικό γράφο
p = nx.density(G_real)  # πιθανότητα επανασύνδεσης ίση με την πυκνότητα του πραγματικού γράφου

G_er = nx.erdos_renyi_graph(n, p)


if nx.is_connected(G_er):
    er_radius = nx.radius(G_er)
    er_diameter = nx.diameter(G_er)
else:
    er_radius = float('inf')
    er_diameter = float('inf')

er_density = nx.density(G_er)
er_clustering_coefficient = nx.average_clustering(G_er)

print("Erdős-Rényi Γράφος")
print("Radius:", er_radius)
print("Diameter:", er_diameter)
print("Density:", er_density)
print("Clustering Coeff:", er_clustering_coefficient)

# Watts-Strogatz
k = 4
p_ws = 0.1

G_ws = nx.watts_strogatz_graph(n, k, p_ws)


if nx.is_connected(G_ws):
    ws_radius = nx.radius(G_ws)
    ws_diameter = nx.diameter(G_ws)
else:
    ws_radius = float('inf')
    ws_diameter = float('inf')

ws_density = nx.density(G_ws)
ws_clustering_coefficient = nx.average_clustering(G_ws)

print("Watts-Strogatz Γράφος")
print("Radius:", ws_radius)
print("Diameter:", ws_diameter)
print("Density:", ws_density)
print("Clustering Coef:", ws_clustering_coefficient)

#Barabasi-Albert
m = 2

G_ba = nx.barabasi_albert_graph(n, m)


if nx.is_connected(G_ba):
    ba_radius = nx.radius(G_ba)
    ba_diameter = nx.diameter(G_ba)
else:
    ba_radius = float('inf')
    ba_diameter = float('inf')

ba_density = nx.density(G_ba)
ba_clustering_coefficient = nx.average_clustering(G_ba)

print("Barabási-Albert Γράφος")
print("Radius:", ba_radius)
print("Diameter:", ba_diameter)
print("Density:", ba_density)
print("Clustering Coef:", ba_clustering_coefficient)

#create dataframe
metrics = {
    "Graph Type": ["Real", "Erdős-Rényi", "Watts-Strogatz", "Barabási-Albert"],
    "Radius": [real_radius, er_radius, ws_radius, ba_radius],
    "Diameter": [real_diameter, er_diameter, ws_diameter, ba_diameter],
    "Density": [real_density, er_density, ws_density, ba_density],
    "Clustering Coefficient": [real_clustering_coefficient, er_clustering_coefficient, ws_clustering_coefficient, ba_clustering_coefficient]
}

df_metrics = pd.DataFrame(metrics)

with pd.ExcelWriter("graph_metrics.xlsx") as writer:
    df_metrics.to_excel(writer, sheet_name="Metrics", index=False)

print("process completed")
