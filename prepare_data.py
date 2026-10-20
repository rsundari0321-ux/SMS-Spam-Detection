import pandas as pd

df = pd.read_csv("SMSSpamCollection", sep="\t", header=None, names=["Category", "Message"])
df.to_csv("email.csv", index=False)

print("Dataset converted successfully!")
print(df.head())
print("Total messages:", len(df))
