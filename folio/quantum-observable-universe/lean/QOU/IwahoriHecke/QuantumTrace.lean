import QOU.IwahoriHecke.TensorEmbedding

/-!
# The site-weighted (quantum) trace on the R-matrix representation

`QOU.IwahoriHecke.BraidingTrace` joined the braiding to the classical character **at
`q = 1`**, and said plainly that the `q ≠ 1` bridge was open. This file supplies the
structure that bridge needs.

## Why the plain trace is the wrong functional

`QOU.MathlibExt.MarkovTrace` defines `markovTrace ρ w = ρ.character w` — the **plain**
matrix trace of a braid word — and proves it cyclic. That is correct as far as it goes, and
it is not the Markov trace of the R-matrix representation: for a quantum-group braiding one
must weight the trace site-by-site,

    tr_w(x) = tr(W · ρ(x)),   W = diagonal (fun a => ∏ₘ w (a m)),

which is the *quantum* trace. `QOU.MassTheory.WeightedPermutationCharacter` computes exactly
this weighted trace for a **permutation**, with the physical weight `w = (1, q²)`. This file
computes the same shape for the **braiding**.

## The content

**`braidAt_comm_siteWeight`** — the braiding commutes with the site weight, for **every**
weight `w : Fin 2 → R`, with no condition on `w` at all.

That is stronger than one might expect and the reason is structural: `Ř`'s only off-diagonal
entries connect `e_i ⊗ e_j` to `e_j ⊗ e_i`, and those two basis states carry the *same*
site-weight `w i · w j`. So the weight cannot tell them apart, whatever it is. Concretely,
whenever `Ř_{ij} a b ≠ 0`, either `a = b` or `b = a ∘ (i j)` — and a permutation of the sites
does not change `∏ₘ w (a m)`.

From it:

* **`qTrace_sigma_mul_comm`** — cyclicity `tr_w(σ_a · y) = tr_w(y · σ_a)` when one factor is a
  generator;
* **`qTrace_one`** — `tr_w(1) = (∑ₖ w k)^n`, which is `weighted_permutation_character`'s value
  at the identity permutation, so the two agree where they overlap;
* **`qTrace_smul_one`** at the physical weight `w = (1, q²)`: `tr_w(1) = (1 + q²)^n`.

## 🛑 What is still missing, and it is the deep half

**The Markov axiom is not here.** A Markov trace must satisfy `tr(x σ_n) = z · tr(x)` for
`x` in the smaller algebra — the *peel* — and that is the property the Jones polynomial
actually consumes. It needs the tower `H_n(q) ⊆ H_{n+1}(q)` and a compatibility between the
weight and the extra strand. Nothing here supplies it, and `QOU.MathlibExt.MarkovTrace`'s own
docstring records the same gap for the weighted block traces ("not the normalisation
`tr_M(1) = 1` nor the Markov peel axiom").

**Full cyclicity is not here either.** `qTrace_sigma_mul_comm` covers the case where one
factor is a *generator*, which is what the commutation lemma gives directly. Extending it to
`tr_w(xy) = tr_w(yx)` for arbitrary `x` needs the image of the action to lie in the
centralizer of `W`, i.e. an induction over the algebra rather than over its generators.

So: the weighted trace exists on the actual R-matrix representation, it is compatible with
the weight, and it agrees with the permutation character where they meet. It is **not** yet
a Markov trace, and this file does not call it one.

-- Ref: [jones1987] Hecke algebra representations of braid groups and link polynomials
-- Ref: [jimbo1986]; [leitner2026] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.QuantumTrace

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open Equiv Finset

variable {R : Type*} [CommRing R] {n : ℕ} {i j : Fin n} (q qi : R)

/-! ## The site weight -/

/-- The **site-wise weight** on `V^{⊗n}`: the diagonal matrix whose entry at a basis state
`a` is the product of the per-site weights `∏ₘ w (a m)`. For `w = (1, q²)` this is the
`K^{⊗n}` of the quantum trace. -/
def siteWeight (w : Fin 2 → R) : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R :=
  Matrix.diagonal (fun a => ∏ m, w (a m))

/-- Permuting the sites does not change the total weight. -/
theorem prod_weight_comp_equiv (w : Fin 2 → R) (a : Fin n → Fin 2) (e : Equiv.Perm (Fin n)) :
    (∏ m, w (a (e m))) = ∏ m, w (a m) :=
  Fintype.prod_equiv e _ _ (fun _ => rfl)

/-- A nonzero entry of `Ř` sits either on the diagonal or on the transposed diagonal. -/
private theorem rCheck_ne_zero_cases {u v : Fin 2 × Fin 2} (h : rCheck q qi u v ≠ 0) :
    u = v ∨ u = (v.2, v.1) := by
  by_contra hc
  push_neg at hc
  rw [rCheck_apply, if_neg hc.1, if_neg hc.2] at h
  exact h rfl

/-- **A nonzero braiding entry connects states of equal weight.**

The two cases are the whole reason the commutation below needs no hypothesis on `w`: a
nonzero entry either sits on the diagonal (`a = b`), or is the swap entry, in which case
`b = a ∘ (i j)` — and permuting sites leaves `∏ₘ w (a m)` alone. -/
theorem prod_weight_eq_of_braidAt_ne_zero (w : Fin 2 → R) {a b : Fin n → Fin 2}
    (hz : braidAt q qi i j a b ≠ 0) :
    (∏ m, w (a m)) = ∏ m, w (b m) := by
  classical
  rw [braidAt, embedPair_apply] at hz
  by_cases hoff : ∀ m, m ≠ i → m ≠ j → a m = b m
  · rw [if_pos hoff] at hz
    rcases rCheck_ne_zero_cases q qi hz with hd | hs
    · -- diagonal: `a` and `b` agree everywhere
      have : a = b := by
        funext m
        by_cases hmi : m = i
        · subst hmi; exact congrArg Prod.fst hd
        · by_cases hmj : m = j
          · subst hmj; exact congrArg Prod.snd hd
          · exact hoff m hmi hmj
      rw [this]
    · -- swap entry: `b = a ∘ (i j)`
      have hb : ∀ m, b m = a (Equiv.swap i j m) := by
        intro m
        by_cases hmi : m = i
        · subst hmi; rw [Equiv.swap_apply_left]; exact (congrArg Prod.snd hs).symm
        · by_cases hmj : m = j
          · subst hmj; rw [Equiv.swap_apply_right]; exact (congrArg Prod.fst hs).symm
          · rw [Equiv.swap_apply_of_ne_of_ne hmi hmj]; exact (hoff m hmi hmj).symm
      calc (∏ m, w (a m)) = ∏ m, w (a (Equiv.swap i j m)) :=
            (prod_weight_comp_equiv w a (Equiv.swap i j)).symm
        _ = ∏ m, w (b m) := Finset.prod_congr rfl (fun m _ => by rw [hb m])
  · rw [if_neg hoff] at hz; exact absurd rfl hz

/-- **The braiding commutes with the site weight — for every weight.**

No hypothesis on `w`. `Ř`'s off-diagonal entries connect `e_i ⊗ e_j` to `e_j ⊗ e_i`, which
carry the same site weight, so the weight cannot separate them. This is the Cartan-level
equivariance of Jimbo's `Ř`, and it is what makes the weighted trace below a *trace*. -/
theorem braidAt_comm_siteWeight (w : Fin 2 → R) :
    braidAt q qi i j * siteWeight w = siteWeight (n := n) w * braidAt q qi i j := by
  classical
  ext a b
  rw [siteWeight, Matrix.mul_diagonal, Matrix.diagonal_mul]
  by_cases hz : braidAt q qi i j a b = 0
  · rw [hz, zero_mul, mul_zero]
  · rw [prod_weight_eq_of_braidAt_ne_zero q qi w hz, mul_comm]

/-! ## The weighted trace -/

variable {m : ℕ}

/-- **The site-weighted (quantum) trace** of an element of `H_{m+1}(q)`, through the
R-matrix representation: `tr_w(x) = tr(W · ρ(x))`. -/
noncomputable def qTrace (hqi : q * qi = 1) (w : Fin 2 → R)
    (x : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) : R :=
  Matrix.trace (siteWeight w * heckeActionN q qi hqi x)

/-- **The weighted trace of the identity** is the `n`-th power of the total weight,
`(∑ₖ w k)^{m+1}`.

This is exactly `QOU.MassTheory.WeightedPermutationCharacter`'s value at the identity
permutation, so the braiding's weighted trace and the permutation character agree where they
overlap. -/
theorem qTrace_one (hqi : q * qi = 1) (w : Fin 2 → R) :
    qTrace q qi (m := m) hqi w 1 = (∑ k, w k) ^ (m + 1) := by
  classical
  rw [qTrace, map_one, mul_one, siteWeight, Matrix.trace_diagonal]
  rw [show ((∑ k, w k) ^ (m + 1)) = ∏ _x : Fin (m + 1), ∑ k, w k by
    rw [Finset.prod_const, Finset.card_univ, Fintype.card_fin]]
  exact (Fintype.prod_sum (fun (_ : Fin (m + 1)) (k : Fin 2) => w k)).symm

/-- **Cyclicity against a generator.** `tr_w(σ_a · y) = tr_w(y · σ_a)`.

This is what `braidAt_comm_siteWeight` gives directly: the weight can be moved past the
generator's image, and the ordinary trace is cyclic. Extending it to arbitrary `x` in place
of `σ_a` would need the whole image to centralise `W`, which is an induction over the
algebra rather than over its generators — see the module docstring. -/
theorem qTrace_sigma_mul_comm (hqi : q * qi = 1) (w : Fin 2 → R) (a : Fin m)
    (y : QOU.IwahoriHecke.Balanced.BalancedHecke (coxA m) q) :
    qTrace q qi hqi w (QOU.IwahoriHecke.Balanced.sigma (coxA m) q qi a * y)
      = qTrace q qi hqi w (y * QOU.IwahoriHecke.Balanced.sigma (coxA m) q qi a) := by
  classical
  have hcomm : siteWeight (n := m + 1) w * strandBraid q qi a
      = strandBraid q qi a * siteWeight w :=
    (braidAt_comm_siteWeight q qi w).symm
  rw [qTrace, qTrace, map_mul, map_mul, heckeActionN_sigma]
  calc Matrix.trace (siteWeight w * (strandBraid q qi a * heckeActionN q qi hqi y))
      = Matrix.trace ((siteWeight w * strandBraid q qi a) * heckeActionN q qi hqi y) := by
        rw [mul_assoc]
    _ = Matrix.trace (heckeActionN q qi hqi y * (siteWeight w * strandBraid q qi a)) :=
        Matrix.trace_mul_comm _ _
    _ = Matrix.trace (siteWeight w * (heckeActionN q qi hqi y * strandBraid q qi a)) := by
        rw [hcomm, ← mul_assoc, ← mul_assoc, Matrix.trace_mul_comm]
        congr 1
        noncomm_ring

/-! ## The physical weight -/

/-- At the physical weight `w = (1, q²)` — the `K = diag(1, q²)` of the corpus's
Schur–Weyl normalisation — the weighted trace of the identity is `(1 + q²)^{m+1}`. -/
theorem qTrace_one_physical (hqi : q * qi = 1) :
    qTrace q qi (m := m) hqi ![1, q ^ 2] 1 = (1 + q ^ 2) ^ (m + 1) := by
  rw [qTrace_one]
  congr 1
  simp [Fin.sum_univ_two]

end QOU.IwahoriHecke.QuantumTrace
