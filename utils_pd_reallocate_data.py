import pandas as pd
df_a = pd.read_csv('./bank_0_8.csv')
df_b = pd.read_csv('./bank_8_16.csv')
res= df_a["id"]==df_b['id']
res.sum()==df_a.shape[0] # true

df_id=df_a["id"]
total_df=pd.concat([df_a.iloc[:, 1:], df_b.iloc[:, 1:]], axis=1)
alice_new_df=total_df.iloc[:, :15]
alice_new_df=pd.concat([df_id, alice_new_df], axis=1)
alice_new_df.to_csv("./my_bank_0_15.csv", index=False)
bob_new_df=total_df.iloc[:, 15:]
bob_new_df=pd.concat([df_id, bob_new_df], axis=1)
bob_new_df.to_csv("./my_bank_16.csv", index=False)