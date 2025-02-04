import pandas as pd
df = pd.read_csv ('Popular_Spotify_Songs.csv', encoding='latin-1')
pd.set_option('display.max_columns', None, 'display.width', 1000)
pd.set_option('display.max_rows',None)
#print(df)
#upload CSV file, had to change encoding due to error message.

df.drop(columns = ['artist_count','released_day','in_spotify_playlists','in_spotify_charts','in_apple_playlists','in_apple_charts','in_deezer_playlists','in_deezer_charts','in_shazam_charts','bpm','key','mode','danceability_%','valence_%','energy_%','acousticness_%','instrumentalness_%','liveness_%', 'speechiness_%'], inplace = True)
#print(df.info())
df['streams'] = pd.to_numeric(df['streams'], errors='coerce', downcast='integer')
df = df.dropna()
df['streams'] = df['streams'].astype(int)
#print(df)
# add in display options - all columns and rows visible and dropping any columns we don't need to see.
# checked to see types of columns, had to change streams from object to int.
# convert streams to a numberic value. errors = coerece to show any value in 'streams' that's NaN then delete row by df.dropna() and ensure streams col=int

streams_per_year = df.groupby('released_year')['streams'].sum().reset_index()
#groupby function to group together the released year to get a sum of total amount of streams for each year.

list_of_streams = df['streams'].tolist()
total_streams = sum(list_of_streams)
print(f'The total number of Spotify streams is: {total_streams}')
#the added up all streams in a list to get the total sum for streams across spotify

max_year = streams_per_year['streams'].idxmax()
highest_streams_year = streams_per_year.iloc[max_year]
print(f'The year with the most streams was: {highest_streams_year["released_year"]}, which had a total of {highest_streams_year["streams"]} streams')

min_year = streams_per_year['streams'].idxmin()
lowest_streams_year = streams_per_year.iloc[min_year]
print(f'The year with the least streams was: {lowest_streams_year["released_year"]}, which had a total of {lowest_streams_year["streams"]} streams')
#find the row with the max/min value of 'streams'
#after finding that row, iloc used to identify the whole row that includes info on the released year.


popular_song = df.loc[df['streams'].idxmax()]
song = popular_song['track_name']
artist = popular_song['artist(s)_name']
stream_count = popular_song['streams']
year= popular_song ['released_year']
print(f'The song with the most streams on Spotify is: {song} by {artist} which has {stream_count} streams and was released in {year}')

least_popular = df.loc[df['streams'].idxmin()]
least_song = least_popular['track_name']
least_artist = least_popular['artist(s)_name']
least_stream_count = least_popular['streams']
least_year = least_popular ['released_year']
print(f'The song with the least streams on Spotify is: {least_song} by {least_artist} which has {least_stream_count} and was released in {least_year}')
#find the row of data that has the highest and lowest streams,then give the max/min value/ df.loc to locate the row and get info from multiple cols.


from matplotlib import pyplot as plt

x = streams_per_year['released_year']
y = streams_per_year['streams']
plt.plot(x,y)
plt.title ('Spotify Streams by Year')
plt.xlabel ('Released Year')
plt.ylabel ('Number of Streams')
plt.show()
