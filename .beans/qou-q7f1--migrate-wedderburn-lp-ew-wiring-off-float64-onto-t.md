---
# qou-q7f1
title: Migrate wedderburn_lp_ew_wiring off float64 onto the MPFR LP path (62 baselined f64 fields)
status: in-progress
type: task
priority: normal
created_at: 2026-08-18T16:24:41Z
updated_at: 2026-08-19T11:54:27Z
---

## Scope (PR #5260, owner directive "no f64 path")

`wedderburn_lp_ew_wiring.py` runs float64 end-to-end and its witness carries
**62 raw float64 fields**, tolerated by an entry in
`raw-float64-baseline.json`. Baselines drain, never grow — this is the drain.

f64 sites in the producer:

    133, 204, 346   q0_value = float(sympy.Float(Q_50_DIGIT_STR, 50))
    45-82           _hoefsmit_f64_matrices -> np.array(..., dtype=np.float64)
    135, 202        t = np.zeros(..., dtype=float);  G = np.zeros(..., dtype=float)
    141, 224        float(np.trace(M_ij))
    250             np.array(..., dtype=np.complex128)
    273             q_0_float = float(q_0)

The 50-dps substrate constant is truncated to f64 on entry, so everything after
it is f64 regardless of what the LP solver can do.

**The pieces now exist, but it is not a drop-in.**

  * `pyhecke.lp_dual_solver.solve_..._mpfr` (line 292) solves at ≈50 dps and
    takes decimal strings, so the boundary adds no truncation.
  * `gram.gram_matrix_mp_strings()` / `tr_m_mp_strings()` feed exactly that
    boundary — and were returning **convention C** until PR #5260 fixed them
    (bean qou-h4ab). Any earlier attempt at this migration would have moved
    onto wrong numbers, 18.5 % off.

**Blockers, measured:**

  1. `solve_..._mpfr` needs the `clarabel-operator-selection-lp` CLI or a
     `pyhecke_native` wheel built `--features clarabel-lp`. Neither is present
     in this sandbox (no prebuilt binary; `cargo` is available, so it is
     buildable).
  2. Its own docstring: "EXPERIMENTAL ... NOT yet cross-checked against the
     scipy backend to 1e-25 — that needs a scipy+numpy environment. The scipy
     backend therefore remains the default." So the cross-check is itself a
     prerequisite deliverable, not an afterthought.
  3. `gram_matrix_mp` is the 6x6 H_3 NF Gram. This producer builds an
     n_pairs x n_pairs Gram over **pair amplitudes at H_{3A}** — a different
     object, so the mp Gram is not a substitute for `_full_wedderburn_gram`.
     An mpmath Hoefsmit builder is needed too (`hoefsmit_matrices_numeric`
     exists and is used at mp precision by `rho_k_h3a_refinement`).

**Expected outcome.** Not a value change of the kind that moves a conclusion —
f64 vs 50-dps on a well-conditioned Gram is ~1e-16 — unless the LP is
ill-conditioned, in which case the dual could move materially and that is worth
knowing. The witness's own `t_legacy` values differ from the KLR-positive `t`
by design, so do not read a `t` change as a precision result.

Do the cross-check (blocker 2) first: without it, a migrated result has nothing
to be validated against.


---

## Blocker 1 CLEARED; blocker 2 was mis-stated by me (2026-08-18)

**Blocker 1 — the MPFR binary — is gone.**

    cargo build --release --features clarabel-mpfr \
                --bin clarabel-operator-selection-lp     # 53.4 s, exit 0

System GMP/MPFR were already present, so `rug` compiled without setup. It was
never built here, not unbuildable. This also un-blocks bean qou-cp1w's demo —
same binary.

**Blocker 2 — "cross-check to 1e-25" — is NOT achievable as written, and I
should not have recorded it as a prerequisite deliverable without reading the
rest of the file.** Two docstrings in `lp_dual_solver.py` disagree:

  * line 302 (`solve_..._mpfr`): "NOT yet cross-checked against the scipy
    backend to 1e-25"
  * line 380 (`solve_operator_selection_lp`): "cross-checked equivalent to
    scipy to ~1e-12 (clarabel_lp_crosscheck.py)"

Both are true, and the first is unreachable **in principle**: the reference is
scipy/HiGHS in **float64**, whose own answer is good to ~1e-16 relative at
best. Agreement to 1e-25 against an f64 oracle is not a meaningful target —
you cannot validate 50 dps against 16. So "do the cross-check first" was
advice toward an impossible goal.

Ran the existing check now that there is something to check against:

    13/13 cases agree; worst relative objective 2.00e-12; worst duality gap
    5.8e-13. "All cases agree ... safe to consider as default."

**What the real validation of a 50-dps solve looks like** (replacing my earlier
recommendation): a KKT/residual check computed AT 50 dps from the returned
`*_str` values — primal feasibility, dual feasibility, complementary slackness
— which needs no f64 oracle. The binary returns `x_star_str`, `y_star_str`,
`y0_star_str`, `primal_obj_str`, `dual_obj_str` at full precision, so the
inputs for that check are already in hand. Not done here.

**Blocker 3 stands unchanged**: `gram_matrix_mp` is the 6x6 H_3 NF Gram, while
this producer needs an n_pairs x n_pairs Gram over pair amplitudes at H_{3A}.
An mpmath Hoefsmit builder is still required — `_hoefsmit_f64_matrices` has no
mp twin. That is the actual bulk of this bean and none of it is done.


---

## Blocker 2 RESOLVED — replaced, not satisfied (2026-08-19)

The stated goal ("cross-check against scipy to 1e-25") is unachievable, so it
was replaced with a check that answers the same question without an oracle:
`computations/lp_dual_kkt_residual_50dps.py`.

KKT verified against the problem data at 50 dps — primal equality, primal
inequality, bounds, dual sign, dual feasibility, strong duality, complementary
slackness — with every input entering as a decimal string and every operation
under `mp.workdps(50)`. No float64 at any point, and no second solver.

    r_eq     |sum x - n_target|      5.26e-24     <- headline
    r_Gx     min (Gx)_i              3.81e-16  ok (>= 0)
    r_y      min y_i                 9.77e-20  ok (>= 0)
    r_dual / scale                   2.43e-25
    r_gap  / scale                   1.44e-21
    r_cs   / scale                   1.69e-20

**`r_eq` at 5.26e-24 is 8 orders below anything f64 can exhibit.** That is the
substantive result: the MPFR path delivers real sub-f64 accuracy, and no
comparison against an f64 oracle could ever have demonstrated it. This is what
the 1e-25 note was reaching for and could not get from scipy.

**Two yardstick corrections to my own check, both forced by the measurement:**

1. The first cut used a flat 1e-40 and printed "KKT NOT satisfied" — a
   statement about the tolerance, not the solve. `|x| ~ 2.65e5` here, so the
   objective is a near-total cancellation; an absolute residual on it is not
   comparable with one on `sum x - n_target`, whose terms are O(1). The three
   cancelling rows are now scale-relative.
2. The assertions still carried the discarded 1e-40 after the verdict moved on,
   so the witness read "7 assertions, FAILURES" beside a printed "KKT
   SATISFIED". An artifact contradicting its own conclusion is worse than
   either verdict; the assertions now use the verdict's criterion, and the
   one-sided rows assert only the violating direction.

**NOT claimed:** that the solve is accurate to 50 dps. Its *convergence*
tolerance (`dual_tol` 1e-9), not its arithmetic precision, governs how far the
residuals fall. 1e-18 relative was picked to sit below f64 resolution and above
what that convergence can be expected to give — passing it is a real claim, but
a bounded one.

**Blockers 1 and 2 are now done. Blocker 3 is untouched and is the bulk of this
bean:** `gram_matrix_mp` is the 6x6 H_3 NF Gram; `wedderburn_lp_ew_wiring`
needs an n_pairs x n_pairs Gram over pair amplitudes at H_{3A}, and
`_hoefsmit_f64_matrices` still has no mpmath twin. Writing that builder is the
next real step, and the KKT check above is now available to validate whatever
it produces.


---

## Blocker 3: the mp Hoefsmit builder ALREADY EXISTS on main (2026-08-19)

`computations/hoefsmit_mpmath.py` landed in PR #5264 ("NO FLOAT64 in probes"),
merged to main 2026-08-19. Its rationale is verbatim the blocker recorded here:

> the numpy fast path is float64 **by construction** — `BlockCache` computes its
> block values with `math.sqrt` against a 1e-15 degeneracy threshold, and the
> character routine returns `float(np.trace(...))`. Handing those functions a
> 50-dps `mpf` for `q` does not make them exact; numpy coerces on contact.

API: `BlockCacheMP`, `seminormal_matrices_mp(shape, cache=)` -> mp.matrix
sigmas, `chi_lambda_of_word_mp(sigmas, dim, word, n_gens_required)` -> mpf.

**I checked before writing rather than after.** Had I started from this bean's
text I would have re-implemented it. Merged main into the branch (275 commits)
to pick it up.

**Remaining for this bean, now genuinely the last piece:** port
`_hoefsmit_f64_matrices`, `_klr_positive_supply_vector` and
`_full_wedderburn_gram` in `wedderburn_lp_ew_wiring.py` onto those three
functions, and drop the `float(sympy.Float(Q_50_DIGIT_STR, 50))` truncations at
lines 133/204/346. The validation for whatever that produces already exists —
`lp_dual_kkt_residual_50dps.py`, oracle-free at 50 dps.

## Sibling convergence: PR #5265 fixed the same gram.py sites

#5265 ("Convention-D tranche ... pyhecke.gram was straddling C and D
internally") independently made the SAME three C->D corrections I did — `z_mp`,
`tr_m_mp`, and `gram_matrix_mp`'s inline `z_`. Posted on their PR citing it and
proposing they land first, since their branch is scoped to convention D and
mine is not; I drop the duplicate source change on rebase.

Additive from this branch: their PR touches **no test files**, and the three
lockstep regression tests are what close the hole the bug came through —
`test_gram_values.py` pinned the f64 `z` to D (and asserts it is not C) while
nothing pinned the mirror. Offered them the tests directly.
