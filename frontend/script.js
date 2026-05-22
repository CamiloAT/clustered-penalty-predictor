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

    // ===== ZONE SELECTORS =====
    const KEEPER_MAP = { 1: 'L', 2: 'C', 3: 'R', 4: 'L', 5: 'C', 6: 'R', 7: 'L', 8: 'C', 9: 'R' };

    function setupZoneSelector(netId, inputId, indicatorId, keeperMode) {
        const zones = document.querySelectorAll(`#${netId} .goal-zone`);
        const input = document.getElementById(inputId);
        const indicator = document.getElementById(indicatorId);

        zones.forEach(zone => {
            zone.addEventListener('click', () => {
                zones.forEach(z => z.classList.remove('selected'));
                zone.classList.add('selected');
                input.value = zone.dataset.zone;
                indicator.textContent = `Zona ${zone.dataset.zone} seleccionada`;
                indicator.classList.add('has-selection');

                if (keeperMode) {
                    document.getElementById('keeper').value = KEEPER_MAP[zone.dataset.zone];
                }

                document.getElementById(keeperMode ? 'keeperError' : 'zoneError').classList.add('hidden');
            });
        });
    }

    setupZoneSelector('goalNetKeeper', 'zone_keeper', 'keeperZoneIndicator', true);
    setupZoneSelector('goalNetKicker', 'zone', 'kickerZoneIndicator', false);

    // ===== FORM SUBMIT =====
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const keeperZone = document.getElementById('zone_keeper').value;
        const kickerZone = document.getElementById('zone').value;
        let hasError = false;

        if (!keeperZone) {
            document.getElementById('keeperError').classList.remove('hidden');
            hasError = true;
        } else {
            document.getElementById('keeperError').classList.add('hidden');
        }

        if (!kickerZone) {
            document.getElementById('zoneError').classList.remove('hidden');
            hasError = true;
        } else {
            document.getElementById('zoneError').classList.add('hidden');
        }

        if (hasError) return;

        resultPanel.classList.remove('hidden');
        loadingState.classList.remove('hidden');
        predictionContent.classList.add('hidden');

        const formData = new FormData(form);
        const payload = {
            team: formData.get('team'),
            zone: parseInt(kickerZone),
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
        document.querySelectorAll('.goal-zone.selected').forEach(z => z.classList.remove('selected'));
        document.querySelectorAll('.zone-indicator').forEach(el => {
            el.textContent = 'Selecciona una zona';
            el.classList.remove('has-selection');
        });
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

        const stepsText = document.getElementById('stepsText');
        const timeText = document.getElementById('timeText');
        if(stepsText) stepsText.textContent = data.steps_run;
        if(timeText) timeText.textContent = data.time_taken.toFixed(2) + "s";

        const chart = document.querySelector('.circular-chart');

        const animContainer = document.getElementById('animationContainer');
        const animContent = document.getElementById('animContent');
        const animText = document.getElementById('animText');

        if (animContainer) {
            animContainer.classList.remove('hidden');
            animContent.className = 'anim-content';
            void animContent.offsetWidth;

            if (isGoal) {
                animContent.classList.add('anim-goal');
                animText.textContent = '¡GOLAZO!';
            } else {
                animContent.classList.add('anim-miss');
                animText.textContent = data.predicted_outcome === 'Atajada' ? '¡ATAJADA!' : '¡FALLÓ!';
            }

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
