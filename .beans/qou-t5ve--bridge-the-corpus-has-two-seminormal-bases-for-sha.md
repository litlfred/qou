---
# qou-t5ve
title: 'Bridge: the corpus has TWO seminormal bases for shape (2,1) and nothing said so'
status: completed
type: task
priority: normal
created_at: 2026-09-04T06:26:14Z
updated_at: 2026-09-04T06:27:01Z
---

## What was found, and how

Chasing "formalise `trSummand` for general `n`" (the item left open by #6570),
the corpus-grep checklist path 6 (`.beans/`) turned up **`qou-u86i`,
completed**: `QOU/SchurWeyl/HoefsmitRep.lean`, landed 2026-08, already
carrying `S0`, `S1`, `S0_quadratic`, `S1_quadratic` and `S0_S1_braid`.

**So `rhoMixedSigma1` in `descartes-knot-eigenbasis.lean` is a duplicate of
`S0`** — the same matrix `diag(q, −q⁻¹)`, re-derived in #6570 a few hours
earlier. Recorded in `rhoMixedSigma1_eq_S0` so the duplication is visible in
the code, not only in a bean.

That is the second time in this arc the checklist caught the same class of
error (the first was reporting the general-`n` characters as "upstream and
open" when the Rust has computed them for months), and both times it was run
one step later than it should have been.

## The part that is NOT a duplicate, and matters more

`rhoMixedSigma2` is **not** `S1`. The two are different bases of the same
shape-`(2,1)` representation:

| | form | off-diagonals |
|---|---|---|
| `QOU.SchurWeyl.S1` (library) | **square-root-free**, not symmetric | `1` and `(q⁴+q²+1)/(q²+1)²` |
| `rhoMixedSigma2` (matches the compute) | **orthogonal**, symmetric | both `√(1+q²+q⁴)/(1+q²)` |

`pyhecke_native.seminormal_matrices_mpfr` — the path this corpus actually
runs, and the one `qou-4m9u` established is the *correct* family (the Python
`_build_ysn_matrices` fails the braid relation at 0.7315, the Rust satisfies
it at 2e-50) — returns the **orthogonal** form. The library Lean carries the
**square-root-free** one. Nothing in the corpus said they differ.

## The bridge

`rhoMixedSigma2_conj_S1`: conjugation by the diagonal gauge `diag(b, 1)`,

    ρ(σ₂) · diag(b,1) = diag(b,1) · S1

stated without inverses; `hoefsmitOffDiag_pos` gives `b > 0`, so the gauge is
invertible and this is a genuine similarity. Verified numerically at five `q`
to 1e-41 before the Lean was written.

## Why this is worth having

**A Lean statement proved about `S1` transfers to the numbers the Rust path
produces only through this conjugation.** Reading a `pyhecke_native` matrix as
though it were `S1` entry-by-entry is wrong; only basis-independent quantities
— trace, determinant, spectrum, the Hecke and braid relations — match
directly. That is a live hazard for anyone wiring the two together, which is
exactly what the general-`n` `trSummand` work would do.

## Still open

`trSummand` for general `n`. `HoefsmitRep.lean` has `cellContent`,
`axialDistance` and the `(2,1)`/`(2,2)` cases; it carries 21 sorries and does
not yet give the general-`n` seminormal construction. Not started here.
