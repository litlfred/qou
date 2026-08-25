---
# qou-h4ab
title: 'wedderburn-lp-ew-wiring is stale on main: t_legacy_matrix_entries moves ~13% on re-run'
status: completed
type: task
priority: normal
created_at: 2026-08-17T01:44:20Z
updated_at: 2026-08-23T18:06:46Z
---

## Evidence (PR #5260)

Re-running `wedderburn_lp_ew_wiring.py` on current main moves:

    t_legacy_matrix_entries_min/max  0.6003377241833765 -> 0.6803696974650493
    (a second pair moves from 0.3727036271108378)

~13 %. **Verified pre-existing**, not caused by the y_λ layer fix on #5260: the
same move reproduces with this branch's changes stashed. A 13 % shift is ~7
orders too large to be the 1.85e-9 straddle, so it is a different cause.

Not diagnosed. Candidates worth checking first: the committed witness predates a
convention change (the field is named `t_legacy_*`, which suggests a legacy
trace convention that may have been re-defined), or an upstream input it reads
was regenerated without this consumer being re-run.

The witness asserts 3 assertions, all passing, in both the old and new state —
so this is a silent value drift, not a failing check.


---

## DIAGNOSED — and the obvious fix is the wrong one (owner: "no f64 path")

**Cause of the ~13% move:** the 2026-08-15 owner ruling made convention D
canonical, and `pyhecke.gram.z` moved `1/(√q+1/√q)` -> `q³/(q²+1)`
(0.4993203 -> 0.6126880, +22.70%). `wedderburn_pair_volumes` puts `z` directly
in its `std` channel (`std = z·(M_i M_j)_12 + (M_i M_j)_22`), and `full` is the
weighted sum of sym/std/alt. The committed witness is dated **2026-06-22**, two
months before the ruling, so it is convention-C output.

The two observed ratios sit exactly where that predicts — between 1 (channels
without z) and 1.227 (the z ratio):

    0.6003377 -> 0.6803697   ratio 1.1333
    0.3727036 -> 0.4493842   ratio 1.2057

So the value drift is fully explained and the new numbers are the canonical
convention-D ones.

**I regenerated it, and then reverted that.** Owner correction: *"no f64 path."*
`wedderburn_lp_ew_wiring.py` is float64 end-to-end — `Q_50_DIGIT_STR` is
`float()`-ed at lines 133/204/346, matrices are `dtype=np.float64`, `t` and `G`
are numpy f64 — and the witness sits in `raw-float64-baseline.json` at **62
fields**. Regenerating refreshes 62 float64 values *through* the float64
pipeline: it makes the staleness go away while entrenching the debt the
NO-FLOAT64 discipline exists to drain. Staleness was the symptom; the f64
pipeline is the defect.

**What I fixed instead, because it is the prerequisite.** The f64-free path was
itself returning **convention C** — `z_mp` 18.5% off the f64 `z`, and
`gram_matrix_mp` disagreeing with `G` by 3.36e-01 against a docstring promising
~1e-15. `lp_dual_solver.solve_..._mpfr` consumes
`gram_matrix_mp_strings()` / `tr_m_mp_strings()` for precisely this boundary,
so *any* migration off f64 would have landed on wrong numbers. Fixed to D with
lockstep regression tests; now 8.4e-17 and 1.7e-16.

**Why the mirror drifted unnoticed:** `test_gram_values.py` pinned the f64 `z`
to D — `test_z_value` even asserts it is not the C value — and never touched
`z_mp`, `tr_m_mp` or `gram_matrix_mp`. Guarding the original and leaving the
high-precision twin unguarded is the hole; the new tests close it.

**Remaining, filed separately:** migrating this producer off f64. The pieces
exist (`solve_..._mpfr` at `lp_dual_solver.py:292`, now-correct mp Gram/trace
strings) but it needs the `clarabel-operator-selection-lp` MPFR binary, which
is not built here, and that path is labelled EXPERIMENTAL and "NOT yet
cross-checked against the scipy backend to 1e-25". Not a drop-in, and not
something to land inside this PR.


## 2026-08-19 — DIAGNOSED: it is the convention C -> D migration, not drift

The `t_legacy_matrix_entries` move (proton 0.6003377 -> 0.6803697, +13.3%;
neutron 0.3727036 -> 0.4493842, +20.6%) is **not unexplained value drift**.
`wedderburn_pair_volumes.py:179` reads

    z_mark = q0**3 / (q0**2 + 1)          # convention D

which is the canonical Markov parameter under the owner ruling of
2026-08-15. The committed witness predates that migration and is
**convention-C-frame** throughout.

`full = w_sym*sym + w_std*(z_mark*mij_12 + mij_22) + w_alt*alt` is AFFINE in
`z_mark`, so the frame is testable by swapping that one line. Re-evaluating
the same function with `z_C = sqrt(q0)/(q0+1) = 0.499320` instead of
`z_D = 0.612688`:

| atom | committed | conv D | conv C |
|---|---|---|---|
| proton | 0.6003377241833765 | 0.68036969746 (rel 0.1333) | 0.60033772418337637 (**rel 2.1e-16**) |
| neutron | 0.3727036271108378 | 0.44938418327 (rel 0.2057) | 0.37270362711083759 (**rel 5.7e-16**) |

Convention C reproduces the committed numbers to machine zero. That is the
whole explanation; nothing else moved.

Two things follow:

1. **The differing per-atom ratios (1.133 vs 1.206) were the clue, not a
   puzzle.** A q0 re-pin would scale everything by the same 11.5 ppb; a
   convention change enters affinely through `V_std_pair` alone, whose
   `mij_12` coefficient differs per atom. The earlier note that this is "~7
   orders too large to be the y_lambda straddle" was right to exclude that
   cause and had no candidate to replace it.
2. **Regenerating this witness is a C -> D frame migration, and must be
   labelled as one.** It is the same class as the Q_beta `c_k` ladder
   (bean `qou-cds1`), which AGENTS.md flags as C-conditional pending
   re-derivation. The regenerated values are not "corrections" to the old
   ones — both are correct in their own frame.

Not claimed: whether every *downstream* consumer of this witness is
D-ready. Only this producer's frame was established.
