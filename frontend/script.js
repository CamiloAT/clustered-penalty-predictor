document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('penaltyForm');
    const resultPanel = document.getElementById('resultPanel');
    const loadingState = document.getElementById('loadingState');
    const predictionContent = document.getElementById('predictionContent');
    const resetBtn = document.getElementById('resetBtn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        resultPanel.classList.remove('hidden');
        loadingState.classList.remove('hidden');
        predictionContent.classList.add('hidden');

        const formData = new FormData(form);
        const payload = {
            team: formData.get('team'),
            zone: parseInt(formData.get('zone')),
            foot: formData.get('foot'),
            keeper: formData.get('keeper'),
            penalty_number: parseInt(formData.get('penalty_number')),
            match_pressure: parseInt(formData.get('match_pressure'))
        };

        try {
            const response = await fetch('http://127.0.0.1:8000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });
            
            if (!response.ok) throw new Error("Error en la API. Asegúrate de tener FastAPI corriendo con uvicorn.");
            
            const data = await response.json();
            displayPrediction(data);
        } catch (error) {
            alert(error.message);
            loadingState.classList.add('hidden');
            resultPanel.classList.add('hidden');
        }
    });

    resetBtn.addEventListener('click', () => {
        resultPanel.classList.add('hidden');
        form.reset();
    });

    function displayPrediction(data) {
        loadingState.classList.add('hidden');
        predictionContent.classList.remove('hidden');

        const probability = Math.round(data.probability_goal);
        const isGoal = data.predicted_outcome === 'Gol';
        const cluster = data.assigned_cluster;
        const profile = data.cluster_profile;

        const probText = document.getElementById('probText');
        const probPath = document.getElementById('probPath');
        const outcomeText = document.getElementById('outcomeText');
        const clusterText = document.getElementById('clusterText');
        const profileText = document.getElementById('profileText');
        const chart = document.querySelector('.circular-chart');

        probText.textContent = `${probability}%`;
        setTimeout(() => {
            probPath.setAttribute('stroke-dasharray', `${probability}, 100`);
        }, 100);

        if (isGoal) {
            outcomeText.textContent = 'GOL';
            outcomeText.className = 'stat-value success';
            chart.classList.add('green');
            chart.classList.remove('red');
        } else {
            outcomeText.textContent = data.predicted_outcome.toUpperCase();
            outcomeText.className = 'stat-value fail';
            chart.classList.add('red');
            chart.classList.remove('green');
        }

        clusterText.textContent = `Clúster ${cluster}`;
        profileText.textContent = profile;
    }
});
