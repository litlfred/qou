**Audit (compound β-decay empirical probe).**

*To extract $y_{\mathrm{target}}(A_{\mathrm{magic}})$, a chain
of β-decays along the β-stability valley was historically proposed to sum Q-values:*

$$
  \sum_{\text{decay chain}\;\text{to } A_{\mathrm{magic}}}
    \mathfrak{Q}_\beta
  \;=\;
  E_0 \cdot
    \bigl(\mathfrak{m}_{\mathrm{ref}} - \mathfrak{m}(A_{\mathrm{magic}})
          - \text{leptonic mass}\bigr).
$$

*Rearranging, the magic-shell binding contribution was extracted from
the **total chain Q-value** minus the non-magic contributions:*

$$
  \Delta \mathfrak{m}_{\mathrm{shell}}(A_{\mathrm{magic}})
  \;=\;
  \sum_{\text{chain}} \mathfrak{Q}_\beta
  \;-\;
  \sum_{\text{non-magic β-decays}} \mathfrak{Q}_\beta^{(3)},
$$

*where $\mathfrak{Q}_\beta^{(3)}$ are the level-3 (non-magic) Q-values
predictable from the pair-coupling shadow price at each intermediate
step.  The **residual** was identified as $\Delta\mathfrak{m}_{\mathrm{shell}}$, the
pure shell contribution.*

**Numerical β-decay table (reference data, AME 2020):**

See [Table 2](#tbl:compound-beta-shell-calibration-table2-data).

**First-cut naïve formula (for comparison only).**

*Ignoring the knot-operator difference:*

$$
  y_{\mathrm{target}}^{\mathrm{naïve}}(A_{\mathrm{magic}})
  \;=\;
  \frac{\mathfrak{Q}_\beta}{E_0 \cdot A_{\mathrm{magic}} \cdot m_p}.
$$

*Numerical check at $q_0$:*

See [Table 3](#tbl:compound-beta-shell-calibration-table3-data).

*The naïve ratios are all $\ll 1$, confirming that $\mathfrak{Q}_\beta$ directly
**does not give** $y_{\mathrm{target}}$ — the missing piece is the
**knot-operator transition** between parent and daughter.*

*Note: This numerical approach is flagged for post-hoc curve fitting and a unit mismatch in the naïve formula. It is retained here for audit purposes until the core theory formalizes the structural derivation.*
