/-!
# Knot-indexed bi-filtration `H_q^(n, K)` — definition

`def:hq-bi-filtration` from `hq-bi-filtration.md`. The bi-filtration
of the substrate convolution algebra `H_q` by:

- depth axis `n` (iterated-integral depth on grouplikes — the
  Goncharov/keystone axis), and
- knot axis `K` (Bring-embeddable knot/braid class via dominant
  cell `λ_K` and central primitive idempotent `e_{λ_K}`).

Definition: `H_q^{(n, K)} := { α ∈ G^{(n)}(H_q) : e_{λ_K} * α * e_{λ_K} = α }`.

This file is the **definition layer**. Conjectural structure on
the bi-filtration (joint Galois × braid action, etc.) lives in
companion blocks under their own conjecture classes
(`conj:joint-galois-braid-action`).
-/

import Mathlib.Algebra.Hopf.Basic

namespace QOU.AlgebraicSubstrate.HqBiFiltration

variable {R : Type*} [CommRing R]
variable {q : R}

/-- The substrate convolution Hopf algebra `H_q`. Placeholder;
    wired through `def:frobenius-hopf-substrate`. -/
opaque ConvolutionHopfAlgebra (q : R) : Type

/-- Iterated-integral depth filtration `G^{(n)}(H_q)` on grouplikes
    of `H_q`. Wired through `conj:gb-depth-period-correspondence`. -/
opaque GroupLikeDepth (q : R) (n : ℕ) : Type

/-- Central primitive idempotent `e_{λ_K}` for a partition
    `λ_K ⊢ n_K` (the dominant Wedderburn cell of the Hecke
    algebra `H_{n_K}(q)` for knot/braid class `K`). Wired through
    `prop:explicit-central-idempotent`. -/
opaque CentralIdempotent (q : R) (lam : List ℕ) : Type

/-- **Definition (`def:hq-bi-filtration`).** The knot-indexed
    bi-filtration of `H_q`:

      `H_q^{(n, K)}` := grouplikes at depth `n` localised on the
      `λ_K`-Wedderburn block.

    Two-axis grading: depth `n` (Goncharov side) × knot index
    `K` (Hecke cell side). -/
opaque BiFiltration (q : R) (n : ℕ) (lam : List ℕ) : Type

/-- Compatibility with convolution: `H_q^{(n_1, K_1)} *_q H_q^{(n_2, K_2)}
    ⊆ ⊕ H_q^{(n_1 + n_2, K')}` for `K'` ranging over cell-mergings.
    Conjectural part of the bi-filtration; recorded as a property
    rather than a theorem. -/
def convolution_compatible
    (q : R) (n₁ n₂ : ℕ) (lam₁ lam₂ : List ℕ) : Prop :=
  -- Ref: [manuscript] §def:hq-bi-filtration "Compatibility with
  -- the Hopf and braid structures" — closure properties of the
  -- bi-filtration under convolution, coproduct, bar involution,
  -- and Markov trace.
  -- Ref: [kontsevich1995] https://arxiv.org/abs/q-alg/9505016
  -- — operadic structure of period algebras.
  True

/-- Compatibility with bar involution: `* : H_q^{(n, K)} → H_q^{(n, K^*)}`
    where `K^*` is the mirror knot. -/
def bar_compatible (q : R) (n : ℕ) (lam : List ℕ) : Prop :=
  -- Ref: [manuscript] §rem:chirality-period-pairing — bar
  -- involution acts on partitions by transpose, swapping cells of
  -- chiral pairs and fixing self-conjugate cells.
  True

/-- The figure-8 instance: `H_q^{(2, 4_1)}` contains the
    Bring-figure-8 depth-2 witness via the self-conjugate (2,2)
    cell. -/
def figure_eight_instance (q : R) : Prop :=
  -- Ref: [manuscript] §conj:bring-figure-eight-depth-2-witness —
  -- numerical witness Vol(4_1) = 2 Cl_2(π/3) at 50 dps.
  True

end QOU.AlgebraicSubstrate.HqBiFiltration
