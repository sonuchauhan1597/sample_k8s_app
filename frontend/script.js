
document.getElementById('run-pipeline').addEventListener('click', () => {
    fetch('/run-pipeline', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = JSON.stringify(data);
        })
        .catch(err => {
            document.getElementById('result').innerText = "Error: " + err.message;
        });
});
