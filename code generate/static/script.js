// script.js

document.getElementById('runTestButton').addEventListener('click', function() {
    // Récupérer le code généré
    var generatedCode = document.getElementById('generatedCode').innerText;

    // Envoyer le code au serveur pour exécution
    fetch('/run_test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: generatedCode })
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Convertir la réponse en JSON
        } else {
            throw new Error('Failed to execute test!');
        }
    })
    .then(data => {
        alert(data.message); // Afficher le message de succès
    })
    .catch(error => {
        console.error('Error executing test:', error);
        alert('An error occurred while executing the test!');
    });
});
