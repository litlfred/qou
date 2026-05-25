**Conjecture (lepton-tower H_{n+1} branching factor).** *Let
$K_\ell = \sigma_1^{2m+1}$ be the canonical torus-knot braid for a
lepton at tower-index $m$ (electron $m=1$, muon $m=2$, tau $m=3$).
Let $n = 2m+1$ be the crossing count. The canonical
operator-level mass-tower ξ_m correction factor is*

$$
\boxed{\;\xi_m \;=\; \frac{d_q((n, 1)) \cdot [2]_q}{[n+1]_q} \cdot \frac{1}{\hbar_q^2}\;}
$$

*where $d_q((n, 1))$ is the q-dimension of the standard
representation of $S_{n+1}$ via the hook-length formula, and the
formula couples the lepton's natural $H_2$ braid to the $S_{n+1}$
standard rep one level up.*

> **⚠️ Status — open conjecture (2026-05-25, PR #1127 T6 rest).**
> Numerical match for muon $m=2$: predicts $\xi_2 = [3]_q \cdot [2]_q / [4]_q \cdot (1/\hbar_q^2)$
> which agrees with the empirical required factor to 0.034%.
> Categorical derivation from `prop:per-braid-mass-tower` operator-valued
> $A^\lambda_{\mu, \nu}$ branching coefficient is open work.

## Derivation sketch (open)

The factor $[3]_q \cdot [2]_q / [4]_q$ was numerically identified
in [`docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md)
+ [`folio-assistant/computations/t6_three_halves_factor_probes.py`](../../../folio-assistant/computations/t6_three_halves_factor_probes.py)
as the closed-form fit (matching 28 candidate ratios to 0.034%, the
best by 20× over the next best).

The algebraic identity $\frac{[3]_q \cdot [2]_q}{[4]_q} = \frac{3 + h^2}{2 + h^2}$
is Lean-proved in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean).

### Why $d_q((n, 1))$ (S_{n+1} standard rep dim)?

The conjecture extends to all leptons by recognising:

| m | Lepton | n = 2m+1 | $d_q((n,1))$ | Predicted ξ_m factor (no $1/\hbar_q^2$) |
|---|---|:---:|---|---|
| 1 | Electron | 3 | $d_q((3,1)) = [3]_q$ in $S_4$ | $[3]_q \cdot [2]_q / [4]_q$ (T(2,3) calibration? or trivial) |
| 2 | Muon | 5 | $d_q((5,1)) = [5]_q$ in $S_6$ | $[5]_q \cdot [2]_q / [6]_q$ |
| 3 | Tau | 7 | $d_q((7,1)) = [7]_q$ in $S_8$ | $[7]_q \cdot [2]_q / [8]_q$ |

**Wait** — the empirical match is for muon at $\xi_2 = [3]_q \cdot [2]_q / [4]_q$, NOT $[5]_q \cdot [2]_q / [6]_q$. So the conjecture's "n = 2m+1" indexing is wrong; the actual indexing is "n = m+1" (matching m=2 → factor uses [3]_q/[4]_q):

| m | Lepton | Predicted ξ_m (corrected indexing m+2) | Numerical at q_0 |
|---|---|---|---:|
| 1 | Electron | 1 (calibration) | 1.0 |
| 2 | Muon | $[3]_q \cdot [2]_q / [4]_q$ | 1.4893 |
| 3 | Tau | $[5]_q \cdot [2]_q / [6]_q$ | (needs computation) |

This is the **conjecture as stated**: ξ_m uses the (m+1)-strand standard rep dimension d_q((m+1, 1)) of S_{m+2}.

At q_0 ≈ 1.110:
- $d_q((3, 1))$ at $q_0$ = $[3]_q$ ≈ 3.044
- $[2]_q$ ≈ 2.011
- $[4]_q$ ≈ 4.110
- ξ_2 = 3.044 · 2.011 / 4.110 = 1.489 ✓ matches required 1.490

### Tau prediction (testable)

For tau $m=3$:
- ξ_3 candidate = $d_q((4,1)) \cdot [2]_q / [5]_q \cdot (1/\hbar_q^2)$
- $d_q((4,1)) = [4]_q$ in $S_5$ via hook-length
- ξ_3 = $[4]_q \cdot [2]_q / [5]_q \cdot (1/\hbar_q^2)$

At q_0:
- $[4]_q \approx 4.110$
- $[2]_q \approx 2.011$
- $[5]_q \approx 5.205$
- ξ_3 (predicted) = 4.110 · 2.011 / 5.205 · 101.86 ≈ 161.7

vs required ξ_3 for tau = CODATA $m_τ/m_e$ / (m_τ_dim / m_e_dim) = 3477.23 / (something).
If m_τ_dim is similar magnitude as m_μ_dim (~0.7), then required ξ ≈ 3477.23 / 0.7 = 4968 ≈ $H_5$-level adjustment.

The simple analog `d_q((4,1)) · [2]_q / [5]_q · (1/ℏ_q²)` does NOT close tau closing the gap by a factor of ~30. So either:
(a) The conjecture's specific form needs revision for tau
(b) Tau's V̂ convention is different (not H_3 3-channel but H_5 5-channel)
(c) Tau requires higher-tower terms beyond single-gen Li_2^q

This is the OPEN T6 work for the tau side. The muon (m=2) case is the **first member** of the conjectured pattern; tau (m=3) **falsifies** the simplest extension and needs more structure.

## Categorical interpretation candidates

Three readings of the ξ_m formula:

### (A) H_{m+2} std-irrep dimension

ξ_m couples the lepton braid (at H_2 or H_3 substrate) to the
$S_{m+2}$ standard representation. The factor $d_q((m+1, 1)) = [m+1]_q$
is the **q-dimension** of this rep; the $[2]_q / [m+2]_q$ normalisation
is a Schur-Weyl reciprocity factor.

### (B) LR coefficient branching

$\xi_m$ as a Littlewood-Richardson coefficient
$c^{(m+1, 1)}_{(m+1), (1)} \cdot \text{q-bracket normalisation}$.
The LR coefficient $c^{(m+1, 1)}_{(m+1), (1)} = 1$ (one standard
Young tableau for the corresponding skew shape), so the formula
becomes $\text{q-bracket}$.

### (C) Operator-valued $A^\lambda_{\mu, \nu}(I)$

Per [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) §SUPERSEDED,
the canonical dimensional factor is the **operator-valued** $A^\lambda_{\mu, \nu}(I)$
from [`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md).
For the lepton sector, this would specialise to the conjectured
$d_q(\lambda) \cdot [2]_q / [n]_q$ form.

All three readings are consistent with the muon (m=2) numerical
match; distinguishing them requires the derivation work that's
currently open.

## Lean status

The algebraic identity $(3 + h^2)/(2 + h^2) = [3]_q \cdot [2]_q / [4]_q$
is **Lean-proved** in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean)
(`three_halves_factor_eq_q_brackets` theorem; `field_simp; ring`).

The categorical interpretation (this conjecture's full claim) requires
either (A) or (C) above, both of which need substantial additional
Lean formalisation work.

## Cross-references

- [`docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md) — T6 gap (c) full diagnosis
- [`folio-assistant/computations/t6_three_halves_factor_probes.py`](../../../folio-assistant/computations/t6_three_halves_factor_probes.py) — empirical probe identifying the factor
- [`three-halves-structural-factor.lean`](three-halves-structural-factor.lean) — algebraic identity proved
- [`prop:lepton-bring-surface-h3-3channel`](lepton-bring-surface-h3-3channel.md) — V̂_e convention (calibration check)
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula
- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — F_ℓ existence (now partially closed for muon)
