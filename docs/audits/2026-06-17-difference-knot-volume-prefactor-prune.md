# Difference-link volume → binding: constant-prefactor prune (2026-06-17)

**Probe:** [`difference_knot_volume_prefactor_probe.py`](../../computations/probes/difference_knot_volume_prefactor_probe.py)
(witness `difference-knot-volume-prefactor.witness.json`).
**Route:** the one un-refuted geometric candidate for the `q₀^(10A−5)` /
per-isotope binding residual — the **Sage per-piece JSJ volume** of the
difference link `D = W_atom·W_free⁻¹`
([`2026-06-13-difference-knot-jsj-classification.md`]), whose decisive test is

    B_AME ≈ m_e · Σ Vol(hyperbolic pieces of D) · ρ / ℏ_q²   (CONSTANT prefactor m_e·ρ/ℏ_q²).

**Discipline:** formalize-first prune — run the *cheap, non-rigorous* version
of the test before paying for the Sage step; no fit; promotes nothing.

## Environment update (vs the 2026-06-13 probe)

SnapPy 3.3.2 installs cleanly here (`pip install snappy`). Re-tested the
Sage-gating the prior probe reported:

| operation | without Sage (SnapPy 3.3.2) |
|---|---|
| `.volume()` (non-rigorous) | ✅ works |
| `canonical_retriangulation` | ✅ works on geometric inputs — **but raises "degenerate tetrahedra" on the composite difference links** (returns nothing usable) |
| `verify_hyperbolicity` (rigorous interval volume) | ❌ **still `SageNotAvailable`** |

So rigorous per-piece volumes remain Sage-only, but the **constant-prefactor
test needs volumes only to ~1%** — which the non-rigorous volume supplies — and
rigor cannot turn a non-constant prefactor constant. Hence the prune is valid.

## Result — NON-CONSTANT prefactor (2.36×)

| iso | A | cusps `=2A−1` | Vol(D) (non-rig.) | B_AME (MeV) | k = B_AME/Vol(D) |
|---|---|---|---|---|---|
| ²H | 2 | 3 | 6.088 | 2.225 | **0.365** |
| ³H | 3 | 5 | 12.467 | 8.482 | **0.680** |
| ³He | 3 | 5 | 16.547 | 7.718 | **0.466** |
| ⁴He | 4 | 7 | 32.847 | 28.296 | **0.861** |

`k` spread (max/min) = **2.358** — far from the `< 1.1` a single-`ρ` closure
needs. The geometric closure `B ≈ m_e·Vol(D)·ρ/ℏ_q²` with one constant `ρ` is
**refuted** at this (non-rigorous) level.

## Why rigor is very unlikely to rescue it

1. **A 2.36× prefactor gap** would require the rigorous per-piece volumes to
   move atom-specifically by ~2× relative to the degenerate-triangulation
   totals — implausible (verified volumes of the same manifold differ from the
   degenerate best-effort by percent-level, not 2×).
2. **Volume instability already visible:** ³H reads `Vol = 12.47` here vs
   `14.65` in the 2026-06-13 audit (~17% run-to-run, from the degenerate
   triangulation) — but even the *most* favourable re-reading does not collapse
   the 2.36× spread.
3. **Consistent with the H1 refutation**
   ([`2026-06-13-9b-h1-exponent-location-refuted.md`]): the per-nucleon
   increment is carried by the **experimental** `B_AME(A)` curve, not by any
   single framework-side quantity (trace exponent *or* difference-link volume).
   A constant-prefactor geometric law is exactly the kind of single-quantity
   predictor that finding rules out.

## Verdict

The difference-link-volume route **closes negative** at the constant-prefactor
level. The `2A−1` chain-object count is geometrically real (cusp count, prior
audit), but the per-object *weight* is not a constant times the hyperbolic
volume. Combined with the H1 experimental-side result and the §6c observe-last
refutation, **all three framework-side routes to `q₀^(10A−5)` (trace collapse,
phase sum, difference-link volume) are now refuted or fitted-adjacent** — the
residual is a property of `B_AME(A)` itself (Track-A / CAL-4), not derivable
from a single categorical/geometric invariant. **Recommend NOT prioritising the
Sage rigorous step** (it would confirm, not rescue).

*Sage follow-up (only if the recommendation is overridden):* the definitive test
is `verify_hyperbolicity` + `splitting_surfaces` (Sage) per-piece volume sum vs
the constant prefactor — but expect it to confirm the 2.36× non-constancy.
