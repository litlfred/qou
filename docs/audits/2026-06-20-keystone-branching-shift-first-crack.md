# First structural crack at the q-deformed keystone (muon) shift

**Date:** 2026-06-20
**Branch:** `claude/keystone-branching-shift-probe-2026-06-20`
**Status:** Negative / sharpening result — naive Res functor mechanism refuted for the h⁴ channel
**Tool:** `pyhecke_native` v0.9.0 (built in-sandbox per PR #2511)
**Script:** [`scripts/keystone_branching_shift_probe.py`](scripts/keystone_branching_shift_probe.py)

## What was asked

The functor-resolution doc
[`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md)
§4 step 2 names exactly one well-posed object to evaluate now that the H₅
algebra is reachable:

> Evaluate the precise algebraic shift in the H₃(q) Markov trace induced by
> evaluating the knot through the ℓ=2 (E₍₃,₂₎) projector versus the ℓ=1
> (E₍₃,₁,₁₎) projector.

via the classical S₅ → S₃ restriction branchings

$$(3,2)\downarrow S_3 = (3)\oplus 2\cdot(2,1), \qquad
  (3,1,1)\downarrow S_3 = (1,1,1)\oplus 2\cdot(2,1)\oplus(3).$$

**Discipline.** Per the critical-distance license and the 2026-06-13 doc §1,
the 210 ppb muon target is an *anchor-shift artifact*. This probe does **not**
fit `1.000000210`; it reports what the structural object gives and at what
order of magnitude, so the mechanism stands or falls on its size.

## What it gives (q₀ = 1.1099785955541805, dps = 50)

The H₃ inputs (mpfr Borromean characters, f64 Markov weights):

| ν | y_ν^{H3} | χ_ν^{Bor} |
|---|----------|-----------|
| (3) | +0.4153957863 | +1.000000000 |
| (2,1) | +0.2809296340 | +1.994185810 (= 2 − 3h⁴ − h⁶) |
| (1,1,1) | +0.0227449457 | +1.000000000 |

**Model A — branching-multiplicity trace** $T_g=\sum_{\nu}m(\nu;\mu_g)\,y_\nu\,\chi_\nu$:

- $T_\mu = 1.5358475659$, $T_e = 1.5585925116$
- $T_e - T_\mu = 2.2744945706\times10^{-2}$
- isolated (1,1,1) term $= 2.2744945706\times10^{-2}$, agreeing with the
  difference to $|\Delta| = 6.9\times10^{-18}$ (machine zero).

**Model B — H₅ home-block weight ratio** $r = y_{(3,2)}^{H5}/y_{(3,1,1)}^{H5}$:

- $y_{(3,2)}^{H5} = 0.0617237153$, $y_{(3,1,1)}^{H5} = 0.0167666090$
- $r = 3.6813475805$.

## Structural verdict (no fitting)

1. **The h⁴-bearing (2,1) channel cancels exactly between generations.** Its
   S₅→S₃ branching multiplicity is **2 in both** (3,2) and (3,1,1) — a
   classical, q-independent symmetric-group fact (verified by hand via
   S₅→S₄→S₃ box removal and reproduced to 6.9e-18 numerically). So the
   `2·y₍₂,₁₎·χ₍₂,₁₎` term is identical in $T_\mu$ and $T_e$ and drops out of the
   difference. **The naive Res functor multiplicity model carries no
   h⁴-driven generation splitting.**

2. **The entire Model-A split is the antisymmetric (1,1,1) sign channel**
   (χ = 1, h-**independent**), present in the electron block (3,1,1) and absent
   in the muon block (3,2). Its size is 2.27×10⁻² in absolute terms (the
   isolated (1,1,1) term) and ~1.46×10⁻² as a *relative* split
   ($\Delta T / T_e \approx 1.459\%$).

3. **Both well-posed objects are 4–7 orders of magnitude too large** to *be*
   the 210 ppb shift (Model A ~6.9×10⁴× too large; Model B ~1.3×10⁷× too large),
   and neither is bar-even-h⁴ in origin. This **confirms** the anchor-shift
   framing: 210 ppb is not the leading block-selection effect.

## Consequence for `conj:s5-so3-fiber-action` / GAP-A-4

The keystone narrative's hoped reading — "reaching ℓ=2 unlocks the Borromean
h⁴ coefficient and that produces the muon shift" — is **refuted at the
multiplicity level**: the h⁴ channel is multiplicity-symmetric across the two
generations and cancels. Any genuine generation splitting from this functor
lives in the (1,1,1)↔(3) sign/trivial channels (h-independent) and is a
percent-level effect, not a fine bar-even correction.

What remains well-posed and *not yet* run: whether the **q-deformed Wenzl
projector weights** $w_\lambda(q)$ — as opposed to classical multiplicities —
break the (2,1) symmetry between the H₅ blocks. That requires the operator
$E_\lambda$ to act on the knot module with q-dependent (not just
multiplicity-counted) weight, the open structural input the resolution doc
still flags. This probe establishes the **baseline**: at the classical
multiplicity level the mechanism is null, so any non-null result must come
from the q-deformation of the projector weights, and must be argued bar-even
to be a candidate for a sub-ppm correction.
