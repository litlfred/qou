import HeckeTemperleyLieb.HeckeH2AlgebraInstance
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# The pair Skein mass formula under convention D, derived

Owner ruling 2026-11-27 (Carl): *"Derive the convention D. Formula. Go ahead
and migrate the convention D"*.

The convention-C pair formula of `lem:pair-skein-mass-formula`,

    S_ab = (q·μ_a + q⁻¹·μ_b) / (q^{1/2} + q^{-1/2}),

was stated, not derived: its own proof block records that the denominator
`q^{1/2} + q^{-1/2}` "is not derived above". This file derives the pair mass
instead, from objects the corpus already has:

* the rank-two Hecke algebra `H₂(q) = span{1, σ}` (`QOU.Machinery.H3.H2A`),
  with `σ² = h·σ + 1`, `h = q − q⁻¹`;
* its Markov trace `trace₂ z (a + b·σ) = a + z·b`
  (`QOU.Machinery.H3.H2A.markovTrace_H2A`);
* the convention-D Markov parameter `z_D = q³/(q² + 1)`.

**Pair mass.** A pair of strands carrying dressed masses `μ_a`, `μ_b` meets
at one positive crossing, weighted by `μ_a`, and one negative crossing,
weighted by `μ_b`. This is the Borromean pattern: every pair of strands
crosses once each way, so the pairwise linking number is zero. The pair mass
is the Markov trace of that weighted crossing element:

    S_ab := trace₂ z_D (μ_a·σ + μ_b·σ⁻¹).

**Result** (`pairMassD_closed`):

    S_ab = (q³·μ_a + q⁻¹·μ_b) / (q² + 1).

Both weights come from the algebra: `trace₂ z_D σ = z_D = q³/(q²+1)` and
`trace₂ z_D σ⁻¹ = z_D − h = q⁻¹/(q²+1)`. At `q = 1` the pair mass is the
mean `(μ_a + μ_b)/2` (`pairMassD_at_one`). No square root appears and no
number is fitted.

**Nucleon split** (`neutron_sub_proton`). With the nucleon mass the sum of
its three pair masses, in the strand orders `(u, u, d)` and `(u, d, d)`,

    m_n − m_p = κ · (μ_d − μ_u),   κ = trace₂ z_D (σ + σ⁻¹) = (q⁴+1)/(q(q²+1)),

and `q·κ = trace₂ z_D (σ²)` is the Hopf-link trace (`q_mul_kappaD`). The
difference uses only linearity of the trace, so it holds for every strand
order that puts the odd flavour last.

Base ring (§7c): a generic field `R`.
-/

namespace QOU.MassTheory.PairSkeinD

open QOU.Machinery.H3

variable {R : Type*} [Field R]

/-- The Hecke parameter `h = q − q⁻¹`. -/
def hD (q : R) : R := q - q⁻¹

/-- The convention-D Markov parameter `z_D = q³/(q² + 1)`. -/
def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The crossing generator `σ ∈ H₂(q)`. -/
def sig (q : R) : H2A R (hD q) := ⟨0, 1⟩

/-- The inverse crossing `σ⁻¹ = σ − h`. -/
def sigInv (q : R) : H2A R (hD q) := ⟨-(hD q), 1⟩

/-- `σ · σ⁻¹ = 1` in `H₂(q)`. -/
theorem sig_mul_sigInv (q : R) : sig q * sigInv q = 1 := by
  ext <;> simp [sig, sigInv]

/-- The pair mass: the convention-D Markov trace of one positive crossing
weighted by `μ_a` and one negative crossing weighted by `μ_b`. -/
def pairMassD (q μa μb : R) : R :=
  H2A.trace₂ (h := hD q) (zD q) (μa • sig q + μb • sigInv q)

/-- The pair mass is linear in the weights: `S_ab = μ_a·z_D + μ_b·(z_D − h)`. -/
theorem pairMassD_eq (q μa μb : R) :
    pairMassD q μa μb = μa * zD q + μb * (zD q - hD q) := by
  simp [pairMassD, H2A.trace₂, sig, sigInv]
  ring

/-- `trace₂ z_D σ⁻¹ = z_D − h = 1/(q(q² + 1))`. -/
theorem zD_sub_hD (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    zD q - hD q = q⁻¹ / (q ^ 2 + 1) := by
  unfold zD hD
  field_simp
  ring

/-- **The convention-D pair Skein mass formula (derived).**

    S_ab = (q³·μ_a + q⁻¹·μ_b) / (q² + 1). -/
theorem pairMassD_closed (q μa μb : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    pairMassD q μa μb = (q ^ 3 * μa + q⁻¹ * μb) / (q ^ 2 + 1) := by
  rw [pairMassD_eq, zD_sub_hD q hq hq2]
  unfold zD
  field_simp

/-- **Classical limit.** At `q = 1` the pair mass is the mean of the two
weights. -/
theorem pairMassD_at_one (μa μb : R) (h2 : (2 : R) ≠ 0) :
    pairMassD (1 : R) μa μb = (μa + μb) / 2 := by
  rw [pairMassD_closed 1 μa μb one_ne_zero (by norm_num; exact h2)]
  norm_num

/-- The nucleon mass: the sum of the pair masses of its three strands, in
strand order `(x₁, x₂, x₃)`. -/
def nucleonMassD (q μ₁ μ₂ μ₃ : R) : R :=
  pairMassD q μ₁ μ₂ + pairMassD q μ₁ μ₃ + pairMassD q μ₂ μ₃

/-- The splitting constant `κ = trace₂ z_D (σ + σ⁻¹) = 2·z_D − h`. -/
def kappaD (q : R) : R := H2A.trace₂ (h := hD q) (zD q) (sig q + sigInv q)

theorem kappaD_eq (q : R) : kappaD q = 2 * zD q - hD q := by
  simp [kappaD, H2A.trace₂, sig, sigInv]
  ring

/-- `κ = (q⁴ + 1)/(q(q² + 1))`. -/
theorem kappaD_closed (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    kappaD q = (q ^ 4 + 1) / (q * (q ^ 2 + 1)) := by
  rw [kappaD_eq]
  unfold zD hD
  field_simp
  ring

/-- `q·κ` is the convention-D Hopf-link trace `trace₂ z_D (σ²)`. -/
theorem q_mul_kappaD (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q * kappaD q = H2A.trace₂ (h := hD q) (zD q) (sig q * sig q) := by
  rw [kappaD_eq]
  simp [H2A.trace₂, sig]
  unfold zD hD
  field_simp
  ring

/-- **Nucleon split under convention D (derived).** For the proton strand
order `(u, u, d)` and the neutron strand order `(u, d, d)`,

    m_n − m_p = κ · (μ_d − μ_u). -/
theorem neutron_sub_proton (q μu μd : R) :
    nucleonMassD q μu μd μd - nucleonMassD q μu μu μd
      = kappaD q * (μd - μu) := by
  simp only [nucleonMassD, pairMassD_eq, kappaD_eq]
  ring

/-- The nucleon split with denominators cleared:

    (m_n − m_p) · q(q² + 1) = (q⁴ + 1) · (μ_d − μ_u). -/
theorem neutron_sub_proton_cleared (q μu μd : R) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    (nucleonMassD q μu μd μd - nucleonMassD q μu μu μd) * (q * (q ^ 2 + 1))
      = (q ^ 4 + 1) * (μd - μu) := by
  rw [neutron_sub_proton, kappaD_closed q hq hq2]
  have : q * (q ^ 2 + 1) ≠ 0 := mul_ne_zero hq hq2
  field_simp

end QOU.MassTheory.PairSkeinD
