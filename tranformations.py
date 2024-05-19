import pandas as pd

country_to_continent = {
    'Switzerland': 'Europe', 'Iceland': 'Europe', 'Denmark': 'Europe', 'Norway': 'Europe', 'Canada': 'North America',
    'Finland': 'Europe', 'Netherlands': 'Europe', 'Sweden': 'Europe', 'New Zealand': 'Oceania', 'Australia': 'Oceania',
    'Israel': 'Asia', 'Costa Rica': 'North America', 'Austria': 'Europe', 'Mexico': 'North America',
    'United States': 'North America', 'Brazil': 'South America', 'Luxembourg': 'Europe', 'Ireland': 'Europe',
    'Belgium': 'Europe', 'United Arab Emirates': 'Asia', 'United Kingdom': 'Europe', 'Oman': 'Asia', 'Venezuela': 'South America',
    'Singapore': 'Asia', 'Panama': 'North America', 'Germany': 'Europe', 'Chile': 'South America', 'Qatar': 'Asia',
    'France': 'Europe', 'Argentina': 'South America', 'Czech Republic': 'Europe', 'Uruguay': 'South America',
    'Colombia': 'South America', 'Thailand': 'Asia', 'Saudi Arabia': 'Asia', 'Spain': 'Europe', 'Malta': 'Europe',
    'Taiwan': 'Asia', 'Kuwait': 'Asia', 'Suriname': 'South America', 'Trinidad and Tobago': 'North America',
    'El Salvador': 'North America', 'Guatemala': 'North America', 'Uzbekistan': 'Asia', 'Slovakia': 'Europe',
    'Japan': 'Asia', 'South Korea': 'Asia', 'Ecuador': 'South America', 'Bahrain': 'Asia', 'Italy': 'Europe',
    'Bolivia': 'South America', 'Moldova': 'Europe', 'Paraguay': 'South America', 'Kazakhstan': 'Asia', 'Slovenia': 'Europe',
    'Lithuania': 'Europe', 'Nicaragua': 'North America', 'Peru': 'South America', 'Belarus': 'Europe', 'Poland': 'Europe',
    'Malaysia': 'Asia', 'Croatia': 'Europe', 'Libya': 'Africa', 'Russia': 'Europe', 'Jamaica': 'North America',
    'North Cyprus': 'Europe', 'Cyprus': 'Europe', 'Algeria': 'Africa', 'Kosovo': 'Europe', 'Turkmenistan': 'Asia',
    'Mauritius': 'Africa', 'Hong Kong': 'Asia', 'Estonia': 'Europe', 'Indonesia': 'Asia', 'Vietnam': 'Asia',
    'Turkey': 'Asia', 'Kyrgyzstan': 'Asia', 'Nigeria': 'Africa', 'Bhutan': 'Asia', 'Azerbaijan': 'Asia', 'Pakistan': 'Asia',
    'Jordan': 'Asia', 'Montenegro': 'Europe', 'China': 'Asia', 'Zambia': 'Africa', 'Romania': 'Europe', 'Serbia': 'Europe',
    'Portugal': 'Europe', 'Latvia': 'Europe', 'Philippines': 'Asia', 'Somaliland region': 'Africa', 'Morocco': 'Africa',
    'Macedonia': 'Europe', 'Mozambique': 'Africa', 'Albania': 'Europe', 'Bosnia and Herzegovina': 'Europe', 'Lesotho': 'Africa',
    'Dominican Republic': 'North America', 'Laos': 'Asia', 'Mongolia': 'Asia', 'Swaziland': 'Africa', 'Greece': 'Europe',
    'Lebanon': 'Asia', 'Hungary': 'Europe', 'Honduras': 'North America', 'Tajikistan': 'Asia', 'Tunisia': 'Africa',
    'Palestinian Territories': 'Asia', 'Bangladesh': 'Asia', 'Iran': 'Asia', 'Ukraine': 'Europe', 'Iraq': 'Asia',
    'South Africa': 'Africa', 'Ghana': 'Africa', 'Zimbabwe': 'Africa', 'Liberia': 'Africa', 'India': 'Asia', 'Sudan': 'Africa',
    'Haiti': 'North America', 'Congo (Kinshasa)': 'Africa', 'Nepal': 'Asia', 'Ethiopia': 'Africa', 'Sierra Leone': 'Africa',
    'Mauritania': 'Africa', 'Kenya': 'Africa', 'Djibouti': 'Africa', 'Armenia': 'Asia', 'Botswana': 'Africa', 'Myanmar': 'Asia',
    'Georgia': 'Europe', 'Malawi': 'Africa', 'Sri Lanka': 'Asia', 'Cameroon': 'Africa', 'Bulgaria': 'Europe', 'Egypt': 'Africa',
    'Yemen': 'Asia', 'Angola': 'Africa', 'Mali': 'Africa', 'Congo (Brazzaville)': 'Africa', 'Comoros': 'Africa', 'Uganda': 'Africa',
    'Senegal': 'Africa', 'Gabon': 'Africa', 'Niger': 'Africa', 'Cambodia': 'Asia', 'Tanzania': 'Africa', 'Madagascar': 'Africa',
    'Central African Republic': 'Africa', 'Chad': 'Africa', 'Guinea': 'Africa', 'Ivory Coast': 'Africa', 'Burkina Faso': 'Africa',
    'Afghanistan': 'Asia', 'Rwanda': 'Africa', 'Benin': 'Africa', 'Syria': 'Asia', 'Burundi': 'Africa', 'Togo': 'Africa',
    'Puerto Rico': 'North America', 'Belize': 'North America', 'Somalia': 'Africa', 'Somaliland Region': 'Africa', 'Namibia': 'Africa',
    'South Sudan': 'Africa', 'Taiwan Province of China': 'Asia', 'Hong Kong S.A.R., China': 'Asia', 'Trinidad & Tobago': 'North America',
    'Northern Cyprus': 'Europe', 'North Macedonia': 'Europe', 'Gambia': 'Africa'
}

def country_continent(country_name):
    return country_to_continent.get(country_name, 'Unknown')

#happy = pd.read_csv("happy.csv")
#happy['Continent'] = happy['Country'].apply(get_continent)
#print(happy)


def drop_rank(df):
    df.drop(columns=[ 'Happiness Rank'], inplace=True)
    return df
#happy = drop_rank(happy)
#print(happy)