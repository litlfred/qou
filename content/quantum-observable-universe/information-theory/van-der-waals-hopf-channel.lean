import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination


/-!
# QOU.VanDerWaals — van der Waals as the Hopf symmetric block

Van der Waals is identified as the **symmetric-block idempotent** of the
2-strand inter-molecular Hecke algebra `H_2(q)`:

  `e₊ = (σ + q⁻¹) / (q + q⁻¹)`   (trivial rep, `σ ↦ q`),

the Hopf / `[2]_q` channel with vanishing hyperbolic volume
([`hopf-diquark`](../observations/hopf-diquark.md), `Vol(𝓛_H) = 0`) — a
linking, volume-less correlation, the topological signature of dispersion.
Its complement is the directional (antisymmetric / hydrogen-bond) block
`e₋ = (q − σ) / (q + q⁻¹)` (sign rep, `σ ↦ −q⁻¹`).

LaTeX label: `def:van-der-waals-hopf-channel`.
**Ground ring**: a field `R` (so `q⁻¹` and `(q+q⁻¹)⁻¹` exist).
-/

namespace QOU.VanDerWaals

variable {R : Type*} [Field R]

/-- **Van der Waals channel** — the symmetric-block idempotent
    `e₊ = (σ + q⁻¹)/(q + q⁻¹)` of the inter-molecular `H_2(q)` (the Hopf /
    `[2]_q` block, `Vol = 0`). -/
def vdwSymmetricBlock (q σ : R) : R := (σ + q⁻¹) / (q + q⁻¹)

/-- The complementary **directional (hydrogen-bond) block**
    `e₋ = (q − σ)/(q + q⁻¹)` (antisymmetric / sign rep). -/
def directionalBlock (q σ : R) : R := (q - σ) / (q + q⁻¹)

/-- The two blocks partition unity: `e₊ + e₋ = 1`. -/
-- Ref: [manuscript] information-theory/van-der-waals-hopf-channel
theorem blocks_partition_unity (q σ : R) (hq2 : q + q⁻¹ ≠ 0) :
    vdwSymmetricBlock q σ + directionalBlock q σ = 1 := by
  unfold vdwSymmetricBlock directionalBlock
  rw [← add_div]
  have hnum : σ + q⁻¹ + (q - σ) = q + q⁻¹ := by ring
  rw [hnum, div_self hq2]

/-- **The van der Waals block is idempotent** (cleared form): given the Hecke
    relation `σ² = (q − q⁻¹)σ + 1`, `(σ + q⁻¹)² = (σ + q⁻¹)(q + q⁻¹)`, i.e.
    `e₊² = e₊` after dividing by `(q + q⁻¹)²` — the algebraic signature of a
    genuine Wedderburn projector. Sorry-free. -/
-- Ref: [manuscript] information-theory/van-der-waals-hopf-channel
theorem vdw_idempotent_cleared (q σ : R) (hq : q ≠ 0)
    (hHecke : σ ^ 2 = (q - q⁻¹) * σ + 1) :
    (σ + q⁻¹) ^ 2 = (σ + q⁻¹) * (q + q⁻¹) := by
  have hqq : q⁻¹ * q = 1 := inv_mul_cancel₀ hq
  linear_combination hHecke - hqq

end QOU.VanDerWaals
