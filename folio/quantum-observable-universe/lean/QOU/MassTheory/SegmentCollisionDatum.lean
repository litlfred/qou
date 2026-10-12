/-
# Segment collision datum — the owner's 2026-10-12 reformulation of `RelativeReebDatum`

Owner, 2026-10-12 (verbatim gist): two knot particles approach along a direction in
computational space-time; at the exceptional divisor it is not the whole knot that meets
the point `p` but **one braid segment from each**; the collision should take the incoming
angle that is a relative minimum of the rotational energy (O'Hara + Bring); the segment's
contribution lives on the fundamental weights; the unknown substrate phase is the
categorical trace of the γγ entanglement history, taken as a limit inside the two
light cones. This file states the three structural claims that picture rests on, and
proves what can be proved.

## Part A — the single-segment marginal is UNIVERSAL (generic `R`)

The bridge between the two particles is one generator `g n`, with particle `a` below it
(`a ∈ H n`) and particle `b` above it (`b ∈ shifted (n+1)`). Under the disjoint-block law
(`DisjointBlockMultiplicative`, conditional in the corpus on the classical `TowerSpan`),
the functional the bridge sees, `c ↦ tr (a * c * b)` on `span {1, g n}`, is

    tr (a * b)       = tr a * tr b,
    tr (a * g n * b) = z * (tr a * tr b),

so the state on the colliding pair is the universal Markov state `(1, z)` scaled by
`tr a * tr b`. **The whole history of each particle enters only through its total trace.**
That is the owner's "the unknown initial photonic state does not matter", and it is a
theorem here, conditional only on the disjoint-block law: the iterated conditional
expectation the owner describes already lands on the scalar.

The same fact is the negative half: a single-segment collision can see nothing of either
history except its trace, so it cannot tell two particles with the same trace apart. The
probe `segment_collision_probe.py` measures the dichotomy: one segment from each, the local
ratio is exactly `z` for every pair; two segments from either side, it is not.

## Part B — the two fundamental channels (generic field)

On `□ ⊗ □ = Sym ⊕ Alt`, `g` acts as `q` and `−q⁻¹`. A state with total `t` and
`g`-expectation `z t` puts weight `t (z q + 1)/(q² + 1)` on Sym and `t q (q − z)/(q² + 1)`
on Alt. At convention D, `z = q³/(q² + 1)`, these are `t (q⁴+q²+1)/(q²+1)²` and
`t q²/(q²+1)²`; both are nonzero, so both channels are live at the collision (the D
annihilation `y_(1³) = 0` is a three-row statement and does not reach a two-box bridge).

## Part C — the local O'Hara term is CHIRALITY-BLIND (archimedean, `ℝ`)

The cross term of the Möbius/O'Hara energy between two straight segments of half-length
`ℓ` through closest points at distance `d`, meeting at angle `θ`, is
`∫∫ ds dt / (d² + s² + t² − 2 s t cos θ)`. Reversing one segment (`θ ↦ π − θ`) is the
reflection `t ↦ −t`, so the energy is invariant. Reversing one strand's orientation with
over/under fixed flips the crossing sign, `σ ↔ σ⁻¹`; the energy also depends on `d`
only through `d²`, so it is blind to over/under as well. Consequence
(`minimiser_eq_pi_div_two`): if the total energy is reflection-symmetric and has a
unique minimiser on `(0, π)`, that minimiser is the perpendicular crossing `π/2`.
**Any selection of `σ` over `σ⁻¹` at the collision must come from a chiral term,
the Bring part or the light-cone data, never from O'Hara.** Scope (b), invariant:
the reflection.

## Part D — the datum itself: a primary conjecture class, no instance

`SegmentCollisionDatum d ℓ` carries the Bring part of the local energy and the selected
angle, with the two clauses that make the selection well posed (minimiser, unique).
§3b-cond: the consequence is stated as a theorem taking the class as hypothesis.

§7c: Parts A and B over generic `R` / field `K`; Parts C and D over `ℝ` because
`Real.cos`, the integral and the order on angles are archimedean.

-- Ref: [manuscript] rem:light-cone-affine; meridian-exceptional-divisor-note;
   lem:bring-cone-reeb-quaternionic-twist; bean qou-jfx8 (reformulation), qou-pzsi
   (route 1, flowed O'Hara link energy), qou-uh5f (Möbius constant)
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import QOU.MathlibExt.DisjointBlockTraceLaw
import QOU.Brings.BringUTContactChirality

namespace QOU.MassTheory.SegmentCollision

/-! ## Part A — the single-segment marginal is universal -/

section PartA

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- **The bridge sees the free product.** Particle `a` below the bridge, particle `b`
above it: their unbridged composite has trace `tr a * tr b`. -/
theorem bridge_free (hD : DisjointBlockMultiplicative T) (n : ℕ)
    (a : A) (ha : a ∈ T.H n) (b : A) (hb : b ∈ shifted T (n + 1)) :
    T.tr (a * b) = T.tr a * T.tr b :=
  hD (n + 1) a (T.H_mono (Nat.le_succ n) ha) b hb

/-- **The bridge crossing sees only `z` times the free product.** -/
theorem bridge_crossing (hD : DisjointBlockMultiplicative T) (n : ℕ)
    (a : A) (ha : a ∈ T.H n) (b : A) (hb : b ∈ shifted T (n + 1)) :
    T.tr (a * T.g n * b) = T.z * (T.tr a * T.tr b) := by
  have hag : a * T.g n ∈ T.H (n + 1) :=
    (T.H (n + 1)).mul_mem (T.H_mono (Nat.le_succ n) ha) (T.g_mem n)
  rw [hD (n + 1) (a * T.g n) hag b hb, T.markov n a ha]
  ring

/-- **The inverse bridge crossing sees only `z⁻` times the free product.** -/
theorem bridge_crossing_inv (hD : DisjointBlockMultiplicative T) (n : ℕ)
    (a : A) (ha : a ∈ T.H n) (b : A) (hb : b ∈ shifted T (n + 1)) :
    T.tr (a * T.ginv n * b) = T.zinv * (T.tr a * T.tr b) := by
  have hag : a * T.ginv n ∈ T.H (n + 1) :=
    (T.H (n + 1)).mul_mem (T.H_mono (Nat.le_succ n) ha) (T.ginv_mem n)
  rw [hD (n + 1) (a * T.ginv n) hag b hb, T.markov_inv n a ha]
  ring

/-- **Universality of the single-segment marginal.** For every letter
`c = α + β g + γ g⁻¹` on the bridge, the collision functional is the universal
Markov value of `c` times `tr a * tr b`. Neither particle's history enters except
through its trace. -/
theorem bridge_local_state (hD : DisjointBlockMultiplicative T) (n : ℕ)
    (a : A) (ha : a ∈ T.H n) (b : A) (hb : b ∈ shifted T (n + 1)) (α β γ : R) :
    T.tr (a * (algebraMap R A α + β • T.g n + γ • T.ginv n) * b)
      = (α + β * T.z + γ * T.zinv) * (T.tr a * T.tr b) := by
  have e : a * (algebraMap R A α + β • T.g n + γ • T.ginv n) * b
      = α • (a * b) + β • (a * T.g n * b) + γ • (a * T.ginv n * b) := by
    simp only [mul_add, add_mul, Algebra.algebraMap_eq_smul_one, mul_smul_comm,
      smul_mul_assoc, mul_one]
  rw [e, map_add, map_add, map_smul, map_smul, map_smul,
    bridge_free T hD n a ha b hb, bridge_crossing T hD n a ha b hb,
    bridge_crossing_inv T hD n a ha b hb, smul_eq_mul, smul_eq_mul, smul_eq_mul]
  ring

/-- **Two particles with the same trace are indistinguishable to a single-segment
collision**, whatever their histories. -/
theorem bridge_cannot_separate (hD : DisjointBlockMultiplicative T) (n : ℕ)
    (a a' : A) (ha : a ∈ T.H n) (ha' : a' ∈ T.H n) (htr : T.tr a = T.tr a')
    (b : A) (hb : b ∈ shifted T (n + 1)) (α β γ : R) :
    T.tr (a * (algebraMap R A α + β • T.g n + γ • T.ginv n) * b)
      = T.tr (a' * (algebraMap R A α + β • T.g n + γ • T.ginv n) * b) := by
  rw [bridge_local_state T hD n a ha b hb, bridge_local_state T hD n a' ha' b hb, htr]

/-! ### Part E — a k-segment window is blind until it reaches a bond

A particle word factors as `a = L * N`: everything up to and including its top inter-nucleon
bond (`L ∈ H m`) times its top nucleon block (`N ∈ shifted m`). A collision window that
stays above the bond (`x ∈ shifted m`) sees `a` only through `tr L` and the top block. So
two particles with the same top block are separated by no window that stops short of the
bond. For the production `A = 3` chains the top block is 3 strands, so the window must be
at least 4 segments deep on that side (`segment_collision_probe.py`, part Q4). -/

/-- **Window factorisation.** -/
theorem window_factor (hD : DisjointBlockMultiplicative T) (m : ℕ)
    (L : A) (hL : L ∈ T.H m) (N : A) (hN : N ∈ shifted T m) (x : A) (hx : x ∈ shifted T m) :
    T.tr (L * N * x) = T.tr L * T.tr (N * x) := by
  rw [mul_assoc]
  exact hD m L hL (N * x) ((shifted T m).mul_mem hN hx)

/-- **Same top block ⇒ same window state.** Stated without division:
`tr(a x)·tr(a') = tr(a' x)·tr(a)` for `a = L N`, `a' = L' N`. -/
theorem window_cannot_separate (hD : DisjointBlockMultiplicative T) (m : ℕ)
    (L L' : A) (hL : L ∈ T.H m) (hL' : L' ∈ T.H m) (N : A) (hN : N ∈ shifted T m)
    (x : A) (hx : x ∈ shifted T m) :
    T.tr (L * N * x) * T.tr (L' * N) = T.tr (L' * N * x) * T.tr (L * N) := by
  have h1 := window_factor T hD m L hL N hN x hx
  have h2 := window_factor T hD m L' hL' N hN x hx
  have h3 := window_factor T hD m L hL N hN 1 (shifted T m).one_mem
  have h4 := window_factor T hD m L' hL' N hN 1 (shifted T m).one_mem
  simp only [mul_one] at h3 h4
  rw [h1, h2, h3, h4]
  ring

/-! ### Part F — the computational tower: solved sub-collisions compose by traces

Owner, 2026-10-12 (bean `qou-a1hh`): composing collisions up a tower (nucleons → nuclei →
molecules, e.g. C + O → CO), the cost of "solving" sub-computations grows. Under the
disjoint-block law a chain of already-solved pieces joined by single-crossing letters
needs only each piece's trace and one Markov value per bond: the composite trace is
`μ₁ μ₂ · tr a · tr b · tr c`. The cost of a composite is the sum of its parts' costs plus
`O(#bonds)`; what grows up the tower is only what a deeper window (Part E) must see.

Prior art: the same law was MEASURED on the production chains,
`tr(atom)/tr(free) = ∏(z_D + d_kind)` to 1e-50 on D, T, ³He, ⁴He
(`docs/audits/2026-09-16-sdp-analysis-entangled-deviation-and-light-cone-recursion.md`).
`chain3_trace` derives it from the disjoint-block law, which the corpus holds conditional on
`TowerSpan`; it does not remove that condition. -/

/-- A single-crossing bond letter at generator `n`. -/
def bondLetter (n : ℕ) (α β γ : R) : A := algebraMap R A α + β • T.g n + γ • T.ginv n

/-- **Three solved pieces, two single-crossing bonds**: the composite trace is the product
of the pieces' traces and the two bonds' Markov values. -/
theorem chain3_trace (hD : DisjointBlockMultiplicative T) (n m : ℕ) (hnm : n + 1 ≤ m)
    (a : A) (ha : a ∈ T.H n) (b : A) (hb : b ∈ shifted T (n + 1)) (hbm : b ∈ T.H m)
    (c : A) (hc : c ∈ shifted T (m + 1)) (α₁ β₁ γ₁ α₂ β₂ γ₂ : R) :
    T.tr (a * bondLetter T n α₁ β₁ γ₁ * b * bondLetter T m α₂ β₂ γ₂ * c)
      = (α₁ + β₁ * T.z + γ₁ * T.zinv) * (α₂ + β₂ * T.z + γ₂ * T.zinv)
          * (T.tr a * T.tr b * T.tr c) := by
  have hl : bondLetter T n α₁ β₁ γ₁ ∈ T.H m := by
    have hle : T.H (n + 1) ≤ T.H m := T.H_mono hnm
    refine (T.H m).add_mem ((T.H m).add_mem ((T.H m).algebraMap_mem α₁) ?_) ?_
    · exact (T.H m).smul_mem (hle (T.g_mem n)) β₁
    · exact (T.H m).smul_mem (hle (T.ginv_mem n)) γ₁
  have hab : a * bondLetter T n α₁ β₁ γ₁ * b ∈ T.H m :=
    (T.H m).mul_mem ((T.H m).mul_mem (T.H_mono (by omega) ha) hl) hbm
  have h2 := bridge_local_state T hD m _ hab c hc α₂ β₂ γ₂
  have h1 := bridge_local_state T hD n a ha b hb α₁ β₁ γ₁
  unfold bondLetter at *
  rw [h2, h1]
  ring

end PartA

/-! ## Part B — the two fundamental channels -/

section PartB

variable {K : Type*} [Field K]

/-- **Channel weights from a state on `span {1, g}`.** With `g = q·P_S − q⁻¹·P_A`,
`P_S + P_A = 1`, a state of total `t` and `g`-value `z t` has these weights. -/
theorem channel_weights (q z t wS wA : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h1 : wS + wA = t) (h2 : q * wS - q⁻¹ * wA = z * t) :
    wS = t * (z * q + 1) / (q ^ 2 + 1) ∧ wA = t * q * (q - z) / (q ^ 2 + 1) := by
  have hA : wA = t - wS := by linear_combination h1
  have hS : wS * (q ^ 2 + 1) = t * (z * q + 1) := by
    subst hA
    field_simp at h2
    linear_combination h2
  refine ⟨by field_simp; linear_combination hS, ?_⟩
  rw [hA]
  field_simp
  linear_combination -hS

/-- **Convention D channel weights.** At `z = q³/(q²+1)` the Sym and Alt weights are
`t (q⁴+q²+1)/(q²+1)²` and `t q²/(q²+1)²`. -/
theorem channel_weights_conventionD (q t wS wA : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h1 : wS + wA = t) (h2 : q * wS - q⁻¹ * wA = q ^ 3 / (q ^ 2 + 1) * t) :
    wS = t * (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 ∧
      wA = t * q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  obtain ⟨hS, hA⟩ := channel_weights q (q ^ 3 / (q ^ 2 + 1)) t wS wA hq hq2 h1 h2
  constructor
  · rw [hS]; field_simp; ring
  · rw [hA]; field_simp; ring

/-- **Both channels are live under convention D** (`t ≠ 0`): the Alt weight
`t q²/(q²+1)²` does not vanish, so the two-box bridge is not annihilated. -/
theorem alt_weight_ne_zero_conventionD (q t : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (ht : t ≠ 0) : t * q ^ 2 / (q ^ 2 + 1) ^ 2 ≠ 0 := by
  exact div_ne_zero (mul_ne_zero ht (pow_ne_zero 2 hq)) (pow_ne_zero 2 hq2)

end PartB

/-! ## Part C — the local O'Hara cross term is chirality-blind -/

section PartC

open Real

/-- The O'Hara/Möbius cross-term kernel of two straight segments. -/
noncomputable def segKernel (d θ s t : ℝ) : ℝ :=
  1 / (d ^ 2 + s ^ 2 + t ^ 2 - 2 * s * t * Real.cos θ)

/-- The local cross-term energy of two segments of half-length `ℓ`. -/
noncomputable def segEnergy (d θ ℓ : ℝ) : ℝ :=
  ∫ s in (-ℓ)..ℓ, ∫ t in (-ℓ)..ℓ, segKernel d θ s t

/-- Reversing one segment is the reflection `t ↦ −t`. -/
theorem segKernel_reflect (d θ s t : ℝ) :
    segKernel d (π - θ) s t = segKernel d θ s (-t) := by
  simp only [segKernel, Real.cos_pi_sub]
  ring_nf

/-- **The local O'Hara term is chirality-blind**: `E(π − θ) = E(θ)`. -/
theorem segEnergy_reflect (d θ ℓ : ℝ) : segEnergy d (π - θ) ℓ = segEnergy d θ ℓ := by
  unfold segEnergy
  congr 1
  funext s
  simp_rw [segKernel_reflect]
  rw [intervalIntegral.integral_comp_neg (fun t => segKernel d θ s t), neg_neg]

/-- Swapping which segment passes over (`d ↦ −d`) leaves the kernel unchanged. -/
theorem segKernel_neg_d (d θ s t : ℝ) : segKernel (-d) θ s t = segKernel d θ s t := by
  simp only [segKernel, neg_sq]

/-- **The local O'Hara term is blind to over/under**: `E(−d) = E(d)`. -/
theorem segEnergy_neg_d (d θ ℓ : ℝ) : segEnergy (-d) θ ℓ = segEnergy d θ ℓ := by
  simp only [segEnergy, segKernel_neg_d]

/-- **A reflection-symmetric energy with a unique minimiser on `(0, π)` selects the
perpendicular crossing.** -/
theorem minimiser_eq_pi_div_two (E : ℝ → ℝ) (hE : ∀ θ, E (π - θ) = E θ) (θs : ℝ)
    (hmem : θs ∈ Set.Ioo 0 π)
    (huniq : ∀ θ ∈ Set.Ioo 0 π, E θ = E θs → θ = θs) : θs = π / 2 := by
  have hmem' : π - θs ∈ Set.Ioo 0 π := ⟨by linarith [hmem.2], by linarith [hmem.1]⟩
  have h := huniq (π - θs) hmem' (hE θs)
  linarith

end PartC

/-! ## Part D — the datum: a primary conjecture class, no instance -/

section PartD

open Real

/-- **The segment collision datum** at closest distance `d` and segment half-length `ℓ`:
a Bring contribution to the local energy, and the selected angle, which is the unique
minimiser on `(0, π)` of O'Hara + Bring. No instance is supplied: the Bring term
has no derivation yet (bean `qou-pzsi`, route 2 undefined). -/
class SegmentCollisionDatum (d ℓ : ℝ) where
  /-- The Bring-surface part of the local energy, as a function of the angle. -/
  bring : ℝ → ℝ
  /-- The selected incoming angle, which starts the Reeb (geodesic) flow. -/
  θstar : ℝ
  θstar_mem : θstar ∈ Set.Ioo 0 π
  /-- It is a minimiser of the total local energy. -/
  isMin : ∀ θ ∈ Set.Ioo 0 π, segEnergy d θstar ℓ + bring θstar ≤ segEnergy d θ ℓ + bring θ
  /-- And the only one. -/
  unique : ∀ θ ∈ Set.Ioo 0 π,
    segEnergy d θ ℓ + bring θ = segEnergy d θstar ℓ + bring θstar → θ = θstar

/-- **If the Bring term is achiral, the selected angle is perpendicular** — so a chiral
selection (`σ` over `σ⁻¹`) is possible only if the Bring term breaks `θ ↦ π − θ`. -/
theorem θstar_eq_pi_div_two_of_achiral (d ℓ : ℝ) [D : SegmentCollisionDatum d ℓ]
    (hB : ∀ θ, D.bring (π - θ) = D.bring θ) : D.θstar = π / 2 :=
  minimiser_eq_pi_div_two (fun θ => segEnergy d θ ℓ + D.bring θ)
    (fun θ => by simp only [segEnergy_reflect, hB]) D.θstar D.θstar_mem D.unique

end PartD

/-! ## Part G — chirality wired in (owner ruling 2026-10-12: strands follow the fibre Reeb flow)

Part D derived `θ* = π/2` from an ACHIRAL Bring term. Under the fibre ruling
(`BringUTContactChirality` §6, orientation superseded by §9: the canonical orientation is the
geodesic one) the ambient `UT(Σ₄)` carries a chiral invariant, the fibre linking residue, canonically
`ℓ = −1/6 ∈ ℚ/ℤ` (`canonicalResidue`; `+1/6` in the superseded fibre orientation). Its
orientation-reverse is `−ℓ`, and `ℓ ≢ −ℓ` in either orientation.

A local Bring energy on the oriented manifold is a function `E θ ℓ` of the crossing angle and the
residue. The mirror configuration (crossing sign flipped) lives in the orientation-reversed
manifold, so `E` is **covariant**: `E (π − θ) ℓ = E θ (−ℓ)`. Then:

* `mirror_symmetric_iff_residue_even`: `E` is reflection-symmetric at `ℓ` iff it is even in the
  residue at `ℓ`;
* `chiral_of_residue_odd`: if `E` sees the residue (`E θ ℓ ≠ E θ (−ℓ)` for some `θ`), it is not
  reflection-symmetric, Part D's achirality hypothesis is unavailable, and `θ*` is no longer forced
  to `π/2`;
* `bring_residue_not_self_mirror`: at the Bring residue `1/6`, `ℓ` and `−ℓ` are different points of
  `ℚ/ℤ`, so for an `E` that is periodic in `ℓ` the residue-evenness test is a genuine condition and
  not a tautology.

**Still not derived:** the residue dependence of the Bring energy itself, i.e. a formula for `E`.
What is derived is where chirality enters (through `ℓ` alone) and that it cannot cancel
(`ℓ ≠ −ℓ` mod 1). -/

section PartG

open Real QOU.Brings.UTContactChirality

/-- **Reflection symmetry at a residue is residue-evenness**, for a covariant energy. -/
theorem mirror_symmetric_iff_residue_even (E : ℝ → ℚ → ℝ)
    (hcov : ∀ θ ℓ, E (π - θ) ℓ = E θ (-ℓ)) (ℓ : ℚ) :
    (∀ θ, E (π - θ) ℓ = E θ ℓ) ↔ (∀ θ, E θ (-ℓ) = E θ ℓ) := by
  constructor
  · intro h θ; rw [← hcov]; exact h θ
  · intro h θ; rw [hcov]; exact h θ

/-- **A residue-sensitive energy is chiral**: Part D's achirality hypothesis fails. -/
theorem chiral_of_residue_odd (E : ℝ → ℚ → ℝ) (hcov : ∀ θ ℓ, E (π - θ) ℓ = E θ (-ℓ))
    (ℓ : ℚ) (θ₀ : ℝ) (hodd : E θ₀ (-ℓ) ≠ E θ₀ ℓ) : ¬ ∀ θ, E (π - θ) ℓ = E θ ℓ := by
  intro h
  exact hodd ((mirror_symmetric_iff_residue_even E hcov ℓ).1 h θ₀)

/-- **The Bring residue is not its own mirror in `ℚ/ℤ`**: no integer shift takes `1/6` to `−1/6`. -/
theorem bring_residue_not_self_mirror :
    ∀ n : ℤ, -fibreLinkingResidue (-6) ≠ fibreLinkingResidue (-6) + n := by
  intro n h
  exact fibre_linking_residue_chiral ⟨-n, by push_cast; linarith⟩

/-- **The canonical residue is not its own mirror either** (geodesic ruling, `ℓ = −1/6`). -/
theorem canonical_residue_not_self_mirror :
    ∀ n : ℤ, -canonicalResidue ≠ canonicalResidue + n := by
  intro n h
  exact canonicalResidue_chiral ⟨-n, by push_cast; linarith⟩

end PartG

end QOU.MassTheory.SegmentCollision
