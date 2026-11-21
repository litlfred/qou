import Mathlib.Algebra.Group.Basic
import Mathlib.Data.Finset.Insert
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Abel
import Mathlib.Order.Basic

/-!
# Normalising a nerve 2-cocycle to an alternating one (route R3, surface step S1a)

Let `Q` be a downward-closed predicate on finite sets of indices (the simplices
of a nerve), and let `V : ι → ι → ι → A` satisfy the Čech cocycle identity on
every quadruple whose index set is a simplex. Čech cochains here are
unnormalised: `V i i j` need not vanish. For the surface case of route R3 one
wants to work with values on oriented 2-faces only, so the cocycle must first be
replaced by a cohomologous one that is **alternating** on every simplex.

This file gives that replacement explicitly, with a linear order on the
indices:

* `w1 x y = V x x y`, `V1 = V − δ w1`;
* `w2 x y = 0` if `x ≤ y`, else `V1 y x y`; `V2 = V1 − δ w2`.

## Results, all sorry-free

* `local_cob`: on a simplex `{x,y,z}`, `V` is the coboundary of `u = V x`
  (the acyclicity of a single simplex, by the cocycle identity at apex `x`).
* `V2_eq_sub_cob`: `V2 = V − δ (w1 + w2)` everywhere, so `V2` is cohomologous
  to `V`.
* `V2_alt`: on every 2-simplex `{a,b,c}`, `V2` vanishes on degenerate triples
  and changes sign under each transposition.

## What this does NOT do

It does not compute `H²` of any nerve. It is the reduction that lets a later
file (S1b) work with one value per oriented 2-face.

-- Ref: [manuscript] lifting-and-descent, route R3, surface step S1
Bean `qou-skn4`.
-/

namespace QOU.CentralExtension.Cech.NerveNormalize

variable {ι : Type} [LinearOrder ι] {A : Type} [AddCommGroup A]

/-- Čech coboundary of a function on pairs. -/
def cob (w : ι → ι → A) (i j k : ι) : A := w i j + w j k - w i k

/-- Downward-closed predicate on finite sets: the simplices of a nerve. -/
structure Simplicial (Q : Finset ι → Prop) : Prop where
  mono : ∀ {s t : Finset ι}, t ⊆ s → Q s → Q t

/-- The cocycle identity on every quadruple whose index set is a simplex. -/
def IsCocycle (Q : Finset ι → Prop) (V : ι → ι → ι → A) : Prop :=
  ∀ i j k l, Q {i, j, k, l} → V i j k + V i k l = V j k l + V i j l

variable {Q : Finset ι → Prop} (hQ : Simplicial Q) {V : ι → ι → ι → A}
  (hV : IsCocycle Q V)

include hQ hV in
/-- **One simplex is acyclic.** On a simplex `{x,y,z}`, `V` is the coboundary of
`u = V x`. -/
theorem local_cob {x y z : ι} (hs : Q {x, y, z}) {a b c : ι}
    (ha : a ∈ ({x, y, z} : Finset ι)) (hb : b ∈ ({x, y, z} : Finset ι))
    (hc : c ∈ ({x, y, z} : Finset ι)) : V a b c = cob (V x) a b c := by
  have hsub : ({x, a, b, c} : Finset ι) ⊆ {x, y, z} := by
    intro t ht
    simp only [Finset.mem_insert, Finset.mem_singleton] at ht
    rcases ht with rfl | rfl | rfl | rfl
    · simp
    · exact ha
    · exact hb
    · exact hc
  have e := hV x a b c (hQ.mono hsub hs)
  unfold cob
  linear_combination (norm := abel) -e

/-- First normalisation: kill the degenerate values `V x x y`. -/
def w1 (V : ι → ι → ι → A) (x y : ι) : A := V x x y

def V1 (V : ι → ι → ι → A) (x y z : ι) : A := V x y z - cob (w1 V) x y z

/-- Second normalisation: make the pair function antisymmetric, using the order. -/
def w2 (V : ι → ι → ι → A) (x y : ι) : A := if x ≤ y then 0 else V1 V y x y

/-- The normalised cocycle. -/
def V2 (V : ι → ι → ι → A) (x y z : ι) : A := V1 V x y z - cob (w2 V) x y z

theorem V2_eq_sub_cob (x y z : ι) :
    V2 V x y z = V x y z - cob (fun a b => w1 V a b + w2 V a b) x y z := by
  simp only [V2, V1, cob]; abel

section Local

variable {x y z : ι} (hs : Q {x, y, z})

/-- The local pair function after the first normalisation. -/
def u1 (V : ι → ι → ι → A) (x a b : ι) : A := V x a b - V x a a

include hQ hV hs in
theorem V1_local {a b c : ι} (ha : a ∈ ({x, y, z} : Finset ι))
    (hb : b ∈ ({x, y, z} : Finset ι)) (hc : c ∈ ({x, y, z} : Finset ι)) :
    V1 V a b c = cob (u1 V x) a b c := by
  have h1 := local_cob hQ hV hs ha hb hc
  have h2 := local_cob hQ hV hs ha ha hb
  have h3 := local_cob hQ hV hs hb hb hc
  have h4 := local_cob hQ hV hs ha ha hc
  simp only [V1, w1, u1, cob] at *
  rw [h1, h2, h3, h4]; abel

include hQ hV hs in
theorem w2_add_swap {a b : ι} (ha : a ∈ ({x, y, z} : Finset ι))
    (hb : b ∈ ({x, y, z} : Finset ι)) :
    w2 V a b + w2 V b a = u1 V x a b + u1 V x b a := by
  have e1 := V1_local hQ hV hs ha hb ha
  have e2 := V1_local hQ hV hs hb ha hb
  have e3 := V1_local hQ hV hs ha ha ha
  unfold cob u1 at *
  unfold w2
  rcases lt_trichotomy a b with h | rfl | h
  · rw [if_pos h.le, if_neg (not_le.2 h), e1]; abel
  · simp only [le_refl, if_true]
    abel
  · rw [if_neg (not_le.2 h), if_pos h.le, e2]; abel

/-- The local pair function after both normalisations. -/
def u2 (V : ι → ι → ι → A) (x a b : ι) : A := u1 V x a b - w2 V a b

include hQ hV hs in
theorem V2_local {a b c : ι} (ha : a ∈ ({x, y, z} : Finset ι))
    (hb : b ∈ ({x, y, z} : Finset ι)) (hc : c ∈ ({x, y, z} : Finset ι)) :
    V2 V a b c = cob (u2 V x) a b c := by
  have e := V1_local hQ hV hs ha hb hc
  simp only [V2]
  rw [e]
  simp only [cob]
  simp only [u2]
  abel

include hQ hV hs in
theorem u2_antisymm {a b : ι} (ha : a ∈ ({x, y, z} : Finset ι))
    (hb : b ∈ ({x, y, z} : Finset ι)) : u2 V x a b = - u2 V x b a := by
  have e := w2_add_swap hQ hV hs ha hb
  unfold u2
  linear_combination (norm := abel) -e

theorem u2_diag (x a : ι) : u2 V x a a = 0 := by
  unfold u2 u1 w2; simp

include hQ hV hs in
/-- **`V2` is alternating on every 2-simplex.** -/
theorem V2_alt {a b c : ι} (ha : a ∈ ({x, y, z} : Finset ι))
    (hb : b ∈ ({x, y, z} : Finset ι)) (hc : c ∈ ({x, y, z} : Finset ι)) :
    V2 V a a c = 0 ∧ V2 V a c c = 0 ∧ V2 V a c a = 0 ∧
      V2 V b a c = - V2 V a b c ∧ V2 V a c b = - V2 V a b c := by
  have Lb := V2_local hQ hV hs ha hb hc
  have L1 := V2_local hQ hV hs ha ha hc
  have L2 := V2_local hQ hV hs ha hc hc
  have L3 := V2_local hQ hV hs ha hc ha
  have L4 := V2_local hQ hV hs hb ha hc
  have L5 := V2_local hQ hV hs ha hc hb
  have daa := u2_diag (V := V) x a
  have dcc := u2_diag (V := V) x c
  have sab := u2_antisymm hQ hV hs ha hb
  have sac := u2_antisymm hQ hV hs ha hc
  have sbc := u2_antisymm hQ hV hs hb hc
  unfold cob at *
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · linear_combination (norm := abel) L1 + daa
  · linear_combination (norm := abel) L2 + dcc
  · linear_combination (norm := abel) L3 + sac - daa
  · linear_combination (norm := abel) L4 + Lb + sab
  · linear_combination (norm := abel) L5 + Lb + sbc

end Local

end QOU.CentralExtension.Cech.NerveNormalize
