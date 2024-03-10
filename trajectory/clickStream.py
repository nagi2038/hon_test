from pandas import read_csv
columns = [
# 'year',
# 'month',
# 'day',
'session ID',
'order',
'country',
'page 1 (main category)',
'page 2 (clothing model)',
'colour',
'location', 
'model photography', 
'price', 'price 2', 
'page'
    ]

df = read_csv(r'trajectory/e-shop clothing 2008.csv',delimiter=";",dtype= str,
usecols = columns).sort_values(by=['session ID', 'order']).loc[:, columns]

df.drop(['order'],axis=1, inplace=True)


fileName = "click.csv"
with open(fileName, 'w') as file:
    for group , sites in df.groupby('session ID'):
        file.write(sites.values[0][0]  + "," + ",".join(["".join(site[1:]) for site in sites.values ]))
        file.write("\n")