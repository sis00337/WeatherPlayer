# WeatherPlayer | Hack the North

### Members: Denise, Jazica, Kyle, Mike 


## Inspiration
We thought it would be cool to have music that fit the
environment, as if living in a movie.

## What it does
WeatherPlayer lets the user input a city and
returns a list of recommended songs based on
the weather in the city. Users enter the city
they are in to get music suggestions that may
fit the mood of the weather.
 
## How we built it
We used Python with Flask to handle the backend features 
and Pycharm as our IDE. API's used are OpenWeatherMap, 
GeoCode, iTunes. We grabbed artist data from billboard.com
using the BeautifulSoup4 package. We used JSON files to 
store and access data for the music playlist.

## Challenges we ran into
As this is our first Hackathon for most of us, many
seemingly trivial matters are difficult. Our biggest
challenges involved finding the appropriate API's and 
understanding the structure of an app that uses Flask.
 
## Accomplishments that we're proud of
We made something that works in a short time on our own
with minimal guidance. 

## What we learned
We learned to use Flask (and some Jinja templating),
pulling data from API's, and how to work with each 
other effectively using github and reviewing code. 

## What's next for WeatherPlayer
Currently, we are using a fixed library of songs. 
The next step will be to integrate a music API, such as 
Spotify or Youtube, so that music suggestions get updated
as new music appears. Also, song suggestions can be 
more customized to more specific weather conditions.
Finally, we'll want to successfully host the app.
