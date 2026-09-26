---
# qou-0xyc
title: 'GAP: specht_form_nondegenerate (SpechtIrreducible.lean:823) — specht_gram_orthogonal (Sagan 2.4.7) needed'
status: completed
type: task
priority: normal
created_at: 2026-08-05T01:54:57Z
updated_at: 2026-08-08T09:58:41Z
---

## Current status (2026-08-05)

- `specht_gram_diag` (diagonal Gram entry = |C_T|): **PROVED** (sorry-free candidate,
  hand-audit; LSP not available in sandbox). Lines 716–790.
- `specht_gram_orthogonal` (off-diagonal = 0): **one honest sorry** (Sagan 2.4.7 gap).
  Tracked separately in bean `qou-tup9`.
- `specht_form_nondegenerate` (full Gram argument): **fully written** (lines 823–892),
  depends on both gram lemmas. Once `specht_gram_orthogonal` is proved, the whole
  chain becomes sorry-free.

## What is open

`QOU.BraidKnot.SpechtIrreducible.specht_form_nondegenerate` at line 823:
> For `[Field k][CharZero k]` and `μ : YoungDiagram` with `μ.card ≠ 0`,
> `SpechtSubmodule μ ⊓ spechtPerp μ = ⊥`.

## What was attempted

- (1) ℝ shortcut (positive-definiteness over ℝ): DECLINED by owner 2026-07-25 —
  would weaken generic `[Field k][CharZero k]` to ℝ only.
- (2) [UNBLOCKED] Integer Gram matrix of `standardBasis` → corank base-invariant
  across char-0 fields → conclude corank 0 from the ℝ positive-definite case.
  `SpechtStandardBasis.standardBasis` is NOW SORRY-FREE on main (Garnir
  straightening + dominance core both closed).

## Surviving route

Take the ℤ Gram matrix of `standardBasis`, show its rank/corank is
base-invariant across char-0 fields (flatness / universal coefficients), then
conclude corank 0 by specializing to ℝ where `bilinM x x = Σ xd² > 0`.

Needs: a stable-olean session so `SpechtStandardBasis` + `SpechtIrreducible`
dep-cone builds without triggering from-source Mathlib rebuild (~30–60 min).
Use `lake-cache/qou-v4-24-0` restore recipe per `lean-environment-setup.md`.

## Why it matters

`specht_form_nondegenerate` is the sole sorry in `specht_isSimple` (the
body of `specht_isSimple` is already sorry-free, just calls this theorem).
Closing this would make the entire Specht-irreducibility chain sorry-free
(excluding RSK/YoungTableauStandard/JucysMurphy which need upstream Mathlib ports).

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
