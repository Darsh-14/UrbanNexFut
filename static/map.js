document.addEventListener("DOMContentLoaded", function () {
    console.log("Initializing Map...");

    if (document.getElementById('map')) {
        var map = L.map('map').setView([28.6139, 77.2090], 12);

        // Add OpenStreetMap tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
            subdomains: ['a', 'b', 'c']
        }).addTo(map);

        // Fetch green zones dynamically from Flask API
        fetch('/green-zones')
            .then(response => response.json())
            .then(data => {
                console.log("Fetched Data:", data);

                if (data.length === 0) {
                    console.warn("⚠ No green zones found!");
                }

                data.forEach(area => {
                    if (area.lat && area.lon && area.name) {
                        L.marker([area.lat, area.lon]).addTo(map)
                            .bindPopup(`<b>${area.name}</b><br>Potential Greening Area.`);
                    } else {
                        console.warn(`Invalid data for green zone: ${JSON.stringify(area)}`);
                    }
                });
            })
            .catch(error => {
                console.error("❌ Error fetching data:", error);
            });

        // Ensure search button exists before adding an event listener
        const searchBtn = document.getElementById('searchBtn');
        if (searchBtn) {
            searchBtn.addEventListener('click', () => {
                const location = document.getElementById('locationSearch').value;

                fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${location}`)
                    .then(response => response.json())
                    .then(data => {
                        if (data.length > 0) {
                            const lat = data[0].lat;
                            const lon = data[0].lon;

                            // Pan map to new location
                            map.setView([lat, lon], 13);
                            L.marker([lat, lon]).addTo(map).bindPopup(`Location: ${location}`).openPopup();
                        } else {
                            alert('Location not found!');
                        }
                    })
                    .catch(error => console.error('Error:', error));
            });
        } else {
            console.error("Search button not found!");
        }
    } else {
        console.error("Map container not found!");
    }
});