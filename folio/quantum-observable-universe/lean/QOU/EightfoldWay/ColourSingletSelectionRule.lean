import QOU.EightfoldWay.AlternatingChannelRowCap

/-!
# QOU.EightfoldWay.ColourSingletSelectionRule — the selection rule, with its inputs named

Item 7 of the eightfold-way open problems: *colour antisymmetric and spin symmetric force
flavour symmetric*, so the decuplet sits in the symmetric flavour channel.  The chapter
derives neither input.  This module proves the step **between** the inputs and the
conclusion, so that what remains open is exactly the inputs.

Model three quarks by index triples: colour `c : Fin 3 → Fin N_c` and everything else
(spin ⊗ flavour) `r : Fin 3 → R`, with `S₃` permuting the three quarks simultaneously.

* `colourSinglet_eq_smul_det` — at `N_c = 3` the colour-singlet channel is **one-dimensional**:
  every alternating colour function is a multiple of the determinant.
* `symmetric_of_alternating_product` — **the selection rule.**  If the total wavefunction
  `χ(c) · φ(r)` is alternating under `S₃` (Fermi statistics) and the colour factor `χ` is a
  nonzero colour singlet (alternating), then the spin ⊗ flavour factor `φ` is **symmetric**.

## The two inputs, labelled

1. **Fermi statistics** (the total wavefunction is alternating) — an input; spin–statistics is
   not derived in this framework.
2. **Colour singlet** (the colour factor is alternating) — an input; it is the confinement
   requirement, and the colour triple itself is the octonionic one
   (`OctonionColourTripletComplexType`), not a construction from braids.

What stays cited: the Cauchy decomposition
`Sym³(A ⊗ B) = Sym³A ⊗ Sym³B ⊕ S_{(2,1)}A ⊗ S_{(2,1)}B ⊕ Λ³A ⊗ Λ³B`, which pairs spin `3/2`
with the decuplet and spin `1/2` with the octet (`4·10 + 2·8 + 0·1 = 56`).

Base ring `ℚ`; no empirical input.
-/

namespace QOU.EightfoldWay.ColourSingletSelectionRule

open Equiv QOU.EightfoldWay.AlternatingChannelRowCap

/-- An alternating function vanishes on every triple with a repeated value. -/
theorem alt_eq_zero_of_not_injective {N : ℕ} {f : Cube N} (hf : f ∈ altChannel N)
    {t : Fin 3 → Fin N} (ht : ¬ Function.Injective t) : f t = 0 := by
  obtain ⟨i, j, htij, hij⟩ : ∃ i j, t i = t j ∧ i ≠ j := by
    by_contra h
    push_neg at h
    exact ht (fun i j hij => h i j hij)
  have hfix : t ∘ (swap i j : Perm (Fin 3)) = t := by
    funext k
    simp only [Function.comp_apply]
    by_cases hki : k = i
    · subst hki; simp [swap_apply_left, htij]
    · by_cases hkj : k = j
      · subst hkj; simp [swap_apply_right, htij]
      · simp [swap_apply_of_ne_of_ne hki hkj]
  have h := hf (swap i j) t
  rw [hfix, Perm.sign_swap hij] at h
  push_cast at h
  linarith

/-- The identity triple `(0, 1, 2)` in `Fin 3`. -/
def idTriple : Fin 3 → Fin 3 := fun i => i

theorem detWitness_idTriple : detWitness 3 idTriple = 1 := by
  have : (Matrix.of fun i j : Fin 3 =>
      if ((idTriple i : Fin 3) : ℕ) = (j : ℕ) then (1 : ℚ) else 0) = 1 := by
    ext i j
    simp [idTriple, Matrix.one_apply, Fin.ext_iff]
  simp [detWitness, this]

/-- **The colour-singlet channel at `N_c = 3` is one-dimensional**: every alternating colour
function is `f(0,1,2)` times the determinant. -/
theorem colourSinglet_eq_smul_det {f : Cube 3} (hf : f ∈ altChannel 3) :
    f = f idTriple • detWitness 3 := by
  funext t
  simp only [Pi.smul_apply, smul_eq_mul]
  by_cases ht : Function.Injective t
  · have hb : Function.Bijective t := (Finite.injective_iff_bijective).mp ht
    let σ : Perm (Fin 3) := Equiv.ofBijective t hb
    have hts : t = idTriple ∘ σ := by
      funext k; simp [σ, idTriple]
    rw [hts, hf σ idTriple, detWitness_mem 3 σ idTriple, detWitness_idTriple]
    ring
  · rw [alt_eq_zero_of_not_injective hf ht,
      alt_eq_zero_of_not_injective (detWitness_mem 3) ht, mul_zero]

/-- **Selection rule.**  If `χ(c)·φ(r)` is alternating under simultaneous permutation of the
three quarks (Fermi statistics) and `χ` is a nonzero colour singlet, then `φ` is symmetric. -/
theorem symmetric_of_alternating_product {N : ℕ} {R : Type*}
    (χ : Cube N) (φ : (Fin 3 → R) → ℚ)
    (hχ : χ ∈ altChannel N) (hχ0 : χ ≠ 0)
    (hΨ : ∀ (σ : Perm (Fin 3)) (c : Fin 3 → Fin N) (r : Fin 3 → R),
      χ (c ∘ σ) * φ (r ∘ σ) = ((Perm.sign σ : ℤ) : ℚ) * (χ c * φ r)) :
    ∀ (σ : Perm (Fin 3)) (r : Fin 3 → R), φ (r ∘ σ) = φ r := by
  intro σ r
  obtain ⟨c, hc⟩ : ∃ c, χ c ≠ 0 := by
    by_contra h
    push_neg at h
    exact hχ0 (funext h)
  have h := hΨ σ c r
  rw [hχ σ c] at h
  have hs : ((Perm.sign σ : ℤ) : ℚ) ≠ 0 := by
    rcases Int.units_eq_one_or (Perm.sign σ) with h1 | h1 <;> simp [h1]
  have : ((Perm.sign σ : ℤ) : ℚ) * χ c * (φ (r ∘ σ) - φ r) = 0 := by
    linear_combination h
  rcases mul_eq_zero.mp this with h' | h'
  · rcases mul_eq_zero.mp h' with h'' | h''
    · exact absurd h'' hs
    · exact absurd h'' hc
  · linarith

/-- Combined, at `N_c = 3`: with the colour factor the determinant singlet, Fermi statistics
forces the spin ⊗ flavour factor into the symmetric channel. -/
theorem symmetric_of_det_colour {R : Type*} (φ : (Fin 3 → R) → ℚ)
    (hΨ : ∀ (σ : Perm (Fin 3)) (c : Fin 3 → Fin 3) (r : Fin 3 → R),
      detWitness 3 (c ∘ σ) * φ (r ∘ σ) =
        ((Perm.sign σ : ℤ) : ℚ) * (detWitness 3 c * φ r)) :
    ∀ (σ : Perm (Fin 3)) (r : Fin 3 → R), φ (r ∘ σ) = φ r :=
  symmetric_of_alternating_product _ φ (detWitness_mem 3) (detWitness_ne_zero le_rfl) hΨ

end QOU.EightfoldWay.ColourSingletSelectionRule
