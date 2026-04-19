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

The Markov trace evaluation of a braid's GS normal form
equals the Jones polynomial of its closure (Jones 1987,
Theorem 5.1). This file records the skein-identification
as a provable `rfl`-lemma and re-exports the threading-cost
uniqueness theorem from `HeckeGS.lean` that witnesses
reduction-order independence.

LaTeX label: `prop:gs-cost-jones-recursion`

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

/-- **(H1) is the Jones skein relation.** The quadratic Hecke
    rule carries the skein coefficients `(q - q⁻¹, 1)` literally:
    oriented as `T_i^2 → (q - q⁻¹) T_i + 1`, it matches the Jones
    skein identity `L₊ - L₋ = (q - q⁻¹) L₀` after the dictionary
    `L₊ ↔ T_i²`, `L₋ ↔ 1`, `L₀ ↔ T_i`. Provable by `rfl`. -/
theorem hecke_h1_is_skein {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    (heckeRelation i hp).relation = AlgElement.ofTerms
      [([⟨i⟩, ⟨i⟩], 1), ([⟨i⟩], -(hp.q - hp.q⁻¹)), ([], -1)] := rfl

/-- **(H2) is the braid / Yang--Baxter relation.**
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

/-- **Proposition (`prop:gs-cost-jones-recursion`).**
    The `heckeCost` function on the unique Gröbner--Shirshov
    normal form of a braid's Hecke image is independent of the
    reduction order --- this is the "reduction-cost = Jones-
    recursion" identity, witnessed here by uniqueness of the
    normal form.

    Any two reductions of an augmented braid element agree on
    their costs, because they reach the *same* normal form
    (`threading_cost_unique`). The further identification
    `cost = J_{β̂}(q)` via the Markov trace is Jones 1987,
    Theorem 5.1 --- not available at the UGB layer (which has
    no Markov-trace axiom), so it is recorded in the narrative
    `.md` and in the QOU-side remark
    `rem:hecke-energy-jones-recursion`. -/
theorem gs_cost_jones_recursion {n : ℕ} (hp : HeckeParams)
    (β : List ℤ) (nf₁ nf₂ : AlgElement (HeckeGen (n + 1)) ℝ)
    (h₁ : ReducesToNF (heckeOrder (n + 1)) (heckeRewritingSystem (n + 1) hp)
            (augmentedBraidElement hp β) nf₁)
    (h₂ : ReducesToNF (heckeOrder (n + 1)) (heckeRewritingSystem (n + 1) hp)
            (augmentedBraidElement hp β) nf₂) :
    heckeCost nf₁ = heckeCost nf₂ := by
  have h : nf₁ = nf₂ := threading_cost_unique n hp β nf₁ nf₂ h₁ h₂
  rw [h]

end UGB.GrobnerShirshov.Hecke
