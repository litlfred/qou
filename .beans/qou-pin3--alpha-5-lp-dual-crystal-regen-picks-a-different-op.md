---
# qou-pin3
title: 'alpha_5_lp_dual_crystal: regeneration picks a DIFFERENT optimal LP dual vertex — excluded from the tnjb batch'
status: completed
type: task
priority: normal
created_at: 2026-08-08T20:05:00Z
updated_at: 2026-08-08T20:05:00Z
---

Held out of the 2026-08-08 `tnjb` stale-stamp migration, deliberately, and
reverted after the value audit caught it.

## What happened

`alpha-5-lp-dual-crystal.witness.json` is stamped `muon` while its producer
resolves proton, so it was a legitimate tnjb candidate. But regenerating it here
changed **24 LP solution entries** that are not explained by the anchor:

```
data.at_q0_per_stratum.ht6.per_atom.2.lp.y_star.2    0.0 -> 0.020749613956537
data.at_q0_per_stratum.ht6.per_atom.1.lp.y_star.2    0.0 -> 0.000764070473307
data.at_q0_per_stratum.ht6.per_atom.0.lp.y_star.0    0.0 -> 0.000097401828163
...plus ~21 entries at 1e-13 .. 1e-17 (solver tolerance noise)
```

An ~11.5 ppb q₀ move cannot take a dual coordinate from exactly `0.0` to
`0.0207`. What it looks like is a **degenerate LP with multiple optimal dual
solutions**, where the solver landed on a different vertex.

## Why that is plausible here specifically

This producer was the one `REVERT-fail` in the first tnjb pass —
`ModuleNotFoundError: No module named 'pyhecke'`. It only became runnable after
`pyhecke` was put on the path and `clarabel` + a freshly built
`pyhecke-native 0.9.0` were installed in this container. So the committed
witness and my regeneration were produced by **different solver stacks**, and
the difference shows up exactly where a degenerate LP would show it.

## Why it was excluded rather than committed

AGENTS.md §"LP / SDP duals — first-class infra (do not skip)" treats these duals
as load-bearing, not incidental output. Folding a changed dual vertex into an
*anchor* migration would bury a substantive change inside a bookkeeping one —
and the `y_star` values are precisely the shadow prices downstream consumers
read.

Both the witness revert and the manifest entry were undone, so the file is back
to `UNDETERMINED` rather than sitting as a `DECL_MISMATCH`. `allPassed` did not
regress in the regenerated version — this is not a failure, it is an
*unexplained-by-the-stated-cause* change, which is a different and worse thing
to commit silently.

## Next step for whoever picks this up

1. Confirm the LP is degenerate at these strata (multiple optimal duals) — if
   so, the vertex choice is solver-dependent and the witness needs either a
   deterministic tie-break or a recorded solver fingerprint.
2. Decide whether `y_star` consumers depend on the specific vertex. If they do,
   a vertex change is a real downstream event and must not ride in on any sweep.
3. Only then re-run it for the anchor, with the dual change reported separately
   from the q₀ change.


## RESOLVED 2026-08-08 — MY DEGENERACY HYPOTHESIS WAS WRONG. It is CONDITIONING.

Owner asked for all three options (keep held out / regenerate / deterministic
tie-break). They turn out to answer each other, and the diagnosis above was
wrong in its mechanism — recorded because the correction is the useful part.

### There is no degeneracy, because there is a CLOSED FORM

`per_atom_lp` builds `G = diag(|weight_λ|)` — **diagonal**, since Wedderburn
blocks are τ-orthogonal. So the LP is just

    min t·x   s.t.   Σ x = n_target,   x ≥ 0

and stationarity `t = y0·1 + G y` determines the dual outright:

    y0* = min_λ t_λ ,      y_λ* = (t_λ − y0*) / |w_λ| .

No vertex to choose, no tie to break. `alpha5_lp_dual_degeneracy_probe.py`
(new) checks this against the witness: **0 records have a min-t tie** and the
second-smallest `t` sits 13.9 / 4.6 / 296 away from the smallest — nowhere near
a tie. My "multiple optimal duals" reading is refuted.

### What actually happened: 1/|w| ≈ 3e5 amplification

The committed dual satisfies the closed form **6/6**. The regenerated one
satisfies it **2/6**, off by up to 2.07e-02. So the regeneration was the WRONG
one — the committed witness was right and the "better" solver made it worse.

    COMMITTED  (HiGHS simplex)   duality gap 0.0      y0 − min(t) = 0.0
                                 y_star[2] = 0.0 exactly
    REGENERATED(clarabel MPFR IPM) duality gap 4.02e-12  y0 − min(t) = −7.229e-08
                                 y_star[2] = 2.074961e-02

and 7.229e-08 / min|w| = 7.229e-08 / 3.4837e-06 = **2.0750e-02** — the observed
number to five digits. The weights run at ~1e-6, so `y_star` is ill-conditioned
by `1/|w| ≈ 2.9e5`, and an interior-point method that stops at a 1e-12 gap lands
20,000x off in the dual. Simplex lands on the vertex exactly; IPM converges
toward it and stops. Both are correct LP solvers; only one gives an exact dual.

The bean was right that the solver stack changed and right to hold the file out.
It was wrong about why, and "degenerate LP" would have sent the next reader
looking for a tie that is not there.

### The fix: take the dual from the data, not from a solver

`alpha_5_lp_dual_crystal.per_atom_lp` now computes the dual in closed form and
keeps the solver's as a diagnostic — `y_star_solver`, `dual_solver_deviation_rel`,
`dual_conditioning`. A new assertion `lp_dual_matches_closed_form` (tol 1e-9)
fails loudly if any backend ever returns a dual the data does not support.

The recorded conditioning makes the whole story visible in the witness:

    record                        1/|w|      solver deviation
    ht6/per_atom/0                1.19e+05   9.74e-05
    ht6/per_atom/1                4.49e+05   7.64e-04
    ht6/per_atom/2                2.87e+05   2.07e-02
    two_row/per_atom/0            1.67e+01   3.57e-12
    two_row/per_atom/1            9.84e+01   9.09e-11
    two_row/per_atom/2            6.37e+01   1.90e-09

The well-conditioned `two_row` strata never had a problem; the damage tracks
`1/|w|` exactly, which is what a conditioning explanation predicts and a
degeneracy explanation does not.

### All three options, answered

1. **Keep held out** — was the right call, for a better reason than stated.
2. **Regenerate** — would have been WRONG on its own: it replaces an exact dual
   with one that violates stationarity by 2e-2.
3. **Deterministic tie-break** — not applicable (no tie), but its intent is met
   in a stronger form: the dual no longer depends on the solver at all.

With (3) in place, (2) becomes safe. Regenerated: worst `y_star` change vs the
committed witness is **4.19e-06**, down from 2.07e-02 — and that residual is the
genuine q₀-scale input movement (`|Δw|rel` up to 4.15e-06) magnified by the
recorded conditioning, not solver noise. `allPassed` True → True, 4 → 5
assertions.
