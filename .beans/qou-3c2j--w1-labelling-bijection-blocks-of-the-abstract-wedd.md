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

### Bricks 1–2 landed (PR #5151)

`QOU/BraidKnot/SpechtSchurDiagonal.lean`, sorry-free:

- `finrank_homG_specht_self` — `dim Hom_G(S^μ, S^μ) = 1` (this is W2, in the form the
  character machinery consumes);
- `homG_specht_cross_eq_bot` — the off-diagonal vanishing, which
  `specht_exhausts_irreducibles` already argued *inline* and never exported;
- `finrank_homG_specht` — **orthonormality**, `1` on the diagonal and `0` off it, over any
  characteristic-zero field. No algebraic closure anywhere.

Remaining for `n! = Σ_μ (dim S^μ)²`:

1. `χ_reg` — the regular character is `n!` at `1` and `0` elsewhere;
2. `⟨χ_reg, χ_μ⟩ = dim S^μ` (the pairing computes `dim Hom_G(A, S^μ)`, and
   `LinearMap.ringLmapEquivSelf` gives `Hom_A(A, S^μ) ≅ S^μ`);
3. the expansion `χ_reg = Σ_μ ⟨χ_reg, χ_μ⟩ · χ_μ`, which needs the Specht characters to
   **span** the class functions. The corpus has the counting *equality*
   `card_irreducibles_eq_card_partitions`; check whether spanning follows from it directly
   or needs its own argument — that is the one place left where I would expect real work.

Then `⟨χ_reg, χ_reg⟩` computed two ways gives the identity.

**Elaboration hazard, recorded so it is not re-hit:** `finrank_span_singleton` and
`finrank_bot` both time out at `isDefEq` on these modules unless the module argument is
given explicitly — at 10⁶ heartbeats, not merely the default. Name the type; do not raise
the limit.

### Correction to step 3 above — spanning is not needed at all

I wrote that step 3 needs the Specht characters to **span** the class functions, and that
this was the one place I expected real work. Checked: the corpus carries only *upper*
bounds in that direction — `finrank_classFunctions_le` (`≤ #ConjClasses`) and
`card_conjClasses_le` (`≤ #partitions`). Spanning would be a genuinely new argument.

It is also avoidable. Decompose the **module** rather than expanding the character:

- `k[S_n]` is semisimple, so the regular module is the (independent) sup of its isotypic
  components — Mathlib has `sSup_isotypicComponents` and `sSupIndep_isotypicComponents`;
- every simple summand is some `S^μ` (`specht_exhausts_irreducibles`), so the components
  are indexed by partitions;
- `dim Hom_G(A, S^μ) = m_μ` by orthonormality (bricks 1–2), and `= dim S^μ` by
  `ringLmapEquivSelf`;
- `dim_k A = Σ_μ m_μ · dim S^μ = Σ_μ (dim S^μ)²`, i.e. `n! = Σ_μ (dim S^μ)²`.

No class-function spanning, no completeness-of-characters. Revised remaining work is
therefore: the isotypic decomposition of the regular module (Mathlib-supported), the
`Hom_A(A, M) ≅ M` identification, and the dimension count. Bricks 1–2 are what make the
middle step give `m_μ` on the nose rather than `m_μ · dim End`.

### Brick 3 landed (PR #5156)

`QOU/MathlibExt/RegularHom.lean`, sorry-free: `homGRegularEquiv : Hom_G(k[G], V) ≃ₗ[k] V`
and `finrank_homG_regular`. Evaluation at the identity basis vector is the isomorphism.
General — any group, any field, any representation.

With bricks 1–2 this gives, for each partition, that `dim Hom_G(k[G], S^μ)` is the
multiplicity on one side and `dim S^μ` on the other.

**Remaining for `n! = Σ_μ (dim S^μ)²`:** the isotypic decomposition of the regular module
and the dimension count over it. Mathlib supplies `sSup_isotypicComponents` +
`sSupIndep_isotypicComponents`; the work is turning that sup into a `finrank` sum indexed
by `PartitionIndex n`, using `specht_exhausts_irreducibles` to know each component's type
is a Specht module. That is the next brick and the last one before the identity.

### Brick 4a landed (PR #5162); 4b scoped, with its friction named

`QOU/BraidKnot/SpechtBlockDimension.lean`, sorry-free: `finrank_specht_blocks`
(`dim ∏_μ End_k(S^μ) = Σ_μ (dim S^μ)²`) and `finrank_group_algebra` (`dim k[S_n] = n!`).
Both sides of the count, and nothing joining them — deliberately, so the next brick must
supply a map rather than let adjacency imply the identity.

**Brick 4b — the action map and its injectivity.** All the pieces exist:

- `Pi.algHom k _ (fun i => (spechtRepAt i.property).asAlgebraHom)` gives
  `Φ : k[S_n] →ₐ[k] ∏_{μ} End_k(S^μ)` (`Representation.asAlgebraHom` and `Pi.algHom` both
  checked present at this pin);
- injectivity: `x ∈ ker Φ` acts as zero on every simple `k[S_n]`-module, because every
  simple is a Specht module (`specht_exhausts_irreducibles`); `k[S_n]` is semisimple so
  `IsSemisimpleModule.sSup_simples_eq_top` makes it a sup of simple submodules; hence `x`
  acts as zero on `k[S_n]`, and `x = x • 1 = 0`;
- injectivity then yields `n! ≤ Σ_μ (dim S^μ)²` from brick 4a. **One inequality, not the
  identity** — say so when it lands.

**The friction, so the next session budgets for it and does not mistake it for the maths:**
applying `specht_exhausts_irreducibles` to a simple *submodule* `N ≤ k[S_n]` needs `N` as a
`Representation k (Perm (Fin n))`. `Representation.ofModule` supplies one, but on
`RestrictScalars k (MonoidAlgebra k G) ↥N`, and the hypothesis wants
`IsSimpleModule (MonoidAlgebra k G) (·).asModule`. That `ofModule`/`asModule`/`RestrictScalars`
round-trip is the whole risk in 4b; the mathematics above is routine. Budget the session for
the round-trip, not for the argument.

The reverse inequality `Σ_μ (dim S^μ)² ≤ n!` is a separate question — expect it to need the
isotypic independence, i.e. that the multiplicity spaces the bricks 1–3 count do not overlap.

### Brick 4b landed (PR #5167); 4c is blocked on a named Mathlib gap

`SpechtRegularMultiplicity.finrank_homG_regular_specht` — `dim Hom_G(k[S_n], S^μ) = dim S^μ`,
sorry-free. That is the per-partition multiplicity statement in the epic's vocabulary.

**4c (injectivity of the action map ⇒ `n! ≤ Σ_μ (dim S^μ)²`) is blocked**, and the blocker is
plumbing, not mathematics: no transfer of `IsSimpleModule` across the
`Representation.ofModule` / `asModule` / `RestrictScalars` round-trip exists at this pin
(verified with `exact?`, not assumed). Tracked as **`qou-ltzf`** with the full sketch. Nothing
already merged depends on it.

Five bricks merged or open, none carrying a sorry: #5139, #5151, #5156, #5162, #5167.
