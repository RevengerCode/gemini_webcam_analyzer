function aggiornaDescrizione() {
    fetch("/descrizione")
        .then(response => response.json())
        .then(data => {
            document.getElementById("caption").textContent = data.caption;
            document.getElementById("timestamp").textContent = data.timestamp;
            aggiornaStorico();
        });
}

function aggiornaStorico() {
    fetch("/storico")
        .then(response => response.json())
        .then(data => {
            const ul = document.getElementById("storico");
            ul.innerHTML = "";
            data.forEach(item => {
                const li = document.createElement("li");
                li.textContent = `[${item.timestamp}] ${item.caption}`;
                ul.appendChild(li);
            });
        });
}

// Aggiorna ogni 5 secondi (5000 ms)
setInterval(aggiornaDescrizione, 5000);

// Iniziale
document.addEventListener("DOMContentLoaded", aggiornaDescrizione);
