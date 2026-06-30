**Conjecture (lepton-tower closure factor — unifying form).** *Let
$K_\ell$ be the canonical knot for the lepton at tower-index $m$
(electron $m=1$ trefoil / muon $m=2$ figure-eight / tau $m=3$
amphichiral $10_{43}$ candidate). The canonical operator-level
mass-tower $\xi_m$ correction factor is*

$$
\boxed{\;\xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q}\;}
$$

*where $[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ is the
symmetric q-integer. The triple $(2m-1, m, 2m)$ is symmetric in
$h = q - q^{-1}$ — bar-anti-symmetric upper jet, middle index,
bar-symmetric closing trace. This is the **structural** factor
(matching the Lean `lepton_xi` and the verification table below); the
full mass closure additionally carries the universal substrate scalar
$1/\hbar_q^2$, common to all leptons and hence cancelling in the
inter-lepton ratios validated here.*

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

## Provenance — empirical fit (categorical derivation open)

The structural factor was identified **empirically** as the best of
28 candidate q-bracket ratios (matching the required lepton ratios to
$0.034\%$, the best by $20\times$ over the next-best candidate;
[`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md)).
It is therefore a **conjecture** (fit-identified), not a derived
result. The categorical derivation — why the q-bracket triple
$(2m-1, m, 2m)$ falls out of the per-braid mass tower's
operator-valued $A^\lambda_{\mu,\nu}(I)$ branching at the lepton's
amphichiral knot — remains open work for Option E (Kashiwara crystal).

The algebraic identity
$\frac{[3]_q \cdot [2]_q}{[4]_q} = \frac{3 + h^2}{2 + h^2}$ (the muon
case) is Lean-proved in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean).

> **History.** Earlier indexing attempts ($n = 2m+1$, then $n = m+1$)
> and a tau probe that carried the substrate scalar $1/\hbar_q^2$
> explicitly were superseded by the unifying structural form above;
> those working notes have been removed to keep the conjecture clean.

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

All three readings are consistent with the muon (m=2) canonical
match; distinguishing them requires the derivation work that's
currently open.

## Resolution — unifying formula

The "simple extension" pattern `[m+1]_q · [2]_q / [m+2]_q` is FALSIFIED for tau (predicted ξ_3 = `[4]_q · [2]_q / [5]_q` $\approx$ 1.59 vs required $\approx$ 2.47, off by 35 %).

The **correct unifying formula**:

$$
\boxed{\;\xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q}\;}
$$

canonical structural verification at $q_0 \approx 1.110$ (the formal derivation witness):

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

All proofs are `field_simp; ring` over generic `[Field R]` per AGENTS.md §7c.

The categorical derivation (why $\xi_m = [2m-1]_q \cdot [m]_q / [2m]_q$ specifically — i.e., how the q-bracket triple $(2m-1, m, 2m)$ falls out of the per-braid mass tower's operator-valued $A^\lambda_{\mu, \nu}(I)$ branching at the lepton's H_{2m+1}-substrate amphichiral knot) remains open work for Option E (Kashiwara crystal).

## Cross-references

- [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md) — T6 gap (c) full diagnosis (muon side)
- [`docs/audits/-t6-f-ell-derivation-attempt.md`](../../../docs/audits/-t6-f-ell-derivation-attempt.md) — T6/F_ℓ workplan +  tau followup section
- the canonical formalism — muon categorical canonical evaluation
- the canonical formalism — tau amphichiral q-bracket canonical evaluation
- [`prop:three-halves-structural-factor`](three-halves-structural-factor.md) — Lean-proved structural identities (muon + tau)
- [`prop:lepton-bring-surface-h3-3channel`](lepton-bring-surface-h3-3channel.md) — $\hat{V}_e$ convention (calibration check)
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula
- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — F_ℓ existence (partially closed: muon + tau q-bracket forms now identified; categorical derivation open for Option E)
