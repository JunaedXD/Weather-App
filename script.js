document.getElementById("getWeather").addEventListener("click", async () => {
    const city = document.getElementById("city").value.trim();
    if (!city) { alert("Please enter a city name"); return; }

    try {
        const response = await fetch("/get_weather", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ city })
        });

        const data = await response.json();

        const weatherCard = document.getElementById("weatherCard");
        if (response.ok) {
            weatherCard.style.display = "block";
            weatherCard.innerHTML = `
                <p>📍 <strong>${data.city}, ${data.country}</strong></p>
                <p>🌡️ Temperature: ${data.temperature} °C</p>
                <p>☁️ Weather: ${data.weather}</p>
                <p>💧 Humidity: ${data.humidity}%</p>
                <p>🌬️ Wind: ${data.wind} m/s</p>
            `;
        } else {
            weatherCard.style.display = "block";
            weatherCard.innerHTML = `<p style="color:red;">${data.error}</p>`;
        }
    } catch (err) {
        alert("Error connecting to the server.");
        console.error(err);
    }
});
