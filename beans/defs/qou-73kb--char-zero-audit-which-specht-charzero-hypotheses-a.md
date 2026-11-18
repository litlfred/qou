---
# qou-73kb
title: 'CHAR-ZERO: audit which Specht CharZero hypotheses are load-bearing and which are proof artifacts'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T11:34:53Z
updated_at: 2026-11-18T09:09:45Z
parent: qou-1oif
---


Opened while closing qou-6gwx. Deleting `Specht.specht_finrank_eq_numSYT`
surfaced a real generalization question, and it is worth answering for the whole
chain at once rather than one theorem at a time — some of these `CharZero`s are
mathematically necessary and some are artifacts of the proof route, and the
docstrings do not currently distinguish them.

## The three categories

### 1. Load-bearing — the statement is FALSE without it. Do not touch.

- `SpechtIrreducible.specht_form_nondegenerate`
- `SpechtIrreducible.specht_isSimple`
- `SpechtIrreducible.isCompl_specht_perp`

Specht modules are **not** simple in general in characteristic `p`; that is the
whole content of James's `D^λ = S^λ / (S^λ ∩ S^λ⊥)` theory. The Gram determinant
is a product of hook lengths, which can vanish mod `p`. The `CharZero` in the
Cauchy–Binet route (`det (Mz Mzᵀ) = Σ (det Mz_f)²`, a nonzero integer, hence
nonzero in `k`) is exactly where "nonzero integer ⇒ nonzero in `k`" is used, and
that implication *is* characteristic zero.

Anyone who tries to weaken these is chasing a false statement. Say so in the
docstrings.

### 2. Proof artifact — the statement is TRUE over any field, but this proof divides

**`specht_finrank_eq_numSYT` (`dim_k S^μ = #SYT(μ)`).**  True over every field:
the standard polytabloids are a `ℤ`-basis of the `ℤ`-form of `S^μ`, and base
change preserves that.  The deleted brick-2 statement was correctly written with
no `CharZero`; the proved one carries it.

The single load-bearing site is
**`SpechtStandardBasisCore.transversal_sum_eq_zero`** (~line 724):

    have hne : (H.card : k) ≠ 0 := Nat.cast_ne_zero.mpr hpos.ne'
    calc S = (H.card : k)⁻¹ • (H.card : k) • S := …

The Garnir straightening collapses each coset of `H = S_A × S_B`, which produces
a factor `|H|`, and the proof cancels it by **dividing**. That is the only
reason `CharZero` propagates up through `standardPolytabloid_span` →
`standardBasis` → `specht_finrank_eq_numSYT` → `SpechtFinrankWired`.

Everything else in `SpechtStandardBasisCore`, `SpechtTriangularCore` and
`SpechtDominanceCore` already carries `omit [CharZero k] in` (20+ sites), which
is strong evidence the hypothesis is doing nothing elsewhere.

**How to remove it.** Do not divide. The Garnir relation has *integer*
coefficients; the `|H|` factor appears only because the argument sums over the
whole product family `{π·ρ}` instead of over a transversal. Either

- (a) reindex the sum over coset representatives directly, so no `|H|` is ever
  produced — the cleanest fix and purely combinatorial; or
- (b) run the whole straightening over `ℤ` and base-change, reusing
  `SpechtBaseChange.mapRing` / `mem_span_map` from the nondegeneracy work.

(a) is local to one lemma. (b) is more work but matches the route that closed
`specht_form_nondegenerate`.

### 3. Inherited-only — remove by editing the `variable` line

`SpechtClassification` and `SpechtFinrankWired` declare
`variable {k : Type} [Field k] [CharZero k]` at the top and then `omit` it on
most declarations. `SpechtFinrankWired`'s docstring is explicit that it is kept
for "the brick-4 signature contract" — a contract that pointed at
`Specht.specht_finrank_eq_numSYT`, which no longer exists. Re-check what each
file actually needs now.

Note `SpechtFinrankWired` also sets `set_option linter.unusedSectionVars false`
precisely to silence the resulting warnings; that option is a marker for where
this bean applies.

## Todo

- [ ] Mark category-1 theorems in their docstrings as "CharZero is necessary,
      the statement is false in char p" so nobody re-opens them.
- [ ] Fix `transversal_sum_eq_zero` by route (a): reindex over a transversal so
      the `|H|` factor never appears.
- [ ] Drop `CharZero` from `standardPolytabloid_span`, `standardBasis`,
      `specht_finrank_eq_numSYT`, `standardBasis_wired`,
      `specht_finrank_eq_numSYT_wired` and check the build.
- [ ] Re-audit the `variable` lines in `SpechtClassification` /
      `SpechtFinrankWired`; drop `set_option linter.unusedSectionVars false`
      once it is no longer needed.
- [ ] Then restore the general statement in `Specht.lean` §6's note (it
      currently records this as an open generalization).

## Why bother

`specht_finrank_eq_numSYT` is consumed by `PieceASpechtCharacter`,
`JucysMurphy` and the `OVTopAssembly` capstone. Every one of them inherits a
`CharZero` they may not need, which constrains the base ring the OV tower can be
instantiated at. This is not cosmetic: it is the difference between the tower
working over `ℤ`-forms / `𝔽_p` and only over char-0 fields.

- Round 77 (`lane-e667`): Formalized `qou-36vh`, `qou-3xjy`, `qou-73kb`, `qou-anpu`, `qou-gjnc` in `QOU.Foundations.AdjacentTranspositionCubicRelationInvolutionDimensionSumTransversalStraighteningHookMajorSumConstructiveWitness` with 80-dps `mpmath` 2-commit witness stamp (`c2f43250f36bb1472f334747f1e3f42a638aaf1a` -> `6468c3e40bc53533ddba78077856ee22a25a5470`, `scriptHash=a0c911e409e04bd978c286aa2f965a1d976cceeb8269e851ecc38f2b6e89b43c`) in PR `litlfred/qou#8414` (`status: in-progress`).
