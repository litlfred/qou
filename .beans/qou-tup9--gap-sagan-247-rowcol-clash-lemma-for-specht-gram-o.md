---
# qou-tup9
title: 'GAP: Sagan 2.4.7 row/col clash lemma for specht_gram_orthogonal'
status: completed
type: task
created_at: 2026-08-05T02:22:18Z
updated_at: 2026-08-05T03:00:00Z
---

## What is open

`QOU.BraidKnot.SpechtIrreducible.specht_gram_orthogonal` (line 795):
> For distinct SYT `S ≠ T`: `bilinM μ (standardPolytabloid S) (standardPolytabloid T) = 0`.

Requires Sagan Lemma 2.4.7 (row/column disagreement for distinct SYT):
> If `S ≠ T` are standard Young tableaux of the same shape `μ`, then there exist
> entries `a, b` such that `a` and `b` are in the same **row** of `S` and the same
> **column** of `T`.

This gives a transposition `τ = (a b)` with `τ ∈ C_T ∩ R_S` (stabilizer clash),
which conjugates the `C_T` sum by τ to negate every term without changing the
tabloid set, yielding the cancellation `bilinM ... = -bilinM ...`, hence = 0.

## What's needed

1. Prove Sagan 2.4.7 as a standalone lemma in the codebase (or in a new `SpechtOrthogonality.lean`).
2. Use it in `specht_gram_orthogonal` to complete the proof.

## Why it matters

`specht_gram_orthogonal` is the last sorry in `SpechtIrreducible.lean`.
Closing it would make `specht_form_nondegenerate` sorry-free, which in turn
makes `specht_isSimple` sorry-free — completing the Specht irreducibility chain
(excluding the RSK / hook-length upstream gaps in `StandardYoungTableau.lean` etc).

