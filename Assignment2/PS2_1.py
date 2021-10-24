import pandas as pd
import matplotlib.pyplot as plt


def CountEq_LargestEq(country):
    country = country.upper()
    frame = pd.read_table('earthquakes-2021-10-13_19-14-37_+0800.tsv').groupby('Country')
    grouped_frame = frame.get_group(country).sort_values("Mag", ascending=False)
    print('The total number of earthquakes since 2150 B.C.: %d\n' % grouped_frame.shape[0])
    grouped_frame.rename(columns={'Mo': 'Month', 'Dy': 'Day'}, inplace=True)
    print(grouped_frame[['Country', 'Year', 'Month', 'Day', 'Mag']].head(1))


if __name__ == '__main__':
    Sig_Eqs = pd.read_table('earthquakes-2021-10-13_19-14-37_+0800.tsv')
    grouped_sig = Sig_Eqs.groupby("Country").sum().sort_values("Deaths", ascending=False)
    print(grouped_sig["Deaths"].head(10))
    mag = Sig_Eqs[Sig_Eqs["Mag"] > 6.0]
    grouped_mag = mag[["Year", "Mag"]].groupby("Year").count().plot()
    plt.show()
    CountEq_LargestEq(input('Country:'))
