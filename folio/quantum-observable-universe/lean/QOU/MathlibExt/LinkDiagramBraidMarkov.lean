import QOU.MathlibExt.LinkDiagramMarkov
import QOU.MathlibExt.BraidGroup
import QOU.MathlibExt.MarkovMoves
import Mathlib.GroupTheory.FreeGroup.Reduce

/-!
# Closures of braids and Markov invariance

The closure of a braid word (`braidClosure`) descends to the braid group
`QOU.MathlibExt.Braid.BraidGroup m`: words that represent the same braid have Reidemeister
equivalent closures. The proof shows that the elements `g` of the free group whose reduced word can
be deleted from any word without changing the closure form a normal subgroup, and that this
subgroup contains the Artin relators (`braidClosure_farComm`, `braidClosure_braid`,
`braidClosure_cancel`). It therefore contains their normal closure, which is the kernel of the map
from the free group to the braid group.

With conjugation (`braidClosure_append_comm`) and stabilisation (`braidClosure_stab`) this gives
the easy direction of Markov's theorem for codes (`reidemeisterEquiv_of_markovEquiv`): braids that
are Markov equivalent in the Artin tower `artinBraidTower` have Reidemeister equivalent closures.

The converse (Reidemeister equivalent closures come from Markov equivalent braids) is Markov's
theorem proper. It is not proved here.

`ReidemeisterEquiv` includes the turn slide (`Move.slide`) as a primitive move, and the
conjugation and far-commutation steps use it. Whether the slide follows from the other moves is
not settled here, so every result in this file holds for the move set that includes it.

-- Ref: [kassel2008] Kassel–Turaev, "Braid Groups", GTM 247, §2.5 (closure and Markov moves)
-/

namespace QOU.MathlibExt.PL.Diagram

open FreeGroup QOU.MathlibExt.Braid QOU.MathlibExt.MarkovMoves

variable {m : ℕ}

/-- The closure of a word, as a bundled code. -/
abbrev bc (w : List (Fin m × Bool)) : Bundled := ⟨_, braidClosure w⟩

/-- Free reduction inside a word does not change its closure. -/
theorem braidClosure_red {L₁ L₂ : List (Fin m × Bool)} (h : FreeGroup.Red L₁ L₂)
    (u v : List (Fin m × Bool)) :
    ReidemeisterEquiv (bc (u ++ L₁ ++ v)) (bc (u ++ L₂ ++ v)) := by
  induction h with
  | refl => exact .refl _
  | tail _ hs ih =>
    refine ih.trans ?_
    obtain @⟨A, B, x, b⟩ := hs
    exact (braidClosure_congr (by simp)).trans
      ((braidClosure_cancel (u ++ A) (B ++ v) x b).trans (braidClosure_congr (by simp)))

/-- Replacing a word by the reduced word of the free group element it represents does not change
its closure. -/
theorem braidClosure_toWord_mk (L u v : List (Fin m × Bool)) :
    ReidemeisterEquiv (bc (u ++ L ++ v)) (bc (u ++ (FreeGroup.mk L).toWord ++ v)) := by
  rw [toWord_mk]
  exact braidClosure_red reduce.red u v

/-- `g` can be deleted from any word without changing the closure. -/
def Deletable (g : FreeGroup (Fin m)) : Prop :=
  ∀ u v : List (Fin m × Bool), ReidemeisterEquiv (bc (u ++ g.toWord ++ v)) (bc (u ++ v))

theorem deletable_one : Deletable (1 : FreeGroup (Fin m)) := fun u v => by
  rw [toWord_one]; exact braidClosure_congr (by simp)

/-- The product of two reduced words reduces to the reduced word of the product. -/
theorem braidClosure_mul (x y : FreeGroup (Fin m)) (u v : List (Fin m × Bool)) :
    ReidemeisterEquiv (bc (u ++ (x * y).toWord ++ v)) (bc (u ++ (x.toWord ++ y.toWord) ++ v)) := by
  have h := braidClosure_toWord_mk (x.toWord ++ y.toWord) u v
  rw [← mul_mk, mk_toWord, mk_toWord] at h
  exact h.symm

theorem Deletable.mul {x y : FreeGroup (Fin m)} (hx : Deletable x) (hy : Deletable y) :
    Deletable (x * y) := fun u v =>
  (braidClosure_mul x y u v).trans ((braidClosure_congr (by simp)).trans
    ((hy (u ++ x.toWord) v).trans (hx u v)))

theorem Deletable.inv {x : FreeGroup (Fin m)} (hx : Deletable x) : Deletable x⁻¹ := fun u v => by
  refine ((hx (u ++ x⁻¹.toWord) v).symm.trans ((braidClosure_congr (by simp)).trans
    ((braidClosure_mul x⁻¹ x u v).symm.trans ?_)))
  rw [inv_mul_cancel, toWord_one]
  exact braidClosure_congr (by simp)

theorem Deletable.conj {x : FreeGroup (Fin m)} (hx : Deletable x) (y : FreeGroup (Fin m)) :
    Deletable (y * x * y⁻¹) := fun u v => by
  refine (braidClosure_mul (y * x) y⁻¹ u v).trans ((braidClosure_congr (by simp)).trans
    ((braidClosure_mul y x u (y⁻¹.toWord ++ v)).trans ((braidClosure_congr (by simp)).trans
      ((hx (u ++ y.toWord) (y⁻¹.toWord ++ v)).trans ((braidClosure_congr (by simp)).trans
        ((braidClosure_mul y y⁻¹ u v).symm.trans ?_))))))
  rw [mul_inv_cancel, toWord_one]
  exact braidClosure_congr (by simp)

/-- The deletable elements form a normal subgroup of the free group. -/
def deletableSubgroup (m : ℕ) : Subgroup (FreeGroup (Fin m)) where
  carrier := {g | Deletable g}
  one_mem' := deletable_one
  mul_mem' := Deletable.mul
  inv_mem' := Deletable.inv

instance (m : ℕ) : (deletableSubgroup m).Normal :=
  ⟨fun _ hx y => Deletable.conj hx y⟩

/-- A word whose free group element is deletable can be deleted. -/
theorem deletable_word {L : List (Fin m × Bool)} (h : Deletable (FreeGroup.mk L))
    (u v : List (Fin m × Bool)) : ReidemeisterEquiv (bc (u ++ L ++ v)) (bc (u ++ v)) :=
  (braidClosure_toWord_mk L u v).trans (h u v)

/-- A word that can be deleted from any word represents a deletable element. -/
theorem deletable_of_word {L : List (Fin m × Bool)}
    (hL : ∀ u v, ReidemeisterEquiv (bc (u ++ L ++ v)) (bc (u ++ v))) :
    Deletable (FreeGroup.mk L) := fun u v =>
  (braidClosure_toWord_mk L u v).symm.trans (hL u v)

/-- Every Artin relator is deletable. -/
theorem relators_deletable : braidRelators m ⊆ deletableSubgroup m := by
  rintro r (⟨i, j, hij, rfl⟩ | ⟨i, h, rfl⟩)
  · have hr : of i * of j * (of i)⁻¹ * (of j)⁻¹ =
        FreeGroup.mk [(i, true), (j, true), (i, false), (j, false)] := by
      simp [FreeGroup.of, inv_mk, invRev, mul_mk]
    show Deletable _
    rw [hr]
    refine deletable_of_word fun u v => ?_
    have hc := braidClosure_cancel (u ++ [(j, true)]) ([(j, false)] ++ v) i true
    have hc' := braidClosure_cancel u v j true
    exact (braidClosure_congr (by simp)).trans
      ((braidClosure_farComm u ([(i, false), (j, false)] ++ v) i j true true (Or.inl hij)).symm.trans
        ((braidClosure_congr (by simp)).trans (hc.trans ((braidClosure_congr (by simp)).trans hc'))))
  · set k : Fin m := ⟨i.val + 1, h⟩
    have hr : of i * of k * of i * (of k * of i * of k)⁻¹ =
        FreeGroup.mk [(i, true), (k, true), (i, true), (k, false), (i, false), (k, false)] := by
      simp [FreeGroup.of, inv_mk, invRev, mul_mk]
    show Deletable _
    rw [hr]
    refine deletable_of_word fun u v => ?_
    have h1 := braidClosure_cancel (u ++ [(k, true), (i, true)]) ([(i, false), (k, false)] ++ v) k true
    have h2 := braidClosure_cancel (u ++ [(k, true)]) ([(k, false)] ++ v) i true
    have h3 := braidClosure_cancel u v k true
    exact (braidClosure_congr (by simp)).trans
      ((braidClosure_braid u ([(k, false), (i, false), (k, false)] ++ v) i k rfl).trans
        ((braidClosure_congr (by simp)).trans (h1.trans ((braidClosure_congr (by simp)).trans
          (h2.trans ((braidClosure_congr (by simp)).trans h3))))))

/-- The kernel of the map onto the braid group consists of deletable elements. -/
theorem normalClosure_le_deletable :
    Subgroup.normalClosure (braidRelators m) ≤ deletableSubgroup m :=
  Subgroup.normalClosure_le_normal relators_deletable

/-- **The closure descends to the braid group.** Free group elements with the same image in the
braid group have Reidemeister equivalent closures. -/
theorem braidClosure_of_mk_eq {x y : FreeGroup (Fin m)}
    (h : PresentedGroup.mk (braidRelators m) x = PresentedGroup.mk (braidRelators m) y) :
    ReidemeisterEquiv (bc x.toWord) (bc y.toWord) := by
  have hd : Deletable (x⁻¹ * y) := normalClosure_le_deletable (by
    rw [← PresentedGroup.mk_eq_one_iff, _root_.map_mul, _root_.map_inv, h, inv_mul_cancel])
  have h1 := braidClosure_mul x (x⁻¹ * y) [] []
  rw [mul_inv_cancel_left] at h1
  exact (braidClosure_congr (w' := x.toWord ++ []) (by simp)).trans ((hd x.toWord []).symm.trans
    ((braidClosure_congr (w' := [] ++ (x.toWord ++ (x⁻¹ * y).toWord) ++ []) (by simp)).trans
      (h1.symm.trans (braidClosure_congr (by simp)))))

/-! ### The Artin tower and Markov invariance -/

/-- Adding a strand to a braid on the right: `σᵢ ↦ σᵢ`, as a map of free groups. -/
theorem map_castSucc_relator {n : ℕ} {r : FreeGroup (Fin n)} (hr : r ∈ braidRelators n) :
    FreeGroup.map Fin.castSucc r ∈ braidRelators (n + 1) := by
  rcases hr with ⟨i, j, hij, rfl⟩ | ⟨i, h, rfl⟩
  · exact Or.inl ⟨i.castSucc, j.castSucc, by simpa using hij, by simp⟩
  · refine Or.inr ⟨i.castSucc, by simp only [Fin.coe_castSucc]; omega, ?_⟩
    have : (Fin.castSucc ⟨i.val + 1, h⟩ : Fin (n + 1)) =
        ⟨i.castSucc.val + 1, by simp only [Fin.coe_castSucc]; omega⟩ :=
      Fin.ext rfl
    simp [this]

/-- The inclusion of braid groups that adds a strand: `σᵢ ↦ σᵢ`. -/
def braidIncl (n : ℕ) : BraidGroup n →* BraidGroup (n + 1) :=
  PresentedGroup.toGroup (f := fun i : Fin n => (σ i.castSucc : BraidGroup (n + 1))) (by
    intro r hr
    have hl : FreeGroup.lift (fun i : Fin n => (σ i.castSucc : BraidGroup (n + 1))) =
        (PresentedGroup.mk (braidRelators (n + 1))).comp (FreeGroup.map Fin.castSucc) :=
      FreeGroup.ext_hom _ _ fun i => rfl
    rw [hl]
    exact PresentedGroup.one_of_mem (map_castSucc_relator hr))

theorem braidIncl_mk (n : ℕ) (x : FreeGroup (Fin n)) :
    braidIncl n (PresentedGroup.mk (braidRelators n) x) =
      PresentedGroup.mk (braidRelators (n + 1)) (FreeGroup.map Fin.castSucc x) := by
  have : (braidIncl n).comp (PresentedGroup.mk (braidRelators n)) =
      (PresentedGroup.mk (braidRelators (n + 1))).comp (FreeGroup.map Fin.castSucc) :=
    FreeGroup.ext_hom _ _ fun i => by
      show braidIncl n (PresentedGroup.of i) = _
      exact (PresentedGroup.toGroup.of (rels := braidRelators n) _).trans rfl
  exact DFunLike.congr_fun this x

/-- The Artin braid groups as a tower: stabilisation adds a strand and the generator `σₙ`. -/
def artinBraidTower : BraidTower BraidGroup where
  incl := braidIncl
  gen n := σ (Fin.last n)

/-- A word representing a braid. -/
noncomputable def braidRep (β : BraidGroup m) : FreeGroup (Fin m) :=
  Classical.choose (PresentedGroup.mk_surjective (braidRelators m) β)

theorem mk_braidRep (β : BraidGroup m) : PresentedGroup.mk (braidRelators m) (braidRep β) = β :=
  Classical.choose_spec (PresentedGroup.mk_surjective (braidRelators m) β)

/-- **The closure of a braid**: the closure of any word representing it. Up to Reidemeister
equivalence it does not depend on the word (`braidGroupClosure_spec`). -/
noncomputable def braidGroupClosure (β : BraidGroup m) : Bundled := bc (braidRep β).toWord

theorem braidGroupClosure_spec {β : BraidGroup m} {x : FreeGroup (Fin m)}
    (hx : PresentedGroup.mk (braidRelators m) x = β) :
    ReidemeisterEquiv (braidGroupClosure β) (bc x.toWord) :=
  braidClosure_of_mk_eq ((mk_braidRep β).trans hx.symm)

/-- The closure of a product is that of the concatenated words. -/
theorem braidClosure_mul' (x y : FreeGroup (Fin m)) :
    ReidemeisterEquiv (bc (x * y).toWord) (bc (x.toWord ++ y.toWord)) :=
  (braidClosure_congr (w' := [] ++ (x * y).toWord ++ []) (by simp)).trans
    ((braidClosure_mul x y [] []).trans (braidClosure_congr (by simp)))

theorem braidGroupClosure_conj (a b : BraidGroup m) :
    ReidemeisterEquiv (braidGroupClosure (a * b)) (braidGroupClosure (b * a)) := by
  have hab : PresentedGroup.mk (braidRelators m) (braidRep a * braidRep b) = a * b := by
    rw [_root_.map_mul, mk_braidRep, mk_braidRep]
  have hba : PresentedGroup.mk (braidRelators m) (braidRep b * braidRep a) = b * a := by
    rw [_root_.map_mul, mk_braidRep, mk_braidRep]
  exact (braidGroupClosure_spec hab).trans ((braidClosure_mul' _ _).trans
    ((braidClosure_append_comm _ _).trans ((braidClosure_mul' _ _).symm.trans
      (braidGroupClosure_spec hba).symm)))

theorem braidGroupClosure_stab (n : ℕ) (x : BraidGroup n) (b : Bool) :
    ReidemeisterEquiv (braidGroupClosure x)
      (braidGroupClosure (braidIncl n x * (if b then σ (Fin.last n) else (σ (Fin.last n))⁻¹))) := by
  set g : FreeGroup (Fin (n + 1)) := if b then FreeGroup.of (Fin.last n)
    else (FreeGroup.of (Fin.last n))⁻¹ with hg
  have hgw : g.toWord = [(Fin.last n, b)] := by
    cases b <;> simp [hg, toWord_of, toWord_inv, invRev]
  have hy : PresentedGroup.mk (braidRelators (n + 1))
      (FreeGroup.map Fin.castSucc (braidRep x) * g) =
      braidIncl n x * (if b then σ (Fin.last n) else (σ (Fin.last n))⁻¹) := by
    rw [_root_.map_mul, ← braidIncl_mk, mk_braidRep]
    cases b <;> simp [hg, σ, PresentedGroup.of]
  have hm : FreeGroup.map Fin.castSucc (braidRep x) =
      FreeGroup.mk ((braidRep x).toWord.map fun y => (y.1.castSucc, y.2)) := by
    conv_lhs => rw [← mk_toWord (x := braidRep x)]
    exact FreeGroup.map.mk
  have h2 := braidClosure_toWord_mk ((braidRep x).toWord.map fun y => (y.1.castSucc, y.2)) []
    [(Fin.last n, b)]
  rw [← hm] at h2
  refine (braidClosure_stab (braidRep x).toWord b).trans ?_
  refine (braidClosure_congr (w' := [] ++ ((braidRep x).toWord.map fun y => (y.1.castSucc, y.2)) ++
    [(Fin.last n, b)]) (by simp)).trans (h2.trans ?_)
  rw [← hgw]
  exact ((braidClosure_mul' _ _).symm.trans (braidGroupClosure_spec hy).symm)

/-- **Markov invariance of closures** (the easy direction of Markov's theorem): Markov equivalent
braids in the Artin tower have Reidemeister equivalent closures. -/
theorem reidemeisterEquiv_of_markovEquiv {p q : Tot BraidGroup}
    (h : MarkovEquiv artinBraidTower p q) :
    ReidemeisterEquiv (braidGroupClosure p.2) (braidGroupClosure q.2) := by
  induction h with
  | rel _ _ hm =>
    cases hm with
    | conj n a b => exact braidGroupClosure_conj a b
    | stab n x => simpa using braidGroupClosure_stab n x true
    | stabInv n x => simpa using braidGroupClosure_stab n x false
  | refl => exact .refl _
  | symm _ _ _ ih => exact ih.symm
  | trans _ _ _ _ _ ih ih' => exact ih.trans ih'

end QOU.MathlibExt.PL.Diagram
