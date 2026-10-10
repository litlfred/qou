/-
# Far commutation at general rank, reduced to the 4-element commuting cell

Companion to `HeckeDihedralBraidReduction` (merged): the same parabolic
localization, applied to a NON-adjacent generator pair (order-2 product,
`M i j = 2`). The dihedral group is `⟨sᵢ,sⱼ⟩ ≅ ℤ₂ × ℤ₂` with the 4-element
cell `[e, sᵢ, sⱼ, sᵢsⱼ]` (lengths `[0,1,1,2]`), and far commutation
`σᵢσⱼ = σⱼσᵢ` localizes to a finite check on that cell. With this file,
ALL THREE presentation-law kinds are covered at general rank:

| law | status |
|---|---|
| Hecke quadratic | proved outright at every rank (`mulStep_quadratic`, merged) |
| braid (m = 3) | reduced to the S₃ coset datum (`braid_of_dihedral`, merged) |
| far commutation (m = 2) | reduced to the ℤ₂×ℤ₂ coset datum (**this file**) |

Proved here (sorry-free):

* `descentC2σi` / `descentC2σj` — the two cell descent structures
  (`decide`-checked), and **`cell_far_commute`** — far commutation on the
  4-element cell (finite check);
* **`CommutingCosetStructure`** — the parabolic factorization datum
  `W ≃ C × Fin 4` with length additivity and cell-wise actions;
* **`far_commute_of_commuting`** — `σᵢσⱼ = σⱼσᵢ` on ANY module carrying
  the datum (fibre localization + the cell check);
* `commutingSelf` — the rank-2 self-instance (non-vacuous inhabitation).

As with the braid, the remaining open content is exactly the existence of
the coset datum for each `M i j = 2` pair of a Coxeter system (Bourbaki
parabolic decomposition) — the algebra layer is complete for all three
law kinds.

HONESTY (STRICT): conditional on the coset datum; its general-Coxeter
existence is not proved; no general-n class instance declared. Nothing
wired; `1/(8π)` stays phase-4. Base ring (§7c): generic `[CommRing R]`.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeDescentQuadratic

namespace QOU.Machinery.HeckeGeneral

variable {W : Type*} {R : Type*} [CommRing R]

/-! ## The 4-element commuting cell -/

/-- Descent structure of the first generator on the ℤ₂×ℤ₂ cell
`[e, sᵢ, sⱼ, sᵢsⱼ]` (step pairs `0↔1, 2↔3`; lengths `[0,1,1,2]`). -/
def descentC2σi : DescentStructure (Fin 4) where
  t := ![1, 0, 3, 2]
  len := ![0, 1, 1, 2]
  t_invol := by decide
  len_ne := by decide

/-- Descent structure of the second generator on the cell
(step pairs `0↔2, 1↔3`). -/
def descentC2σj : DescentStructure (Fin 4) where
  t := ![2, 3, 0, 1]
  len := ![0, 1, 1, 2]
  t_invol := by decide
  len_ne := by decide

/-- **Far commutation on the cell** — the finite check that anchors the
reduction. -/
theorem cell_far_commute (h : R) (V : Fin 4 → R) :
    mulStep descentC2σi h (mulStep descentC2σj h V)
      = mulStep descentC2σj h (mulStep descentC2σi h V) := by
  funext e
  fin_cases e <;>
    simp [mulStep, descentC2σi, descentC2σj] <;> ring

/-! ## The commuting coset structure and the reduction -/

/-- **Commuting (order-2 pair) coset structure**: the parabolic
factorization datum for a non-adjacent generator pair. `W` factors as
`C × Fin 4` (coset space × the ℤ₂×ℤ₂ cell), lengths are additive along
the cell, and the two step maps act cell-wise. -/
structure CommutingCosetStructure (W : Type*) where
  /-- The coset space. -/
  C : Type*
  /-- The parabolic factorization `W ≃ C × (ℤ₂×ℤ₂ cell)`. -/
  equiv : W ≃ C × Fin 4
  /-- The global length. -/
  len : W → ℕ
  /-- The length of the minimal coset representative. -/
  len0 : C → ℕ
  /-- Step map of the first generator. -/
  ti : W → W
  /-- Step map of the second generator. -/
  tj : W → W
  /-- Length additivity along the cell. -/
  len_add : ∀ w, len w = len0 (equiv w).1 + descentC2σi.len (equiv w).2
  /-- The first generator acts cell-wise. -/
  ti_eq : ∀ w, equiv (ti w) = ((equiv w).1, descentC2σi.t (equiv w).2)
  /-- The second generator acts cell-wise. -/
  tj_eq : ∀ w, equiv (tj w) = ((equiv w).1, descentC2σj.t (equiv w).2)

namespace CommutingCosetStructure

variable (S : CommutingCosetStructure W)

/-- The first generator's induced descent structure. -/
def Di : DescentStructure W where
  t := S.ti
  len := S.len
  t_invol := fun w => by
    apply S.equiv.injective
    rw [S.ti_eq, S.ti_eq, descentC2σi.t_invol]
  len_ne := fun w => by
    rw [S.len_add (S.ti w), S.len_add w, S.ti_eq]
    dsimp only
    have h := descentC2σi.len_ne (S.equiv w).2
    omega

/-- The second generator's induced descent structure. -/
def Dj : DescentStructure W where
  t := S.tj
  len := S.len
  t_invol := fun w => by
    apply S.equiv.injective
    rw [S.tj_eq, S.tj_eq, descentC2σj.t_invol]
  len_ne := fun w => by
    rw [S.len_add (S.tj w), S.len_add w, S.tj_eq]
    dsimp only
    have h : descentC2σi.len (descentC2σj.t (S.equiv w).2)
        ≠ descentC2σi.len (S.equiv w).2 := descentC2σj.len_ne (S.equiv w).2
    omega

@[simp] lemma Di_t : S.Di.t = S.ti := rfl
@[simp] lemma Di_len : S.Di.len = S.len := rfl
@[simp] lemma Dj_t : S.Dj.t = S.tj := rfl
@[simp] lemma Dj_len : S.Dj.len = S.len := rfl

/-- The fibre restriction of a state over a fixed coset. -/
def fib (v : W → R) (c : S.C) : Fin 4 → R := fun e => v (S.equiv.symm (c, e))

lemma ti_symm (c : S.C) (e : Fin 4) :
    S.ti (S.equiv.symm (c, e)) = S.equiv.symm (c, descentC2σi.t e) := by
  apply S.equiv.injective
  rw [S.ti_eq]
  simp [Equiv.apply_symm_apply]

lemma tj_symm (c : S.C) (e : Fin 4) :
    S.tj (S.equiv.symm (c, e)) = S.equiv.symm (c, descentC2σj.t e) := by
  apply S.equiv.injective
  rw [S.tj_eq]
  simp [Equiv.apply_symm_apply]

lemma len_symm (c : S.C) (e : Fin 4) :
    S.len (S.equiv.symm (c, e)) = S.len0 c + descentC2σi.len e := by
  rw [S.len_add]
  simp [Equiv.apply_symm_apply]

/-- Cell-restriction of the first generator's action. -/
theorem restrict_i (h : R) (v : W → R) (c : S.C) (e : Fin 4) :
    mulStep S.Di h v (S.equiv.symm (c, e))
      = mulStep descentC2σi h (S.fib v c) e := by
  simp only [mulStep, Di_t, Di_len, fib, ti_symm, len_symm]
  congr 1
  exact if_congr (by omega) rfl rfl

/-- Cell-restriction of the second generator's action. -/
theorem restrict_j (h : R) (v : W → R) (c : S.C) (e : Fin 4) :
    mulStep S.Dj h v (S.equiv.symm (c, e))
      = mulStep descentC2σj h (S.fib v c) e := by
  simp only [mulStep, Dj_t, Dj_len, fib, tj_symm, len_symm]
  congr 1
  refine if_congr ?_ rfl rfl
  show S.len0 c + descentC2σi.len (descentC2σj.t e) < S.len0 c + descentC2σi.len e
      ↔ descentC2σi.len (descentC2σj.t e) < descentC2σi.len e
  omega

/-- **FAR COMMUTATION AT GENERAL RANK, from the coset datum**:
`σᵢσⱼ = σⱼσᵢ` on any descent module carrying a commuting coset structure —
fibre localization plus the 4-element cell check. Together with the merged
quadratic (all ranks, outright) and braid (reduced to the S₃ datum), all
three presentation-law kinds are now covered at general rank. -/
theorem far_commute_of_commuting (h : R) (v : W → R) :
    mulStep S.Di h (mulStep S.Dj h v)
      = mulStep S.Dj h (mulStep S.Di h v) := by
  funext w
  have hw : w = S.equiv.symm ((S.equiv w).1, (S.equiv w).2) := by
    simp [Prod.mk.eta, Equiv.symm_apply_apply]
  rw [hw]
  set c := (S.equiv w).1
  set e := (S.equiv w).2
  have fib_i : ∀ u : W → R, S.fib (mulStep S.Di h u) c
      = mulStep descentC2σi h (S.fib u c) :=
    fun u => funext fun e' => S.restrict_i h u c e'
  have fib_j : ∀ u : W → R, S.fib (mulStep S.Dj h u) c
      = mulStep descentC2σj h (S.fib u c) :=
    fun u => funext fun e' => S.restrict_j h u c e'
  rw [S.restrict_i, S.restrict_j, fib_j, fib_i]
  exact congrFun (cell_far_commute h (S.fib v c)) e

end CommutingCosetStructure

/-- The rank-2 self-instance: `W = Fin 4` with the trivial coset space —
non-vacuous inhabitation, re-deriving the cell check. -/
def commutingSelf : CommutingCosetStructure (Fin 4) where
  C := PUnit
  equiv := (Equiv.punitProd (Fin 4)).symm
  len := descentC2σi.len
  len0 := fun _ => 0
  ti := descentC2σi.t
  tj := descentC2σj.t
  len_add := fun w => by simp [Equiv.punitProd]
  ti_eq := fun w => by simp [Equiv.punitProd]
  tj_eq := fun w => by simp [Equiv.punitProd]

end QOU.Machinery.HeckeGeneral
