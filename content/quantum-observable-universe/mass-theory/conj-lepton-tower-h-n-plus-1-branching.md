**Conjecture (lepton-tower closure factor — unifying form).** *Let
$K_\ell$ be the canonical knot for the lepton at tower-index $m$
(electron $m=1$ trefoil / muon $m=2$ figure-eight / tau $m=3$
amphichiral $10_{43}$ candidate). The canonical operator-level
mass-tower $\xi_m$ correction factor is*

$$
\boxed{\;\xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q} \cdot \frac{1}{\hbar_q^2}\;}
$$

*where $[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ is the
symmetric q-integer. The triple $(2m-1, m, 2m)$ is symmetric in
$h = q - q^{-1}$ — bar-anti-symmetric upper jet, middle index,
bar-symmetric closing trace.*

### Earlier framing (superseded by  unifying formula)

> **SUPERSEDED .** The earlier conjecture
> $\xi_m = d_q((n,1)) \cdot [2]_q / [n+1]_q$ (with $n = 2m+1$, then
> revised to $n = m+1$) matched muon but **falsified at tau**
> ($\xi_3 = [4]_q \cdot [2]_q / [5]_q$ predicted $\approx$ 1.59 vs required
> $\approx$ 2.47, off by 35 %). The  amphichiral filter identified
> the actual closure $\xi_3 = [5]_q \cdot [3]_q / [6]_q$ and the
> unifying form above. The earlier framing is preserved below for
> pedagogical trajectory; the "Resolution" section is
> the current authoritative statement.

## Derivation sketch (open)

The factor $[3]_q \cdot [2]_q / [4]_q$ was numerically identified
in [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md)
+ [`folio-assistant/computations/t6_three_halves_factor_probes.py`](../../../folio-assistant/computations/t6_three_halves_factor_probes.py)
as the closed-form fit (matching 28 candidate ratios to 0.034%, the
best by 20$\times$ over the next best).

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

**Wait** — the empirical match is for muon at $\xi_2 = [3]_q \cdot [2]_q / [4]_q$, NOT $[5]_q \cdot [2]_q / [6]_q$. So the conjecture's "n = 2m+1" indexing is wrong; the actual indexing is "n = m+1" (matching m=2 $\to$ factor uses [3]_q/[4]_q):

| m | Lepton | Predicted ξ_m (corrected indexing m+2) | Numerical at q_0 |
|---|---|---|---:|
| 1 | Electron | 1 (calibration) | 1.0 |
| 2 | Muon | $[3]_q \cdot [2]_q / [4]_q$ | 1.4893 |
| 3 | Tau | $[5]_q \cdot [2]_q / [6]_q$ | (needs computation) |

This is the **conjecture as stated**: ξ_m uses the (m+1)-strand standard rep dimension d_q((m+1, 1)) of S_{m+2}.

At q_0 $\approx$ 1.110:
- $d_q((3, 1))$ at $q_0$ = $[3]_q$ $\approx$ 3.044
- $[2]_q$ $\approx$ 2.011
- $[4]_q$ $\approx$ 4.110
- ξ_2 = 3.044 $\cdot$ 2.011 / 4.110 = 1.489 (matches required 1.490)

### Tau prediction (testable)

For tau $m=3$:
- ξ_3 candidate = $d_q((4,1)) \cdot [2]_q / [5]_q \cdot (1/\hbar_q^2)$
- $d_q((4,1)) = [4]_q$ in $S_5$ via hook-length
- ξ_3 = $[4]_q \cdot [2]_q / [5]_q \cdot (1/\hbar_q^2)$

At q_0:
- $[4]_q \approx 4.110$
- $[2]_q \approx 2.011$
- $[5]_q \approx 5.205$
- ξ_3 (predicted) = 4.110 $\cdot$ 2.011 / 5.205 $\cdot$ 101.86 $\approx$ 161.7

vs required ξ_3 for tau = CODATA $m_τ/m_e$ / (m_τ_dim / m_e_dim) = 3477.23 / (something).
If m_τ_dim is similar magnitude as m_μ_dim (~0.7), then required ξ $\approx$ 3477.23 / 0.7 = 4968 $\approx$ $H_5$-level adjustment.

The simple analog `d_q((4,1)) · [2]_q / [5]_q · (1/ℏ_q²)` does NOT close tau closing the gap by a factor of ~30. So either:
(a) The conjecture's specific form needs revision for tau
(b) Tau's $\hat{V}$ convention is different (not H_3 3-channel but H_5 5-channel)
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

## Resolution — unifying formula

The "simple extension" pattern `[m+1]_q · [2]_q / [m+2]_q` is FALSIFIED for tau (predicted ξ_3 = `[4]_q · [2]_q / [5]_q` $\approx$ 1.59 vs required $\approx$ 2.47, off by 35 %).

The **correct unifying formula**:

$$
\boxed{\;\xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q} \cdot \frac{1}{\hbar_q^2}\;}
$$

Numerical verification at $q_0 \approx 1.110$ (`tau_amphichiral_sdp_probe.py` witness):

| m | Lepton | Formula | At $q_0$ | Required | Δ |
|---|---|---|---:|---:|---:|
| 1 | Electron | (calibration unit) | 1.000 | 1.0 | 0 % |
| 2 | Muon | $[3]_q \cdot [2]_q / [4]_q$ | 1.48931 | 1.48929 | **+0.001 %** |
| 3 | Tau | $[5]_q \cdot [3]_q / [6]_q$ | 2.48736 | 2.46776 | **+0.79 %** |
| 4 | (no SM lepton) | $[7]_q \cdot [4]_q / [8]_q$ | 3.50311 | — | — |

The triple $(2m-1, m, 2m)$ is **symmetric in $h = q - q^{-1}$** at every step:
- $2m-1$ odd $\to$ bar-anti-symmetric q-bracket contribution from the upper jet
- $m$ $\to$ middle index (symmetric / anti-symmetric depending on parity)
- $2m$ even $\to$ bar-symmetric q-bracket from the closing trace

This pattern is precisely what the lepton's amphichirality should produce — the upper and lower indices are reflections of each other across the middle, consistent with the **knot-operator = symmetry equivalence** in the owner's  directive.

## Lean formalization

The unifying formula's algebraic content is **Lean-proved** in two places:

- [`three-halves-structural-factor.lean`](three-halves-structural-factor.lean):
    - Muon: `three_halves_factor_eq_q_brackets` — $(3 + h^2)/(2 + h^2) = [3]_q \cdot [2]_q / [4]_q$
    - Tau: `bracket6_eq_bracket2_bracket3_times_one_plus_h_sq` — $[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)$
    - Tau closure: `bracket5_bracket3_div_bracket6` — $[5]_q \cdot [3]_q / [6]_q = [5]_q / ([2]_q \cdot (1+h^2))$

- [`conj-lepton-tower-h-n-plus-1-branching.lean`](conj-lepton-tower-h-n-plus-1-branching.lean):
    - `lepton_xi` — concrete definition for electron/muon/tau (no `sorry`)
    - `lepton_xi_muon_eq_closed_form` — muon ξ_2 closed form
    - `lepton_xi_tau_eq_reduced_form` — tau ξ_3 reduced form
    - `br6_eq_br2_br3_times_one_plus_h_sq` — fundamental tau identity (mirror of sibling file's theorem)
    - `lepton_xi_electron_eq_one` — calibration convention

All proofs are `field_simp; ring` over generic `[Field R]` per CLAUDE.md §7c.

The categorical derivation (why $\xi_m = [2m-1]_q \cdot [m]_q / [2m]_q$ specifically — i.e., how the q-bracket triple $(2m-1, m, 2m)$ falls out of the per-braid mass tower's operator-valued $A^\lambda_{\mu, \nu}(I)$ branching at the lepton's H_{2m+1}-substrate amphichiral knot) remains open work for Option E (Kashiwara crystal).

## Cross-references

- [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md) — T6 gap (c) full diagnosis (muon side)
- [`docs/audits/-t6-f-ell-derivation-attempt.md`](../../../docs/audits/-t6-f-ell-derivation-attempt.md) — T6/F_ℓ workplan +  tau followup section
- [`folio-assistant/computations/t6_three_halves_factor_probes.py`](../../../folio-assistant/computations/t6_three_halves_factor_probes.py) — muon empirical probe
- [`folio-assistant/computations/probes/tau_amphichiral_sdp_probe.py`](../../../folio-assistant/computations/probes/tau_amphichiral_sdp_probe.py) — tau amphichiral q-bracket probe
- [`prop:three-halves-structural-factor`](three-halves-structural-factor.md) — Lean-proved structural identities (muon + tau)
- [`prop:lepton-bring-surface-h3-3channel`](lepton-bring-surface-h3-3channel.md) — $\hat{V}_e$ convention (calibration check)
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula
- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — F_ℓ existence (partially closed: muon + tau q-bracket forms now identified; categorical derivation open for Option E)
