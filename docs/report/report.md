
Predictions are generated for all dyads (90 pairs), resulting in a matrix of size `#dyads × 5`.

---

### Evaluation Protocol

Models will be compared:

- Across architectures (Echo vs baselines).  
- Across horizons (short-, medium-, long-term).  
- Across targets (Goldstein vs QuadClass).  
- Across dyad types (allies, rivals, neutral pairs).

**Metrics:**

- *Goldstein:* MAE, MSE, RMSE, R²  
- *QuadClass:* MSE, RMSE, Negative Binomial Deviance, Distributional Calibration Error

---

## Work Plan

1. Build full data pipeline.  
2. Train baseline models.  
3. Implement Echo v0.  
4. Compare Echo v0 vs baselines.  
5. Conduct ablations.  
6. Evaluate best configuration.  
7. Final evaluation.  
8. (Optional) Dashboard.  
9. (Optional) LLM interpretability module.

---

## Deliverables

- **Full Data Pipeline** (ETL + splits).  
- **Final Model (Echo)**.  
- **Evaluation Report.**  
- **Dashboard (optional).**  
- **Code & Documentation (GitHub/GitLab).**  
- **Final Written Report.**

---

## Risks & Mitigation

- High computational cost (GPU usage).  
- Overfitting/underfitting risks due to dyad frequency imbalance.  
- Data sparsity in low-activity dyads.  
- Noisy or irrelevant text data.  
- Long-horizon prediction degradation.  
- Concept drift due to evolving geopolitical contexts.  
- Outliers from short-term shocks (wars, crises, etc.).

---

## References

### Papers
Chen et al. (2020); von der Maase (2025); Croicu & von der Maase (2025); Zakotianskyi (2025); Liu & Shen (2025).

### Datasets
GDELT, ViEWS, UCDP, CEPII, WGI, World Bank.
