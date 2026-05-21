document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('penaltyForm');
    const resultPanel = document.getElementById('resultPanel');
    const loadingState = document.getElementById('loadingState');
    const predictionContent = document.getElementById('predictionContent');
    const resetBtn = document.getElementById('resetBtn');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Mostrar panel de resultados en estado de carga
        resultPanel.classList.remove('hidden');
        loadingState.classList.remove('hidden');
        predictionContent.classList.add('hidden');

        // TODO: Aquí se hará la llamada al API REST de FastAPI
        // const formData = new FormData(form);
        // fetch('/predict', { method: 'POST', body: formData })...

        // Simulación temporal (Mock API)
        setTimeout(() => {
            simulatePrediction();
        }, 1500);
    });

    resetBtn.addEventListener('click', () => {
        resultPanel.classList.add('hidden');
        form.reset();
    });

    function simulatePrediction() {
        loadingState.classList.add('hidden');
        predictionContent.classList.remove('hidden');

        // Valores aleatorios para la demo
        const probability = Math.floor(Math.random() * 40) + 50; // 50-90%
        const isGoal = probability > 65;
        const cluster = Math.floor(Math.random() * 4) + 1; // 1-4
        
        const profiles = {
            1: "Tiro Central Potente",
            2: "Colocación a Esquina",
            3: "Engaño al Portero",
            4: "Riesgo Alto (Fuera/Palo)"
        };

        // Actualizar UI
        const probText = document.getElementById('probText');
        const probPath = document.getElementById('probPath');
        const outcomeText = document.getElementById('outcomeText');
        const clusterText = document.getElementById('clusterText');
        const profileText = document.getElementById('profileText');
        const chart = document.querySelector('.circular-chart');

        probText.textContent = `${probability}%`;
        // Dash array is "probability, 100"
        setTimeout(() => {
            probPath.setAttribute('stroke-dasharray', `${probability}, 100`);
        }, 100);

        if (isGoal) {
            outcomeText.textContent = 'GOL';
            outcomeText.className = 'stat-value success';
            chart.classList.add('green');
            chart.classList.remove('red');
        } else {
            outcomeText.textContent = 'FALLO';
            outcomeText.className = 'stat-value fail';
            chart.classList.add('red');
            chart.classList.remove('green');
        }

        clusterText.textContent = `Clúster ${cluster}`;
        profileText.textContent = profiles[cluster];
    }
});
