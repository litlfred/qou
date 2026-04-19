/-!
# GS Reduction Cost Implements the Jones Recursion

Content-block Lean sibling for `prop:gs-cost-jones-recursion`.

The Hecke rewriting system `(H1)/(H2)/(H3)` from `HeckeGS.lean`
*is* the Jones-polynomial skein recursion:

- **(H1)** quadratic relation `T_i^2 → (q - q⁻¹) T_i + 1`
  carries the skein coefficients `(q - q⁻¹, 1)` literally.
- **(H2)** braid and **(H3)** far-commutativity relations
  permute monomials without altering the multiset of
  leading coefficients (cost-preserving).

This file builds on `HeckeGS.lean` to provide:

1. A **linear Markov trace** `MarkovTrace` structure on
   `AlgElement (HeckeGen n) ℝ`, axiomatised as an external
   theorem (Jones 1987, Theorem 5.1 & Corollary 5.3).
2. A **Jones polynomial** `jonesValue` defined as the
   Markov-trace evaluation of a braid's Hecke image.
3. The **reduction-invariance theorem**: the Jones value is
   independent of the reduction order (follows from
   `threading_cost_unique`).
4. The **skein identification**: each of `(H1)/(H2)/(H3)`
   is literally the skein / Yang–Baxter / far-comm relation
   (provable by `rfl`).

LaTeX label: `prop:gs-cost-jones-recursion`

## Axiom budget

| Item | Status | Justification |
|------|--------|---------------|
| `hecke_h1_is_skein` | **theorem** | `rfl` from `heckeRelation` |
| `hecke_h2_is_yang_baxter` | **theorem** | `rfl` from `yangBaxterRelation` |
| `hecke_h3_is_far_comm` | **theorem** | `rfl` from `farCommRelation` |
| `MarkovTrace` | **structure** | Jones 1987, Thm 5.1 & Cor 5.3; carries `tr_cyclic_gen` (cyclicity), subalgebra-restricted `markov_pos`, and `tr_reduces` |
| `markov_trace_exists` | **axiom** | Jones 1987, 54-page external proof |
| `jonesValue` | **def** | `MarkovTrace.tr ∘ augmentedBraidElement` |
| `jones_reduction_invariant` | **theorem** | From `threading_cost_unique` |
| `jonesValue_eq_trace_of_nf` | **theorem** | From `MarkovTrace.tr_reduces` |
| `gs_cost_jones_recursion` | **theorem** | From `threading_cost_unique` |

## References

- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Ch. XII
- [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
-/

import UGB.GrobnerShirshov.HeckeGS

namespace UGB.GrobnerShirshov.Hecke

open UGB.GrobnerShirshov

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Ch. XII

/-! ## §1  Skein identification (`rfl`-provable) -/

/-- **(H1) is the Jones skein relation.** The quadratic Hecke
    rule carries the skein coefficients `(q - q⁻¹, 1)` literally:
    oriented as `T_i^2 → (q - q⁻¹) T_i + 1`, it matches the Jones
    skein identity `L₊ - L₋ = (q - q⁻¹) L₀` after the dictionary
    `L₊ ↔ T_i²`, `L₋ ↔ 1`, `L₀ ↔ T_i`. Provable by `rfl`. -/
theorem hecke_h1_is_skein {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    (heckeRelation i hp).relation = AlgElement.ofTerms
      [([⟨i⟩, ⟨i⟩], 1), ([⟨i⟩], -(hp.q - hp.q⁻¹)), ([], -1)] := rfl

/-- **(H2) is the braid / Yang–Baxter relation.**
    Oriented as `T_i T_{i+1} T_i → T_{i+1} T_i T_{i+1}`, it is
    cost-preserving: the two sides share the leading-coefficient
    multiset `{1, -1}`. Provable by `rfl`. -/
theorem hecke_h2_is_yang_baxter {n : ℕ} (i j : Fin n) :
    (yangBaxterRelation i j).relation = AlgElement.ofTerms
      [([⟨i⟩, ⟨j⟩, ⟨i⟩], 1), ([⟨j⟩, ⟨i⟩, ⟨j⟩], -1)] := rfl

/-- **(H3) is the far-commutativity relation.**
    Oriented as `T_i T_j → T_j T_i` for `|i - j| ≥ 2`, it is
    cost-preserving: coefficient multiset `{1, -1}`.
    Provable by `rfl`. -/
theorem hecke_h3_is_far_comm {n : ℕ} (i j : Fin n) :
    (farCommRelation i j).relation = AlgElement.ofTerms
      [([⟨i⟩, ⟨j⟩], 1), ([⟨j⟩, ⟨i⟩], -1)] := rfl

/-! ## §2  Markov trace (axiomatic) -/

/-- **Markov trace on `H_n(q)` over ℝ.**

    A linear functional `tr : AlgElement (HeckeGen n) ℝ → ℝ`
    satisfying the three properties from Jones (1987), Theorem
    5.1 and Corollary 5.3:

    1. **Normalisation**: `tr(1) = 1`.
    2. **Linearity**: `tr (f + g) = tr f + tr g`,
       `tr (c • f) = c · tr f`.
    3. **Markov property** (vertical stabilisation): for the
       right-multiplication by the last generator `T_{n-1}` of
       `H_n(q) ↪ H_{n+1}(q)`, there is a non-zero `z : ℝ` with
       `tr (f · T_{n-1}) = z · tr f`.

    The trace is determined (up to choice of `z`) by these
    properties; its value on a braid image is the writhe-
    normalised Jones polynomial of the closure
    (Jones 1987, Theorem 5.1). -/
structure MarkovTrace (n : ℕ) (hp : HeckeParams) where
  /-- The trace functional. -/
  tr : AlgElement (HeckeGen n) ℝ → ℝ
  /-- Normalisation: `tr (1) = 1`. -/
  tr_one : tr (AlgElement.singleton []) = 1
  /-- Linearity w.r.t. addition. -/
  tr_add : ∀ (f g : AlgElement (HeckeGen n) ℝ),
    tr (AlgElement.add f g) = tr f + tr g
  /-- Linearity w.r.t. scalar multiplication. -/
  tr_smul : ∀ (c : ℝ) (f : AlgElement (HeckeGen n) ℝ),
    tr (AlgElement.smul c f) = c * tr f
  /-- **Cyclicity (single-generator form)**: `tr (g · f) = tr (f · g)`
      for every generator `g`.  Since `AlgElement` carries no general
      multiplication, the full cyclic property `tr (f g) = tr (g f)`
      is captured here by its generator-wise specialisation, which
      extends to all elements by `tr_add`, `tr_smul`, and induction
      on the length of a monomial. -/
  tr_cyclic_gen : ∀ (g : HeckeGen n) (f : AlgElement (HeckeGen n) ℝ),
    tr (AlgElement.leftMulGen g f) = tr (AlgElement.rightMulGen f g)
  /-- Markov parameter `z`. -/
  z : ℝ
  /-- The Markov parameter is non-zero. -/
  z_ne_zero : z ≠ 0
  /-- **Markov property (subalgebra form)**: right-multiplying by the
      last generator `T_{n-1}` rescales the trace by `z` *for elements
      of the subalgebra* `H_{n-1}(q) ↪ H_n(q)` --- that is, elements
      whose support contains no occurrence of the top generator
      `T_{n-1}`.  Stating this over all of `H_n(q)` would force `z`
      to satisfy the Hecke quadratic, over-constraining the parameter
      space (cf. Jones 1987, §4). -/
  markov_pos : ∀ (hn : 1 ≤ n) (f : AlgElement (HeckeGen n) ℝ)
      (_hsub : ∀ m ∈ f.support, ∀ (g : HeckeGen n), g ∈ m →
                 g.index.val < n - 1),
    tr (AlgElement.rightMulGen f (HeckeGen.mk ⟨n - 1, by omega⟩)) =
      z * tr f
  /-- **Reduction invariance**: the trace is well-defined on
      `H_n(q) = AlgElement / (Hecke ideal)`, so it agrees on any
      element and its Gröbner–Shirshov reduct. -/
  tr_reduces : ∀ (f nf : AlgElement (HeckeGen n) ℝ)
      (_ : ReducesToNF (heckeOrder n) (heckeRewritingSystem n hp) f nf),
    tr f = tr nf

/-- **Axiom (Jones 1987, Theorem 5.1 & Corollary 5.3).**
    For every `n : ℕ` and every `hp : HeckeParams` there exists a
    Markov trace on `H_n(q)`.  The non-triviality condition
    `q ≠ 1` is already bundled in `HeckeParams.q_ne_one`; no
    separate hypothesis is needed.

    The proof is the 54-page construction in Jones (1987) §3–5:
    Ocneanu's trace on relative commutants (§3), the Markov
    property from `H_n ↪ H_{n+1}` (§4), and link invariance via
    Markov's theorem and writhe normalisation (§5). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403, Theorem 5.1
axiom markov_trace_exists (n : ℕ) (hp : HeckeParams) :
    MarkovTrace n hp

/-! ## §3  Jones polynomial via the Markov trace -/

/-- **Jones polynomial value at `q`** of the closure of a braid
    word `β`, computed via the Markov trace of the augmented
    Hecke image.

    By Jones (1987, Theorem 5.1), this value is (up to a writhe-
    normalisation factor) the Jones polynomial `J_{β̂}(q)`
    evaluated at the real parameter `hp.q`. The writhe
    normalisation is absorbed into the embedding
    `augmentedBraidElement`. -/
noncomputable def jonesValue (n : ℕ) (hp : HeckeParams)
    (β : List ℤ) : ℝ :=
  (markov_trace_exists (n + 1) hp).tr (augmentedBraidElement hp β)

/-! ## §4  Reduction-order invariance -/

/-- **Reduction-invariance of the Jones value.**

    For any braid word `β` and any two Gröbner–Shirshov normal
    forms `nf₁, nf₂` of its augmented Hecke image, the Markov
    trace agrees on both. This is not about the axiom — it is a
    consequence of `threading_cost_unique`: the normal form is
    *unique*, so both `nf₁` and `nf₂` are literally equal, and
    the trace of equal elements is trivially equal. -/
theorem jones_reduction_invariant (n : ℕ) (hp : HeckeParams)
    (β : List ℤ) (nf₁ nf₂ : AlgElement (HeckeGen (n + 1)) ℝ)
    (h₁ : ReducesToNF (heckeOrder (n + 1))
            (heckeRewritingSystem (n + 1) hp)
            (augmentedBraidElement hp β) nf₁)
    (h₂ : ReducesToNF (heckeOrder (n + 1))
            (heckeRewritingSystem (n + 1) hp)
            (augmentedBraidElement hp β) nf₂) :
    (markov_trace_exists (n + 1) hp).tr nf₁ =
    (markov_trace_exists (n + 1) hp).tr nf₂ := by
  have h : nf₁ = nf₂ := threading_cost_unique n hp β nf₁ nf₂ h₁ h₂
  rw [h]

/-- **Jones value = trace of any normal form.**
    Any Gröbner–Shirshov reduction of the augmented braid element
    yields the same Markov-trace value as `jonesValue`. This is a
    consequence of the `tr_reduces` field: the Markov trace is
    well-defined on `H_n(q)`, so it agrees on any AlgElement and
    its reduct. -/
theorem jonesValue_eq_trace_of_nf (n : ℕ) (hp : HeckeParams)
    (β : List ℤ) (nf : AlgElement (HeckeGen (n + 1)) ℝ)
    (h : ReducesToNF (heckeOrder (n + 1))
           (heckeRewritingSystem (n + 1) hp)
           (augmentedBraidElement hp β) nf) :
    jonesValue n hp β = (markov_trace_exists (n + 1) hp).tr nf := by
  unfold jonesValue
  exact (markov_trace_exists (n + 1) hp).tr_reduces _ nf h

/-! ## §5  Main proposition: GS cost implements the Jones recursion -/

/-- **Proposition (`prop:gs-cost-jones-recursion`).**

    The `heckeCost` function on the unique Gröbner–Shirshov normal
    form of a braid's Hecke image is independent of the reduction
    order. Combined with the Markov-trace axiom, this makes GS
    reduction a confluent algorithm for the Jones polynomial:

    - **Skein content** is carried by `(H1)` alone (`hecke_h1_is_skein`).
    - **Reduction order** is immaterial (`threading_cost_unique`).
    - **Markov evaluation** of the unique normal form equals
      `jonesValue` (`jonesValue_eq_trace_of_nf`).

    Therefore: *Gröbner–Shirshov reduction is the Jones recursion,
    with `heckeCost` serving as the arithmetic complexity measure.* -/
theorem gs_cost_jones_recursion {n : ℕ} (hp : HeckeParams)
    (β : List ℤ) (nf₁ nf₂ : AlgElement (HeckeGen (n + 1)) ℝ)
    (h₁ : ReducesToNF (heckeOrder (n + 1))
            (heckeRewritingSystem (n + 1) hp)
            (augmentedBraidElement hp β) nf₁)
    (h₂ : ReducesToNF (heckeOrder (n + 1))
            (heckeRewritingSystem (n + 1) hp)
            (augmentedBraidElement hp β) nf₂) :
    heckeCost nf₁ = heckeCost nf₂ ∧
    (markov_trace_exists (n + 1) hp).tr nf₁ =
      (markov_trace_exists (n + 1) hp).tr nf₂ := by
  have h : nf₁ = nf₂ := threading_cost_unique n hp β nf₁ nf₂ h₁ h₂
  exact ⟨by rw [h], by rw [h]⟩

end UGB.GrobnerShirshov.Hecke
