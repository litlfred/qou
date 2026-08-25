---
# qou-pin3
title: 'alpha_5_lp_dual_crystal: regeneration picks a DIFFERENT optimal LP dual vertex — excluded from the tnjb batch'
status: completed
type: task
priority: normal
created_at: 2026-08-08T20:05:00Z
updated_at: 2026-08-21T16:21:57Z
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

---

## RESOLVED 2026-08-16 — not degenerate; the duals are ill-conditioned

`computations/alpha_5_lp_dual_crystal_closed_form.py` (stdlib only, reads the
committed witness). Step 1 above is answered, and the answer is no.

### The LP is an argmin

`alpha_5_lp_dual_crystal.py` line 203 builds `G = diag(|weight_λ|)`, and its
own comment notes `|weight_λ| > 0` for non-trivial channels — confirmed, min
`|w|` = 2.2e-06 across all strata, nothing zero. `solve_operator_selection_lp`
(lp_dual_solver.py:358, the **inequality** variant, not
`solve_frobenius_dual_lp`) then solves `min t·x s.t. 1·x = n_target, Gx ≥ 0`.
With `G` diagonal and positive, `Gx ≥ 0` is `x ≥ 0`, so:

```
x*   = n_target · e_argmin(t)
y_0* = min_j t_j                       UNIQUE
s*_j = (t_j − min_j t_j) / |w_j|       UNIQUE
obj  = n_target · min_j t_j
```

Verified against **every field of every stratum** of the committed witness:
`y0_star`, `x_star`, `y_star`, `primal_obj`, six strata, all agree.

So the dual optimum is a **point, not a face**. There is no vertex to choose,
and "the solver landed on a different vertex" is ruled out. Nor could an
11.5 ppb q₀ move flip the argmin: the two cheapest channels differ by 44–52 %
relative in every stratum, not by parts per billion.

### What actually changed

`s*_j` divides by `|w_j|`, and in `ht6` that is ~2e-06 … 8e-06 — an
amplification of **1e+05 to 4.5e+05**. Read the three reported entries
backwards through the closed form:

| entry | new value | implied &#124;y₀* − min t&#124; | relative |
|---|---|---|---|
| 3He ht6 `y_star[2]` | 0.020749613956537 | 7.23e-08 | 2.7e-09 |
| T ht6 `y_star[2]` | 0.000764070473307 | 3.66e-09 | 1.4e-10 |
| D ht6 `y_star[0]` | 0.000097401828163 | 8.20e-10 | 1.7e-09 |

All three are the **argmin** index — the channel whose true `s*` is exactly 0.
A vertex change would have moved *which* index is zero and produced O(1)
relative motion elsewhere; the note above records the rest at 1e-13..1e-17,
which is the same effect on channels with larger `|w|`.

So the two runs agree on `y₀*` to ~1e-09 relative. That is solver tolerance,
and this bean already records that the runs used different solver stacks
(scipy HiGHS f64 vs the freshly built clarabel MPFR). Nothing substantive
changed.

### Revised next steps

1. ~~Confirm the LP is degenerate~~ — done, it is not.
2. Step 2 as written ("do `y_star` consumers depend on the specific vertex")
   is the wrong question, since the vertex is unique. The right one: **does
   any consumer read `y_star` in the `ht6` strata at all?** Those coordinates
   cannot be pinned better than ~1e-02 by any f64 solver, because they are a
   1e-06 division applied to a tolerance-level residual.
3. If they are consumed, publish the residual `t_j − y₀*` beside the quotient
   so the conditioning is visible rather than hidden inside it. A
   deterministic tie-break would fix nothing — there is no tie.
4. The anchor migration this was held out of can proceed on its own terms; the
   dual "change" is not a substantive event to report separately.

### Not the same as `qou/8na1`

`8na1` is a *genuine* radical, in the `H₃` Frobenius trace form, forcing
`y₀ = 0` exactly. This one has no radical and a unique nonzero `y₀*`. I
initially flagged them as plausibly the same and that was wrong; they share
only the word "degenerate".

## Summary of Changes

Answered step 1 — **the LP is not degenerate** — and refuted the "different
optimal dual vertex" reading with a closed form verified against every field of
every stratum of the committed witness. `G = diag(|weight_λ|)` with no zero
weight makes `Gx ≥ 0` into `x ≥ 0`, so the program is an argmin:
`x* = n_target·e_argmin(t)`, `y₀* = min_j t_j`, `s*_j = (t_j − min t)/|w_j|`,
all unique. There is no vertex to choose.

The real cause is conditioning: `s*` divides by `|w_j| ~ 1e-06` in the `ht6`
strata, amplifying error in `y₀*` by 1e+05–4.5e+05. All three reported entries
are the argmin index — the channel whose true `s*` is exactly 0 — and imply a
`y₀*` difference of 8.2e-10 to 7.2e-08 absolute, ~1e-09 relative. That is
solver tolerance between the two stacks this bean already identified (scipy
HiGHS f64 vs clarabel MPFR). Nothing substantive changed in the witness.

Checker: `computations/alpha_5_lp_dual_crystal_closed_form.py`, stdlib only,
reads the committed witness. Landed in #5251.

Revised guidance for the anchor migration: the dual "change" is not a
substantive event and needs no separate report. A deterministic tie-break would
fix nothing — there is no tie. The open question is narrower than this bean
framed it: **does any consumer read `y_star` in the `ht6` strata at all?** Those
coordinates cannot be pinned better than ~1e-02 by any f64 solver.
