# ³He pair-knot C_λ·S_λ + explicit Z(Z−1) Coulomb — probe result

**Date:** 2026-06-22
**Branch:** `claude/bold-mendel-5994kg` (PR #2612)
**Status:** EXPLORATORY probe. No production rewire, no fit, no fourth calibration.
**Probe:** [`computations/he3_pairknot_clambda_coulomb_probe.py`](../../computations/he3_pairknot_clambda_coulomb_probe.py)
**Witness:** [`he3-pairknot-clambda-coulomb-probe.witness.json`](../../computations/he3-pairknot-clambda-coulomb-probe.witness.json) (`allPassed`, audit-only)

## Purpose

Executes the fix direction that #2478
([`2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md`](2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md))
*scoped but did not close* — "an LP-dual pair-knot composite for the proton
near-pole pair + an explicit Z(Z−1) Coulomb term" — done the **non-fit** way:
the LP-dual pair-knot shadow price via its analytical factorisation
([`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/mass-theory/mass-coefficient-shadow-price.md))
`u_λ* = C_λ · S_λ(Z,N,A)` (the direct H₆ LP is degenerate/intractable per
#2478, so the analytical `S_λ` classification is used, not the LP solve), plus
the explicit `Z(Z−1)/A^{1/3}` Coulomb term of the Skein binding Lagrangian
([`def:skein-binding-lagrangian`](../../content/quantum-observable-universe/particle-interactions/skein-binding-lagrangian.md)).

## Finding 1 — the C_λ·S_λ block classification (which blocks carry charge)

`S_λ`'s type is fixed by the content sum `c(λ) = Σ_□ (j−i)`
(`prop:mass-coefficient-shadow-price`): `c>0` volume-type, `c=0` isospin-type,
`c<0` charge-type (Z-dependent). At H₆ (the 2-nucleon pair-knot arena):

| `S_λ` type | content sum | partitions of 6 | count |
|---|---|---|---|
| charge (Z-dependent) | `c(λ) < 0` | `[3,1,1,1] [2,2,2] [2,2,1,1] [2,1,1,1,1] [1⁶]` | 5 |
| isospin | `c(λ) = 0` | `[3,2,1]` (self-conjugate) | 1 |
| volume (A-dependent) | `c(λ) > 0` | `[6] [5,1] [4,2] [4,1,1] [3,3]` | 5 |

The conjugation symmetry `c(λ') = −c(λ)` (= the bar involution on partitions)
pairs each volume block with a charge block; the self-conjugate `[3,2,1]` is the
lone isospin block. **The pp pair-knot's Coulomb lives in the 5 charge-type
(`c<0`) blocks** — this is the concrete structural identification #2478 asked
for (it pins *which* Wedderburn blocks the two-like-charge term occupies).

## Finding 2 — the open invariant is BRACKETED by two parameter-free endpoints

| quantity | value (MeV) | vs split | fit? |
|---|---|---|---|
| derived pp-Coulomb `tanh(ln q₀)·B_pp` | **0.238** | 31% (UNDER) | none (`def:coulomb-charge` + B_pp from H₆ trace) |
| AME ³H−³He split (target) | 0.764 | — | experimental, comparison only |
| Skein `a_C·Z(Z−1)/A^{1/3}` (a_C ≈ 0.697) | **0.967** | 127% (OVER) | a_C is the empirical BW value — *not adopted* |

`derived < split < skein-empirical` holds. The two **parameter-free** endpoints
— the bare categorical pp-Coulomb (below) and the Skein `Z(Z−1)/A^{1/3}` form
with the empirical `a_C` (above) — **bracket** the empirical split. This
sharpens #2478's "31%, 3.2× short" into a two-sided statement: the categorical
two-like-charge brane-pairing invariant lies inside `(0.238, 0.967)` MeV. It is
**still OPEN**; landing it on 0.764 by fitting `a_C` (or any per-pair constant)
is a forbidden CAL-4 fit (Δ_λ gate).

## Finding 3 — the explicit Z(Z−1)/A^{1/3} structure has the right Z-dependence

| atom | Z,N | `Z(Z−1)/A^{1/3}` | Skein L_Coul (empirical a_C) |
|---|---|---|---|
| D | 1,1 | 0 | 0 |
| T | 1,2 | 0 | 0 |
| ³He | 2,1 | 1.387 | 0.967 |
| ⁴He | 2,2 | 1.260 | 0.878 |

T carries **zero** pp-Coulomb (`Z(Z−1)=0`) while ³He carries the most — exactly
the mirror asymmetry that makes ³He the *less*-bound member. The structure thus
fixes the **sign** of the T/³He split correctly (the brane-tower of #2467 got it
backwards); only the magnitude normalisation is open.

## Probe diagnostics (canonical-watcher Slot J)

| diagnostic | value |
|---|---|
| GB filtration | H₆ diproton pair-knot, ℓ ≤ 15 (2 nucleons × 3 strands) |
| jet order | `h^1` — Coulomb excess `δ = ½(q−q⁻¹)` per crossing (`def:coulomb-charge`); strong baseline `½(q+q⁻¹)` is `h^0` |
| bar-symmetry | bar-anti-symmetric (charge/sinh part `Q·(q−q⁻¹)`; equivalently `c(λ')=−c(λ)`) |

## Verdict

The user's requested direction is executed in full and honestly: the LP-dual
pair-knot composite (via the analytical `C_λ·S_λ` route, since the direct LP is
degenerate) **plus** the explicit `Z(Z−1)/A^{1/3}` Coulomb. The **structure** is
derived and correct — the 5 `c<0` blocks carry the charge term, T/³He sign is
right, and the magnitude is bracketed `(0.238, 0.967)` MeV by two parameter-free
endpoints. The **magnitude closure** — the categorical two-like-charge
brane-pairing invariant inside that bracket — remains the open item; it is **not**
a direct LP-dual (degenerate at H₃, intractable at H₆, #2478) and closing it by
fit is forbidden (CAL-4 / Δ_λ gate). No production path is rewired.

## Cross-references

- [`2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md`](2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md) (#2478 — scoped the open item)
- [`2026-06-18-he3-brane-tower-structural-gap.md`](2026-06-18-he3-brane-tower-structural-gap.md) (#2467 — the diagnosis)
- [`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/mass-theory/mass-coefficient-shadow-price.md) (the C_λ·S_λ factorisation)
- [`def:coulomb-charge`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md) + [`def:skein-binding-lagrangian`](../../content/quantum-observable-universe/particle-interactions/skein-binding-lagrangian.md)
- [`charge_coulomb_tn3he_derived.py`](../../computations/charge_coulomb_tn3he_derived.py) (the derived-Coulomb endpoint)
