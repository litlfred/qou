# H₂O build via the assembly projector — workplan

**Branch:** `claude/h2o-molecular-braid-2026-06-08`
**Date:** 2026-06-08
**Status:** WIP — PR opened first (branch+PR policy). Builds on three
PRs merged earlier today (#1999 metallic-q proof + phase-symmetry model;
#2002 optical-fibre section; #2009 metallic lemmas) and on `main`'s new
molecular-assembly-projector infrastructure.

## Key realization (corpus-grep / formalize-first)

`main`'s new [`def:molecular-assembly-projector`](../../content/quantum-observable-universe/molecular-construction/molecular-assembly-projector.md)
— the idempotent `e_{λ,μ} ∈ H_N(q)` (q-Young / Wenzl projector projecting
the composite's parabolic module onto Wedderburn block μ) — **is the
molecular-scale realization of the merged phase-symmetry-from-knot-operator
model** ([`docs/audits/2026-06-08-phase-symmetry-from-knot-operators-model.md`](../audits/2026-06-08-phase-symmetry-from-knot-operators-model.md)):

> the assembly projector **is** the "knot operator that forms the
> structure," and **its stabilizer (the permutations of constituent
> sub-units leaving `e_{λ,μ}` invariant) is the structure's symmetry.**

Benzene: `e_{(2,2,2),(6)}`, stabilizer `S₃` permuting the acetylene units
→ the ring's cyclic symmetry. So H₂O must be built the same way.

## H₂O construction (the build)

- **Constituents:** oxygen `O(8,8) ∈ H₂₄(q)` (A+Z = 16+8 = 24 strands),
  valence 2 + **2 lone pairs**; two hydrogens `H_k ∈ H₂(q)`.
  Total `N = 28`, molecular braid in `H₂₈(q)`.
- **Strand partition** `λ` groups O's bonding strands with each H pair;
  the **assembly projector** `e_{λ,μ}` projects onto the block `μ` that
  realises the two O–H σ-bonds (2 shared electron trefoils, Hopf-linked
  O↔H).
- **C₂ᵥ symmetry = stabilizer of `e_{λ,μ}`** under the `S₂` swapping
  H₁↔H₂ — the H₂O analogue of benzene's `S₃` (this is the
  phase-symmetry-from-knot-operator claim at molecular scale).
- **Bent geometry:** the 2 lone pairs are **phantom sites** (the NH₃→H₂O
  extension of [`ch4-tetrahedral-symmetry`](../../content/quantum-observable-universe/molecular-construction/ch4-tetrahedral-symmetry.md)):
  Td → C₂ᵥ, bond angle pushed from 109.5° toward the observed **104.5°**.
- **The four ice-relevant directions:** 2 donor H + 2 acceptor lone pairs
  = 4 ≈-tetrahedral H-bond directions per H₂O — the input to the ice Ih
  (hexagonal P6₃/mmc) lattice in the phase-symmetry model.

## Blocks to author

1. `def:h2o-molecular-braid` (+`.lean`) — H₂O via `e_{λ,μ}` on `H₂₈(q)`,
   in molecular-construction §"Water". `.lean`: the strand partition +
   assembly-projector instance for H₂O (reuse `molecular-strand-partition`
   + `molecular-assembly-projector` decls from main).
2. `rem:h2o-c2v-from-projector-stabilizer` — C₂ᵥ = Stab(`e_{λ,μ}`) under
   H₁↔H₂; interprets `def:h2o-molecular-braid` + cites the
   phase-symmetry model.
3. `rem:h2o-bent-geometry` — 104.5° from 2 lone-pair phantom sites.
4. (frontier, may split to follow-up) `ex:ice-Ih-from-h2o` — the 4
   H-bond directions tile into hexagonal Ih; Pauling 2-of-4 residual
   entropy.

## Discipline
- Build at **q₀** (owner decision). Numerical claims tiered.
- Reuse main's `molecular-assembly-projector` / `parabolic-hecke-subalgebra`
  / `molecular-strand-partition` decls — do **not** re-derive.
- `.lean` verified via the cache + direct-`lean` recipe (lean-cache ledger).
- Coordinate: the molecular-construction chapter has active sibling work
  (#2003 CO active-set); flag conflicts on `co-*` blocks.
