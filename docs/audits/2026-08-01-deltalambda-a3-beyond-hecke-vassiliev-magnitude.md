# GAP-A-3 beyond-Hecke: the Vassiliev weight-system does NOT supply the A=3 magnitude factor 1.585×

**Date:** 2026-08-01
**Branch:** `claude/deltalambda-beyond-hecke-vassiliev-magnitude-2026-08-01`
**Axis:** per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the A=3 (triton) 3-body **magnitude**.
**Tier:** derivation probe. **Verdict: REFUTE(scope-b) of the bare-weight claim.** 0 fit; nothing wired.
**Gate:** Δ_λ open-for-all for derivation routes (owner reversal 2026-07-13); Subgoal-2 open-for-all (2026-07-11).

- Lean: [`QOU/MassTheory/VassilievMagnitudeA3.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/VassilievMagnitudeA3.lean) — sorry-free, `lean`-direct exit 0.
- Probe: [`computations/deltalambda/vassiliev_magnitude_a3_probe.py`](../../computations/deltalambda/vassiliev_magnitude_a3_probe.py)
  · witness `vassiliev-magnitude-a3.witness.json`.

## The gap

The A=3 3-body magnitude factor `r* = μ₃/c₃ ≈ 1.585` is the ratio between the target additive-residual
moment `μ₃ = +0.4708` (`AdditiveResidualSimplex` #4320) and the Hecke-level near-miss `c₃ = +0.297`
(#4364 `BorromeanMagnitudeLift`, the `H₉` joint-trace lift of the proved Borromean 3-body cluster).
It is now bracketed out of **every Hecke-level ingredient**:

- **not a derived tower LEVEL** — three-walls audit 2026-07-26 (#4364/#4376);
- **not a geometric `W_λ`** — #4392 (`S⁴ = 1`, no other geometric measure);
- **not a coordination-EDGE factor** — #4472 (`K₃` breaks the Brunnian order `O(h⁴) → O(h²)`);
- **not the exact-order Milnor μ̄_A coefficient** — #4480 (ratio exactly `−2`, no combination near `1.585×`).

So the missing `1.585×` would require **genuinely NEW beyond-Hecke structure**. PR #4479 built a
sorry-free Vassiliev / finite-type Lean scaffold (`QOU/KnotTheory/Vassiliev/`); the DD-1 grading crux
(`MilnorVassilievGrading.lean`, merged) pins the factor-of-2 between the Brunnian-deficit Vassiliev
degree `2(A−1)=4` and the length-A Milnor degree `A−1=2`. This audit tests the last un-excluded
candidate with that tool: **does a Vassiliev weight-system correction supply the `1.585×`?**

## The object and the decisive bound

The **proved** Borromean 3-body deficit closed form (A=3), with `h = q − q⁻¹`, is

> `1 − τ_Borr(h) = h⁴ (3 + h²) / (h² + 4)`

(`milnor_weight_parity_convergence_probe.py`; the same `borrDeficit` the Hecke Markov trace evaluates
at `q₀`). Its leading finite-type (Vassiliev degree `2(A−1)=4`) **weight** is the `h → 0` symbol
`(3/4)·h⁴`.

**Decisive structural fact (`leadingWeight_le_borrDeficit`, exact for ALL h).** The leading Vassiliev
weight `(3/4)h⁴` is `≤` the full deficit, because

> `(3+h²)/(h²+4) − 3/4 = (h²/4)/(h²+4) ≥ 0`.

`(3+h²)/(h²+4)` **increases** in `h²` from `3/4` (at `h=0`) toward `1`: the leading term is the
*smallest* term of a positive convergent series. Hence the **weight-to-Hecke ratio is `≤ 1`** for every
`h` (`vassiliev_weight_cannot_supply_magnitude`), while the required factor is `r* > 3/2 > 1`.

The mechanism is structural, not numerical: the finite-type filtration is a *re-expansion of the same
Markov trace* the Hecke level already sums. The Hecke near-miss `c₃ = 0.297` IS the full finite-type
sum; any finite-type truncation (a "weight") is `≤` that sum, never `1.585×` larger. The magnitude gap
lives OUTSIDE the finite-type filtration of this deficit object.

## Numerical confirmation (0 fit, forward, at the muon-canonical q₀)

At `q₀ = 1.10997859555…` (muon-canonical `computations/` layer), `h₀ = q₀ − q₀⁻¹ ≈ 0.20906`:

| quantity | value |
|---|---|
| leading Vassiliev weight coeff (deg-4, in `h`) | `3/4` (exact) |
| full deficit `1−τ_Borr(q₀)` (= Hecke Markov value) | `0.00143784` |
| leading weight `(3/4)h₀⁴` | `0.00143268` |
| **weight / Hecke** | **`0.99641` (≤ 1)** |
| Hecke / weight (the whole finite-type "correction") | `1.00360` (**+0.36 %**) |
| required `r* = μ₃/c₃` | `1.58519` |
| `log₂ 3` (numerology coincidence) | `1.58496` |

The entire finite-type tower beyond the leading weight contributes **+0.36 %**, not the **+58.5 %**
(`r* − 1`) the magnitude gap requires. The Vassiliev weight ratio is `0.996`, three orders of magnitude
short of `1.585`.

## The length-A Milnor reading (degree A−1 = 2) also fails

The genuine μ̄(123) Milnor invariant is realized as an **integer**-valued Vassiliev invariant taking
value `±1` (scaffold `QOU.KnotTheory.Vassiliev.BrunnianVassilievBridge.muBar_realized`, `val : K → ℤ`);
the corpus-measured Milnor ratio is the integer `−2 = J_Hopf(q=1)` (#4480). An integer weight (`±1` or
`−2`) cannot equal `r* ∈ (3/2, 2) ∖ ℤ` (`no_integer_weight_eq_rStar`) — wrong value, and for the `−`
branch wrong sign.

## Numerology dismissal

`r* ≈ log₂ 3 = 1.58496…` is a bare coincidence. `log₂ 3` is irrational: `log₂ 3 = a/b` (`a,b ≥ 1`)
would give `2^a = 3^b`, impossible since `2^a` is even and `3^b` odd (`two_pow_ne_three_pow`). So
`log₂ 3` is not a rational finite-type weight nor a ratio of the integer weights the substrate produces
— the coincidence is NOT a derivation.

## Verdict — REFUTE(scope-b) of the bare-weight claim; NOT a general Vassiliev exclusion

**Classification.** The claim excluded is narrow: *"a single Vassiliev finite-type weight of the
Borromean deficit, as a bare multiplicative magnitude factor, equals `r*`."* This is a **scope-(b)
structural exclusion** citing two proved invariants:

1. **`leadingWeight_le_borrDeficit`** — the leading Vassiliev weight is `≤` the full deficit for all
   `h` (positivity/monotonicity of `(3+h²)/(h²+4)`). So the weight-to-Hecke ratio is `≤ 1`, and a
   factor `> 1` cannot come from truncating a positive series to its leading term.
2. **Integrality** of the finite-type invariants (`val : K → ℤ`, scaffold typing) — the length-A
   Milnor weight is the integer `±1` / `−2`, and no integer lies in `(3/2, 2)`.

**What is NOT claimed.** This does **not** exclude Vassiliev / Kontsevich structure from a *larger*
closure where an integer weight combines with other ingredients (a different object, a q₀-dressing, an
operator-valued combiner). That is untested here. Per the "before declaring refuted" discipline, the
(b) is on the *bare-weight-as-magnitude* claim only; the ingredient is not excluded in general.

Together with the four prior walls this **brackets the A=3 magnitude source completely at the finite-type
level too**: the missing `1.585×` is neither a derived LEVEL, nor a geometric `W_λ`, nor a
coordination-EDGE, nor the exact-order μ̄_A coefficient, **nor a Vassiliev weight-system correction of
the Borromean deficit** — every 0-fit structural quantity of this object is `≤` the Hecke value or an
integer. The A=3 Δ_λ exact magnitude closure remains **open** (scope-a), now with the finite-type route
closed. The `1.585×` requires structure genuinely *outside* the finite-type filtration of the single
Borromean deficit — e.g. a per-isotope operator-valued combiner across multiple Wedderburn channels, or
a cross-cluster interface term, neither of which is a truncation of `1 − τ_Borr`.

## Anti-fit / honesty ledger

- **0 free parameters** throughout; `μ₃`, `c₃`, AME, CODATA, `q₀` never inverted. No word or weight
  was chosen to hit `1.585` — the `(3/4)h⁴` weight is the forced `h → 0` symbol of the proved deficit.
- Verdict **REFUTE(scope-b)** on the *bare-weight-as-magnitude* claim (two cited proved invariants);
  explicitly **not** a general exclusion of the Vassiliev ingredient.
- Nothing wired. "No seventh fit-based ansatz" + PROBE-4 KL-prune stand. Formalize-first honoured: the
  bound and the exclusion are sorry-free Lean statements (lean-direct exit 0) written before the probe.

## Cross-references

- Proved deficit closed form + weight-parity convergence: `milnor_weight_parity_convergence_probe.py`.
- Hecke near-miss lifted: `BorromeanMagnitudeLift.lean` (#4364).
- Exact-order μ̄_A coefficient (ratio −2): `MilnorExactCoefficient.lean` (#4480).
- DD-1 factor-of-2 grading crux: `MilnorVassilievGrading.lean` (merged).
- Vassiliev finite-type scaffold: `QOU/KnotTheory/Vassiliev/` (#4479).
- Four prior A=3-magnitude walls: [`2026-08-01-deltalambda-gap-a4-brane-tower-level.md`](2026-08-01-deltalambda-gap-a4-brane-tower-level.md), [`2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md).
- Target moment: `AdditiveResidualSimplex.lean` (#4320) — `μ₂=0, μ₃=+0.4708, μ₄=−4.591`.
- Option-E ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md).
