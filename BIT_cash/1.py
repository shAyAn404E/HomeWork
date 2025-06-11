import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


df = yf.download("BTC-USD", start="2020-01-01", end="2024-12-31")

df["Date"] = df.index
df["WeekDay"] = df["Date"].dt.weekday

bye = df["Open"][df["WeekDay"] == 2].reset_index(drop=True)
sell = df["Close"][df["WeekDay"] == 4].reset_index(drop=True)



combined = pd.merge(bye, sell, left_index=True, right_index=True)
rezalt1 = df.apply(lambda row: row["Close"] / row["Open"], axis=1)
combined_list = [row.tolist() for _,row in rezalt1.iterrows()]
print(combined_list)

S = []
mo = 1000
for i in combined_list:
    for j in i:
        mo = mo * j
        S.append(mo)

print(mo)
print(S)
plt.plot(S)
plt.show()

# اگر فردی 1000 دلار سرمایه داشته باشد
# start="2020-01-01", end="2024-12-31"
# روزهای شماره 2 با قیمت Open بیت کوین خریداری کرده
# روزهای شماره 4 با قیمت Close فروخته

# میزان سرمایه
# نمودار سود و زیان

# print(bye,sell,df[["WeekDay"]])