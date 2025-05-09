
document.getElementById('predict-btn').addEventListener('click', function () {
    const data = {
        ph: document.getElementById('ph').value,
        hardness: document.getElementById('hardness').value,
        solids: document.getElementById('solids').value,
        chloramines: document.getElementById('chloramines').value,
        sulfate: document.getElementById('sulfate').value,
        organic_carbon: document.getElementById('organic_carbon').value,
        turbidity: document.getElementById('turbidity').value
    };

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        if (res.error) {
            document.getElementById('result-box').innerHTML = `<p style="color:red;">Error: ${res.error}</p>`;
        } else {
            document.getElementById('result-box').innerHTML = `
                <p><strong>Potable:</strong> ${res.potable}</p>
                <p><strong>Suitable for Agriculture:</strong> ${res.agriculture}</p>
            `;
        }
    })
    .catch(err => {
        document.getElementById('result-box').innerText = 'Prediction failed.';
    });
});
