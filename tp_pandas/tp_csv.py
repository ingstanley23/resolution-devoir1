#programme export dataframe en fichier csv
import pandas as pan
#affichage du fichier de travail
df = pan.read_csv("data/haiti_earthquake_pass7days_from_2023-01-18.csv")
#difinir la liste
list = df.values.tolist()
#print(df)


#print(list)
# affichage des entetes de colonnes
df.head(13)
#creer la colonne impact
df.loc[df["magnitude"] < 2, "impact"] = "tres faible"
df.loc[df["magnitude"] >= 2, "impact"] = "faible"
#print(df)
#conertir la liste en dataframe
df1=pan.DataFrame(df)
#print(df1) mesi Graville, ou tre janti
#covertir dataframe en csv
#df1.to_csv("C:\\Users\\Admin\\Desktop\\tp_pandas\\output\\Graville.csv")
df1.to_csv("output/Graville.csv")

#good job

  
  
  
  
  
  
  
            
  
  
  
  
  
  
  
  
  
  
