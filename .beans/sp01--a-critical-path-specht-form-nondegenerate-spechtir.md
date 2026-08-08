---
# sp01
title: 'A [CRITICAL PATH]: specht_form_nondegenerate (SpechtIrreducible.lean:705) — char-0 Gram non-degeneracy'
status: completed
type: task
priority: low
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-08-08T09:58:42Z
parent: sp00
---

Needs char-0 Cauchy-Binet (det(A A^T)=Sum det(A_J)^2>0, Mathlib lacks usable rectangular CB) OR base-change of the radical to Q/R + positive-definiteness of the tabloid-orthonormal form. The slick <e_t,e_t>=|C_t| != 0 arg only gives 'not identically zero', strictly weaker. Gates specht_isSimple. HARD.

Parent: sp00.

## CLOSED 2026-08-08 — `specht_form_nondegenerate` is proved

`QOU/BraidKnot/SpechtIrreducible.lean`. `#print axioms` reports
`[propext, Classical.choice, Quot.sound]` — no `sorryAx` — for both

- `specht_form_nondegenerate` (every `[Field k] [CharZero k]`, `ℂ` included), and
- `specht_isSimple`, which reduces to it.

`SpechtIrreducible.lean` now carries **zero** `sorry` tactics, and is wired into
`QOU.lean` so `lake build` compiles it (it was deliberately excluded while it
carried the stub). Full package build green: 4355 jobs.

## The route — Cauchy–Binet, not base-change rank invariance

The plan recorded in this bean (and in the theorem's old docstring) was
"ℤ-Gram of standardBasis → corank base-invariant across char-0 fields →
conclude corank 0 from the ℝ positive-definite case". What landed is lighter
and avoids the standard basis entirely:

1. **Thin over ℚ.** `exists_linearIndepOn_extension` picks a *set of tableaux*
   `b` whose polytabloids are ℚ-independent and still cover the rest. Because
   that lemma is stated for `LinearIndepOn` over a `Set ι`, what comes back is
   a set of **tableaux**, not of vectors — so there is no vector-to-index step
   and, crucially, **no standard tableau anywhere**. No Garnir straightening,
   no dominance core, no `standardBasis`.
2. **Integrality.** A polytabloid is a signed sum of basis tabloids, so its
   coordinate matrix `Mz` is an integer matrix
   (`SpechtBaseChange.polytabloid_apply_eq_intCast`).
3. **`det (Mz Mzᵀ) ≠ 0` in `k`.** `RankMinor.exists_selector_det_ne_zero`
   (bean qou-ut3p) turns ℚ-independence of the rows into a nonzero maximal
   minor; `CauchyBinet.det_gram_map_ne_zero` (bean qou-8yph) turns that into
   the Gram determinant being nonzero in `k`. **This is the step that reaches
   ℂ**: Cauchy–Binet writes `det (Mz Mzᵀ) = Σ_f (det Mz_f)²`, a sum of squares
   of *integers*, so the positivity lives in ℤ and `k` is never ordered.
4. **Gram = coordinate matrix times its transpose**, because the tabloid basis
   is orthonormal for `bilinM` (`bilinM_apply`).
5. **Invertible Gram ⇒ trivial radical**
   (`GramNondegenerate.span_inf_orthogonalBilin_eq_bot`).

The sub-family spans over `k` and not only ℚ because the coordinates are
integers, so the ℚ-relations from step 1 survive base change
(`SpechtBaseChange.spechtSubmodule_eq_span_of_rat`).

Step (2) of the old plan — the ℝ positive-definiteness detour the owner
declined on 2026-07-25 — is not used, and neither is the rank-invariance
machinery step (iii) called for. The hypothesis stays `[Field k] [CharZero k]`.

## New modules (all sorry-free)

| Module | Role | Bean |
|---|---|---|
| `QOU.MathlibExt.CauchyBinet` | rectangular Cauchy–Binet + the ℤ→k Gram transfer | qou-8yph |
| `QOU.MathlibExt.RankMinor` | independent rows ⇒ nonzero maximal minor | qou-ut3p |
| `QOU.MathlibExt.GramNondegenerate` | invertible Gram ⇒ `W ⊓ Wᗮ = ⊥` | this bean |
| `QOU.BraidKnot.SpechtBaseChange` | polytabloid integrality; relations survive base change | this bean |

The first three are Mathlib gaps stated generically — none mentions Specht
modules, tabloids, or ℤ in its statement.

## `hμ` is not needed

The proof never uses `μ.card ≠ 0`. The binder is retained (renamed `_hμ`) so
the signature still matches `Specht.specht_isSimple`'s contract and the call
site in `specht_isSimple`.

## Correction to the record — the standard-basis cores were ALREADY closed

While checking what my proof avoided, I found that
`SpechtStandardBasis.standardBasis`, `standardPolytabloid_span` and
`specht_finrank_eq_numSYT` all report `[propext, Classical.choice, Quot.sound]`
today, and `grep -E '^\s+sorry\s*$'` finds **no** `sorry` tactic in
`SpechtStandardBasisCore`, `SpechtDominanceCore` or `SpechtTriangularCore`.

So this bean's "Current status (2026-08-05)" section, the "STUB" rows in
`SpechtStandardBasis.lean`'s table, and `SpechtFinrankWired.lean`'s
"only remaining sorry is the spanning / straightening stub" are all **stale**.
A dated warning has been added at the top of `SpechtStandardBasis.lean`'s
status table; the other docstrings still need the same treatment.

Independence from those cores remains a real robustness property of this
proof — it just is not a way around an open problem, because they are not open.

## What is still a stub, and why it is not a task

`Specht.specht_isSimple` (brick 2, `Specht.lean:332`) is still `sorry`. It is
**the same statement**, unprovable *there* only because the proof runs through
`bilinM` and James's submodule theorem, which live in `SpechtIrreducible`,
which imports `Specht`. Brick 2 cannot import its own consumer — the repo's
`…Wired` convention (cf. `SpechtFinrankWired`) exists for exactly this. Nothing
consumes the brick-2 copy. A pointer to the proved version has been added to
its docstring so it is not picked up as an open target again.
