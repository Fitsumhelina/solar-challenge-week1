# ☀️ Cross-Country Solar Potential Analysis – Final Report

**Author:** Fitsum Helina  
**Program:** 10 Academy Week 0 Challenge – Solar Data Discovery  
**Date:** May 21, 2025  

---

## 🔍 1. Introduction

MoonLight Energy Solutions is exploring solar investment opportunities across West Africa. This project analyzes environmental sensor data from **Benin**, **Togo**, and **Sierra Leone** to identify regions with high solar potential and recommend data-driven investment strategies.

---

## 🧠 2. Data Understanding

The dataset includes hourly measurements of solar and environmental variables:
- **Irradiance**: GHI, DNI, DHI
- **Sensor Outputs**: ModA, ModB
- **Weather Conditions**: Temperature, Wind Speed/Direction, Humidity, Precipitation
- **Cleaning Events**: Binary flag indicating sensor/module cleaning

---

## 🧹 3. EDA & Cleaning Summary

### 📍 Benin
- **GHI values stable and consistent**, with moderate DNI and DHI.
- Cleaning events show measurable improvement in ModA/B readings.
- Minor outliers handled using Z-scores.
- **Conclusion**: Strong solar profile, especially in terms of reliability.

### 📍 Togo
- Slightly lower GHI, but higher DNI variability.
- Clear impact of cleaning on module performance.
- RH vs Temp showed less correlation, suggesting local microclimates.

### 📍 Sierra Leone
- Broad range of GHI values, with more atmospheric interference (DHI ↑).
- Wind direction highly variable — potential implications for sensor placement.
- Overall more noisy than Benin or Togo.

---

## 📊 4. Cross-Country Comparison

### 📌 Boxplot Summary
![](your_local_screenshot_or_plot_placeholder.png)

- **Benin** had the highest **median GHI** with tight spread.
- **Togo** showed consistent but slightly lower irradiance.
- **Sierra Leone** had the most variability — possibly less predictable.

### 📈 Statistical Test (ANOVA on GHI)
- **P-value**: 0.000 → statistically significant differences across countries.

### 🏆 GHI Ranking (Mean)
1. Benin
2. Togo
3. Sierra Leone

---

## 🌐 5. Streamlit Dashboard

- Interactive UI allows users to:
  - Select countries
  - View irradiance stats & distribution
  - Compare GHI rankings visually

📸 **Dashboard Screenshot:**
![Dashboard](dashboard_screenshots/dashboard.png)

---

## 💡 6. Recommendation

**Benin** is the top candidate for investment due to:
- Highest and most stable GHI values
- Strong sensor consistency and low variance
- Low cleaning-related performance dips

**Togo** is a viable backup with fewer anomalies.  
**Sierra Leone** may require more site-specific evaluation due to variability.

---

## 📘 7. Reflections

- This project taught me to handle real-world time series data, build robust EDA pipelines, and deploy dashboards.
- I learned how to apply CI/CD, GitHub best practices, and statistical tests to drive meaningful insights.
- Time management and quick iteration were crucial.

---

## 🧩 8. Appendix (optional)

- Links to full notebooks: [`github`](https://github.com/Fitsumhelina/solar-challenge-week1.git)
- Source datasets: available via [10 Academy shared drive]
