**Audit (compound β-decay empirical probe).**

*To extract $y_{\mathrm{target}}(A_{\mathrm{magic}})$, an earlier formulation proposed summing Q-values for a chain of β-decays along the stability valley:*

$$
  \sum_{\text{chain to } A_{\mathrm{magic}}}
    \mathfrak{Q}_\beta
  \;=\;
  E_0 \cdot
    \bigl(\mathfrak{m}_{\mathrm{ref}} - \mathfrak{m}(A_{\mathrm{magic}})
          - \text{leptonic mass}\bigr).
$$

*Rearranging this expression to extract the magic-shell binding contribution subtracts the non-magic contributions from the total chain Q-value:*

$$
  \Delta \mathfrak{m}_{\mathrm{shell}}(A_{\mathrm{magic}})
  \;=\;
  \sum_{\text{chain}} \mathfrak{Q}_\beta
  \;-\;
  \sum_{\text{non-magic β-decays}} \mathfrak{Q}_\beta^{(3)}.
$$

*Here, $\mathfrak{Q}_\beta^{(3)}$ denotes the level-3 (non-magic) Q-values, predicted from the pair-coupling shadow price at each intermediate step, with the residual identified as $\Delta\mathfrak{m}_{\mathrm{shell}}$, the pure shell contribution.*

**Numerical β-decay table (reference data, AME 2020):**

See [Table 2](#tbl:compound-beta-shell-calibration-table2-data).

## Scope limit — circular extraction; exploratory, not a canonical calibration

This chain-summing extraction is **exploratory**; as written it does not yield a fit-free shell-binding calibration, for two reasons.

1. **Circularity.** The subtracted term $\sum \mathfrak{Q}_\beta^{(3)}$ is itself *predicted* from the pair-coupling shadow price, so the residual $\Delta\mathfrak{m}_{\mathrm{shell}}$ is defined as (measured chain sum) $-$ (model prediction). Identifying that residual with "the pure shell contribution" folds the model back into the quantity it is meant to calibrate.
2. **Dimensional consistency.** The rearrangement equates a sum of $\mathfrak{Q}_\beta$ (an energy) with $E_0 \cdot (\mathfrak{m}_{\mathrm{ref}} - \mathfrak{m}(A_{\mathrm{magic}}) - \text{leptonic mass})$, in which $E_0$ is treated as a dimensionless factor while the parenthetical is a mass. The two sides carry different units unless $E_0$ absorbs a mass scale that the rearrangement does not make explicit.

The single magic-crossing Q-value identity in the parent block stands on the categorical trace. The compound-chain calibration built on top of it is demoted to an empirical probe pending (a) an independent, non-shadow-price determination of the non-magic Q-values and (b) an explicit unit audit of the rearrangement. Per the three-calibration discipline it must not be wired into any production shell-binding target as a fit.

