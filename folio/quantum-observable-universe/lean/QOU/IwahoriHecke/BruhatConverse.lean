import QOU.IwahoriHecke.BruhatReflection

/-!
# `BruhatLe → ReflLe` — the converse bridge closes

`QOU.IwahoriHecke.BruhatReflection` proved `ReflLe → BruhatLe` and left the converse open, having
recorded **two** wrong diagnoses of what blocked it (the lifting property; then a non-reduced-subword
statement that turned out to be outright false). This file closes it, so the two definitions of the
Bruhat order — the corpus's **subword** `BruhatLe` and the **reflection-generated** `ReflLe` of
Mathas and Dipper–James — coincide.

## What closes

* **`reflLe_of_bruhatLe`** — the converse.
* **`bruhatLe_iff_reflLe`** — hence the two orders are **the same relation**, so a result stated
  against either may be cited for the other. That is what a consumer of Mathas' Prop 3.7 needs.
* **`reflLe_mul_simple_of_ascent`** — the upward lifting property for `≤ᵣ` that
  `BruhatReflection` isolated as the missing input, now proved.

## How the blocked branch was unblocked

The obstacle `BruhatReflection` named was real: the induction on `ℓ(w)` splits a reduced witness
`ω'` for `u` inside `ω = ω₁ ++ [s]`, and the branch where `ω'` **uses** the final `s` yields
`u·s ≤ᵣ w·s` and needs `u ≤ᵣ w`, i.e. upward lifting for `≤ᵣ`. `reflStep_mul_simple` handled one
step; the chain was open because nothing keeps `s` an ascent at the intermediate elements.

**The fix is that the intermediate elements are all shorter than `w`, so the outer induction
hypothesis applies to them.** Carrying that hypothesis into the lifting lemma — as `ConverseBelow`
— closes the descent case:

* `s` an **ascent** at the intermediate `z` — recurse along the chain, then `reflStep_mul_simple`
  on the last step.
* `s` a **descent** at `z` — then `x ≤ z` in the *subword* order (via `bruhatLe_of_reflLe`), and
  `bruhatLe_mul_simple_of_isRightDescent` — the lifting property proved in `BruhatReflection` —
  gives `x·s ≤ z`. Since `ℓ(z) < ℓ(y) < N`, the carried hypothesis converts that to `x·s ≤ᵣ z`, and
  `z →ᵣ y →ᵣ y·s` finishes.

So the lifting property proved earlier **is** used here — just not where the first wrong diagnosis
said it would be. It resolves the descent case of the chain, not the branch itself.

## Scope

Nothing here is conditional. `DihedralExact` and `M i j ≠ 0` used to be carried exactly as
`Matsumoto` carried them, since the subword property is used throughout; `CoxeterDihedralOrder`
proves both from the geometric representation, so the two order equivalences hold for **every**
Coxeter system.

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, Thm 2.2.2 (the two orders agree)
-- Ref: [humphreys1990] Reflection Groups and Coxeter Groups, §5.10
-- Ref: [mathas1999] Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group, Prop 3.7
-- Ref: [leitner2026] beans qou-3k66, qou-phir
-/

namespace QOU.IwahoriHecke.BruhatConverse

open CoxeterSystem List
open QOU.Machinery.CoxeterParabolic QOU.Machinery.CoxeterBruhat
open QOU.Machinery.CoxeterBruhatOrder QOU.Machinery.CoxeterRankTwo
open QOU.IwahoriHecke.BruhatSubword QOU.IwahoriHecke.Matsumoto
open QOU.IwahoriHecke.BruhatReflection

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd

/-- The converse, restricted to elements shorter than `N`. This is the outer induction hypothesis,
named so that the upward-lifting lemma can take it as an argument — which is exactly what makes its
descent case go through. -/
def ConverseBelow (N : ℕ) : Prop :=
  ∀ w : W, ℓ w < N → ∀ u : W, BruhatLe cs u w → ReflLe cs u w

/-! ## Upward lifting for `≤ᵣ` -/

/-- **The upward lifting property for `≤ᵣ`** — the input `BruhatReflection` isolated and could not
supply.

`x ≤ᵣ y` with `s` a right *ascent* of `y` gives `x·s ≤ᵣ y·s`, provided the converse is already known
below `N` and `ℓ(y) < N`.

Note there is **no hypothesis that `s` is an ascent of `x`**: the first draft carried one and the
compiler reported it unused. In the `refl` case `x = y` supplies it, and neither the ascent nor the
descent case of the chain refers to `x`'s own length. -/
theorem reflLe_mul_simple_of_ascent {N : ℕ} (IH : ConverseBelow cs N) {s : B} {x : W} :
    ∀ {y : W}, ReflLe cs x y → ℓ y < N → ℓ y < ℓ (y * cs.simple s) →
      ReflLe cs (x * cs.simple s) (y * cs.simple s) := by
  intro y h
  induction h with
  | refl => intro _ _; exact Relation.ReflTransGen.refl
  | @tail z y' hxz hzy ih =>
    intro hy'N hy'
    have hzlt : ℓ z < ℓ y' := by
      obtain ⟨t, _, _, hlt⟩ := hzy
      exact hlt
    have hzN : ℓ z < N := by omega
    by_cases hdesc : cs.IsRightDescent z s
    · -- `s` is a descent at `z`: drop to the subword order, lift there, and come back.
      have hxz' : BruhatLe cs x z := bruhatLe_of_reflLe cs hxz
      have hlift : BruhatLe cs (x * cs.simple s) z :=
        bruhatLe_mul_simple_of_isRightDescent cs hxz' hdesc
      have hxsz : ReflLe cs (x * cs.simple s) z := IH z hzN _ hlift
      have hstep : ReflStep cs y' (y' * cs.simple s) :=
        ⟨cs.simple s, cs.isReflection_simple s, rfl, hy'⟩
      exact ((hxsz.tail hzy).tail hstep)
    · -- `s` stays an ascent at `z`: recurse, then push the last step across.
      have hasc : ℓ z < ℓ (z * cs.simple s) := by
        rw [cs.not_isRightDescent_iff] at hdesc
        omega
      exact (ih hzN hasc).tail (reflStep_mul_simple cs hzy hasc hy')

/-! ## The converse -/

private theorem reflLe_aux :
    ∀ (n : ℕ) (w : W), ℓ w = n → ∀ u : W, BruhatLe cs u w → ReflLe cs u w := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ihn =>
    intro w hw u hle
    have IH : ConverseBelow cs n := fun w' hw' u' h' => ihn (ℓ w') hw' w' rfl u' h'
    rcases Nat.eq_zero_or_pos n with hn | hn
    · -- `w = 1`, so `u = 1`.
      have hw1 : w = 1 := cs.length_eq_zero_iff.mp (by omega)
      subst hw1
      have : u = 1 := (bruhatLe_one_iff cs).mp hle
      subst this
      exact Relation.ReflTransGen.refl
    · -- Peel a right descent of `w`.
      have hwne : w ≠ 1 := fun hc => by
        rw [hc, cs.length_one] at hw; omega
      obtain ⟨s, hs⟩ := cs.exists_rightDescent_of_ne_one hwne
      obtain ⟨ω₁, hred₁, hprod₁, hredc, hprodc⟩ := exists_reduced_concat cs hs
      have hwsN : ℓ (w * cs.simple s) < n := by
        have : ℓ (w * cs.simple s) < ℓ w := hs
        omega
      -- A reduced subword of `ω₁ ++ [s]` with product `u`.
      obtain ⟨ω', hsub, hu⟩ := subword_property cs hle hredc hprodc
      obtain ⟨ω'', hsub'', hred'', hprod''⟩ := QOU.Machinery.CoxeterDeletion.exists_reduced_sublist' cs ω'
      have hsubω : ω'' <+ ω₁ ++ [s] := hsub''.trans hsub
      have huω : π ω'' = u := by rw [hprod'', hu]
      obtain ⟨a, b, rfl, ha, hb⟩ := List.sublist_append_iff.mp hsubω
      rcases List.sublist_singleton.mp hb with rfl | rfl
      · -- The witness avoids the final `s`: `u ≤ w·s`, one step below.
        have hua : π a = u := by rw [← huω, cs.wordProd_append]; simp
        have hle' : BruhatLe cs u (w * cs.simple s) := ⟨ω₁, a, hred₁, hprod₁, ha, hua⟩
        have hru : ReflLe cs u (w * cs.simple s) := IH _ hwsN u hle'
        refine hru.tail ⟨cs.simple s, cs.isReflection_simple s, ?_, hs⟩
        rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
      · -- The witness uses the final `s`: `u·s ≤ w·s`, then upward lifting.
        have hua : π a = u * cs.simple s := by
          rw [← huω, cs.wordProd_append, cs.wordProd_singleton, mul_assoc,
            cs.simple_mul_simple_self, mul_one]
        have hle' : BruhatLe cs (u * cs.simple s) (w * cs.simple s) :=
          ⟨ω₁, a, hred₁, hprod₁, ha, hua⟩
        have hru : ReflLe cs (u * cs.simple s) (w * cs.simple s) := IH _ hwsN _ hle'
        -- `s` is an ascent of `u·s` and of `w·s`.
        have hlenu : ℓ u = (a ++ [s]).length := by rw [← huω]; exact hred''
        have hlena : ℓ (u * cs.simple s) ≤ a.length := by
          rw [← hua]; exact cs.length_wordProd_le a
        have hascu : ℓ (u * cs.simple s) < ℓ (u * cs.simple s * cs.simple s) := by
          rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
          simp only [List.length_append, List.length_singleton] at hlenu
          omega
        have hascw : ℓ (w * cs.simple s) < ℓ (w * cs.simple s * cs.simple s) := by
          rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
          exact hs
        have := reflLe_mul_simple_of_ascent cs IH (s := s) hru hwsN hascw
        rwa [mul_assoc, cs.simple_mul_simple_self, mul_one, mul_assoc,
          cs.simple_mul_simple_self, mul_one] at this

/-- **`BruhatLe → ReflLe`.** The converse bridge, closed. -/
theorem reflLe_of_bruhatLe
    {u w : W} (h : BruhatLe cs u w) : ReflLe cs u w :=
  reflLe_aux cs (ℓ w) w rfl u h

/-- **The two Bruhat orders are the same relation.**

The corpus's subword `BruhatLe` and the reflection-generated `ReflLe` of Mathas / Dipper–James agree
on the nose, so a statement proved against either may be cited for the other. -/
theorem bruhatLe_iff_reflLe
    {u w : W} : BruhatLe cs u w ↔ ReflLe cs u w :=
  ⟨reflLe_of_bruhatLe cs, bruhatLe_of_reflLe cs⟩

/-! ## The left-handed mirror — free, and the form the tableau side needs

`BruhatReflection`'s left-handed section (`LeftReflStep` / `LeftReflLe`) exists because the tableau
side of Mathas' Prop. 3.7 produces left multiplications, and it closed `LeftReflLe → BruhatLe` by
transport through `⁻¹`. It recorded the other direction as blocked on `qou-3k66`.

`qou-3k66` is closed above, so the same transport now runs backwards. Nothing here re-proves any
part of the converse — it mirrors `reflStep`/`reflLe` inversion the other way and composes. -/

/-- A right step inverts to a left step — the mirror of
`BruhatReflection.reflStep_inv_of_leftReflStep`. -/
theorem leftReflStep_inv_of_reflStep {v w : W} (h : ReflStep cs v w) :
    LeftReflStep cs v⁻¹ w⁻¹ := by
  obtain ⟨t, ht, hw, hl⟩ := h
  refine ⟨t, ht, ?_, ?_⟩
  · rw [hw, mul_inv_rev, ht.inv]
  · rwa [cs.length_inv, cs.length_inv]

/-- The chain version. As on the right-handed side, the chain does **not** reverse: `⁻¹` is applied
pointwise and `ReflTransGen` is closed under that. -/
theorem leftReflLe_inv_of_reflLe {v w : W} (h : ReflLe cs v w) :
    LeftReflLe cs v⁻¹ w⁻¹ := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih => exact ih.tail (leftReflStep_inv_of_reflStep cs hstep)

/-- **`BruhatLe → LeftReflLe`** — the direction `BruhatReflection` recorded as blocked. -/
theorem leftReflLe_of_bruhatLe
    {u w : W} (h : BruhatLe cs u w) : LeftReflLe cs u w := by
  have h' : BruhatLe cs u⁻¹ w⁻¹ := (bruhatLe_inv_iff cs).mpr h
  simpa using leftReflLe_inv_of_reflLe cs (reflLe_of_bruhatLe cs h')

/-- `LeftReflLe → BruhatLe` in general — the generic form of
`BruhatReflection.bruhatLe_of_leftReflLe_An`, which was stated only on type `A`. -/
theorem bruhatLe_of_leftReflLe
    {u w : W} (h : LeftReflLe cs u w) : BruhatLe cs u w :=
  (bruhatLe_inv_iff cs).mp (bruhatLe_of_reflLe cs (reflLe_inv_of_leftReflLe cs h))

/-- **The subword order and the LEFT-handed reflection order also coincide.** -/
theorem bruhatLe_iff_leftReflLe {u w : W} :
    BruhatLe cs u w ↔ LeftReflLe cs u w :=
  ⟨leftReflLe_of_bruhatLe cs, bruhatLe_of_leftReflLe cs⟩

/-! ## Type `A`: hypothesis-free -/

theorem reflLe_of_bruhatLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : BruhatLe cs u w) :
    ReflLe cs u w :=
  reflLe_of_bruhatLe cs h

/-- **The two orders coincide on type `A`**, with no hypothesis — the symmetric group, hence the
form a consumer of Mathas / Dipper–James works in. -/
theorem bruhatLe_iff_reflLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} :
    BruhatLe cs u w ↔ ReflLe cs u w :=
  bruhatLe_iff_reflLe cs

end QOU.IwahoriHecke.BruhatConverse
