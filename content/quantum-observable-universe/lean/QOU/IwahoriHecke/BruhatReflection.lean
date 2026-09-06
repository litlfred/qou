import QOU.IwahoriHecke.BruhatSubword

/-!
# The reflection-generated Bruhat order, the lifting property, and half the bridge

There are two standard definitions of the Bruhat order and this corpus uses one of them.

* **Subword** (`QOU.Machinery.CoxeterBruhat.BruhatLe`): some reduced word for `w` has a subword
  multiplying to `u`.
* **Reflection-generated** (`ReflLe` here): `w` is reached from `u` by multiplying on the right by
  reflections, each step increasing length. This is the `⊵` of Mathas and of Dipper–James, so it is
  the one a consumer citing that literature is actually working with.

Their equivalence is a **theorem**, not an unfolding, and treating them as interchangeable is how a
corpus ends up with two orders under one name.

## What closes here

**`ReflLe → BruhatLe`**, in full. It is short because both inputs already exist:

* `CoxeterReflectionCocycle.strong_exchange` turns one downward reflection step into one **deleted
  letter** of a reduced word — unconditional, every Coxeter system, no reducedness hypothesis on
  the reflection side;
* `BruhatSubword.bruhatLe_trans` chains the steps.

So any hypothesis of the form "`u ⊵ v` in Mathas' sense" may now be consumed by everything proved
about `BruhatLe` — the subword property, transitivity, antisymmetry.

**And the LIFTING property** (`bruhatLe_mul_simple_of_isRightDescent`, `lifting`) — the fourth and
last of the four `QOU.Machinery.CoxeterBruhat` deferred. With antisymmetry (`CoxeterBruhatOrder`)
and the subword property + transitivity (`BruhatSubword`), **all four are now proved.**

Lifting needs no induction once the subword property is available: a subword of a reduced word for
`w` ending in `s` either uses that final `s` or does not, and *both* branches already exhibit what
is wanted.

## 🛑 The converse bridge is NOT proved, and the obstacle is NOT lifting

`reflStep_of_eraseIdx` shows the atom: deleting **one** letter from a reduced word is exactly a
downward reflection step, with the reflection read off Mathlib's right inversion sequence. The
temptation is to iterate it and get `BruhatLe → ReflLe` for free.

**That does not work.** A subword deletes several letters at once, and the intermediate words are
**not reduced**, so their products need not have strictly decreasing lengths — the chain of
reflection steps a `ReflLe` requires is not the chain of deletions.

**An earlier version of this note said the repair was the lifting property. Lifting is now proved,
in this file, and the converse still does not follow — so that diagnosis was wrong.** The obstacle
that actually remains is one step down: an induction on `ℓ(w)` wants an intermediate `v` with
`ReflStep v w` and `u ≤ v`, and the natural candidate `v = π (ω.eraseIdx j)` fails to deliver
`u ≤ v` because `ω.eraseIdx j` is not reduced — so the subword of it witnessing `u` is not a
witness in the sense `BruhatLe` demands. Bridging that needs "a subword of an *arbitrary* word for
`w` still gives `u ≤ w`", which is not proved here.

So: `ReflLe → BruhatLe` ✅, `BruhatLe → ReflLe` ❌ (open — and not for the reason first written).

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, §2.1–2.2 (both definitions, Thm 2.2.2)
-- Ref: [mathas1999] Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group, Prop 3.7
-- Ref: [manuscript] beans qou-06h7, qou-phir
-/

namespace QOU.IwahoriHecke.BruhatReflection

open CoxeterSystem List
open QOU.Machinery.CoxeterParabolic QOU.Machinery.CoxeterBruhat
open QOU.IwahoriHecke.BruhatSubword QOU.IwahoriHecke.Matsumoto
open QOU.Machinery.CoxeterRankTwo

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd

/-! ## The reflection order -/

/-- One upward step: `w = v · t` for a reflection `t`, with the length going up. -/
def ReflStep (v w : W) : Prop := ∃ t : W, cs.IsReflection t ∧ w = v * t ∧ ℓ v < ℓ w

/-- **The reflection-generated Bruhat order** — Mathas' `⊵`. Transitive and reflexive by
construction, being a reflexive–transitive closure. -/
abbrev ReflLe : W → W → Prop := Relation.ReflTransGen (ReflStep cs)

theorem reflLe_refl (w : W) : ReflLe cs w w := Relation.ReflTransGen.refl

theorem reflLe_trans {u v w : W} (h₁ : ReflLe cs u v) (h₂ : ReflLe cs v w) : ReflLe cs u w :=
  h₁.trans h₂

/-! ## One step is a subword -/

/-- **A single upward reflection step lands inside the subword order.**

`t` is a right inversion of `w = v · t`, so `strong_exchange` produces a *single deleted letter* of
any reduced word for `w` whose product is `v`. Nothing here needs Matsumoto. -/
theorem bruhatLe_of_reflStep {v w : W} (h : ReflStep cs v w) : BruhatLe cs v w := by
  obtain ⟨t, ht, hw, hlt⟩ := h
  subst hw
  obtain ⟨ω, hred, hωw⟩ := cs.exists_reduced_word' (v * t)
  have hinv : cs.IsRightInversion (π ω) t := by
    refine ⟨ht, ?_⟩
    rw [← hωw, mul_assoc, ht.mul_self, mul_one]
    exact hlt
  obtain ⟨j, _, hje⟩ := strong_exchange cs ω hinv
  refine ⟨ω, ω.eraseIdx j, hred, hωw.symm, ω.eraseIdx_sublist j, ?_⟩
  rw [← hje, ← hωw, mul_assoc, ht.mul_self, mul_one]

/-! ## Hence the whole order -/

/-- **`ReflLe → BruhatLe`.** Mathas' Bruhat order refines into this corpus's subword one, so every
statement proved about `BruhatLe` — the subword property, transitivity, antisymmetry — is available
to a consumer whose hypothesis is stated in the reflection form.

Carries `DihedralExact` / `M i j ≠ 0` only because it chains with `bruhatLe_trans`; the one-step
lemma above needs neither. -/
theorem bruhatLe_of_reflLe (hDE : DihedralExact cs) (hfin : ∀ i j : B, i ≠ j → M i j ≠ 0)
    {u w : W} (h : ReflLe cs u w) : BruhatLe cs u w := by
  induction h with
  | refl => exact bruhatLe_refl cs u
  | tail _ hstep ih => exact bruhatLe_trans cs hDE hfin ih (bruhatLe_of_reflStep cs hstep)

/-! ## The converse atom — and why iterating it is not a proof -/

/-- **Deleting one letter of a reduced word is a downward reflection step.**

The reflection is the `j`-th entry of Mathlib's right inversion sequence, and
`wordProd_mul_getD_rightInvSeq` is the identity that names it. This is the atom the converse
direction would iterate.

🛑 **Iterating it does not give `BruhatLe → ReflLe`.** A subword deletes several letters, the
intermediate words are not reduced, and `ReflStep` demands a *strict length increase* at every step
— which the intermediate products need not provide. See the header: the missing input is **not**
the lifting property (proved below), but a subword statement about non-reduced words. -/
theorem reflStep_of_eraseIdx {ω : List B} (hred : cs.IsReduced ω) {j : ℕ} (hj : j < ω.length) :
    ReflStep cs (π (ω.eraseIdx j)) (π ω) := by
  classical
  set t : W := (cs.rightInvSeq ω).getD j 1 with hts
  have hmem : t ∈ cs.rightInvSeq ω := by
    have hjlen : j < (cs.rightInvSeq ω).length := by
      rw [cs.length_rightInvSeq]; exact hj
    rw [hts, List.getD_eq_getElem _ _ hjlen]
    exact List.getElem_mem hjlen
  have ht : cs.IsReflection t := cs.isReflection_of_mem_rightInvSeq ω hmem
  refine ⟨t, ht, ?_, ?_⟩
  · have h := cs.wordProd_mul_getD_rightInvSeq ω j
    rw [← hts] at h
    rw [← h, mul_assoc, ht.mul_self, mul_one]
  · have h1 : ℓ (π ω) = ω.length := hred
    have h2 : ℓ (π (ω.eraseIdx j)) ≤ (ω.eraseIdx j).length := cs.length_wordProd_le _
    have h3 : (ω.eraseIdx j).length = ω.length - 1 := List.length_eraseIdx_of_lt hj
    omega

/-! ## The lifting property — the fourth and last of `CoxeterBruhat`'s four -/

/-- A right descent is witnessed by a reduced word ending in that letter. -/
theorem exists_reduced_concat {w : W} {s : B} (h : cs.IsRightDescent w s) :
    ∃ ω : List B, cs.IsReduced ω ∧ π ω = w * cs.simple s ∧
      cs.IsReduced (ω ++ [s]) ∧ π (ω ++ [s]) = w := by
  obtain ⟨ω, hred, hω⟩ := cs.exists_reduced_word' (w * cs.simple s)
  have hprod : π (ω ++ [s]) = w := by
    rw [cs.wordProd_append, cs.wordProd_singleton, ← hω, mul_assoc,
      cs.simple_mul_simple_self, mul_one]
  refine ⟨ω, hred, hω.symm, ?_, hprod⟩
  have h1 : ℓ (π ω) = ω.length := hred
  have h2 : ℓ (w * cs.simple s) < ℓ w := h
  have h3 : ℓ w ≤ ℓ (w * cs.simple s) + 1 := by
    have := cs.length_mul_le (w * cs.simple s) (cs.simple s)
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one, cs.length_simple] at this
    exact this
  show ℓ (π (ω ++ [s])) = (ω ++ [s]).length
  rw [hprod]
  rw [hω] at h2 h3
  simp only [List.length_append, List.length_singleton]
  omega

/-- The case split the lifting property runs on: a subword of `ω ++ [s]` either uses the final `s`
or does not. -/
private theorem subword_concat_cases {ω' ω : List B} {s : B} (h : ω' <+ ω ++ [s]) :
    (∃ a, a <+ ω ∧ π ω' = π a) ∨ (∃ a, a <+ ω ∧ π ω' = π a * cs.simple s) := by
  obtain ⟨a, b, rfl, ha, hb⟩ := List.sublist_append_iff.mp h
  rcases List.sublist_singleton.mp hb with rfl | rfl
  · exact Or.inl ⟨a, ha, by rw [cs.wordProd_append]; simp⟩
  · exact Or.inr ⟨a, ha, by rw [cs.wordProd_append, cs.wordProd_singleton]⟩

/-- **Lifting, part one.** If `s` is a right descent of `w` and `u ≤ w`, then `u·s ≤ w`.

No induction: the subword property hands over a subword of a reduced word for `w` ending in `s`,
and *either* branch of the split already exhibits `u·s`. If the subword used the final `s`, drop it;
if it did not, append it. -/
theorem bruhatLe_mul_simple_of_isRightDescent (hDE : DihedralExact cs)
    (hfin : ∀ i j : B, i ≠ j → M i j ≠ 0) {u w : W} (h : BruhatLe cs u w)
    {s : B} (hs : cs.IsRightDescent w s) : BruhatLe cs (u * cs.simple s) w := by
  obtain ⟨ω, hred, hωprod, hredc, hcprod⟩ := exists_reduced_concat cs hs
  obtain ⟨ω', hsub, hu⟩ := subword_property cs hDE hfin h hredc hcprod
  rcases subword_concat_cases cs hsub with ⟨a, ha, hpa⟩ | ⟨a, ha, hpa⟩
  · -- The subword avoided the final `s`: append it.
    refine ⟨ω ++ [s], a ++ [s], hredc, hcprod, ha.append (List.Sublist.refl _), ?_⟩
    rw [cs.wordProd_append, cs.wordProd_singleton, ← hpa, hu]
  · -- The subword used the final `s`: drop it.
    refine ⟨ω ++ [s], a, hredc, hcprod, ha.trans (List.sublist_append_left ω [s]), ?_⟩
    have : π a * cs.simple s * cs.simple s = u * cs.simple s := by rw [← hpa, hu]
    rwa [mul_assoc, cs.simple_mul_simple_self, mul_one] at this

/-- **Lifting, part two — the property proper.** If `s` is a right descent of *both* `u` and `w`,
and `u ≤ w`, then `u·s ≤ w·s`.

The branch where the subword used the final `s` gives it outright. The other branch gives `u ≤ w·s`,
and `u·s ≤ u` because `s` is a descent of `u` — a single reflection step — so transitivity finishes
it. This is the fourth of the four properties `QOU.Machinery.CoxeterBruhat` deferred. -/
theorem lifting (hDE : DihedralExact cs) (hfin : ∀ i j : B, i ≠ j → M i j ≠ 0)
    {u w : W} (h : BruhatLe cs u w) {s : B}
    (hsw : cs.IsRightDescent w s) (hsu : cs.IsRightDescent u s) :
    BruhatLe cs (u * cs.simple s) (w * cs.simple s) := by
  obtain ⟨ω, hred, hωprod, hredc, hcprod⟩ := exists_reduced_concat cs hsw
  obtain ⟨ω', hsub, hu⟩ := subword_property cs hDE hfin h hredc hcprod
  rcases subword_concat_cases cs hsub with ⟨a, ha, hpa⟩ | ⟨a, ha, hpa⟩
  · -- `u ≤ w·s`; then `u·s ≤ u` is one reflection step down.
    have hle : BruhatLe cs u (w * cs.simple s) := ⟨ω, a, hred, hωprod, ha, by rw [← hpa, hu]⟩
    have hstep : ReflStep cs (u * cs.simple s) u :=
      ⟨cs.simple s, cs.isReflection_simple s, by rw [mul_assoc, cs.simple_mul_simple_self, mul_one],
        hsu⟩
    exact bruhatLe_trans cs hDE hfin (bruhatLe_of_reflStep cs hstep) hle
  · -- The subword used the final `s`: dropping it is already a subword for `u·s` in `ω`.
    refine ⟨ω, a, hred, hωprod, ha, ?_⟩
    have : π a * cs.simple s * cs.simple s = u * cs.simple s := by rw [← hpa, hu]
    rwa [mul_assoc, cs.simple_mul_simple_self, mul_one] at this

/-! ## Type `A`: hypothesis-free -/

theorem bruhatLe_of_reflLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : ReflLe cs u w) :
    BruhatLe cs u w :=
  bruhatLe_of_reflLe cs (QOU.Machinery.CoxeterDihedralDescent.dihedralExact_le_three cs
    (An_le_three n)) (fun i j hij => An_ne_zero n i j hij) h

/-- **What this buys a Mathas consumer, spelled out.** Given `u ⊵ v ⊵ w` in the reflection sense on
a type-`A` system, `u` appears as a subword of *every* reduced word for `w`. -/
theorem subword_property_of_reflLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : ReflLe cs u w)
    {ω : List (Fin n)} (hred : cs.IsReduced ω) (hw : cs.wordProd ω = w) :
    ∃ ω' : List (Fin n), ω' <+ ω ∧ cs.wordProd ω' = u :=
  subword_property_An cs (bruhatLe_of_reflLe_An cs h) hred hw

end QOU.IwahoriHecke.BruhatReflection
