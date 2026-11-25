import Mathlib.Algebra.Group.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Card

/-!
# Holonomy-level replacement for the trace-on-edges cochain map

Bean `qou-b7fc`; audit `docs/audits/2026-11-25-holography-qns-essay-review.md`
item 3. The essay's edge values `tr(ψ·w_e)` are not a 1-cochain
(`TraceCochainObstructions.trace_add_inverse_conventionD_pos`). Owner question,
2026-11-25: use Yekutieli's non-abelian Stokes instead (corpus:
`QOU.MathlibExt.YekutieliIntegration`, whose `holonomy` is a path-ordered list
product). This file records what that buys, over an arbitrary group `G` (§7c).

1. `gaugeHol_eq`: under a vertex gauge `g_i ↦ h_{i+1} g_i h_i⁻¹` the holonomy of
   a path telescopes to `h_n · hol · h_0⁻¹`; on a closed loop (`h_n = h_0`) it is
   a conjugation. So edge labels are gauge data and face holonomies are
   well-defined up to conjugacy: the holonomy-level map is well-defined.
2. `classFun_gaugeHol_closed`, `classFun_basepoint`: any class function χ
   (`χ(ab) = χ(ba)`, e.g. a Markov trace or a character) of a face holonomy is
   gauge-invariant and independent of the basepoint. These are the
   trace-level observables that survive.
3. `perm3_fixCount_product_not_determined`: χ of a PRODUCT of holonomies is not
   a function of the χ of the factors (S₃, permutation character). The
   non-abelian Stokes identity relates products of face holonomies, so after
   taking traces it gives no linear relation among face traces, and no
   "Π₂ = d Π₁" cochain identity survives. The abelian shadow (determinant /
   abelianisation) gives back the discrete Stokes lemma
   `TraceCochainObstructions.sum_coboundary_eq_zero`.
-/

namespace QOU.BringsSurface.NonabelianStokesTrace

variable {G : Type*} [Group G]

/-- Path-ordered holonomy of the first `n` edges: later edges act on the left. -/
def hol (g : ℕ → G) : ℕ → G
  | 0 => 1
  | n + 1 => g n * hol g n

/-- Vertex gauge transformation of the edge labels. -/
def gauge (h g : ℕ → G) (i : ℕ) : G := h (i + 1) * g i * (h i)⁻¹

theorem gaugeHol_eq (h g : ℕ → G) (n : ℕ) :
    hol (gauge h g) n = h n * hol g n * (h 0)⁻¹ := by
  induction n with
  | zero => simp [hol]
  | succ n ih => simp [hol, gauge, ih, mul_assoc]

/-- On a closed loop the gauged holonomy is a conjugate of the original. -/
theorem gaugeHol_closed (h g : ℕ → G) (n : ℕ) (hc : h n = h 0) :
    hol (gauge h g) n = h 0 * hol g n * (h 0)⁻¹ := by
  rw [gaugeHol_eq, hc]

variable {R : Type*}

/-- A class function is invariant under conjugation. -/
theorem classFun_conj (χ : G → R) (hχ : ∀ a b, χ (a * b) = χ (b * a)) (u x : G) :
    χ (u * x * u⁻¹) = χ x := by
  rw [hχ, ← mul_assoc, inv_mul_cancel, one_mul]

/-- The face trace is gauge-invariant. -/
theorem classFun_gaugeHol_closed (χ : G → R) (hχ : ∀ a b, χ (a * b) = χ (b * a))
    (h g : ℕ → G) (n : ℕ) (hc : h n = h 0) :
    χ (hol (gauge h g) n) = χ (hol g n) := by
  rw [gaugeHol_closed h g n hc, classFun_conj χ hχ]

/-- Moving the basepoint of a loop `x · y` to `y · x` does not change its trace. -/
theorem classFun_basepoint (χ : G → R) (hχ : ∀ a b, χ (a * b) = χ (b * a)) (x y : G) :
    χ (x * y) = χ (y * x) := hχ x y

/-- Number of fixed points: the permutation character of `S₃`. -/
def fixCount (σ : Equiv.Perm (Fin 3)) : ℕ := (Finset.univ.filter fun i => σ i = i).card

/-- The trace of a product is not determined by the traces of its factors: two
pairs with equal factor traces (1, 1) have product traces 3 and 0. -/
theorem perm3_fixCount_product_not_determined :
    fixCount (Equiv.swap 0 1) = 1 ∧ fixCount (Equiv.swap 1 2) = 1 ∧
    fixCount (Equiv.swap 0 1 * Equiv.swap 0 1) = 3 ∧
    fixCount (Equiv.swap 0 1 * Equiv.swap 1 2) = 0 := by
  decide

end QOU.BringsSurface.NonabelianStokesTrace
