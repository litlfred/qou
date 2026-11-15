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

## The converse bridge — open when this file was written, CLOSED since

`reflStep_of_eraseIdx` shows the atom: deleting **one** letter from a reduced word is exactly a
downward reflection step, with the reflection read off Mathlib's right inversion sequence. The
temptation is to iterate it and get `BruhatLe → ReflLe` for free.

**That does not work.** A subword deletes several letters at once, and the intermediate words are
**not reduced**, so their products need not have strictly decreasing lengths — the chain of
reflection steps a `ReflLe` requires is not the chain of deletions.

**Two diagnoses of this obstacle have now been written here and BOTH were wrong. They are recorded
rather than deleted, because each one is a plausible thing to try next and each one is a dead end.**

*First wrong diagnosis:* "the repair is the lifting property". Lifting is now proved, in this file,
and the converse still does not follow.

*Second wrong diagnosis:* "it needs a subword of an **arbitrary** word for `w` to give `u ≤ w`".
That statement is not merely unproved — **it is FALSE**, and `not_forall_bruhatLe_of_sublist` below
proves it false. Take `ω = [i, i]`, whose product is `1`, and the subword `[i]`, whose product is
`sᵢ`: the claim would give `sᵢ ≤ 1`, and `bruhatLe_one_iff` forces `sᵢ = 1`, contradicting
`ℓ(sᵢ) = 1`. Any route through it is dead.

**Where the difficulty actually sits**, stated as precisely as it is currently understood. Induct on
`ℓ(w)` with `ω = ω₁ ++ [s]` reduced for `w`, and split the reduced witness `ω'` for `u`:

* `ω' <+ ω₁` — then `u ≤ w·s`, the induction hypothesis gives `u ≤ᵣ w·s`, and `w·s →ᵣ w` is one
  reflection step. **This branch closes.**
* `ω' = a ++ [s]` — then `u·s ≤ w·s` and the induction hypothesis gives `u·s ≤ᵣ w·s`. What is needed
  is `u ≤ᵣ w`, i.e. an **upward lifting property for `≤ᵣ`**: if `x ≤ᵣ y` and `s` is a right *ascent*
  of both `x` and `y`, then `x·s ≤ᵣ y·s`. **This branch is open.**

The single-step case of that upward lifting **does** go through — if `y = x·t` with `ℓ(x) < ℓ(y)` and
`s` is an ascent of both, then `y·s = (x·s)·(s t s)`, `s t s` is a reflection, and
`ℓ(x·s) = ℓ(x) + 1 < ℓ(y) + 1 = ℓ(y·s)`. What fails is the **chain**: nothing forces `s` to remain
an ascent at the intermediate elements of a `ReflTransGen` chain, and `ReflStep` is not defined for
a descent.

✅ **That third statement of the obstacle was the right one, and it is now proved** —
`QOU.IwahoriHecke.BruhatConverse.reflLe_mul_simple_of_ascent`, and with it
`reflLe_of_bruhatLe` and `bruhatLe_iff_reflLe`. **The two orders are the same relation.**

What unblocked the chain: the intermediate elements of a `ReflTransGen` from `x` to `y` are all
**shorter than `y`**, so the outer induction hypothesis of the converse applies to them. Carried into
the lifting lemma, it closes the descent case — via `bruhatLe_of_reflLe` and this file's own
`bruhatLe_mul_simple_of_isRightDescent`. So the lifting property **is** used, just not where the
first wrong diagnosis put it: it resolves the descent case *inside* the chain, not the branch.

So: `ReflLe → BruhatLe` ✅ (here), `BruhatLe → ReflLe` ✅ (`BruhatConverse`).

The two wrong diagnoses above are kept anyway. `not_forall_bruhatLe_of_sublist` remains a true
refutation and is worth having on the record; and the history of what did *not* work is the part a
reader cannot reconstruct from the finished proof.

## The LEFT-handed variant, and why it is here

`ReflStep` multiplies on the **right** (`w = v · t`).  The tableau side of Mathas' Prop. 3.7
produces the **left** one: swapping two entries of a tableau is the group action, and
`TableauPerm.dOf_smul` gives `dOf (swap a b • t) = swap a b * dOf t` — transposition on the
left.  A consumer that assumes the two are interchangeable fails at the point where
`bruhatLe_of_reflLe_An` is applied: late, and looking like a hard obstruction.

It is a bridge, not a wall.  `LeftReflStep` / `LeftReflLe` below are the mirrored definitions,
and `bruhatLe_of_leftReflLe_An` is the mirrored conclusion, obtained by **transport through
`⁻¹`** rather than by re-proving anything: a reflection is an involution
(`IsReflection.inv`), `ℓ w⁻¹ = ℓ w`, and `CoxeterBruhat.bruhatLe_inv_iff` carries the
conclusion back.  Nothing in the `≤ᵣ → ≤` proof is duplicated.

✅ **The open direction is no longer open.** This paragraph read *"`BruhatLe → LeftReflLe`
transports to `BruhatLe → ReflLe`, which is `qou-3k66` — still open"*, and that was true when it was
written. `QOU.IwahoriHecke.BruhatConverse` closes `qou-3k66`, so the transport that paragraph
describes now goes through: `BruhatConverse.leftReflLe_of_bruhatLe_An` and
`bruhatLe_iff_leftReflLe_An` are the left-handed mirrors, obtained exactly as promised here — by
`⁻¹`, with nothing re-proved. **The observation that the transport is faithful in both directions is
what makes it free.**

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, §2.1–2.2 (both definitions, Thm 2.2.2)
-- Ref: [mathas1999] Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group, Prop 3.7
-- Ref: [leitner2026] beans qou-06h7, qou-phir
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

Used to carry `DihedralExact` / `M i j ≠ 0` because it chains with `bruhatLe_trans`; both are now
proved in `CoxeterDihedralOrder`, so it is unconditional. The one-step
lemma above needs neither. -/
theorem bruhatLe_of_reflLe
    {u w : W} (h : ReflLe cs u w) : BruhatLe cs u w := by
  induction h with
  | refl => exact bruhatLe_refl cs u
  | tail _ hstep ih => exact bruhatLe_trans cs ih (bruhatLe_of_reflStep cs hstep)

/-! ## The converse atom — and why iterating it is not a proof -/

/-- **Deleting one letter of a reduced word is a downward reflection step.**

The reflection is the `j`-th entry of Mathlib's right inversion sequence, and
`wordProd_mul_getD_rightInvSeq` is the identity that names it. This is the atom the converse
direction would iterate.

🛑 **Iterating it does not give `BruhatLe → ReflLe`.** A subword deletes several letters, the
intermediate words are not reduced, and `ReflStep` demands a *strict length increase* at every step
— which the intermediate products need not provide. The converse is proved in
`QOU.IwahoriHecke.BruhatConverse`, and **not** by iterating this: it peels a right descent instead
and lifts. This lemma is not the route; it is kept because it is the honest atom. -/
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
theorem bruhatLe_mul_simple_of_isRightDescent {u w : W} (h : BruhatLe cs u w)
    {s : B} (hs : cs.IsRightDescent w s) : BruhatLe cs (u * cs.simple s) w := by
  obtain ⟨ω, hred, hωprod, hredc, hcprod⟩ := exists_reduced_concat cs hs
  obtain ⟨ω', hsub, hu⟩ := subword_property cs h hredc hcprod
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
theorem lifting
    {u w : W} (h : BruhatLe cs u w) {s : B}
    (hsw : cs.IsRightDescent w s) (hsu : cs.IsRightDescent u s) :
    BruhatLe cs (u * cs.simple s) (w * cs.simple s) := by
  obtain ⟨ω, hred, hωprod, hredc, hcprod⟩ := exists_reduced_concat cs hsw
  obtain ⟨ω', hsub, hu⟩ := subword_property cs h hredc hcprod
  rcases subword_concat_cases cs hsub with ⟨a, ha, hpa⟩ | ⟨a, ha, hpa⟩
  · -- `u ≤ w·s`; then `u·s ≤ u` is one reflection step down.
    have hle : BruhatLe cs u (w * cs.simple s) := ⟨ω, a, hred, hωprod, ha, by rw [← hpa, hu]⟩
    have hstep : ReflStep cs (u * cs.simple s) u :=
      ⟨cs.simple s, cs.isReflection_simple s, by rw [mul_assoc, cs.simple_mul_simple_self, mul_one],
        hsu⟩
    exact bruhatLe_trans cs (bruhatLe_of_reflStep cs hstep) hle
  · -- The subword used the final `s`: dropping it is already a subword for `u·s` in `ω`.
    refine ⟨ω, a, hred, hωprod, ha, ?_⟩
    have : π a * cs.simple s * cs.simple s = u * cs.simple s := by rw [← hpa, hu]
    rwa [mul_assoc, cs.simple_mul_simple_self, mul_one] at this

/-! ## 🛑 A refuted repair — the converse does not go through this (and did not) -/

/-- **The non-reduced-subword statement is FALSE.**

An earlier note in this file proposed closing `BruhatLe → ReflLe` via *"a subword of an arbitrary
(not necessarily reduced) word for `w` still gives `u ≤ w`"*. It does not hold, and this is the
one-line reason: `π [i, i] = 1` while `π [i] = sᵢ`, and `[i]` is a subword of `[i, i]`.

Recorded as a theorem rather than as prose because it is a plausible thing to reach for and the
prose form of it stood in this file for one commit. -/
theorem not_forall_bruhatLe_of_sublist (i : B) :
    ¬ (∀ ω' ω : List B, ω' <+ ω → BruhatLe cs (π ω') (π ω)) := by
  intro hall
  have hsub : ([i] : List B) <+ [i, i] := (List.Sublist.refl [i]).cons i
  have hii : π [i, i] = 1 := by
    simp [cs.wordProd_cons, cs.simple_mul_simple_self]
  have hi : π [i] = cs.simple i := by simp
  have hle := hall [i] [i, i] hsub
  rw [hii, hi] at hle
  have heq : cs.simple i = 1 := (QOU.Machinery.CoxeterBruhatOrder.bruhatLe_one_iff cs).mp hle
  have hlen : ℓ (cs.simple i) = 1 := cs.length_simple i
  rw [heq, cs.length_one] at hlen
  exact absurd hlen (by norm_num)

/-! ## The half of the open branch that DOES work -/

/-- **Upward lifting, one step.** If `y = x·t` is a single upward reflection step and `s` is a right
*ascent* of both `x` and `y`, then `x·s → y·s` is a single upward reflection step too — the
reflection being the conjugate `s t s`.

This is the piece the converse bridge needs iterated, and it is stated here so that the header's
claim about it is a theorem rather than an assertion. **What does not follow is the chain version**:
a `ReflLe` is a `ReflTransGen`, nothing forces `s` to remain an ascent at the intermediate elements,
and `ReflStep` is not defined for a descent. That gap is the open problem. -/
theorem reflStep_mul_simple {x y : W} (h : ReflStep cs x y) {s : B}
    (hx : ℓ x < ℓ (x * cs.simple s)) (hy : ℓ y < ℓ (y * cs.simple s)) :
    ReflStep cs (x * cs.simple s) (y * cs.simple s) := by
  obtain ⟨t, ht, hy', hlt⟩ := h
  refine ⟨cs.simple s * t * cs.simple s, ?_, ?_, ?_⟩
  · have := ht.conj (cs.simple s)
    rwa [cs.inv_simple] at this
  · rw [hy']
    calc x * t * cs.simple s
        = x * (cs.simple s * cs.simple s) * t * cs.simple s := by
          rw [cs.simple_mul_simple_self, mul_one]
      _ = x * cs.simple s * (cs.simple s * t * cs.simple s) := by simp [mul_assoc]
  · have hxs : ℓ (x * cs.simple s) = ℓ x + 1 := by
      rcases cs.length_mul_simple x s with h1 | h1 <;> omega
    have hys : ℓ (y * cs.simple s) = ℓ y + 1 := by
      rcases cs.length_mul_simple y s with h1 | h1 <;> omega
    omega

/-! ## Type `A`: hypothesis-free -/

theorem bruhatLe_of_reflLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : ReflLe cs u w) :
    BruhatLe cs u w :=
  bruhatLe_of_reflLe cs h

/-- **What this buys a Mathas consumer, spelled out.** Given `u ⊵ v ⊵ w` in the reflection sense on
a type-`A` system, `u` appears as a subword of *every* reduced word for `w`. -/
theorem subword_property_of_reflLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : ReflLe cs u w)
    {ω : List (Fin n)} (hred : cs.IsReduced ω) (hw : cs.wordProd ω = w) :
    ∃ ω' : List (Fin n), ω' <+ ω ∧ cs.wordProd ω' = u :=
  subword_property_An cs (bruhatLe_of_reflLe_An cs h) hred hw

/-! ## The left-handed reflection order

The mirror of everything above, for consumers whose step multiplies on the left.  Every proof
here is a transport through `⁻¹`; no argument from the right-handed development is repeated. -/

/-- One upward step **on the left**: `w = t · v` for a reflection `t`, with the length going up.

The mirror of `ReflStep`.  It exists because the tableau side of Mathas' Prop. 3.7 produces
left multiplications (`TableauPerm.dOf_smul`), while `ReflStep` is right-handed. -/
def LeftReflStep (v w : W) : Prop := ∃ t : W, cs.IsReflection t ∧ w = t * v ∧ ℓ v < ℓ w

/-- **The left-handed reflection-generated order.** -/
abbrev LeftReflLe : W → W → Prop := Relation.ReflTransGen (LeftReflStep cs)

/-- A left step inverts to a right step: `t⁻¹ = t` for a reflection, and `ℓ` is
inversion-invariant. -/
theorem reflStep_inv_of_leftReflStep {v w : W} (h : LeftReflStep cs v w) :
    ReflStep cs v⁻¹ w⁻¹ := by
  obtain ⟨t, ht, hw, hl⟩ := h
  refine ⟨t, ht, ?_, ?_⟩
  · rw [hw, mul_inv_rev, ht.inv]
  · rwa [cs.length_inv, cs.length_inv]

/-- The chain version of `reflStep_inv_of_leftReflStep`.  Note the chain does **not** reverse:
`⁻¹` is applied pointwise, and `ReflTransGen` is closed under that. -/
theorem reflLe_inv_of_leftReflLe {v w : W} (h : LeftReflLe cs v w) :
    ReflLe cs v⁻¹ w⁻¹ := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih => exact ih.tail (reflStep_inv_of_leftReflStep cs hstep)

/-- **`LeftReflLe → BruhatLe` in type `A`, hypothesis-free** — the left-handed mirror of
`bruhatLe_of_reflLe_An`, and the lemma a Mathas Prop. 3.7 consumer actually needs.

Proof: transport to the right-handed statement through `⁻¹`, apply
`bruhatLe_of_reflLe_An`, transport the conclusion back with
`CoxeterBruhat.bruhatLe_inv_iff`. -/
theorem bruhatLe_of_leftReflLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : LeftReflLe cs u w) :
    BruhatLe cs u w :=
  (bruhatLe_inv_iff cs).mp (bruhatLe_of_reflLe_An cs (reflLe_inv_of_leftReflLe cs h))

/-- The subword corollary in left-handed form. -/
theorem subword_property_of_leftReflLe_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : LeftReflLe cs u w)
    {ω : List (Fin n)} (hred : cs.IsReduced ω) (hw : cs.wordProd ω = w) :
    ∃ ω' : List (Fin n), ω' <+ ω ∧ cs.wordProd ω' = u :=
  subword_property_An cs (bruhatLe_of_leftReflLe_An cs h) hred hw


end QOU.IwahoriHecke.BruhatReflection
