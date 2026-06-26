---
# t886
title: 'q-Bessel tower gate: build H6/H9 chi_lambda(B_n - B_p) via canonical A-nucleon braid lift (T2/T3 trace-invariance frontier)'
status: todo
type: task
created_at: 2026-06-26T14:55:05Z
updated_at: 2026-06-26T14:55:05Z
---

## Goal (2026-06-26, PR #2849)

The live frontier attack on the T2/T3 trace-invariance / brane-tower problem is
the Jacobi–Anger **tower-convergence gate** (`2026-06-19`): does the bar-odd
residual of `χ_λ(𝓑_n − 𝓑_p)` shrink along `n = 3 → 6 → 9` toward the
Hahn–Exton q-Bessel matrix coefficients (`sinh((2m+1)η)` coeff `= 2·J_{2m+1}(x)`
at a single substrate-fixed `x`)? At `n=3` the physical-weight residual is 6.8%
on Lean-proved closed forms; the decisive gate is whether it shrinks at `n=6,9`.

## Blocker (the actual work)

The corpus has explicit proton/neutron braids **only at H₃**. The `H6/H9`
difference objects require a **first-principles braid construction** — the
canonical A-nucleon embedding committed *a priori* (no scan-to-fit):

> `β_p^{(A)} = atom_canonical_crossings(A, 0, include_inter=False)`,
> `β_n^{(A)} = atom_canonical_crossings(0, A, include_inter=False)`,
> level `n = 3A`; object `χ_λ(β_n^{(A)} − β_p^{(A)})`, `λ ⊢ n`.

This is the same canonical word-builder lift to `A>1` that `2026-06-19`
§"deferred item-A" names. Per the formalize-first discipline the embedding must
be fixed before any residual is seen.

## Task

1. Lift the canonical word-builder to `A=2,3` (verify it reproduces the
   Lean-proved H₃ closed forms at `A=1`, intra-only).
2. Compute `χ_λ(β_n^{(A)} − β_p^{(A)})` at `n=6,9` (exact Hoefsmit engine).
3. Run the single-`x` over-determination residual; report shrink/no-shrink.
4. If it shrinks → gates the `lim spectrum = q-Bessel zeros` master-theorem Lean.
   If not → record the structural negative (scope (a), not (b)).

## Refs

- `docs/audits/2026-06-19-bn-bp-brane-tower-parity-obstruction.md`
- `docs/audits/2026-06-17-jacobi-anger-physical-weight-n3.md` §"decisive tower test"
- `docs/audits/2026-06-26-t2t3-trace-invariance-status-synthesis.md` §"Item 4"
- Producer pattern: `computations/probes/bn_minus_bp_brane_tower_parity_probe.py`
