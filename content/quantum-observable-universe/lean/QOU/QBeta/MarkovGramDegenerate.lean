import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Algebra.BigOperators.Ring.Finset
import QOU.QBeta.TemperleyLiebTower
import QOU.Mathlib.TwoRowDimCatalan

/-!
# The Markov–Gram matrix is singular under convention D

**The excision's mathematical half.** Eleven content blocks assert that the
Markov pairing `⟨x, y⟩_τ := τ(x·y)` on `H_n(q)` is non-degenerate, that
`det G ≠ 0`, and that the inverse `G⁻¹` enters the Frobenius co-Casimir
`C = Σ_{i,j} (G⁻¹)_{ij} b_i b_j`. Under the production convention **D** every
one of those claims is **false as stated about `H_n`**: `det G = 0` exactly,
because the antisymmetric block carries weight `y₍₁³₎ = 0` and is therefore *in*
the radical of the trace form.

Those blocks are not wrong about the mathematics; they are wrong about the
object. The Frobenius structure is real — it lives on the quotient
`H_n / rad τ ≅ TL_n(δ)`, not on `H_n`. This file proves both halves of that
sentence, so the content can be repaired by *citation* rather than by deletion.

## The chain, end to end

1. `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the pin `z(q²+1) = q³`
   forces `y₍₁³₎ = 0`. *(already proved)*
2. `block_mem_radical` — a Wedderburn block whose weight is `0` lies in the trace
   radical. Three lines, and it is where cyclicity is spent.
3. `gram_det_eq_zero_of_radical_combination` — a nonzero radical element in the
   span of the basis puts a nonzero vector in the kernel of `G`, so `det G = 0`.
4. `TemperleyLiebTower.traceRadical_two_sided` — the radical is a two-sided
   ideal, so the quotient is a ring. *(already proved)*
5. `pairing_descends` — the pairing is constant on radical cosets, hence
   descends to that quotient.
6. `mem_radical_of_pairing_zero` — and on the quotient it is non-degenerate.

Steps 1–3 refute the eleven blocks; steps 4–6 tell them where to move the claim.

## Why `det G = 0` is exact, not approximate

This is worth being sharp about, because the C-convention numbers made it look
like a small perturbation. Under **C** the antisymmetric weight is
`y₍₁³₎ = 0.0227449…` — small, nonzero, and `G` is invertible with a large but
finite condition number. Under **D** the weight is `0`, full stop: not `10⁻¹⁶`,
not "numerically singular". The rank drops by exactly the dimension of the
discarded blocks (`24 − 14 = 3² + 1²` at `n = 4`,
`TemperleyLiebTower.radical_four`), and `Σ dim² = Catalan n` counts what
survives. A `G⁻¹` computed under C is not an approximation to a `G⁻¹` under D,
because the latter does not exist.
-/

namespace QOU.QBeta.MarkovGramDegenerate

open Matrix QOU.QBeta.TemperleyLiebTower

section Radical

variable {R : Type*} [CommRing R] {A : Type*} [Ring A]

/-- **A zero-weight Wedderburn block lies in the trace radical.**

If the trace restricted to the block `p` is `τ(x·p) = y·χ(x)` and the weight `y`
vanishes, then `p` pairs to zero against everything, which is exactly membership
in `traceRadical`.

Cyclicity is the whole content: `traceRadical` is stated with the radical
element on the **left** (`τ(p·b) = 0`), while the block hypothesis is stated
with it on the **right**. For the Markov trace cyclicity is the defining
property, so this costs nothing — but it is a real hypothesis and the proof
would not go through without it. -/
theorem block_mem_radical (tau : A → R) (p : A) (y : R) (chi : A → R)
    (hcyc : ∀ x z : A, tau (x * z) = tau (z * x))
    (hblock : ∀ x : A, tau (x * p) = y * chi x)
    (hy : y = 0) : p ∈ traceRadical tau := by
  intro b
  rw [hcyc, hblock, hy, zero_mul]

/-- **The pairing is constant on radical cosets**, hence descends to `A / rad τ`.

With `traceRadical_two_sided` (the radical is a two-sided ideal, so the quotient
is a ring) this is the statement that the Frobenius pairing the content blocks
want is well defined — on the quotient. -/
theorem pairing_descends {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (tau : A →ₗ[R] R) {a a' : A}
    (h : a - a' ∈ traceRadical (⇑tau)) (b : A) :
    tau (a * b) = tau (a' * b) := by
  have hz : tau ((a - a') * b) = 0 := h b
  rw [sub_mul, map_sub, sub_eq_zero] at hz
  exact hz

/-- **Non-degeneracy after the quotient.**

An element pairing to zero against everything *is* in the radical, so its class
in `A / rad τ` is zero. This is definitional — `traceRadical` is defined by that
very condition — and it is stated anyway because it is the half of the descent
the content blocks actually cite: "the induced pairing on the quotient is
non-degenerate" is not an extra theorem to prove, it is what quotienting by the
radical *means*. Saying so explicitly is what stops the claim drifting back onto
`H_n`. -/
theorem mem_radical_of_pairing_zero (tau : A → R) {a : A}
    (h : ∀ b : A, tau (a * b) = 0) : a ∈ traceRadical tau := h

end Radical

section GramMatrix

variable {R : Type*} [CommRing R] [IsDomain R]
variable {A : Type*} [Ring A] [Algebra R A]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **The Markov–Gram matrix** `G_{ij} = τ(b_i · b_j)` of a linear functional
against a finite family. No basis hypothesis: the family may be dependent, and
the statements below are about the matrix regardless. -/
def gram (tau : A →ₗ[R] R) (b : ι → A) : Matrix ι ι R := fun i j => tau (b i * b j)

omit [IsDomain R] [Fintype ι] [DecidableEq ι] in
@[simp] theorem gram_apply (tau : A →ₗ[R] R) (b : ι → A) (i j : ι) :
    gram tau b i j = tau (b i * b j) := rfl

-- `omit ... in` must precede the docstring, not sit between it and the theorem.
omit [IsDomain R] [DecidableEq ι] in
/-- **`G` applied to a coefficient vector is the pairing against the combination.**

`(G *ᵥ c)_i = τ(b_i · Σ_j c_j b_j)`. The bridge between the matrix picture the
content blocks use and the algebra picture the radical lives in. -/
theorem gram_mulVec (tau : A →ₗ[R] R) (b : ι → A) (c : ι → R) (i : ι) :
    (gram tau b *ᵥ c) i = tau (b i * ∑ j, c j • b j) := by
  rw [Finset.mul_sum, map_sum]
  simp only [gram_apply, Matrix.mulVec, dotProduct, mul_smul_comm, map_smul, smul_eq_mul]
  exact Finset.sum_congr rfl fun j _ => mul_comm _ _

/-- **The Markov–Gram determinant vanishes when the radical meets the span.**

If some nonzero coefficient vector `c` produces a combination `a = Σ c_j b_j`
lying in the trace radical, then `c` is a nonzero kernel vector of `G`, so
`det G = 0`.

This is the theorem that refutes the eleven `gram-inverse-unqualified` blocks.
Under convention **D** its hypothesis is *met*, by `block_mem_radical` applied to
the antisymmetric block that `conventionD_kills_antisymmetriser` sends to zero —
so `G⁻¹` does not exist and the co-Casimir `Σ (G⁻¹)_{ij} b_i b_j` is not a
well-formed expression on `H_n`.

Note the hypothesis is about `τ(b_i · a)`, the radical element on the **right**;
`traceRadical` is stated with it on the left, and `traceRadical_star_eq` /
cyclicity is what connects the two. It is taken as a hypothesis here rather than
derived so the theorem holds for a bare linear functional, cyclic or not. -/
theorem gram_det_eq_zero_of_radical_combination
    (tau : A →ₗ[R] R) (b : ι → A) (c : ι → R) (hc : c ≠ 0)
    (hrad : ∀ i : ι, tau (b i * ∑ j, c j • b j) = 0) :
    (gram tau b).det = 0 := by
  refine Matrix.exists_mulVec_eq_zero_iff.mp ⟨c, hc, ?_⟩
  ext i
  rw [Pi.zero_apply, gram_mulVec tau b c i]
  exact hrad i

/-- **Contrapositive, the form the content blocks should cite.**

`det G ≠ 0` *implies* no basis combination lies in the radical. So a block that
wants `G⁻¹` is committing to a trace with trivial radical — which convention D
is not. Stating it this way makes the dependency visible at the point of use
instead of buried in a normalisation. -/
theorem no_radical_combination_of_det_ne_zero
    (tau : A →ₗ[R] R) (b : ι → A)
    (hdet : (gram tau b).det ≠ 0) (c : ι → R) (hc : c ≠ 0) :
    ∃ i : ι, tau (b i * ∑ j, c j • b j) ≠ 0 := by
  by_contra hcon
  push_neg at hcon
  exact hdet (gram_det_eq_zero_of_radical_combination tau b c hc hcon)

end GramMatrix

section RankAccounting

/-! ### What the rank drop is, exactly

The corank of `G` is the dimension of the radical, and the tower already counts
both sides. These are the arithmetic checks that tie the abstract statement to
the numbers the content blocks quote; the block dimensions themselves come from
`TemperleyLiebTower.catalan_four` / `radical_four`. -/

/-- **`n = 3`: `dim H₃ = 6`, `dim TL₃ = 5`, so `G₃` has corank `1`.** The single
lost direction is the antisymmetriser — the one-dimensional `(1³)` block. -/
theorem corank_three : 6 - (1 ^ 2 + 2 ^ 2) = 1 ^ 2 := by norm_num

/-- **`n = 4`: `dim H₄ = 24`, `dim TL₄ = 14`, so `G₄` has corank `10`** — the
`(2,1,1)` block of dimension `3` and the `(1⁴)` block of dimension `1`,
contributing `3² + 1² = 10`. Same statement as
`TemperleyLiebTower.radical_four`, written as a corank. -/
theorem corank_four : 24 - (1 ^ 2 + 3 ^ 2 + 2 ^ 2) = 3 ^ 2 + 1 ^ 2 := by norm_num

/-- **`n = 5`: `dim H₅ = 120`, `dim TL₅ = 42`, corank `78`.** The three-row and
lower blocks of `S₅` — dimensions `6, 5, 4, 1` — give `6² + 5² + 4² + 1² = 78`. -/
theorem corank_five : 120 - (1 ^ 2 + 4 ^ 2 + 5 ^ 2) = 6 ^ 2 + 5 ^ 2 + 4 ^ 2 + 1 ^ 2 := by
  norm_num

/-! #### The same accounting for general `n`

The three theorems above are instances, and they are instances of a weaker kind
than they look: each writes its two-row dimensions out **by hand** (`1, 2` at
`n = 3`; `1, 3, 2` at `n = 4`; `1, 4, 5` at `n = 5`) and then checks an
arithmetic identity between literals. Nothing in them derives those dimensions,
and nothing in them extends to `n = 6`.

`corank_general` below removes the hand-listing. The visible-block dimension
count is `Σ_{ℓ(λ) ≤ 2} (dim V_λ)²` with the dimensions given by the hook length
formula, and `QOU.Mathlib.dimHLF_two_row_sq_sum` proves that sum is `catalan n`
for **every** `n` — so the corank is `n! − catalan n` with nothing enumerated.

**Scope.** This is the *arithmetic* half, and it is unconditional. It says: if
the trace-visible blocks are the two-row ones, the corank is `n! − catalan n`.
That antecedent — Wenzl level `r = 2` in convention D — is carried elsewhere as
a Lean class and is **not** proved here; see `QOU.Mathlib.TwoRowDimCatalan`'s
docstring and bean `qou-fpjy` for why `#print axioms` cannot see that
dependency. -/

/-- **The corank accounting for general `n`**: `n!` minus the two-row
square-sum is `n! − catalan n`.

Supersedes `corank_three` / `_four` / `_five`, which are the `n = 3, 4, 5`
instances with their block dimensions written out by hand. -/
theorem corank_general (n : ℕ) :
    (n.factorial : ℤ)
        - ∑ k ∈ Finset.range (n / 2 + 1),
            ((QOU.BraidKnot.IdentityI.dimHLF [n - k, k] : ℕ) : ℤ) ^ 2
      = (n.factorial : ℤ) - (catalan n : ℤ) :=
  QOU.Mathlib.factorial_sub_two_row_sq_sum n

/-- **`n = 6`: corank `588`** — the value
`computations/probes/tl_n6_discriminator.py` measured, now an instance of
`corank_general` rather than a separate arithmetic check. -/
theorem corank_six_value : (Nat.factorial 6 : ℤ) - (catalan 6 : ℤ) = 588 :=
  QOU.Mathlib.corank_value_six

/-- **`n = 7`: `4611`.** An arithmetic *prediction* — the number a Gram-rank
measurement at `n = 7` would have to produce. No such measurement exists; the
probe reaches `n = 6`. -/
theorem corank_seven_value : (Nat.factorial 7 : ℤ) - (catalan 7 : ℤ) = 4611 :=
  QOU.Mathlib.corank_value_seven

/-- **`n = 8`: `38890`.** Prediction, as for `n = 7`. -/
theorem corank_eight_value : (Nat.factorial 8 : ℤ) - (catalan 8 : ℤ) = 38890 :=
  QOU.Mathlib.corank_value_eight

end RankAccounting

section SharpCorank

/-! ### From "some radical element" to the sharp corank

`gram_det_eq_zero_of_radical_combination` above spends a *single* radical vector
and concludes `det G = 0` — i.e. corank `≥ 1`. That is all the eleven blocks
needed refuting, but it is strictly weaker than what is true, and the gap is
exactly where the arithmetic of `RankAccounting` was left hanging: `corank_three`
and friends are `norm_num` identities about numbers. Nothing connected them to
the rank of any actual matrix, so "corank 10 at `n = 4`" was, in Lean, an
assertion about `24 - 14`.

This section supplies the missing link. A radical **subspace** of dimension `d`
forces corank `≥ d`, by rank–nullity: every such coefficient vector is in
`ker (G *ᵥ ·)`, so the kernel is at least `d`-dimensional and the rank is at most
`card ι - d`. Combined with a matching lower bound on the rank the corank is
pinned exactly, which is how the measurement in
`computations/probes/gram_radical_cellular_revalidation.py` is made rigorous
rather than merely observed.

Stated over a `Field` because rank–nullity is: `finrank` of a kernel is only
well-behaved over a division ring. That is a genuine archimedean-free
requirement (§7c) — no ordering, no `Real`, any field will do, including the
rational function field `ℚ(q)` in which the degeneracy is *generic*. -/

variable {R : Type*} [Field R]
variable {A : Type*} [Ring A] [Algebra R A]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

omit [DecidableEq ι] in
/-- **A radical combination is a kernel vector of `G`.**

The algebra-side condition (`Σ c_j b_j` pairs to zero against every `b_i`) and
the matrix-side condition (`c ∈ ker (G *ᵥ ·)`) are the same statement read
through `gram_mulVec`. -/
theorem mem_ker_mulVecLin_of_radical (tau : A →ₗ[R] R) (b : ι → A) {c : ι → R}
    (hrad : ∀ i, tau (b i * ∑ j, c j • b j) = 0) :
    c ∈ LinearMap.ker (gram tau b).mulVecLin := by
  have h : (gram tau b) *ᵥ c = 0 := by
    funext i
    exact (gram_mulVec tau b c i).trans (hrad i)
  simpa [LinearMap.mem_ker, Matrix.mulVecLin_apply] using h

omit [DecidableEq ι] in
/-- **A radical subspace of dimension `d` costs the Gram matrix `d` of its rank.**

`rank G + dim W ≤ card ι` for any subspace `W` of coefficient vectors whose
combinations all lie in the radical of the pairing. Equivalently
`corank G ≥ dim W`.

This is the general form of the convention-D degeneracy. Instantiated with `W`
the image of the Temperley–Lieb ideal `ker(H_n(q) ↠ TL_n(q))` — which is a
radical subspace precisely because the radical is a two-sided ideal
(`TemperleyLiebTower.traceRadical_two_sided`) containing the three-strand
`q`-antisymmetriser — it gives `rank G ≤ Catalan n`, the upper half of the
corank determination. Nothing here is special to convention D, to `H_n(q)`, or
to any particular `q`: it is rank–nullity, and it is why the degeneracy cannot
be a precision artefact. -/
theorem gram_rank_add_le_card (tau : A →ₗ[R] R) (b : ι → A)
    (W : Submodule R (ι → R))
    (hW : ∀ c ∈ W, ∀ i, tau (b i * ∑ j, c j • b j) = 0) :
    (gram tau b).rank + Module.finrank R W ≤ Fintype.card ι := by
  have hle : W ≤ LinearMap.ker (gram tau b).mulVecLin := fun c hc =>
    mem_ker_mulVecLin_of_radical tau b (hW c hc)
  have hmono : Module.finrank R W
      ≤ Module.finrank R (LinearMap.ker (gram tau b).mulVecLin) :=
    Submodule.finrank_mono hle
  have hrk := LinearMap.finrank_range_add_finrank_ker (gram tau b).mulVecLin
  have hcard : Module.finrank R (ι → R) = Fintype.card ι :=
    Module.finrank_fintype_fun_eq_card R
  have hrank : (gram tau b).rank
      = Module.finrank R (LinearMap.range (gram tau b).mulVecLin) := rfl
  omega

omit [DecidableEq ι] in
/-- **The rank bound, as a bound on the surviving dimension.**

The quotient `H_n / rad τ` is what carries the non-degenerate Frobenius pairing,
and this says its dimension is at most `card ι - dim W`. Read with `W` the
Temperley–Lieb ideal: what survives is `TL_n`, of dimension `Catalan n`. -/
theorem gram_rank_le_card_sub (tau : A →ₗ[R] R) (b : ι → A)
    (W : Submodule R (ι → R))
    (hW : ∀ c ∈ W, ∀ i, tau (b i * ∑ j, c j • b j) = 0) :
    (gram tau b).rank ≤ Fintype.card ι - Module.finrank R W := by
  have := gram_rank_add_le_card tau b W hW
  omega

omit [DecidableEq ι] in
/-- **`rank G ≤ catalan n`** — the surviving dimension is at most `Catalan`.

The three hypotheses are the three things that have to be true for the
Temperley–Lieb reading of the degeneracy, and the conclusion is *derived* from
them by rank–nullity, not assumed:

* `hW` — `W` is a radical subspace (its combinations pair to zero against
  everything). For the intended instance this is the image of
  `ker(H_n(q) ↠ TL_n(q))`, radical because the radical is a two-sided ideal
  containing the three-strand `q`-antisymmetriser.
* `hcard` — the basis is the `T_w` basis, so `card ι = n!`.
* `hdim` — the radical has the predicted dimension. Stated additively,
  `dim W + catalan n = n!`, rather than as `dim W = n! − catalan n`: the
  subtraction form would be a truncated `ℕ` subtraction and would silently hold
  for the wrong reason if `catalan n` exceeded `n!`.

What makes the conclusion worth stating is that `catalan n` here is
`Σ_{ℓ(λ) ≤ 2} (dim V_λ)²` — see `corank_general` and
`QOU.Mathlib.dimHLF_two_row_sq_sum` — so this reads: *what survives the
degenerate trace form is at most the two-row part*, for every `n`, with no
per-`n` computation. -/
theorem gram_rank_le_catalan {n : ℕ} (tau : A →ₗ[R] R) (b : ι → A)
    (W : Submodule R (ι → R))
    (hW : ∀ c ∈ W, ∀ i, tau (b i * ∑ j, c j • b j) = 0)
    (hcard : Fintype.card ι = n.factorial)
    (hdim : Module.finrank R W + catalan n = n.factorial) :
    (gram tau b).rank ≤ catalan n := by
  have h := gram_rank_add_le_card tau b W hW
  omega

end SharpCorank


section LiveChannels

/-! ## Blocks versus channels — giving the distinction a name

The compute layer enumerates its Wedderburn blocks as *all* partitions of `n`
and then weights each by `y_λ`. That is correct as a **block** list, and it was
also correct as a **channel** list under the excised convention C, where every
`y_λ` was nonzero. Under convention D the two sets come apart —
`y_λ = 0` for every `ℓ(λ) ≥ 3` — and nothing in the pipeline noticed, because
nothing in the pipeline could *say* it: there was no name for "block the trace
can actually see".

The gap is not a missing check, it is a missing word. This section supplies it.

The whole thing turns on an observation `rem:gram-matrix-spectral-connection`
already contains: in the Wedderburn basis the Gram matrix is **diagonal, with the
weights themselves on the diagonal**. Everything below is then a corollary of
`Matrix.det_diagonal`, and the live set is simply the support of `y`. -/

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **The Wedderburn Gram matrix**: diagonal, carrying the block weights.

`G_{λμ} = δ_{λμ} · y_λ`. Not an assumption — it is what
`rem:gram-matrix-spectral-connection` derives from
`τ(e_λ e_μ) = δ_{λμ} τ(e_λ)` for orthogonal idempotents. Stating it as a
definition is what lets every statement below be a one-line corollary rather
than an argument. -/
def wedderburnGram (y : ι → R) : Matrix ι ι R := Matrix.diagonal y

/-- **A channel is live when the trace can see it.** The live set is exactly the
support of `y`, and "dead" is the complement.

This is the word the compute layer was missing. It is deliberately defined by
`y_λ ≠ 0` rather than by `ℓ(λ) ≤ 2`: the row bound is a *consequence* of
convention D via Schur–Weyl (a two-dimensional fibre cannot antisymmetrise three
ways), not the definition of observability. Defining liveness by the weight keeps
it correct if the convention ever moves again, and keeps the reason visible. -/
def IsLive (y : ι → R) (i : ι) : Prop := y i ≠ 0

/-- **`det G = ∏ y_λ`.** The Gram determinant is the product of the block
weights — immediately, since the matrix is diagonal. -/
theorem wedderburnGram_det (y : ι → R) :
    (wedderburnGram y).det = ∏ i, y i := by
  unfold wedderburnGram
  exact Matrix.det_diagonal

/-- **One dead channel kills the whole determinant.** If any block is dead then
`det G = 0`, however many live blocks sit beside it.

This is the sharp form of what convention D does: it is not that `G` becomes
ill-conditioned, it is that a single vanishing weight annihilates the product.
`y_(1^3) = 0` at `n = 3` is enough on its own. -/
theorem wedderburnGram_det_eq_zero_of_dead (y : ι → R) {i : ι} (hdead : y i = 0) :
    (wedderburnGram y).det = 0 := by
  rw [wedderburnGram_det]
  exact Finset.prod_eq_zero (Finset.mem_univ i) hdead

end LiveChannels

section LiveChannelsField

variable {R : Type*} [CommRing R] [NoZeroDivisors R] [Nontrivial R]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **`G` is invertible exactly when every channel is live.**

The converse direction is the one the compute layer needs: wanting `G⁻¹` is
*equivalent to* asserting there are no dead channels. Under convention D that
assertion is false for every `n ≥ 3`, so any producer that inverts the full Gram
is committing to something the convention denies — and now has a statement to be
checked against rather than a guard to fall through. -/
theorem wedderburnGram_det_ne_zero_iff_all_live (y : ι → R) :
    (wedderburnGram y).det ≠ 0 ↔ ∀ i, IsLive y i := by
  rw [wedderburnGram_det]
  unfold IsLive
  constructor
  · intro h i
    exact fun hy => h (Finset.prod_eq_zero (Finset.mem_univ i) hy)
  · intro h
    exact Finset.prod_ne_zero_iff.mpr fun i _ => h i

omit [Fintype ι] [DecidableEq ι] in
/-- **Restricted to the live channels, the Gram is invertible.**

The positive half, and the reason the excision is a relocation rather than a
loss: drop the dead blocks and the determinant is a product over the survivors,
every factor nonzero. This is `H_n/rad ≅ TL_n` in the diagonal picture — the
quotient is not a repair, it is what is left when the zeros are removed. -/
theorem wedderburnGram_restrict_live_det_ne_zero
    (y : ι → R) (s : Finset ι) (hs : ∀ i ∈ s, IsLive y i) :
    ∏ i ∈ s, y i ≠ 0 :=
  Finset.prod_ne_zero_iff.mpr fun i hi => hs i hi

end LiveChannelsField


end QOU.QBeta.MarkovGramDegenerate
