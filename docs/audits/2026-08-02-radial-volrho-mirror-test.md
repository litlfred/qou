# The `ρ = tr_M` radial binding-handle ansatz fails the T/³He mirror test (scope-a)

**Date:** 2026-08-02 · **Bean:** qou-0g4z (front 1 of the C_knot attack menu) · **Axis:** Δ_λ / binding
magnitude · **Discipline:** 0-fit, formalize-first, scope-(a); nothing wired.

## The compass

PR #4556 refuted a single-universal `C_knot` (deficit spread 2.83× across D/T/³He/⁴He); PR #4592 refuted
the angular (q-Reeb eigenphase) route — the eigenphases are compact/difference-only and cannot carry an
absolute scale. What survives is a **radial** hypothesis: the mass formula runs on
`m = m_e·Vol(K)·ρ(K)/ℏ_q²`, but the binding formula `B = m_e·|S(K)|` carries **no** geometric dressing,
so the deficit `C_knot = B_AME/(m_e·|S(K)|)` might BE the missing `Vol(K)·ρ(K)/ℏ_q²` factor.

## The decisive test (0-fit)

Tritium (³H = 1p2n) and ³He (2p1n) are **mirror nuclei** (p↔n). IF they are also mirror knots
(`Vol(T) = Vol(³He)`), the radial ansatz forces, with `ρ(K) = tr_M(K) = Σ_λ y_λ χ^λ` (the
paper-canonical per-block density, `mass_vol_density.density_per_block`):

```
C_knot(T)/C_knot(³He)  =  ρ(T)/ρ(³He)          (Vol and ℏ_q² cancel).
```

Both sides are derived numbers (`B_AME` enters only through the fixed `C_knot` from #4556). From the
committed χ witnesses (`computations/deltalambda/radial_volrho_mirror_test_probe.py`, exit 0):

| quantity | T | ³He | ratio T/³He |
|----------|---|-----|-------------|
| `C_knot` (#4556) | 4.444 | 3.292 | **1.35** (> 1, T more bound) |
| `ρ = tr_M(K)` | 0.104071 | 0.206578 | **0.50** (< 1, T smaller trace) |
| ratio-of-ratios | | | **2.68** (= 1 iff ansatz holds) |

## Verdict — refuted **in direction** (scope-a)

The two ratios lie on **opposite sides of unity**: `C_knot` says T is more bound (1.35) while `tr_M`
says T is smaller (0.50). `ρ = tr_M` is therefore **anti-correlated** with `C_knot` across the mirror
pair — a stronger failure than a magnitude miss. The `ρ = tr_M` radial ansatz (with `Vol(T)=Vol(³He)`)
is excluded.

**Honest scope.** This is **scope-(a)**: it refutes the *specific* ansatz `ρ = tr_M` under the
mirror-knot assumption. It does **not** exclude the radial handle in general. The survivors are:

1. **A density `ρ ≠ tr_M`.** The per-block Markov trace is not the only density reading
   (`density_borromean` is a global scalar; the reconciliation is the OPEN per-block-vs-global question,
   `mass_vol_density.compare_density_readings`). A different derived `ρ` whose T/³He ratio is `> 1` could
   still work — but it must be *derived*, not reverse-engineered from `C_knot` (that would be a fit).
2. **Genuinely distinct volumes `Vol(T) ≠ Vol(³He)`.** The two braids differ (`tr_M(T) ≠ tr_M(³He)`), so
   "mirror nuclei ⇒ mirror knots ⇒ equal Vol" is an **assumption**, not established. If the p↔n swap
   changes the knot's hyperbolic volume, `Vol` carries the asymmetry and this test does not apply. The
   clean next step is `Vol(T)`, `Vol(³He)` from SnapPy on the actual braid closures.

Nothing wired; no fit; `free_parameters = 0`; `B_AME` diagnostic-only.

## Machine-checked (Lean, sorry-free, lean-direct exit 0)

`content/quantum-observable-universe/lean/QOU/MassTheory/RadialVolRhoMirrorTest.lean`:

- `mirror_ratio_of_radial` — the ansatz forces `C_knot(T)/C_knot(³He) = ρ(T)/ρ(³He)` (Vol, ℏ_q² cancel;
  generic field).
- `cknot_ratio_gt_one` / `trM_ratio_lt_one` — the witnessed ratios straddle 1.
- `mirror_test_excludes_rho_trM` — the conjunction (radial ansatz + equal Vol + `ρ=tr_M`) implies
  `False`.
- `rho_trM_radial_ansatz_refuted` — capstone.

## Where front 1 goes next

Get `Vol(T)` and `Vol(³He)` explicitly (SnapPy, actual braid closures). Two outcomes:
`Vol(T)=Vol(³He)` ⇒ the radial handle needs a density other than `tr_M` (survivor 1); `Vol(T)≠Vol(³He)`
⇒ re-run the test with the true volumes. Either way the mirror pair is the sharpest discriminator, and
`ρ = tr_M` is now off the table.
