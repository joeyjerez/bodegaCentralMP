/* Localización */
function showPosition(position) {

    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var apiKey = getMapsKey();
    var img_url = `http://maps.googleapis.com/maps/api/staticmap?center=${lat},${lon}&zoom=14&size=250x250&sensor=false&key=${apiKey}`;

    document.getElementById("mapa").innerHTML = "<img src='" + img_url + "'>";

    var units = 'metric';
    var lang = 'sp';
    var apiid = getWeatherKey();
    var url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=${units}&lang=${lang}&appid=${apiid}`;

    $.get(url, function (data) {
        var iconurl = `http://openweathermap.org/img/w/${data.weather[0].icon}.png`;
        var html = `<h4 id="clima_local" class="text-capitalize fs-4 my-0 py-0">${data.name}<span class="fs-6 fw-bold text-danger">(${data.sys.country})</span>, ${data.main.temp}°C <a href="https://openweathermap.org/find?q=${data.name}%2C%20${data.sys.country}" target="_blank"><img class="img-clima" src="${iconurl}" alt="Haz click para más información"></a></h4>`;
        $('#info_clima').removeClass('fw-bold text-danger').html(html);
    }, 'json').fail(function () {
        $('#info_clima').addClass('fw-bold text-danger').html("<h4>No se ha encontrado su ciudad actual</h4>");
    });
}

function showError(error) {

    switch(error.code) {
        case error.PERMISSION_DENIED:
            $('#info_clima').addClass('fw-bold text-danger').html("<p class='py-0 my-0'>Ubicación bloqueada por el usuario</p>");
            break;
        case error.POSITION_UNAVAILABLE:
            $('#info_clima').addClass('fw-bold text-danger').html("<p class='py-0 my-0'>Ubicación actual no disponible</p>");
            break;
        case error.TIMEOUT:
            $('#info_clima').addClass('fw-bold text-danger').html("<p class='py-0 my-0'>Petición de ubicación expirada</p>");
            break;
        case error.UNKNOWN_ERROR:
            $('#info_clima').addClass('fw-bold text-danger').html("<p class='py-0 my-0'>Ha ocurrido un error desconocido</p>");
            break;
    }

}

function getLocation() {

    var x = document.getElementById("info_clima");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition,showError)        
    } else {
        x.innerHTML = "La Geolocalización no es soportada por tu navegador.";
    }
    
}

/* Fin localización */