function fetchData(endpoint) {
    fetch(`http://127.0.0.1:5000/${endpoint}`)
        .then(response => response.json())
        .then(data => {
            const dataDiv = document.getElementById("data");
            dataDiv.innerHTML = `<h2>${endpoint.charAt(0).toUpperCase() + endpoint.slice(1)}</h2>`;
            data.forEach(item => {
                dataDiv.innerHTML += `<pre>${JSON.stringify(item, null, 2)}</pre>`;
            });
        })
        .catch(err => console.error(err));
}
