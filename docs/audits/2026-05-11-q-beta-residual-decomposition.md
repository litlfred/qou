# Q_β residual decomposition — Frobenius factorization + dual-basis identity

**Status:** numerical + structural audit. Per owner directive
2026-05-11 ("please do an analysis to narrow down where the errors
are coming from … re-derive E_0 via Frobenius pairing / dual / Wenzl
bridge").

## TL;DR

Three sharp findings:

1. **Frobenius factorization** of the 1.00744 residual ratio:
   $$1.00744 = \underbrace{1.00168}_{\text{brane-tower } N=0} \times \underbrace{1.00579}_{\text{basis-change typed vs single-wrap}}$$
   The two factors are numerically separable and structurally distinct.

2. **Dual-basis identity** $G^{-1} \cdot t = e_\gamma$ at H_3 — the dual
   of the Markov-trace vector is the indicator of the identity element.
   Equivalent to: the framework's "net" $\sum_i (\Delta_\text{NF})_i$ IS
   the Frobenius counit $\varepsilon(\beta)$, the structurally-canonical
   projection. **No weights are missing.**

3. **Per-N bound** vs **lift formula** distinction: the brane-tower
   bound $\hbar_q^{2(N+1)}/(1-\hbar_q^2)$ predicts ≤ 1 ppb at $N \geq 4$,
   but the actual residual depends on the **lift formula** at the
   canonical truncation level $n_\star$. 5 naive $N=1$ lifts ALL made
   the residual WORSE (42×–134× and wrong-sign). The bound is the
   worst-case ceiling; closure requires the open level-selection
   conjecture, not just incrementing N.

## (1) Frobenius factorization of the 1.00744 ratio

The "calibration vs derived" ratio
$E_0^\text{derived} / E_0^\text{calibrated} = 4.186 / 4.155 = 1.00744$
decomposes exactly:

| Factor | Value at $q_0$ | Origin |
|---|---:|---|
| Brane-tower $N=0$ residual | **1.00168** | Single Planck-tick truncation in $E_0$ |
| Basis-change typed-vs-single-wrap | **1.00579** | Typed-crossings 6-term NF picks up nonzero $L_\pm, e^-$ contributions that exactly cancel at single wrap |
| **Product** | **1.00744** | Full discrepancy |

Computation:

| Quantity | Value | Formula |
|---|---:|---|
| $E_0$ derived | 4.18598 MeV | $m_e / (q_0(q_0-1))$ |
| $E_0$ cal symbolic (single wrap) | 4.17897 MeV | $Q_\beta^{\text{CODATA}} / \lvert h(h-2)/2 \rvert$ |
| $E_0$ cal typed (6-term) | 4.15493 MeV | $Q_\beta^{\text{CODATA}} / 0.18829$ |
| $\hbar_q^2/(1-\hbar_q^2)$ at $q_0$ | 0.009915 | per-braid-mass-tower N=0 bound |
| Observed N=0 residual | 0.00168 | $4.186/4.179 - 1$ |
| **Observed / bound** | **0.169** | **well inside** |

The 0.168% N=0 residual sits at 17% of the framework's own structural
bound — fully consistent with the per-braid-mass-tower theorem.

## (2) Dual-basis identity at H_3 — no missing weights

Tested 4 candidate Q_β forms (commit `c84a39cc` analysis extended):

| Form | Q_β value | Residual |
|---|---:|---:|
| **Form 1: $\varepsilon(\Delta_\text{NF}) \cdot E_0$ (current)** | **0.7836 MeV** | **+1.31 keV ✓** |
| Form 2: $m_e \cdot \mathrm{tr}_M(\Delta_\text{NF}) = m_e \cdot \sum t_i (\Delta_\text{NF})_i$ | 0.0422 MeV | −740 keV |
| Form 3: $m_e \cdot \langle \Delta_\text{NF}, G^{-1} t \rangle$ | 0.0112 MeV | −771 keV |
| Form 4: $m_e \cdot \sum_\lambda y_\lambda \chi_\lambda(\Delta_\text{NF})$ | 0.0422 MeV | −740 keV |

**Structural identity discovered**: $G^{-1} \cdot t = e_\gamma$ where
$e_\gamma = (1, 0, 0, 0, 0, 0)$ in the NF basis ordering.

Proof:
- $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ (Frobenius pairing)
- For the identity $b_\gamma = \mathbf{1}$: $G_{\gamma j} = \mathrm{tr}_M(b_j) = t_j$
- So the γ-row of $G$ equals $t^T$: $G \cdot e_\gamma = t$
- Therefore $G^{-1} \cdot t = e_\gamma$. ∎

**Consequence**: Form 3 reduces to $m_e \cdot (\Delta_\text{NF})_\gamma = m_e \cdot h^2/2 \approx 0.011$ MeV — far from $Q_\beta$. The dual-basis form gives only the **vacuum debt** $\gamma$-coefficient, not the full energy.

**Form 1 ($\varepsilon$) is structurally canonical** because:
- $\varepsilon(\beta) = \sum_i x_i$ is the **Frobenius counit** of the algebra
- It represents the topological **vacuum-net content** of the operator
- $Q_\beta$ = energy released = vacuum debt difference $= \varepsilon(\beta_n) - \varepsilon(\beta_p) = \varepsilon(\Delta_\text{NF})$
- Multiplied by $E_0$ (the cat-units → MeV scale) gives the energy
- **No weighting by Markov trace or G^{-1}** — those would measure different physical quantities

**Verdict on user's "are we missing weights?"**: NO. The framework's
unweighted-sum × $E_0$ form IS the structurally-canonical Frobenius
counit projection. The 1.31 keV residual lives entirely in $E_0$.

## (3) Why N ≥ 4 not done everywhere

The framework's per-braid-mass-tower bound at level $N$:
$$|R_N| \le \Delta_\text{max} \cdot \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2}$$

| $N$ | Bound at $q_0$ | Predicted Q_β residual |
|:-:|---:|---:|
| **0** (current) | 0.99% | bound: 7.77 keV; observed: 1.31 keV ✓ |
| 1 | 0.01% | bound: 0.076 keV (76 ppm) |
| 2 | 1 ppm | bound: 0.7 eV (0.96 ppm) |
| 3 | 9.4 ppb | bound: 7 meV |
| **4** | **0.09 ppb** | **target: 1 ppb** |

To hit 1 ppb requires $N \geq 4$. **Why not do this?**

The bound is the **worst-case ceiling for ANY truncation rule**. The
actual residual depends on which **lift formula** carries $E_0$ from
N=0 → N=1 → ... → N=4. Empirical evidence from PR #637's probes
(commit `e1b005b2`):

| Lift formula at N=1 | Q_β residual | vs N=0 baseline |
|---|---:|---:|
| N=0 baseline (no lift) | +1.31 keV | (target) |
| N=1 multiplicative $\Sigma_{N1}/\Sigma_{N0}$ | +55.5 keV | **42× WORSE** |
| N=1 additive $1 + \Sigma\delta$ | +176 keV | **134× WORSE** |
| N=1 cyclotomic Σ-Habiro residue | +17 keV | **13× WORSE** |
| N=1 per-nucleon difference | −113 keV | **86× WORSE** |
| N=1 3-term assembly (T1+T4+T5) | wrong sign | **structural fail** |

**ALL FIVE** naive N=1 lifts made the residual WORSE. Reason: per
`brane-tower-z-habiro.md`, $\Phi_q(z)$'s analytic infinite product
diverges at $|z| \to q$; uncontrolled truncation amplifies error
catastrophically.

The canonical truncation level $n_\star$ that gives the bound's
predicted improvement requires the **cyclotomic projection
$\pi_{n_\star}^{(z)}$** at the right level, not raw $\Phi_q^{(N)}$
truncation. Per the conjecture in `brane-tower-z-habiro.md §"Status
of n_⋆"`:

> "The level-selection rule $n_\star$ is **the open part**."

Three candidate substrate-derived rules for β-decay all give
$n_\star = 2$:
- Habiro $m_\text{max} = \lceil\sqrt{2 \deg_u \Delta}\rceil = 2$
- Coxeter length $\ell(T_\beta) = 2$
- Generator rank of $H_3 = 2$

So even if the right lift formula is identified, β-decay specifically
gets only to $n_\star = 2$, where the bound predicts ~1 ppm — **not
yet 1 ppb**. To reach 1 ppb on Q_β requires either:
- (a) a higher canonical $n_\star$ at the β-decay sector (open), OR
- (b) a different operator class whose $n_\star$ is naturally higher

Both are R&D-grade open problems. **The bound is necessary but not
sufficient** — the lift formula matters as much as the truncation
depth.

## Implications for the 10-gap Lean roadmap

This analysis confirms the localization in `MassComputationChainRoadmap.lean`:

| Gap | Contributes to 1.31 keV? | Status |
|---|:-:|---|
| 1. q_0 inversion | ✗ (~3 ppb only) | open |
| 2. Crossing recurrence | ✗ (cancels in Δ at single wrap) | open |
| 3. Typed-crossings encoding | ✗ (single wrap doesn't use it) | open |
| **4. Φ_q convergence** | **✓ N=0 truncation residual** | open (existing sorry) |
| **5. n_⋆ existence** | **✓ open closure path** | tautological instance |
| 6. Wedderburn weights | ✗ (Frobenius counit doesn't use them) | partial |
| 7. atom_braid_word | ✗ (per-nucleon, tautological) | open |
| 8. Per-nucleon shift | ✗ (A ≥ 2 only) | open |
| 9. Frobenius co-Casimir n=8..12 | ✗ (cancels p↔n at A=1) | n ≤ 7 closed |
| 10. Wenzl bridge tr_M | ✗ (cancels in Δ) | A ≤ 3 closed |

**Only gaps 4 + 5** are on the critical path for closing the
1.31 keV residual. Gap 6 (Wedderburn weights) is no longer critical
given the dual-basis identity finding — Form 1 uses the counit
directly, not the weights.

## Per-nucleon mass tables — what changes with this analysis?

**Nothing** — the per-nucleon mass predictions remain:
- $m_p$ derived (via mass_endomorphism Φ_q tower): 955.5 MeV (+1.84%)
- $m_n$ derived (full symbolic 50 dps): 348.7 MeV (−62.9%)

These are dominated by the **per-nucleon pole-distance asymmetry**
$\hat V_p$ near $q_0$ vs $\hat V_n$ far — a structural feature of
the brane tower that does NOT cancel in the per-nucleon residue,
unlike the β-decay difference which cancels almost everything.

So the Q_β prediction at single wrap is structurally "easy" (Frobenius
counit at H_3 with co-Casimir cancelling) while per-nucleon masses
are structurally "hard" (require resolving the pole-distance
asymmetry).

## Verdict for the audit

The +1.31 keV / 0.168% Q_β residual is:
1. **Numerically isolated** to the $E_0$ N=0 truncation factor 1.00168
2. **Structurally canonical** — no missing weights, the formula uses the Frobenius counit which is the correct categorical projection
3. **Bound-consistent** — observed 0.168% sits at 17% of the framework's structural N=0 ceiling of 0.99%
4. **Closure-blocked** — by the open $n_\star$ conjecture, NOT by missing weights or wrong formula

Going to N ≥ 4 requires resolving the level-selection rule first.
Until that lands, the 1.31 keV residual is the framework's
structurally-clean current best in non-calibrated mode.
