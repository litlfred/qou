/-
# The cut axis at the root of unity (volume reading of closure ∪ axis)

Thread "Derive the electron's categorical weight" (2026-11-28). Owner card: "Volume reading at
roots of unity". Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §17.

Cutting the axis of `closure(β) ∪ A` open leaves an endomorphism of the colour-`N` module, which is
a scalar `c_N(β)`. On the block of quantum dimension `a` the cut axis contributes
`[aN]/[N] = Σ_{m<a} q^{N(a−1−2m)}` (`charSum v N a`), while the closed axis contributes
`[aN]/[a]` (`charSum v a N`, file `AxisConvolutionOperator`). This file proves, over any field
with `q = v²`:

* `cut_closed`: `[N]·(cut scalar) = [a]·(closed scalar)`, both equal to `[aN]` (stated before
  dividing by `q − q⁻¹`).
* `charSum_at_root`: at `q^N = −1` (Kashaev's root `q = e^{iπ/N}`, Murakami's `e^{2πi/N}` in
  `q²`), the cut scalar is `a·(−1)^{a−1}`: the axis weights each block by its signed classical
  dimension.
* `cutAxis_at_root`: hence `c_N(β) = f^{−6} Σ_a μ_a(β)·a·(−1)^{a−1}` at the root, where `μ_a(β)`
  is the (framed) trace of `β` on the multiplicity space of the block.

The volume is the growth `(2π/N) log |c_N(β)|` (`KnotConvolutionVolume.growth`). Numerics (probe
`computations/probes/coloured_ladder/axis_volume_reading_probe.py`): `e` stays polynomial, `μ`
grows at `5.333`, the volume of the mapping torus (a cited value, not a measurement), with the
one-loop `(3/2) log N`. No measured mass enters.
-/
import QOU.Observations.AxisConvolutionOperator
import Mathlib.Tactic

namespace QOU.Observations.AxisKashaevReading

open QOU.Observations.KnotConvolutionOperator QOU.Observations.AxisConvolutionOperator

variable {F : Type*} [Field F]

/-- **Cut versus closed axis**: `[N]·[aN]/[N] = [a]·[aN]/[a]`, before dividing by `q − q⁻¹`. -/
theorem cut_closed (v : F) (hv : v ≠ 0) (N a : ℕ) :
    (v ^ (2 * (N : ℤ)) - v ^ (-(2 * (N : ℤ)))) * charSum v N a =
      (v ^ (2 * (a : ℤ)) - v ^ (-(2 * (a : ℤ)))) * charSum v a N := by
  rw [charSum_mul v hv, charSum_mul v hv, mul_comm (N : ℤ)]

/-- **The cut axis at the root**: if `q^N = −1` then `[aN]/[N] = a·(−1)^{a−1}`. -/
theorem charSum_at_root (v : F) (N a : ℕ) (h : v ^ (2 * (N : ℤ)) = -1) :
    charSum v N a = a * (-1 : F) ^ ((a : ℤ) - 1) := by
  unfold charSum
  have hterm : ∀ m ∈ Finset.range a,
      v ^ (2 * (N : ℤ) * ((a : ℤ) - 1 - 2 * m)) = (-1 : F) ^ ((a : ℤ) - 1) := by
    intro m _
    rw [zpow_mul, h, zpow_sub₀ (by norm_num : (-1 : F) ≠ 0), zpow_mul]
    have h2 : ((-1 : F) ^ (2 : ℤ)) = 1 := by norm_num
    rw [h2, one_zpow, div_one]
  rw [Finset.sum_congr rfl hterm, Finset.sum_const, Finset.card_range, nsmul_eq_mul]

/-- The cut axis as a convolution operator: scalar `[aN]/[N]` on the block of dimension `a`. -/
def cutAxisOp (v : F) (N : ℕ) : ConvOp F := ⟨fun a => charSum v N a⟩

/-- The cut invariant of `closure(β) ∪ axis` from the multiplicity traces `μ_a(β)`. -/
def cutAxis (v : F) (N : ℕ) (blocks : Finset ℕ) (μ : ℕ → F) (frame : F) : F :=
  frame * ∑ a ∈ blocks, μ a * (cutAxisOp v N).c a

/-- **At the root the cut axis weights each block by its signed dimension.** -/
theorem cutAxis_at_root (v : F) (N : ℕ) (h : v ^ (2 * (N : ℤ)) = -1) (blocks : Finset ℕ)
    (μ : ℕ → F) (frame : F) :
    cutAxis v N blocks μ frame =
      frame * ∑ a ∈ blocks, μ a * (a * (-1 : F) ^ ((a : ℤ) - 1)) := by
  simp only [cutAxis, cutAxisOp, charSum_at_root v N _ h]

/-- At `q = 1` the cut axis is `a` on the block of dimension `a`. -/
theorem cutAxis_at_one (N a : ℕ) : (cutAxisOp (1 : F) N).c a = a := by
  simp [cutAxisOp, charSum_at_one]

end QOU.Observations.AxisKashaevReading
