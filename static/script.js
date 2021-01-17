let weather = document.querySelector(".weather");

const API_KEY = `fb948a68fea5555ccf35cc9260208dd9`;

function getWeather(lat, lon){
    fetch(
    `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    ).then(function(response){
        return response.json();
    }).then(function(json){
        let temperature = json['main']['temp'];
        let cityName = json['name'];
        let sunny_or_cloudy = json['weather'][0]['main'];
        weather.textContent = `${temperature} °C @ ${cityName} ${sunny_or_cloudy}`;
    })
}

function geoError(){
    weather.innerText = "Loading weather failed";
}

function geoSucces(position){
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;
    getWeather(latitude, longitude);
}

function askLocation(){
    navigator.geolocation.getCurrentPosition(geoSucces, geoError);
}

function init(){
    askLocation();
}

init();
