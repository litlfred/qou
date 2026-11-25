/-
  Bring's surface as the regular map `{5,4}` with rotation group `S₅`: finite facts
  (audit `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §14, item 5).

  Darts are the 120 elements of `S₅`. The vertex rotation is `S = (1 2 3 4)` (order 4), the
  edge involution is `A = (0 1)` (order 2), and the face rotation is `S·A = (0 2 3 4 1)`
  (order 5). The identification of this regular map with Bring's surface is classical
  \cite{edge1978}; what is proved here is the finite group theory and the counts.

  1. `S`, `A`, `S·A` have orders 4, 2, 5 (`orderOf_S`, `orderOf_A`, `orderOf_SA`).
  2. `S` and `A` generate `S₅` (`closure_S_A`), via the `5`-cycle `S·A` and the swap `A`.
  3. Cosets: vertices = `120/4 = 30`, edges = `120/2 = 60`, faces = `120/5 = 24`
     (`index_S`, `index_A`, `index_SA`), so `χ = 30 − 60 + 24 = −6` and genus `4` (`euler`).
  4. Gauss–Bonnet: a `(2,4,5)` triangle has area `π/20` and a genus-4 hyperbolic surface has
     area `12π`, so the tessellation has `240` triangles (`triangle_count`).

  Measured, not proved here (`bring_map_hodge_probe.py`): the combinatorial Hodge Laplacian on
  1-cochains of this map has kernel of dimension `8 = 2g`, and those harmonic 1-cochains are
  closed and co-closed (zero discrete vorticity).

  -- Ref: [edge1978] Edge, Bring's curve, J. London Math. Soc. 1978
-/
import Mathlib.GroupTheory.Perm.Closure
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.GroupTheory.Index
import Mathlib.Tactic.NormNum.Prime

namespace QOU.BringRegularMap

open Equiv

/-- Vertex rotation `(1 2 3 4)`. -/
def S : Perm (Fin 5) := swap 1 2 * swap 2 3 * swap 3 4
/-- Edge involution `(0 1)`. -/
def A : Perm (Fin 5) := swap 0 1

instance : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
instance : Fact (Nat.Prime 5) := ⟨by norm_num⟩

theorem orderOf_S : orderOf S = 4 := by
  have := orderOf_eq_prime_pow (x := S) (n := 1) (p := 2) (by decide) (by decide)
  simpa using this

theorem orderOf_A : orderOf A = 2 := orderOf_eq_prime (by decide) (by decide)

theorem orderOf_SA : orderOf (S * A) = 5 := orderOf_eq_prime (by decide) (by decide)

theorem SA_isCycle : (S * A).IsCycle :=
  Perm.isCycle_of_prime_order (by rw [orderOf_SA]; norm_num) (by rw [orderOf_SA]; decide)

/-- **`S` and `A` generate `S₅`.** -/
theorem closure_S_A : Subgroup.closure ({S, A} : Set (Perm (Fin 5))) = ⊤ := by
  have h : Subgroup.closure ({S * A, A} : Set (Perm (Fin 5))) = ⊤ :=
    Perm.closure_prime_cycle_swap (by simp; norm_num) SA_isCycle (by decide) ⟨0, 1, by decide, rfl⟩
  refine eq_top_iff.mpr (h ▸ (Subgroup.closure_le _).mpr ?_)
  intro x hx
  rcases hx with rfl | rfl
  · exact Subgroup.mul_mem _ (Subgroup.subset_closure (by simp)) (Subgroup.subset_closure (by simp))
  · exact Subgroup.subset_closure (by simp)

theorem card_S5 : Nat.card (Perm (Fin 5)) = 120 := by
  rw [Nat.card_eq_fintype_card, Fintype.card_perm]; rfl

theorem index_of_order (g : Perm (Fin 5)) {m : ℕ} (hm : orderOf g = m) (hpos : 0 < m) :
    (Subgroup.zpowers g).index = 120 / m := by
  have h := (Subgroup.zpowers g).index_mul_card
  rw [card_S5, Nat.card_eq_fintype_card, Fintype.card_zpowers, hm] at h
  rw [← h, Nat.mul_div_cancel _ hpos]

/-- Vertices: `30` cosets of `⟨S⟩`. -/
theorem index_S : (Subgroup.zpowers S).index = 30 := by
  rw [index_of_order S orderOf_S (by norm_num)]
/-- Edges: `60` cosets of `⟨A⟩`. -/
theorem index_A : (Subgroup.zpowers A).index = 60 := by
  rw [index_of_order A orderOf_A (by norm_num)]
/-- Faces: `24` cosets of `⟨S·A⟩`. -/
theorem index_SA : (Subgroup.zpowers (S * A)).index = 24 := by
  rw [index_of_order (S * A) orderOf_SA (by norm_num)]

/-- **Euler characteristic `−6`, genus `4`.** -/
theorem euler :
    ((Subgroup.zpowers S).index : ℤ) - (Subgroup.zpowers A).index
      + (Subgroup.zpowers (S * A)).index = -6 ∧ (2 : ℤ) - 2 * 4 = -6 := by
  rw [index_S, index_A, index_SA]; norm_num

/-- **Gauss–Bonnet count.** Areas in units of `π`: a `(2,4,5)` triangle has area
`1 − (1/2 + 1/4 + 1/5) = 1/20`; genus 4 has area `2(2g − 2) = 12`; so `240` triangles. -/
theorem triangle_count :
    (1 : ℚ) - (1/2 + 1/4 + 1/5) = 1/20 ∧ (2 * (2 * 4 - 2) : ℚ) / (1/20) = 240 := by
  norm_num

end QOU.BringRegularMap
