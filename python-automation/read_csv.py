### this script downloads a csv file from a website
### link: https://football-data.co.uk/mmz4281/2223/E0.csv

import pandas as pd

football_data = pd.read_csv('https://football-data.co.uk/mmz4281/2223/E0.csv')

### renames two headers from the CSV to be more descriptive
football_data.rename(columns={'FTHG':'home_goals', 'FTAG':'away_goals'}, inplace = True)

print(football_data)