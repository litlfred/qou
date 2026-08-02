# Charm mass: derive-then-check of the complex-mass tower_law (negative)

**Date:** 2026-08-02
**Scope:** `conj:complex-mass-constituent-functional` (QOU.MassTheory.ComplexMassConstituent), PR #4584.
**Trigger:** author request to attempt (1) the operator-selection SDP for gg→cc̄ and (2) the complex-mass functional closure.

## What was attempted

The two open steps to actually produce a charm mass from the complex-mass scaffold:

1. **Operator-selection SDP** for the gg→cc̄ channel — which knot-operator the two-gluon demand profile selects.
2. **Close the mass functional** — evaluate `charm_block_determined`: `M(proj 5 s) = contRatio(5)·M(proj 3 s)`, with `contRatio` the plain Morgan–Voyce / Fibonacci continuant ratio `b_n/b_{n-2}`, and compare `Re(block)` to the observed charm/light hierarchy.

## Step 1 — blocked (two independent gaps)

- **No solver in-environment.** numpy / sympy / cvxpy are absent in the sandbox Python; `solve_psd_operator_selection_sdp` cannot run here.
- **No derived demand profile (the real gap).** The two-gluon demand vector for gg→cc̄ is **not derived anywhere in the corpus**. Constructing it is itself open research; inventing one to feed the SDP would be a fit. So step 1 is blocked at the framework level, not just the tooling level.

## Step 2 — clean scope-(a) negative

`computations/charm_mass_tower_probe.py` (pure Python), witness `charm-mass-tower.witness.json`:

| quantity | value |
|---|---|
| substrate argument `X = [2]_q = q₀ + 1/q₀` | 2.011 |
| `contRatio(5)` at substrate | **5.85** |
| `contRatio(7)` at substrate | 5.87 (≈ contRatio(5) → nearly geometric ladder) |
| observed `m_c/m_u` (current) | 577 → needs `X ≈ 24` |
| observed `m_c/m_d` (current) | 270 → needs `X ≈ 16` |
| observed constituent `m_c/m_light` | 4.46 → needs `X ≈ 1.65` |

**Verdict (scope-(a)):** the plain-continuant-ratio reading of `contRatio` is **refuted as the sole hierarchy mechanism**. At the substrate it gives a nearly *n-independent* ~5.85×-per-generation **geometric ladder**, which matches **neither** mass scheme: it undershoots the current-mass charm/light hierarchy by ~100× (would need `X≈24`, wildly off the substrate `X≈2`), and overshoots the constituent-mass ratio by ~30%. The observed quark hierarchy is not a constant continuant ratio.

**This is scope-(a), not (b).** It refutes `contRatio = b_n/b_{n-2}` as the *whole* story; it does **not** exclude the complex-mass functional. The missing steepness could live in the complex-volume / Chern-Simons **imaginary** part (untested here — no solver, and the composite charmed-hadron braid's complex volume is underived), or `contRatio` could be a non-continuant categorical object. Both are open.

## Consequence for the scaffold (PR #4584)

The Lean class stands (it does not assert `contRatio = b_n/b_{n-2}`; that identification is narrative). But the natural first guess for `contRatio` is now **empirically excluded** at the substrate, sharpening the open closure: a viable `contRatio` must be either steeper-than-continuant (current scheme) or carried by the Im/CS part. No charm mass is predicted; `m_c` remains OPEN.

## Beans (env has no beans CLI — recorded here)

- **GAP (charm-mass step 1):** derive the two-gluon demand profile for gg→cc̄ in the skein-operator basis `{γ,σ₀,σ₁,L₊,L₋,e⁻}`, then run `solve_psd_operator_selection_sdp` to test whether it selects the `n=5` channel.
- **GAP (charm-mass step 2):** the continuant-ratio `contRatio` is scope-(a) refuted; test the complex-volume/CS (Im) contribution to the hierarchy once a composite charmed-hadron braid + its complex volume are available.
