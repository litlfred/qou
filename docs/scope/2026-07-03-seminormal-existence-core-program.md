# Scope — discharging `seminormalVector_data_exists` (the last brick-5 chain core)

**Status:** scoping + route recommendation (2026-07-03). No construction attempted here.

**Context.** After PRs [#3229](https://github.com/litlfred/qou/pull/3229) and
[#3236](https://github.com/litlfred/qou/pull/3236) (both merged), the entire OV
independence/completeness chain in
[`QOU/BraidKnot/JucysMurphy.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/JucysMurphy.lean)
— `jucysMurphy_eigenvalue`, `exists_indep_seminormal_family`, `seminormalVectors_span`, and the
punchline `centralC2_acts_by_contentSqSum` — rests on **one** cited `sorry`:

> `seminormalVector_data_exists` : for every standard tableau `T` of shape `μ` there is a nonzero
> `v ∈ S^λ ≤ M^λ` with `ρ(X_s) v = cellContent(T's cell of s) • v` for every `s`
> (`[Field k] [CharZero k]`).

The proved surroundings that any route may reuse: L1
(`linearIndependent_of_joint_eigenvectors` — joint eigenvectors with distinct tuples are
independent), L2 (`syt_content_tuple_injective` — the content tuple determines the SYT, via the
diagonal row-count formula), `jucysMurphy_commute`, the brick-4 standard-basis/dominance
machinery (`SpechtStandardBasis`, `SpechtDominanceCore`, `SpechtTriangularCore`,
`specht_finrank_eq_numSYT_wired`), and the `n ≤ 12` Plancherel instances.

## Why the "cheap" generic route does NOT shrink the debt

A commuting family on a nonzero finite-dimensional space over an algebraically closed (or
splitting) field has *some* simultaneous eigenvector (restrict-to-eigenspace induction — a
provable generic lemma). But the core demands the eigenvector for **every** `T` with the
**prescribed** content tuple. Getting from "some tuple" to "every SYT tuple, each realized" is
exactly the OV *simple-spectrum + spectrum-classification* theorem: a joint eigenspace could a
priori be fat, and a tuple could be missed, without the branching/triangularity input. So a
generic-existence de-abstraction leaves the cited debt essentially unchanged — **not** a
productive slice (recorded so the next session does not re-derive this dead end).

## Route A — Young's seminormal representation matrices (explicit)

Define the seminormal action on the free module with SYT basis (explicit `s_i`-matrices with
axial-distance coefficients), verify the Coxeter presentation, then intertwine with the concrete
`S^λ ⊆ M^λ`.

- **Cost:** the braid-relation verification for the seminormal matrices is famously heavy, and
  the statement demands `v` *inside* `Specht.SpechtSubmodule`, so a nontrivial intertwiner
  (uniqueness/irreducibility input) is unavoidable on top.
- **Verdict:** not recommended — most of the work (the presentation check) does not touch the
  Specht model the core is stated against.

## Route B — Gelfand–Zetlin / branching induction (the OV road)

Build `S^λ|_{S_{n−1}} ≅ ⊕_{corners c} S^{λ−c}` (James's branching rule) and descend: `v_T` is the
image of `v_{T|n−1}` under the corner inclusion; `X_n`'s eigenvalue on the `c`-component is
`content(c)`.

- **Needs (none of which exist in the repo):** the `S_{n−1} ↪ S_n` compatible action on
  `Mtab`/Specht, corner-removal Specht maps, the dominance filtration of the restriction and its
  char-0 splitting, and the `X_n`-eigenvalue on each component. Estimate: 4–5 PR-sized bricks
  (B1 restriction functor, B2 corner maps, B3 branching splitting, B4 `X_n` action, B5 induction
  assembly).
- **Upside:** the infra is exactly what the capstone's *labelled decomposition*
  (`sn_isotypic_specht_split`, `dim = #SYT` naming, the `PlancherelSnData` labelling residual)
  also needs — it is the long-road investment.
- **Verdict:** the canonical multi-PR program; right if the goal is the full labelling, oversized
  if the goal is only this core.

## Route C — Murphy's triangularity (RECOMMENDED)

Murphy (1981/1992): on the standard-polytabloid basis `{e_T}` of `S^λ`, each JM element acts
**upper-triangularly with respect to dominance order**, with diagonal entry the content:

>  (M)  `X_k · e_T = cellContent(T's cell of k) • e_T + (combination of e_S for S ⊳ T)`.

Given (M), the eigenvector is produced *without any new representation theory* by triangular
correction: process tableaux along a linear extension of dominance; for maximal `T`, `e_T` is
already an eigenvector; inductively, apply the commuting operators `(X_k − c_S(k))` scaled by
`1/(c_T(k) − c_S(k))` (denominators nonzero in char 0 **because distinct standard tableaux have
distinct content tuples — the already-proved L2**) to strip the dominating components of `e_T`.

- **(C1) Generic lemma (provable in-sandbox, the L3 of this program):** a finite commuting family
  acting triangularly on a filtered/flagged finite-dimensional space with prescribed diagonal
  tuples, the tuples pairwise distinct, admits for each index a simultaneous eigenvector with
  that tuple, congruent to the basis vector modulo the higher flag. Pure linear algebra in the
  L1/L2 style; no Specht content.
- **(C2) The concrete core (the new, strictly smaller citation):** Murphy's triangularity (M) on
  the polytabloid basis. Finite combinatorial algebra **directly in the Specht model** — and the
  repo already carries the closest neighbours: brick-4's dominance machinery
  (`standardPolytabloid_dominance_order`, `SpechtDominanceCore`, `SpechtTriangularCore` from the
  #3091/#3110 line) proves dominance-triangularity statements for the *basis*; (M) is the same
  genre one level up (the JM *action* against that basis). Ref: G.E. Murphy, *J. Algebra* 69
  (1981) 287–297 and 152 (1992) 492–513.
- **(C3) Assembly:** `seminormalVector_data_exists` from C1 + C2 + L2, in the established
  de-abstraction pattern (assembly sorry-free; cited debt = C2 only).
- **Verdict:** **recommended.** It reuses the proved L2 as the non-degeneracy input, its generic
  half is in-sandbox provable, and its cited residue (M) is a concrete statement about
  polytabloids adjacent to machinery already on `main` — plausibly closable in one or two focused
  sessions, and independently valuable (Murphy's basis is the standard modern route to the
  labelled decomposition, so C2 feeds Route B's goals too).

## Recommended next steps (in order)

1. **C1**: state + prove the generic triangular-diagonalization lemma (session-sized).
2. **C3 skeleton**: replace the `seminormalVector_data_exists` `sorry` with the assembly, citing
   only (M) — the same shrink pattern as L1/L2.
3. **C2**: attack (M) with the brick-4 dominance tools; if it stalls, it remains the honest named
   core, strictly smaller than what it replaced.
