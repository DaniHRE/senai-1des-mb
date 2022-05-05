import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

data = {'Pais': ['Brasil', 'Colombia', 'Índia'],
        'Capital': ['Brasília', 'Bogotá', 'Nova Delhi']}

df = pd.DataFrame(data, columns=['Pais', 'Capital'])
df['População'] = 0
df = pd.DataFrame(data, columns=['Pais', 'Capital', 'População'])
qde = df['Pais'].count()
for i in range(qde):
    df['População'][i] = float(input(f'População do {df["Pais"][i]}: '))



# MAT PLOT LIB EXEMPLO
# plt.rcdefaults()
# fig, ax = plt.subplots()
# countries = []
#
# for i in range(qde):
#     countries.append(df['Pais'][i])
#
# print(countries)
# y_pos = np.arange(len(countries))
# performance = 3 + 10 * np.random.rand(len(df['População'][:]))
# error = np.random.rand(len(df['População'][:]))
#
# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=countries)
# ax.invert_yaxis()
# ax.set_xlabel('População dos Países')
# ax.set_title('População dos Países')
#
# plt.show()

print(df)
