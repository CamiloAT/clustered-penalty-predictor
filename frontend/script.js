document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('penaltyForm');
    const resultPanel = document.getElementById('resultPanel');
    const loadingState = document.getElementById('loadingState');
    const predictionContent = document.getElementById('predictionContent');
    const resetBtn = document.getElementById('resetBtn');
    
    // Modal Logic
    const metricsModal = document.getElementById('metricsModal');
    const showMetricsBtn = document.getElementById('showMetricsBtn');
    const closeMetricsBtn = document.getElementById('closeMetricsBtn');

    if (showMetricsBtn && metricsModal && closeMetricsBtn) {
        showMetricsBtn.addEventListener('click', () => {
            metricsModal.classList.remove('hidden');
        });
        closeMetricsBtn.addEventListener('click', () => {
            metricsModal.classList.add('hidden');
        });
        metricsModal.addEventListener('click', (e) => {
            if (e.target === metricsModal) {
                metricsModal.classList.add('hidden');
            }
        });
    }

    // Visual Goal Net Logic
    const zones = document.querySelectorAll('.goal-zone');
    const zoneInput = document.getElementById('zone');

    zones.forEach(zone => {
        zone.addEventListener('click', () => {
            zones.forEach(z => z.classList.remove('selected'));
            zone.classList.add('selected');
            zoneInput.value = zone.dataset.zone;
        });
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const zoneError = document.getElementById('zoneError');
        const zoneValue = document.getElementById('zone').value;
        if (!zoneValue) {
            zoneError.classList.remove('hidden');
            return;
        } else {
            zoneError.classList.add('hidden');
        }

        resultPanel.classList.remove('hidden');
        loadingState.classList.remove('hidden');
        predictionContent.classList.add('hidden');

        const formData = new FormData(form);
        const payload = {
            team: formData.get('team'),
            zone: parseInt(zoneValue),
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
        
        // Data augmentation stats
        const stepsText = document.getElementById('stepsText');
        const timeText = document.getElementById('timeText');
        if(stepsText) stepsText.textContent = data.steps_run;
        if(timeText) timeText.textContent = data.time_taken.toFixed(2) + "s";

        const chart = document.querySelector('.circular-chart');
        
        // Animation Logic
        const animContainer = document.getElementById('animationContainer');
        const animContent = document.getElementById('animContent');
        const animText = document.getElementById('animText');
        
        if (animContainer) {
            animContainer.classList.remove('hidden');
            animContent.className = 'anim-content'; // Reset classes
            
            // Force a reflow to restart animation
            void animContent.offsetWidth; 
            
            if (isGoal) {
                animContent.classList.add('anim-goal');
                animText.textContent = '¡GOLAZO!';
            } else {
                animContent.classList.add('anim-miss');
                animText.textContent = data.predicted_outcome === 'Atajada' ? '¡ATAJADA!' : '¡FALLÓ!';
            }
            
            // Ocultar overlay a pantalla completa de la animación luego de completada
            setTimeout(() => {
                animContainer.classList.add("hidden");
            }, 2500);
        }

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
