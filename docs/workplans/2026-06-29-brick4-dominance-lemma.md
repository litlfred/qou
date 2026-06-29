# Brick-4 dominance lemma — discharge `dominance_relation_exists`

**Branch:** `claude/ov-brick4-cores-2026-06-29` · **Started:** 2026-06-29

## Context

PR #3091 (merged, `8a02b4c`) reduced the brick-4 standard-basis *independence*
half (`dim S^μ = #SYT`) to a **single** relation-level core:

> `QOU.BraidKnot.SpechtDominanceCore.dominance_relation_exists (μ) : Nonempty (DominanceData μ)`

`DominanceData` bundles a partial order `dom` on `Tabloid μ`
(reflexive/transitive/antisymmetric) under which **column permutations weakly
decrease** the tabloid (`dom_colStab : π ∈ C_t ⟹ dom {π•t} {t}`). Everything else
in the independence chain — the two order-independent `Triangular` fields, the
`LinearOrder` construction (a reusable Szpilrajn-for-Fintypes lever), the support
plumbing — is already sorry-free.

## This tranche

Turn `dominance_relation_exists` from an **opaque** stub into a **concrete
construction** reduced to exactly Sagan's dominance lemma:

1. Define the dominance order concretely via partial sums of the row-pattern:
   `S d i m = #{ l | l < m ∧ tabloidRowPattern d l ≤ i }`, `dom a b :≡ ∀ i m, S a i m ≤ S b i m`.
2. Prove `dom_refl`, `dom_trans` (pointwise `≤`) and `dom_antisymm` (`S` determines
   `tabloidRowPattern`, then `tabloidRowPattern_injective`) **sorry-free**.
3. Isolate `dom_colStab` (column permutations weakly decrease dominance) as the
   single cited core `dominance_colStab_lemma` (`[sagan2001]` Thm 2.5.2 / §2.4).

Net: the brick-4 independence debt becomes one precisely-stated combinatorial
lemma — column permutations and the dominance order — rather than an opaque
`Nonempty (DominanceData)`.

## Status

- [ ] Construct `dom` + prove refl/trans/antisymm sorry-free (probe in flight).
- [ ] Isolate `dom_colStab` as the single cited core.
- [ ] Integrate into `SpechtDominanceCore.lean`, verify `lean`-direct, merge.

## Remaining brick-4 / OV cores (future tranches)

- `standardPolytabloid_straightening` — the Garnir spanning core (brick 4, *spanning* half).
- B1 irreducibility: `specht_submodule_dichotomy` (James §8), `specht_form_nondegenerate` (char-0 Gram).
