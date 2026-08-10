# The division-ring collapse for `k[S_n]` — measured scope of residual item 1

**Date:** 2026-08-10
**Context:** follow-on to PR #4876 (`sn_wedderburnArtin_alg`), which listed four
residual items between Mathlib + corpus and
`SnWedderburnPartitionBridge.sn_isotypic_specht_split`, and named item 1 — the
division-ring collapse `𝔇 i ≃ R` — as "the substantive one".

This note records what item 1 actually costs. The headline is a **re-scoping,
not a closure and not a refutation**: the hard half of item 1 is already owned
by the corpus, sorry-free, and more general than the residual list implies.

## 1. What Mathlib supplies (measured over all 6990 modules)

Earlier claims in this arc were measured over an *import closure* (the
37-module cone of `SnWedderburnPartitionBridge`, 406,384 constants; and a
86-module representation-theory closure, 369,328 constants). An import closure
cannot witness absence in Mathlib as a whole. The check below is over **every**
Mathlib module present in the workspace (6990 `.olean` files), by scanning the
compiled name tables directly:

| name | modules containing it | reading |
|---|---|---|
| `Specht` | **0** | no Specht module theory upstream |
| `AbsolutelyIrreducible` | **0** | no absolute-irreducibility predicate |
| `SchurIndex` | **0** | no Schur index |
| `numSYT` | **0** | no standard-tableau count |
| `IsCentralSimple` | 1 — `Mathlib.Algebra.Central.Defs` | definitions only |
| `YoungDiagram` | 2 — `Mathlib.Combinatorics.Young.{YoungDiagram,SemistandardTableau}` | combinatorics only, no representation theory |

So PR #4876's "0 hits for `Specht`" **stands at full-Mathlib scope**, which is
stronger than the scope it was originally asserted at. Two corrections to the
narrower probes: `IsCentralSimple` *does* exist upstream (it was absent only
from the chosen import set), and Mathlib *does* carry `YoungDiagram` — the
corpus already builds on it.

## 2. What the corpus already owns

The residual list reads as though item 1 were the theorem "ℚ is a splitting
field for `S_n`", to be built from nothing. It is not. The corpus already
carries the hard half:

- [`SpechtIrreducible.specht_isSimple`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtIrreducible.lean)
  — `#print axioms` reports `[propext, Classical.choice, Quot.sound]`, so it is
  genuinely sorry-free, and its statement is quantified over an **arbitrary**
  characteristic-zero field:

  ```
  ∀ {k : Type} [Field k] [CharZero k] (μ : YoungDiagram),
    ∀ N ≤ Specht.SpechtSubmodule μ, (stable under the S_n action) →
      N = ⊥ ∨ N = Specht.SpechtSubmodule μ
  ```

  Simplicity over *every* char-0 field — not merely over ℚ or ℂ — is precisely
  the content that an absolute-irreducibility argument needs, and it is already
  discharged.

- [`SpechtBaseChange`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtBaseChange.lean)
  — sorry-free; the Specht data is defined over ℤ functorially (a ring hom acts
  coefficient-wise and carries `polytabloid` to `polytabloid`), and a spanning
  relation established over ℚ transfers along `ℚ →+* k`.

## 3. The reduction, and what is genuinely left

Item 1 reduces to absolute simplicity of `S^μ`, i.e. `End_{k[S_n]}(S^μ) ≃ k`,
by the standard argument: if `S^μ ⊗_k K` stays simple for `K` an algebraic
closure, then `End ⊗_k K ≅ End_K(S^μ ⊗ K) = K` by Schur, so `dim_k End = 1`.
`specht_isSimple` supplies the "stays simple" input at `K` directly, since it
holds for every char-0 field.

What is **not** yet available, and is the true remaining content of item 1:

1. **The tensor comparison** `S^μ_k ⊗_k K ≅ S^μ_K` as `K[S_n]`-modules.
   `SpechtBaseChange` gives coefficient-wise maps and span transfer, not this
   isomorphism.
2. **Bijectivity of the End base-change map.** Mathlib has
   `Module.End.baseChangeHom` and `Module.endTensorEndAlgHom` as *algebra homs
   only*; no bijectivity lemma for finite-dimensional modules was found. That
   lemma is the load-bearing step and would have to be supplied.
3. **The linkage from Wedderburn's existential to the simples.** The `𝔇 i` of
   `sn_wedderburnArtin_alg` come from an existential with no handle tying block
   `i` to a particular simple module; proving `𝔇 i ≃ R` requires knowing
   `𝔇 i ≃ End(S_i)ᵒᵖ`.

Point 3 matters for how the residual list should be read. Items 1 and 3 (the
size identification `𝔫 i = dim_R S^{λ_i}`) are **not independent of item 2**
(the reindexing `Fin N ≃ PartitionIndex n`): all three need the same
block-to-simple correspondence. Treating them as four separable items
understates the coupling and overstates how much of the work item 1 carries on
its own.

## 4. Status

Item 1 is **open**, and the four-path corpus-grep checklist was run before
saying so (`docs/audits/`, `content/`, `computations/`, `docs/coordination/`).
Nothing here refutes any route; per the scope discipline this is a
**scope-limited re-scoping** of an open item — the estimate of its cost moves
down, and the estimate of its independence from item 2 moves down with it.

An alternative route worth weighing before starting: rather than extracting
`𝔇 i` from Mathlib's existential and collapsing it, construct
`k[S_n] ≃ₐ[k] ∏_λ Matrix (d_λ) k` directly from the Specht modules. That
formulation never introduces the opaque `𝔇 i`, so it sidesteps point 3 entirely
and folds items 1–3 into one construction.
