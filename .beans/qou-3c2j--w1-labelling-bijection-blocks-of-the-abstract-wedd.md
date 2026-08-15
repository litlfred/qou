---
# qou-3c2j
title: 'W1: labelling bijection — blocks of the abstract Wedderburn split <-> PartitionIndex n (uses specht_isSimple + specht_exhausts_irreducibles + spechtIso_imp_dom_both, all now closed)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T14:41:43Z
updated_at: 2026-08-15T20:59:57Z
---


## Entry note (2026-08-15, after W2 closed in PR #5139)

W2 supplies what W1 needs on the division-ring side: `simple_end_scalar` says
the commutant of *every* simple `k[S_n]`-module is `k`, so a block's `𝔇 i` is
already known to be the base field once the block is identified with a simple.

W1 is the identification itself. Available now, all sorry-free:

- `SpechtClassification.specht_exhausts_irreducibles` — every simple is a Specht
  module (surjectivity of the labelling);
- `spechtIso_imp_dom_both` + `partitionDom` antisymmetry — distinct partitions
  give non-isomorphic Specht modules (injectivity);
- `card_partitionIndex` / `card_irreducibles_eq_card_partitions` — the counts
  match;
- `WedderburnSn.sn_wedderburnArtin_alg` — the abstract split with `Fin N` blocks.

So the content is: build `Fin N ≃ PartitionIndex n` from the abstract split's
block set. The blocks of `∏ᵢ Matrix(𝔫ᵢ)(𝔇ᵢ)` correspond to the simple modules
(the simple right ideals), and the two maps above are inverse. The friction to
expect is *not* mathematical — it is getting from Mathlib's existentially-bound
`N`/`𝔫`/`𝔇` to a statement about simple modules, since the equivalence is
`Nonempty`-wrapped and carries no named simples.

### Correction to my own entry note, same session — measured, not assumed

I wrote above that W1 is "build `Fin N ≃ PartitionIndex n` from the abstract
split's block set". Having now read the actual signature, that framing is wrong
and would waste the next session.

`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing` binds **`n`, `D`, `d`
and the equivalence all existentially**, and its statement mentions no simple
module at all. There is no handle on which block is which — nothing to reindex.
Any `Fin N ≃ PartitionIndex n` extracted from it would be a choice with no
stated relation to `S^μ`, which is exactly the over-generality trap
`SnWedderburnPartitionBridge` already documents (`sn_block_dim_eq_specht` is
false as a ∀-over-splits claim).

**So W1/W3 should build the split directly, not reindex Mathlib's.** The target
map is the action map `k[S_n] → ∏_{μ} Module.End k (S^μ)`; it is partition-indexed
by construction, so the labelling is not a separate step. Then:

- each factor becomes `Matrix (Fin dᵢ) (Fin dᵢ) k` via `LinearMap.toMatrix` on
  `SpechtStandardBasis` (which is indexed by `StandardYoungTableau μ`, so the
  size is `dim S^μ` by construction — that is W3, mechanically);
- W2's `simple_end_scalar` is what makes the factor `End_k` rather than an
  algebra over a larger `𝔇`;
- the real work moves to **surjectivity** of the action map (Jacobson density /
  the double-centraliser theorem), plus injectivity from faithfulness.

Re-scope W1 and W3 accordingly before starting: they are one construction, not
two, and the hard core is the density argument.

### Proposed route for W1+W3 as one construction (not yet attempted)

Density is **not** the only way in, and probably not the right one: the pinned
Mathlib has no Jacobson density theorem (searched the olean module names —
`Jacobson/{Artinian,Ideal,Polynomial,Radical,Ring,Semiprimary}`, `JacobsonNoether`,
`Spectrum/Prime/Jacobson`; all radical/ring-theoretic, none the density theorem).

The multiplicity route uses W2 as its hinge and asks less of Mathlib:

1. `k[S_n]` is semisimple (`MaschkeSnSemisimple`), so the regular module is
   `⊕ᵢ Sᵢ^{mᵢ}` over the simples.
2. `mᵢ = dim_{𝔇ᵢ} Hom_A(A, Sᵢ)` and `Hom_A(A, Sᵢ) ≅ Sᵢ`, so with **W2's
   `𝔇ᵢ = k`** this reads `mᵢ = dim_k Sᵢ`.
3. Hence `dim_k A = Σᵢ mᵢ·dim_k Sᵢ = Σᵢ (dim_k Sᵢ)²`, i.e. **`n! = Σ_μ (dim S^μ)²`
   comes out as a *conclusion*, not an input.**
4. The block algebra is then `∏_μ End_k(S^μ)`, and `LinearMap.toMatrix` on
   `SpechtStandardBasis` (indexed by `StandardYoungTableau μ`) turns each factor
   into `Matrix (Fin (dim S^μ))` — W3, mechanically.

Note what step 3 buys: it *produces* the RSK sum-of-squares that
`OVTopAssembly.sum_numSYT_sq_eq_factorial` currently carries as `sorryAx`,
rather than consuming it. If that holds up, the epic closes its own keystone
instead of routing around it.

**Unverified premise, do not treat as settled:** whether the pinned Mathlib's
isotypic API supports step 2 off the shelf. `IsIsotypicOfType` exists
(`Mathlib.RingTheory.SimpleModule.Isotypic`); I have not checked whether it
carries a multiplicity-as-`Hom`-dimension lemma or whether that has to be built.
Probe that first — it is the difference between a session and a tranche.

### Premise probed the same session — step 2 is supported, with one wrinkle

Measured against the pinned Mathlib rather than assumed:

- `IsIsotypicOfType.linearEquiv_finsupp` — an isotypic semisimple module of type
  `S` is `≃ₗ[R] (ι →₀ S)`. **Wrinkle: `ι` is existentially bound**, same shape as
  the Wedderburn statement, so it does not hand over a multiplicity *number*.
  It is still enough, because the number comes from the other side:
- `LinearMap.ringLmapEquivSelf : (R →ₗ[R] M) ≃ₗ[S] M` — i.e. `Hom_A(A, M) ≅ M`.

So `dim_k S_j = dim_k Hom_A(A, S_j) = m_j · dim_k End_A(S_j) = m_j` **using W2**
for the last equality, which pins `m_j = dim_k S_j` without ever needing `ι`
named. The one further ingredient is Schur's `Hom_A(Sᵢ, S_j) = 0` for `i ≠ j`,
for which the corpus already has `specht_pairwise_noniso`.

Verdict: the route is viable and W2 is load-bearing in it. Not attempted yet —
this is a premise check, not a proof.
