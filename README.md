# Clustered Penalty Predictor ⚽

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

A modern, interactive, and complete Machine Learning pipeline for predicting soccer penalty outcomes using historical data from the World Cup. This project implements a dual-modeling approach: K-Means clustering for profiling and Random Forest classification for outcome prediction.

---

## Project Information

**Course:** 8108277 ELECTIVA II - MACHINE LEARNING APLICADO  
**Credits:** 3 (1 - 0)  
**Professor:** VIVIANA ALEXANDRA VILLANUEVA CIPAGAUTA  

### Team Members
| Name | Code |
| :--- | :--- |
| **Diego Fernando Aguirre Tenjo** | 202212048 |
| **Camilo Andrés Arias Tenjo** | 202210549 |

---

## Main Features

### Data Preprocessing & Augmentation
* **Feature Augmentation:** Algorithmic generation of `Steps_Run` and `Time_Taken` based on contextual data (pressure, foot) to simulate biomechanical variables.
* **Feature Engineering:** Calculation of historical success rates for both teams and goalkeepers.

### Dual Machine Learning Modeling
* **Unsupervised (K-Means):** Groups penalties into distinct profiles (clusters) representing different shooting styles.
* **Supervised (Random Forest):** Predicts the specific outcome (`Gol`, `Atajada`, `Fallo`) by injecting the computed cluster as a powerful predictive feature.

### Modern Interactive Interface (Frontend)
* Stunning dark-themed glassmorphism UI.
* Interactive 3x3 goal net to visually select the target zone (`Zone`).
* Breathtaking CSS animations for Goal (`¡GOLAZO!`) and Miss (`¡FALLO!`) outcomes.

---

## Execution and Development

1. **Install required dependencies:**
   Make sure you have Python installed, then run the following command in the project root:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the API (Backend) in development mode:**
   Launch the FastAPI server that loads the trained `.pkl` models:
   ```bash
   uvicorn api.main:app --reload
   ```
3. **Open the Interface (Frontend):**
   Simply open the `frontend/index.html` file in your preferred web browser.

> [!NOTE]
> This project adheres to the CRISP-DM methodology, structurally separating data processing, modeling pipelines, the API exposure, and the frontend visualization.
