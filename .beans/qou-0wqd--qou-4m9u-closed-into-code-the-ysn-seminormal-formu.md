---
# qou-0wqd
title: 'qou-4m9u closed into code: the YSN seminormal formula, and what it moves downstream'
status: in-progress
type: task
priority: high
created_at: 2026-09-05T05:54:36Z
updated_at: 2026-09-05T05:55:35Z
---


## What landed (PR #6708, commit a1f8dbc)

`_build_ysn_matrices` computed the seminormal diagonal entry at axial distance
`rho` as `h / q_int(rho)`. That satisfies the Hecke QUADRATIC relation (trace
`h`, det -1, eigenvalues {q, -1/q}) and VIOLATES the BRAID relation, so the
family was not a representation of `H_n(q)` -- constant defect 0.7315 on 7 of 7
partitions (`docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md`).

Correct entry, the standard Hoefsmit/Young seminormal form:

    a_rho = h / (1 - q^(-2 rho))

## How it was IDENTIFIED (not guessed, not fitted)

Against `pyhecke_native.seminormal_matrices_mpfr` -- the Rust MPFR family the
2026-08-31 audit measures satisfying quadratic + braid + commuting at 2e-50 --
compared as a MULTISET of each generator's diagonal entries, so a differing
tableau order between the two implementations can yield neither a false match
nor a false mismatch:

    a_rho = h/(1 - q^(-2 rho))    37/37 generators, 9 partitions, worst 4.79e-51
    a_rho = h/q_int(rho)          11/37

The 11 that main gets right are exactly the generators with NO mixing block
(same-row / same-column, diagonal `q` or `-1/q`), where the formula is never
reached. **Main was wrong at every generator that used it.**

Two independent corroborations that this is the intended object:
  * at `rho = -2` it is `-1/(q(q^2+1))`, the value `qou-4m9u` derived
    SYMBOLICALLY by imposing braid + det = -1 and solving (3 solutions: one
    degenerate/reducible, two differing only by a basis sign);
  * at `rho = +2` it is `q^3/(q^2+1) = z_D`, the canonical convention-D Markov
    parameter of the 2026-08-15 owner ruling.

The error was NOT small -- main's value is 14-32 % of the correct one:

    rho    correct        main           ratio
     -4   -0.16029993   -0.05087018      0.317
     -2   -0.40362774   -0.10396371      0.258
     +2   +0.61268804   +0.10396371      0.170   (correct = z_D)
     +4   +0.36936023   +0.05087018      0.138

`bsq = a_rho*a_neg + 1` untouched -- it is exactly the det = -1 condition and
was already right, which is why `b` was correct GIVEN `a`, and why the defect
was constant across partitions.

## Verified

`computations/audits/ysn_braid_relation_audit.py` exits 0 (it exits 1 on main).
Braid 0.7315 -> 7.5e-17 (float64 eps) on every partition; quadratic and
commuting unchanged.

## Still open

1. **Precision.** The family is still built in float64 (`math.sqrt`, `1.0`
   literals, no `mp.dps`), so it agrees with Rust only to ~1e-16. The audit's
   corrected ordering is representation-first, precision-third; this is step 1.
2. **Downstream re-measurement (step 2) -- IN FLIGHT, and the scoping question
   is not yet answered.** Whether the Python family is even on the executed
   path when `pyhecke_native` is present is UNMEASURED as of this writing.
   Yesterday's instrumentation (bean `qou-w2vy`) established that
   `atom_character_raw` is served by the Rust kernel for 8/8 partitions across
   the whole dimension range, so `binding_from_frobenius_pairing` may be
   unaffected; `unified_iterative_correction` has the same
   `_lp_kernel_steps`-first shape and may be too. If both are kernel-served,
   the Python family is live only in a container WITHOUT `pyhecke_native` --
   which per AGENTS.md is the DEFAULT, since it cannot be pip-installed.
   **Do not assume either way: instrument.** Inferring the executed path from
   wall-clock time was yesterday's recorded error.
