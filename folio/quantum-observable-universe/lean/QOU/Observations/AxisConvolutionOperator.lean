/-
# The braid axis as a convolution operator (closure ∪ axis)

Thread "Derive the electron's categorical weight" (2026-11-27). Owner card: "Convolution op of
closure ∪ axis". Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §16.

The least-trace lepton words `e = σ₁σ₂σ₁`, `μ = σ₁²σ₂⁻¹` have the same closure (the Hopf link),
so every closure invariant agrees on them. The braid axis is an unknot `A` encircling the three
strands; the link `closure(β) ∪ A` is the 4-strand closure of `β · σ₃σ₂σ₁σ₁σ₂σ₃`.

On the spin-`J` isotypic part of `V_j^{⊗3}` (quantum dimension `a = 2J + 1`) the axis coloured
`b = 2j + 1 = N` acts by the scalar `s_{a}(b) = [a b] / [a]`, the encircling (Hopf) ratio
`S_{jJ}/S_{0J}`. So the axis is a central convolution operator, one scalar per block, exactly as
in `KnotConvolutionOperator` (`axisOp`). This file proves, over any field and with `q = v²`:

* `hopf_encircling`: `Σ_{k<b} [d_k] θ_{d_k} = θ_a θ_b [a b]`, `d_k = a + b − 1 − 2k`,
  `θ_d = v^{d² − 1}` (the twist `q^{2J(J+1)}`). This is the fusion sum that turns the full twist
  of the axis around the `J` block into the scalar `[ab]/[a]`.
* `charSum_mul`: `[a] · Σ_{m<b} q^{a(b−1−2m)} = [a b]`, so `s_a(b)` is the character of `V_j` at
  `K = q^a`, a Laurent polynomial (no division, no transcendental input).
* `charSum_at_one`: at `v = 1` the scalar is `b = N` on every block. The axis is invisible at
  `q = 1`; it separates braids with equal closures only through their isotypic split.

The 4-strand numerical check (`m(β ∪ A) = f^{−6} Σ_J χ_J(β) s_{2J+1}(N)`, N = 2, 3, 4) is in
`computations/probes/coloured_ladder/axis_convolution_probe.py`. No measured value enters.
-/
import QOU.Observations.KnotConvolutionOperator
import Mathlib.Tactic

namespace QOU.Observations.AxisConvolutionOperator

open QOU.Observations.KnotConvolutionOperator

variable {F : Type*} [Field F]

/-- Quantum integer in `v` with `q = v²`: `(q^n − q^{−n}) (q − q^{−1})⁻¹`. -/
noncomputable def qn (v : F) (n : ℤ) : F := (v ^ (2 * n) - v ^ (-(2 * n))) / (v ^ 2 - v ^ (-2 : ℤ))

/-- Ribbon twist on the module of quantum dimension `d`: `θ_d = v^{d² − 1} = q^{2J(J+1)}`. -/
def theta (v : F) (d : ℤ) : F := v ^ (d ^ 2 - 1)

/-- Telescoping along a string of step `−2`. -/
theorem telescope (G : ℤ → F) (x : ℤ) (b : ℕ) :
    ∑ k ∈ Finset.range b, (G (x - 2 * k) - G (x - 2 * k - 2)) = G x - G (x - 2 * b) := by
  induction b with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    push_cast
    ring_nf

/-- One fusion summand, multiplied out: `θ_d [d] (q − q⁻¹) = v^{(d+1)²−2} − v^{(d−1)²−2}`. -/
theorem theta_qn (v : F) (hv : v ≠ 0) (d : ℤ) :
    theta v d * (v ^ (2 * d) - v ^ (-(2 * d))) =
      v ^ ((d + 1) ^ 2 - 2) - v ^ ((d - 1) ^ 2 - 2) := by
  unfold theta
  rw [mul_sub, ← zpow_add₀ hv, ← zpow_add₀ hv]
  congr 2 <;> ring

/-- **Encircling (Hopf) fusion sum.** For blocks of quantum dimensions `a` and `b`,
`Σ_{k<b} [d_k] θ_{d_k} = θ_a θ_b [ab]` with `d_k = a + b − 1 − 2k`. When `b ≤ a` the `d_k` are
exactly the dimensions in `V_a ⊗ V_b`. Stated before dividing by `q − q⁻¹`. -/
theorem hopf_encircling (v : F) (hv : v ≠ 0) (a : ℤ) (b : ℕ) :
    ∑ k ∈ Finset.range b, theta v (a + b - 1 - 2 * k) *
        (v ^ (2 * (a + b - 1 - 2 * k)) - v ^ (-(2 * (a + b - 1 - 2 * k)))) =
      theta v a * theta v b * (v ^ (2 * (a * b)) - v ^ (-(2 * (a * b)))) := by
  have h := telescope (fun e : ℤ => v ^ (e ^ 2 - 2)) (a + b) b
  simp only at h
  have hl : ∀ k ∈ Finset.range b,
      theta v (a + b - 1 - 2 * k) *
        (v ^ (2 * (a + b - 1 - 2 * k)) - v ^ (-(2 * (a + b - 1 - 2 * k)))) =
      v ^ ((a + b - 2 * k) ^ 2 - 2) - v ^ ((a + b - 2 * k - 2) ^ 2 - 2) := by
    intro k _
    rw [theta_qn v hv]
    congr 2 <;> ring
  rw [Finset.sum_congr rfl hl, h]
  unfold theta
  rw [mul_sub, ← zpow_add₀ hv, ← zpow_add₀ hv, ← zpow_add₀ hv]
  congr 2 <;> ring

/-- Character of the colour-`b` module at `K = q^a`: `Σ_{m<b} q^{a(b−1−2m)}`. -/
def charSum (v : F) (a : ℤ) (b : ℕ) : F :=
  ∑ m ∈ Finset.range b, v ^ (2 * a * (b - 1 - 2 * m))

/-- **The encircling scalar is a character**: `[a] · Σ_{m<b} q^{a(b−1−2m)} = [ab]`, stated
before dividing by `q − q⁻¹`. -/
theorem charSum_mul (v : F) (hv : v ≠ 0) (a : ℤ) (b : ℕ) :
    (v ^ (2 * a) - v ^ (-(2 * a))) * charSum v a b = v ^ (2 * (a * b)) - v ^ (-(2 * (a * b))) := by
  have h := telescope (fun e : ℤ => v ^ (2 * a * e)) b b
  simp only at h
  unfold charSum
  rw [Finset.mul_sum]
  have hl : ∀ m ∈ Finset.range b,
      (v ^ (2 * a) - v ^ (-(2 * a))) * v ^ (2 * a * ((b : ℤ) - 1 - 2 * m)) =
      v ^ (2 * a * ((b : ℤ) - 2 * m)) - v ^ (2 * a * ((b : ℤ) - 2 * m - 2)) := by
    intro m _
    rw [sub_mul, ← zpow_add₀ hv, ← zpow_add₀ hv]
    congr 2 <;> ring
  rw [Finset.sum_congr rfl hl, h]
  congr 2 <;> ring

/-- **The axis is invisible at `q = 1`**: the scalar is `b = N` on every block. -/
theorem charSum_at_one (a : ℤ) (b : ℕ) : charSum (1 : F) a b = b := by
  simp [charSum]

/-- The axis coloured `N` as a central convolution operator: scalar `s_a(N)` on the block of
quantum dimension `a`. -/
def axisOp (v : F) (N : ℕ) : ConvOp F := ⟨fun a => charSum v a N⟩

/-- The mass of `closure(β) ∪ axis` from the isotypic characters `χ_a(β)` of the braid (block of
quantum dimension `a`, multiplicity trace times `[a]`, framed) and the axis framing factor. -/
def axisMass (v : F) (N : ℕ) (blocks : Finset ℕ) (χ : ℕ → F) (frame : F) : F :=
  frame * ∑ a ∈ blocks, χ a * (axisOp v N).c a

/-- At `q = 1` the axis multiplies the closure mass by `N`: it cannot separate braids with the
same closure there. -/
theorem axisMass_at_one (N : ℕ) (blocks : Finset ℕ) (χ : ℕ → F) (frame : F) :
    axisMass (1 : F) N blocks χ frame = N * (frame * ∑ a ∈ blocks, χ a) := by
  simp only [axisMass, axisOp, charSum_at_one, Finset.mul_sum]
  exact Finset.sum_congr rfl fun _ _ => by ring

/-- Colour 2 (the fundamental axis): `s_a(2) = q^a + q^{−a}`. -/
theorem charSum_two (v : F) (a : ℤ) : charSum v a 2 = v ^ (2 * a) + v ^ (-(2 * a)) := by
  simp [charSum, Finset.sum_range_succ]

end QOU.Observations.AxisConvolutionOperator
