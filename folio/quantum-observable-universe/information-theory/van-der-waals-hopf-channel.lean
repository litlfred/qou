import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.Group.Invertible.Defs
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
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

**Ground ring (§7c): a commutative ring `R`, no field.** The two inverses the
block needs are of different kinds and are carried differently:

* `q⁻¹` is invertible *by fiat* — `q` is the substrate parameter, a unit of
  the ground ring — so it is carried as `q : Rˣ` and `q⁻¹` is the `Units`
  inverse. No non-vanishing hypothesis is needed or wanted.
* `[2]_q = q + q⁻¹` **genuinely vanishes** at `q² = −1`, so its invertibility
  does *not* follow from `q`'s. It is carried as an `[Invertible (q + q⁻¹)]`
  instance — the exact content of the old `hq2 : q + q⁻¹ ≠ 0`, but as an
  explicit inverse rather than a field division.

Nothing here is archimedean; the substrate evaluation at `q₀ ∈ ℝ` is
downstream.
-/

namespace QOU.VanDerWaals

variable {R : Type*} [CommRing R]

/-- **Van der Waals channel** — the symmetric-block idempotent
    `e₊ = (σ + q⁻¹)·⅟[2]_q` of the inter-molecular `H_2(q)` (the Hopf /
    `[2]_q` block, `Vol = 0`). -/
def vdwSymmetricBlock (q : Rˣ) (σ : R)
    [Invertible ((q : R) + ((q⁻¹ : Rˣ) : R))] : R :=
  (σ + ((q⁻¹ : Rˣ) : R)) * ⅟((q : R) + ((q⁻¹ : Rˣ) : R))

/-- The complementary **directional (hydrogen-bond) block**
    `e₋ = (q − σ)·⅟[2]_q` (antisymmetric / sign rep). -/
def directionalBlock (q : Rˣ) (σ : R)
    [Invertible ((q : R) + ((q⁻¹ : Rˣ) : R))] : R :=
  ((q : R) - σ) * ⅟((q : R) + ((q⁻¹ : Rˣ) : R))

/-- The two blocks partition unity: `e₊ + e₋ = 1`. -/
-- Ref: [leitner2026] information-theory/van-der-waals-hopf-channel
theorem blocks_partition_unity (q : Rˣ) (σ : R)
    [Invertible ((q : R) + ((q⁻¹ : Rˣ) : R))] :
    vdwSymmetricBlock q σ + directionalBlock q σ = 1 := by
  unfold vdwSymmetricBlock directionalBlock
  rw [← add_mul]
  have hnum : σ + ((q⁻¹ : Rˣ) : R) + ((q : R) - σ)
      = (q : R) + ((q⁻¹ : Rˣ) : R) := by ring
  rw [hnum, mul_invOf_self]

/-- **The van der Waals block is idempotent** (cleared form): given the Hecke
    relation `σ² = (q − q⁻¹)σ + 1`, `(σ + q⁻¹)² = (σ + q⁻¹)(q + q⁻¹)`, i.e.
    `e₊² = e₊` after dividing by `(q + q⁻¹)²` — the algebraic signature of a
    genuine Wedderburn projector.

    In this cleared form nothing is divided at all: the identity is a
    `linear_combination` of the Hecke relation and the unit relation
    `q⁻¹ · q = 1`, so `[2]_q` need not be invertible here. Sorry-free. -/
-- Ref: [leitner2026] information-theory/van-der-waals-hopf-channel
theorem vdw_idempotent_cleared (q : Rˣ) (σ : R)
    (hHecke : σ ^ 2 = ((q : R) - ((q⁻¹ : Rˣ) : R)) * σ + 1) :
    (σ + ((q⁻¹ : Rˣ) : R)) ^ 2
      = (σ + ((q⁻¹ : Rˣ) : R)) * ((q : R) + ((q⁻¹ : Rˣ) : R)) := by
  have hqq : ((q⁻¹ : Rˣ) : R) * (q : R) = 1 := q.inv_mul
  linear_combination hHecke - hqq

end QOU.VanDerWaals
