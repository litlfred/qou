# Beyond hooks: two-row CHARACTERS reduce to the 2-dim sl₂, but the GERM does not (qou-o6ov)

**Date:** 2026-09-03
**Directive (owner):** does a similar exterior-power/determinant handle reach beyond hooks (two-row shapes)?
**Scope:** scope-(a); two negatives + one exact positive; no MeV, no fit, nothing wired.
**Probes:** [`magnus_two_row_reduction_probe.py`](../../computations/deltalambda/magnus_two_row_reduction_probe.py),
[`magnus_two_row_rmatrix_probe.py`](../../computations/deltalambda/magnus_two_row_rmatrix_probe.py)
**Follows:** #6430 (the hook column reduces to the reduced Burau, all orders).

## The question

#6430 reduced the **hook** column of the tr-decay to the `(n−1)`-dim reduced Burau `ρ^V`,
because hooks `(k,1ⁿ⁻ᵏ) = Λⁿ⁻ᵏ(V)` are irreducible Schur functors of the reflection rep. Does
an analogous small-object handle reach **two-row** shapes `(n−k,k)`?

## Finding 1 — two-rows do NOT reduce to `ρ^V` (the determinant handle is hook-specific)

Test: `tr_{(n−k,k)}(ρ) =?= q^{twist}·s_{(n−k,k)}(eig ρ^V)`, Jacobi–Trudi
`s_{(n−k,k)} = h_{n−k}h_k − h_{n−k+1}h_{k−1}`. **Fails** — the ratio is wild and irregular
(`~1e-4` at A=2, `~1e-13` at A=3), because `S^{(n−k,k)}(V)` is **reducible** over `S_n` (it is
not the single irrep `(n−k,k)`). The exterior-power/determinant reduction is **special to
single-column Schur functors** (hooks); it does not extend to two-rows.

## Finding 2 — two-row CHARACTERS reduce EXACTLY to the 2-dim sl₂ R-matrix

The Schur–Weyl-natural home for two-row characters is the 2-dim `U_q(sl₂)` fundamental: the braid
group acts on `(ℂ²)^⊗n` via the R-matrix, and
`(ℂ²)^⊗n = ⊕_{k} (sl₂ irrep, dim n−2k+1) ⊗ (Hecke two-row (n−k,k))`, so
`tr_{(ℂ²)^⊗n}(g) = Σ_k (n−2k+1)·tr_{(n−k,k)}(g)`. Verified **exact** (A=2, exact mpf):
```
Σ_k (n−2k+1)·tr_{(n−k,k)}(ρ) = 134.902131743 = tr_{(ℂ²)^⊗6}(ρ),   |Δ_rel| = 9e-140.
```
So the two-row **plain characters** collapse exactly onto the 2-dim (n-independent) R-matrix
building block — the correct "beyond hooks" home for the *characters*.

## Finding 3 — but the GERM Ω₂ is realization-dependent (the decay object does NOT reduce)

The same weighted sum with the germ inserted **fails** by 6.5%:
```
Σ_k (n−2k+1)·tr_{(n−k,k)}(ρΩ₂) = −331.806   vs   tr_{(ℂ²)^⊗6}(ρΩ₂) = −353.274,   |Δ_rel| = 0.065.
```
The plain character matches to 140 digits but the germ-inserted trace is off — so the mismatch
is **not** a convention/framing error; it is intrinsic. The reason: the germ
`A_i = q·∂_q σ_i · σ_i⁻¹` is a **log-derivative of the representation matrix**, i.e.
**representation-specific**, not an abstract Hecke-algebra element. Two realizations of the same
irrep `(n−k,k)` — the seminormal one and the R-matrix isotypic one — are related by a
**q-dependent intertwiner** `P(q)`, and `A_i^{R} = q∂P·P⁻¹ + P A_i^{sem} P⁻¹ + …` differs from
`P A_i^{sem} P⁻¹` by the `∂P` terms. So the R-matrix germ ≠ the seminormal germ, and the 2-dim
reduction carries the *character* but not the *decay object*.

## Why hooks worked and this is the boundary

This pins down exactly why #6430 was the breakthrough and why it stops at hooks: the
exterior-power functor `Λʲ(V)` is **germ-natural** — built from the seminormal reflection rep
with a **q-independent** structure, so its induced-derivation germ equals the seminormal hook
germ (matched to 1e-91 in #6430). The Schur–Weyl R-matrix realization is **not** germ-natural
(q-dependent intertwiner), so it fails to carry the germ. A germ-aware two-row handle would need
a construction built from the seminormal `V` in a q-independent way (e.g. the projection onto
the `(n−k,k)` constituent of a Schur functor `S^{(n−k,k)}(V)` with the induced germ) — the plain
Schur functor `s_{(n−k,k)}(eig ρ^V)` over-counts because it traces the whole reducible
`S^{(n−k,k)}(V)`, not the `(n−k,k)` piece.

## Honest limits

- **A=2 exact** (plain 1e-140, germ 6.5% off); A=3 tensor trace (2⁹=512-dim) is a compute cost,
  not run — but the germ-realization-dependence is a **structural** argument, general in `n`.
- **Two negatives + one positive-but-insufficient.** The determinant handle is hook-only; the
  2-dim R-matrix reaches two-row characters but not the germ. The two-row slice of the *decay*
  stays open.

## Bottom line

The reduced-Burau/exterior-power reduction is **hook-specific**. Two-row **characters** reduce
exactly to the 2-dim `U_q(sl₂)` R-matrix (Schur–Weyl, verified to 140 digits), but the germ
`Ω₂` — the log-derivative that defines the decay object — is **representation-dependent**, so
the 2-dim reduction does **not** carry it (6.5% off, not a convention error). The breakthrough
of #6430 was germ-*naturality* of the exterior-power functor; that naturality is what fails for
two-rows. A germ-natural two-row construction (projected Schur functor of the seminormal `V`) is
the next candidate; the two-row slice of the decay remains open.
