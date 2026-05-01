**Proposition (compound β-decay calibration across magic shells).**
*Let $E_0^{(2)} = Q_\beta = 0.782$ MeV be the free-neutron β-decay
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

| Decay type | Hecke-algebra change | Level |
|:---|:---|:---:|
| Non-magic β-decay | One neutron-word → proton-word (level-3 swap) | 3 |
| Magic-crossing β-decay | Neutron-word → proton-word **AND** $\sigma_{\mathrm{shell}}$ transition | 4 |
| Double-magic anchor decay | Full shell operator change on both $Z$ and $N$ sides | 4–5 |

*The simple formula $y_{\mathrm{target}} = Q_\beta / (E_0 \cdot A \cdot m_p)$
applies only for non-magic decays.  For magic-crossing decays, the
Q-value reflects the **difference of shell-operator contributions**
between parent and daughter, not the shell magnitude itself.*

**Compound β-decay principle.**

*To extract $y_{\mathrm{target}}(A_{\mathrm{magic}})$, use a chain
of β-decays along the β-stability valley, summing Q-values:*

$$
  \sum_{\text{decay chain}\;\text{to } A_{\mathrm{magic}}}
    Q_\beta
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
  \sum_{\text{chain}} Q_\beta
  \;-\;
  \sum_{\text{non-magic β-decays}} Q_\beta^{(3)},
$$

*where $Q_\beta^{(3)}$ are the level-3 (non-magic) Q-values
predictable from the pair-coupling shadow price at each intermediate
step.  The **residual** is $\Delta\mathfrak{m}_{\mathrm{shell}}$, the
pure shell contribution.*

**Numerical β-decay table (reference data, AME 2020):**

| $A_{\mathrm{magic}}$ | representative β-decay | Q (MeV) | Shell crossed |
|:---:|:---:|:---:|:---:|
| 2 | $^{3}\mathrm{H} \to {}^{3}\mathrm{He}$ | 0.01859 | N=2 |
| 8 | $^{14}\mathrm{C} \to {}^{14}\mathrm{N}$ | 0.15648 | N=8 |
| 20 | $^{40}\mathrm{K} \to {}^{40}\mathrm{Ca}$ | 1.311 | Z=20, N=20 |
| 28 | $^{56}\mathrm{Mn} \to {}^{56}\mathrm{Fe}$ | 3.695 | near Z=N=28 |
| 50 | $^{120}\mathrm{Ag} \to {}^{120}\mathrm{Cd}$ | 8.0 | Z=50 |
| 82 | $^{210}\mathrm{Bi} \to {}^{210}\mathrm{Po}$ | 1.163 | Z=82 |

**First-cut naïve formula (for comparison only).**

*Ignoring the knot-operator difference:*

$$
  y_{\mathrm{target}}^{\mathrm{naïve}}(A_{\mathrm{magic}})
  \;=\;
  \frac{Q_\beta}{E_0 \cdot A_{\mathrm{magic}} \cdot m_p}.
$$

*Numerical check at $q_0$:*

| $A_{\mathrm{magic}}$ | $y^{\mathrm{naïve}}$ | $B/(A \cdot m_p)$ (target) | ratio |
|:---:|:---:|:---:|:---:|
| 2 | $1.27 \times 10^{-5}$ | $7.54 \times 10^{-3}$ (${}^{4}\mathrm{He}$) | $1.7 \times 10^{-3}$ |
| 8 | $2.67 \times 10^{-5}$ | $8.50 \times 10^{-3}$ (${}^{16}\mathrm{O}$) | $3.1 \times 10^{-3}$ |
| 20 | $8.93 \times 10^{-5}$ | $9.11 \times 10^{-3}$ (${}^{40}\mathrm{Ca}$) | $9.8 \times 10^{-3}$ |
| 28 | $1.80 \times 10^{-4}$ | $9.21 \times 10^{-3}$ (${}^{56}\mathrm{Ni}$) | $1.95 \times 10^{-2}$ |

*The naïve ratios are all $\ll 1$, confirming that $Q_\beta$ directly
**does not give** $y_{\mathrm{target}}$ — the missing piece is the
**knot-operator transition** between parent and daughter.*

**Full categorical statement.**

*The Q-value of a magic-crossing β-decay is:*

$$
  Q_\beta(A_{\mathrm{magic}}\text{-crossing})
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
transition ([shell-transition knot](#prop:shell-transition-knot)).
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
    \sum_{\text{chain through } A_{\mathrm{magic}}} Q_\beta
    \;-\;
    \sum_{\text{non-magic steps}} Q_\beta^{(3)}
  \Bigr).
$$

*The RHS is fully determined by AME β-decay data plus the
categorical level-3 shadow prices — no free parameters beyond $E_0$.*

**Consequences.**

1. *Shell $y_{\mathrm{target}}$ values are not independently calibrated;
   they follow from β-decay Q-values and level-3 shadow prices.*
2. *The shell sector introduces **no new calibration**: $E_0 = Q_\beta$ is the $H^2$ input of the [three-calibration discipline](#prop:three-calibration-discipline) (alongside $H^0$ = $m_e$ and $H^1$ = $m_\mu/m_e$); shell binding is derived from chain Q-values and level-3 shadow prices.*
3. *Predictions for all magic-anchor binding energies (${}^{4}\mathrm{He}$, ${}^{16}\mathrm{O}$,
   ${}^{40}\mathrm{Ca}$, ${}^{56}\mathrm{Ni}$, ${}^{208}\mathrm{Pb}$) are parameter-free given the β-decay table.*

**Open:** *full implementation of the chain-Q-value derivation,
including correct separation of non-magic vs magic contributions at
each intermediate step, is the next step in tower binding.*
