### This script uses pandas to pull the tables from the wikipedia link and stores them in a list called simpsons

import pandas as pd
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

print(len(simpsons))

print(simpsons[1])