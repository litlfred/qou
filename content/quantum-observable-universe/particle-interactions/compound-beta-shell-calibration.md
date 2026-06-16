**Proposition (compound β-decay calibration across magic shells).**
*Let $E_0^{(2)} = \mathfrak{Q}_\beta = 0.782$ MeV be the free-neutron β-decay
Q-value — the **$H^2$ calibration** of the
[three-calibration discipline](#prop:three-calibration-discipline).
For each magic
$A_{\mathrm{magic}} \in \{2, 8, 20, 28, 50, 82, 126\}$, the
shell-binding target $y_{\mathrm{target}}(A_{\mathrm{magic}})$ is
**derivable**, not independently calibrated, from the cumulative
β-decay chain reaching the magic anchor.*

*The derivation is **NOT** a simple Q-value division — it accounts
for the change of knot operator between parent and daughter atoms
across the shell boundary.*

**Non-magic vs magic β-decays (key distinction).**

*A β-decay $(Z, N) \to (Z+1, N-1)$ in the Hecke algebra corresponds to:*

See [Table 1](#tbl:compound-beta-shell-calibration-table1-data).

*The simple formula $y_{\mathrm{target}} = \mathfrak{Q}_\beta / (E_0 \cdot A \cdot m_p)$
applies only for non-magic decays.  For magic-crossing decays, the
Q-value reflects the **difference of shell-operator contributions**
between parent and daughter, not the shell magnitude itself.*

**Compound β-decay principle.**

*To extract $y_{\mathrm{target}}(A_{\mathrm{magic}})$, use a chain
of β-decays along the β-stability valley, summing Q-values:*

$$
  \sum_{\text{decay chain}\;\text{to } A_{\mathrm{magic}}}
    \mathfrak{Q}_\beta
  \;=\;
  E_0 \cdot
    \bigl(\mathfrak{m}_{\mathrm{ref}} - \mathfrak{m}(A_{\mathrm{magic}})
          - \text{leptonic mass}\bigr).
$$

*Rearranging, the magic-shell binding contribution is extracted from
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
step.  The **residual** is $\Delta\mathfrak{m}_{\mathrm{shell}}$, the
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

**Full categorical statement.**

*The Q-value of a magic-crossing β-decay is:*

$$
  \mathfrak{Q}_\beta(A_{\mathrm{magic}}\text{-crossing})
  \;=\;
  E_0 \cdot
  \Bigl(
    \bigl|\mathrm{tr}_M^{\mathrm{parent}}\bigr|
    \;-\;
    \bigl|\mathrm{tr}_M^{\mathrm{daughter}}\bigr|
    \;-\;
    \bigl|\mathrm{tr}_M^{\mathrm{e^- + \bar\nu}}\bigr|
  \Bigr),
$$

*where the parent contains $\sigma_{\mathrm{shell}}$ (via
[shell self-duality](#prop:shell-schur-weyl-self-duality)) and the
daughter contains a **different** shell operator or a cross-shell
transition ([shell-transition knot](#conj:shell-transition-knot)).
The Q-value measures the **difference of shell-operator
contributions**, not either side individually.*

*To extract $y_{\mathrm{target}}(A_{\mathrm{magic}})$, combine
multiple β-decay Q-values along the isobar chain through the magic
anchor:*

$$
  y_{\mathrm{target}}(A_{\mathrm{magic}})
  \;=\;
  \frac{1}{E_0 \cdot A_{\mathrm{magic}} \cdot m_p}
  \cdot
  \Bigl(
    \sum_{\text{chain through } A_{\mathrm{magic}}} \mathfrak{Q}_\beta
    \;-\;
    \sum_{\text{non-magic steps}} \mathfrak{Q}_\beta^{(3)}
  \Bigr).
$$

*The RHS is fully determined by AME β-decay data plus the
categorical level-3 shadow prices — no free parameters beyond $E_0$.*

**Consequences.**

1. *Shell $y_{\mathrm{target}}$ values are not independently calibrated;
   they follow from β-decay Q-values and level-3 shadow prices.*
2. *The shell sector introduces **no new calibration**: $E_0 = \mathfrak{Q}_\beta$ is the $H^2$ input of the [three-calibration discipline](#prop:three-calibration-discipline) (alongside $H^0$ = $m_e$ and $H^1$ = $m_\mu/m_e$); shell binding is derived from chain Q-values and level-3 shadow prices.*
3. *Predictions for all magic-anchor binding energies (${}^{4}\mathrm{He}$, ${}^{16}\mathrm{O}$,
   ${}^{40}\mathrm{Ca}$, ${}^{56}\mathrm{Ni}$, ${}^{208}\mathrm{Pb}$) are parameter-free given the β-decay table.*

**Open:** *full implementation of the chain-Q-value derivation,
including correct separation of non-magic vs magic contributions at
each intermediate step, is the next step in tower binding.*
