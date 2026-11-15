/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).
-/
import QOU.MathlibExt.BraidedBlockShiftTrace
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Ring

/-!
# Unbonded particles have no Gram geometry beyond their species

Issue #7895, round 5.  Nodes are particles: elements `a`, `b` of a braided
Markov tower supported on disjoint strand windows (`a ∈ H n`, `b ∈ shifted n`).

1. `connected_eq_zero`: the connected two-point function
   `tr (a * b) - tr a * tr b` vanishes.  This is the corpus disjoint-block law
   `HeckeSandwichReduces.disjointBlock_of_braided`, restated as a statement
   about correlations.
2. `distSq_eq_of_factorised`, `distSq_species`: for any symmetric bilinear
   "Gram" whose off-diagonal entries factorise as `t i * t j`, the squared
   distance `G i i + G j j - 2 G i j` is a function of the pair of diagonal data
   `(G i i, t i)`, `(G j j, t j)` only.  Particles of equal species data are
   pairwise equidistant: the configuration is a regular simplex, whatever the
   windows' positions.

So any nearness between particles must come from letters that straddle two
windows (bond letters).  Nothing here selects a bond.

3. `cov_eq_zero_of_left`, `cov_eq_zero_of_right`: in the state `x ↦ tr (P x)` of
   a bond element `P`, two particles are still uncorrelated whenever one cut
   separates them with `P` on one side.  A γγ letter `V = σ_g σ_{g+1}⁻¹` (or any
   power) uses two adjacent generators; when the windows' nearest interior
   generators are two apart (`3i+1`, `3i+3`), every such `P = β^T β` lies on one
   side of a cut, so a single γγ letter cannot correlate two particles.  Only a
   bond word whose letters reach both windows' interiors can.
4. `cov_eq_zero_of_chain`: in a chain `0 — 1 — 2` the end particles are
   uncorrelated whatever the bonds are: correlation is strictly
   nearest-neighbour along the bond graph.

Base ring: generic `CommRing R` for (1), `CommRing` for (2); no ordering.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] issue #7895.
-/

namespace QOU.Optimization.ParticleGram

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
  QOU.MathlibExt.HeckeSandwichReduces

section Tower

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A) [BraidedTower T]

/-- On a braided tower, two particles on disjoint strand windows are uncorrelated. -/
theorem connected_eq_zero {n : ℕ} {a b : A} (ha : a ∈ T.H n) (hb : b ∈ shifted T n) :
    T.tr (a * b) - T.tr a * T.tr b = 0 := by
  rw [disjointBlock_of_braided T n a ha b hb, sub_self]

/-- Unnormalised covariance of `a`, `b` in the state `x ↦ tr (P x)` (up to `tr P`):
`tr (a P b) tr P - tr (a P) tr (P b)`.  Dividing by `(tr P)²` gives the
covariance `⟨a, b⟩ - ⟨a, 1⟩⟨1, b⟩` of the probe. -/
def cov (a P b : A) : R := T.tr (a * P * b) * T.tr P - T.tr (a * P) * T.tr (P * b)

/-- **Cut on the right.**  If the bond element `P` and the left particle `a` both
live below the cut (`H n`) and the right particle above it (`shifted n`), the
covariance vanishes. -/
theorem cov_eq_zero_of_left {n : ℕ} {a P b : A} (ha : a ∈ T.H n) (hP : P ∈ T.H n)
    (hb : b ∈ shifted T n) : cov T a P b = 0 := by
  have hD := disjointBlock_of_braided T
  rw [cov, hD n (a * P) (Subalgebra.mul_mem _ ha hP) b hb, hD n P hP b hb]; ring

/-- **Cut on the left.**  If `P` and the right particle live above the cut and the
left particle below it, the covariance vanishes. -/
theorem cov_eq_zero_of_right {n : ℕ} {a P b : A} (ha : a ∈ T.H n) (hP : P ∈ shifted T n)
    (hb : b ∈ shifted T n) : cov T a P b = 0 := by
  have hD := disjointBlock_of_braided T
  rw [cov, mul_assoc, hD n a ha (P * b) (Subalgebra.mul_mem _ hP hb), hD n a ha P hP]; ring

/-- **Bond locality (no next-nearest correlation).**  Let the nucleus bond element
be `P = Rᵗ M R` with the left bond part `M` below the cut (`H n`) and the right
bond part `R`, `Rᵗ` above it (`shifted n`).  If the left particle `a ∈ H n`
commutes with `Rᵗ` (it is far from the right bond) and the right particle
`b ∈ shifted n`, then `a` and `b` are uncorrelated in the state of `P`.  This is
the case of particles `0` and `2` of a chain `0 — 1 — 2` with bonds `B₀`, `B₁`,
`P = B₁ᵗ B₀ᵗ B₀ B₁`, `M = B₀ᵗ B₀`, `R = B₁`, cut between the two bonds. -/
theorem cov_eq_zero_of_chain {n : ℕ} {a M R Rt b : A} (ha : a ∈ T.H n) (hM : M ∈ T.H n)
    (hR : R ∈ shifted T n) (hRt : Rt ∈ shifted T n) (hb : b ∈ shifted T n)
    (hc : a * Rt = Rt * a) : cov T a (Rt * M * R) b = 0 := by
  have hD := disjointBlock_of_braided T
  have haM : a * M ∈ T.H n := Subalgebra.mul_mem _ ha hM
  have hRbR : R * b * Rt ∈ shifted T n :=
    Subalgebra.mul_mem _ (Subalgebra.mul_mem _ hR hb) hRt
  have hRR : R * Rt ∈ shifted T n := Subalgebra.mul_mem _ hR hRt
  have e1 : T.tr (a * (Rt * M * R) * b) = T.tr (a * M) * T.tr (R * b * Rt) := by
    rw [show a * (Rt * M * R) * b = Rt * ((a * M) * (R * b)) by
          rw [show a * (Rt * M * R) * b = (a * Rt) * M * R * b by noncomm_ring, hc]; noncomm_ring,
      T.tr_mul_comm, show a * M * (R * b) * Rt = (a * M) * (R * b * Rt) by noncomm_ring,
      hD n _ haM _ hRbR]
  have e2 : T.tr (Rt * M * R) = T.tr M * T.tr (R * Rt) := by
    rw [mul_assoc, T.tr_mul_comm, mul_assoc, hD n _ hM _ hRR]
  have e3 : T.tr (a * (Rt * M * R)) = T.tr (a * M) * T.tr (R * Rt) := by
    rw [show a * (Rt * M * R) = Rt * ((a * M) * R) by
          rw [show a * (Rt * M * R) = (a * Rt) * M * R by noncomm_ring, hc]; noncomm_ring,
      T.tr_mul_comm, mul_assoc, hD n _ haM _ hRR]
  have e4 : T.tr (Rt * M * R * b) = T.tr M * T.tr (R * b * Rt) := by
    rw [show Rt * M * R * b = Rt * (M * (R * b)) by noncomm_ring, T.tr_mul_comm,
      show M * (R * b) * Rt = M * (R * b * Rt) by noncomm_ring, hD n _ hM _ hRbR]
  rw [cov, e1, e2, e3, e4]; ring

end Tower

section Gram

variable {R : Type*} [CommRing R] {ι : Type*}

/-- Squared Gram distance `G i i + G j j - 2 G i j`. -/
def distSq (G : ι → ι → R) (i j : ι) : R := G i i + G j j - 2 * G i j

/-- If the off-diagonal entry factorises, the distance depends only on the
diagonal data and the one-point values. -/
theorem distSq_eq_of_factorised (G : ι → ι → R) (t : ι → R) {i j : ι}
    (hij : G i j = t i * t j) : distSq G i j = G i i + G j j - 2 * (t i * t j) := by
  rw [distSq, hij]

/-- **Species law.**  If every off-diagonal entry factorises and the diagonal
and one-point data depend only on a species label `s`, then two pairs of
distinct particles with the same species labels are at the same distance. -/
theorem distSq_species {S : Type*} (G : ι → ι → R) (t : ι → R) (s : ι → S)
    (a : S → R) (τ : S → R) (hdiag : ∀ i, G i i = a (s i)) (ht : ∀ i, t i = τ (s i))
    (hoff : ∀ i j, i ≠ j → G i j = t i * t j) {i j k l : ι} (hij : i ≠ j) (hkl : k ≠ l)
    (hs1 : s i = s k) (hs2 : s j = s l) : distSq G i j = distSq G k l := by
  rw [distSq_eq_of_factorised G t (hoff i j hij), distSq_eq_of_factorised G t (hoff k l hkl),
    hdiag, hdiag, hdiag, hdiag, ht, ht, ht, ht, hs1, hs2]

/-- One species: every pair of distinct particles is at squared distance
`2 (a - τ²)`, i.e. the particles form a regular simplex. -/
theorem distSq_one_species (G : ι → ι → R) (a τ : R) (hdiag : ∀ i, G i i = a)
    (hoff : ∀ i j, i ≠ j → G i j = τ * τ) {i j : ι} (hij : i ≠ j) :
    distSq G i j = 2 * (a - τ * τ) := by
  rw [distSq, hdiag, hdiag, hoff i j hij]; ring

end Gram

end QOU.Optimization.ParticleGram
