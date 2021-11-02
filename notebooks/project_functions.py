l= (pd.DataFrame(data= df, columns=data.feature_names)
pf = (   
    l.pipe(csnap)
    #pd.DataFrame(data = df,columns=data.feature_names)
    .rename(columns={"Logged GDP per capita": "GDP"})
    .query('Ladder score > 7')
    .sort_values("Ladder score", ascending=False)
    .reset_index(drop=True)
    #.loc[:, ["alcohol", "ci", "hue"]]
)

pf