# Per-block θ_λ carry — absolute binding still open, but the signed difference is structural (no fit)

**Date:** 2026-06-02
**Probe:** [`probe_theta_carry_binding.py`](../../computations/probe_theta_carry_binding.py)
→ `probe-theta-carry-binding.witness.json`
**Status:** EXPLORATORY (production-vs-exploratory-discipline); asserts the
refutation. Δ_λ / A≥3-absolute binding remains an open gate.

## The idea (owner, 2026-06-02): "preserve information until observation"

The production binding uses the **scalar** Markov trace `tr_M = Σ_λ y_λ χ^λ`,
which collapses the per-Wedderburn-block q-Reeb phase `θ_λ = arccos(χ^λ/d_λ)` at
step 5 — *before* the archimedean observation `τ` (step 9). This probe tests the
alternative: **carry** the per-block phase shift `Δθ_λ = θ_λ(atom) − θ_λ(free)`
and collapse it only via the `y_λ`-weighted observation (the Markov/Plancherel
measure = `τ`):

$$B(K) = E \cdot \sum_{\lambda:\,|\chi/d|\le 1} y_\lambda(q_0)\,\bigl|\Delta\theta_\lambda\bigr| .$$

Scales tested: derived `μ₀ = m_e/(3·(q−q⁻¹)/2) ≈ 1.630 MeV` (0 fit) and one
global scale (1 param / 4 isotopes). Rotation channels only (`|χ/d|≤1`); growth
channels (`|χ/d|>1`) reported separately.

## Results

| | D | T | ³He | ⁴He | worst |
|---|---|---|---|---|---|
| `B = μ₀·Σ y_λ|Δθ_λ|` (0 fit) | −98.96 % | −99.87 % | −99.89 % | −100.0 % | 100 % |
| `B = scale·Σ y_λ|Δθ_λ|` (1 global scale, 511.5 MeV/rad) | +228 % | −59 % | −66 % | −99 % | 228 % |

**Absolute binding is NOT closed.** The Markov-weighted `|Δθ_λ|` is nearly
A-independent (like the scalar `Δtr_M`), so it cannot track the ~13× binding
growth from D to ⁴He. The premature-collapse fix alone is insufficient at the
`|Δθ|` functional level — the A≥3-absolute gate stands.

## The useful signal — the signed difference is structural, no fit

| quantity | value |
|---|---|
| **T/³He difference** `scale·(Σy|Δθ|_T − Σy|Δθ|_³He)` | **+8.18 %** vs AME |

T and ³He share `n=9` (same partitions, same `y_λ`), so the difference is a pure
test of the signed per-block structure. The phase-carry reproduces it to **+8.18 %
with NO isotope-specific fit** (the same global absolute scale). This is the
**signed per-block object the volume side proved necessary** (#1709: a positive
volume gets the ³H/³He sign *wrong*) — and it does so **without** the fitted
`(1+q)/2` (CAL-4, [discipline assessment](2026-05-31-isospin-mirror-v9-discipline-assessment.md)).
So:

- ✅ The signed phase-carry gets the mirror **difference** sign + ~8 % magnitude,
  parameter-free (modulo one global scale) — strictly better than both the
  wrong-sign volume and the fitted `(1+q)/2`.
- 🔴 It does **not** close **absolute** binding (the A-dependence is missing).

## Verdict / next

Confirms cheat-sheet §9.3 with a clean compute: **differences are structural,
absolute is open.** The `|Δθ_λ|` functional is too flat for the A≥3 magnitude —
consistent with `tr ~ exp(Vol)` (the phase is the linear/angle part; the
amplitude/growth lives in the `|χ/d|>1` channels excluded here). The next probe
should carry the **growth (hyperbolic) channels** `arccosh(|χ/d|)` alongside the
rotation phase — i.e. recover the full `exp(Vol)` per block, not just the linear
angle — which is the §9.3 "full-order `θ_λ`" item. Coordinate with the
operator-valued combiner (#1698).
