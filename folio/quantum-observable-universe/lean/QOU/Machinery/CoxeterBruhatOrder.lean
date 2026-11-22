import QOU.Machinery.CoxeterBruhat
import QOU.Machinery.CoxeterDeletion

/-!
# Bruhat order: antisymmetry, and a reduced witness

`QOU.Machinery.CoxeterBruhat` defines `u ≤ w` by the subword criterion and lists four things it
deliberately does **not** prove — transitivity, antisymmetry, the subword property and the
lifting property — noting that "each needs the exchange condition" and that the repo has it.

`QOU.Machinery.CoxeterDeletion` now supplies the consequence of exchange that these actually
consume. This file spends it, and closes **one** of the four.

## What closes

* **`eq_of_bruhatLe_of_length_le`** — `u ≤ w` together with `ℓ(w) ≤ ℓ(u)` forces `u = w`. The
  whole argument is a length squeeze: the witnessing subword `ω'` satisfies
  `ℓ(u) ≤ |ω'| ≤ |ω| = ℓ(w) ≤ ℓ(u)`, so `|ω'| = |ω|`, and a sublist of full length is the list
  (`List.Sublist.eq_of_length`).
* **`bruhatLe_antisymm`** — hence antisymmetry, one of the four.
* **`bruhatLe_one_iff`** — `w ≤ 1 ↔ w = 1`.
* **`bruhatLe_reduced_witness`** — the witnessing subword may always be taken **reduced**. This
  is where `exists_reduced_sublist'` is spent: a subword of a reduced word need not itself be
  reduced, and several arguments want one that is.

## 🛑 What does not close, and why — transitivity in particular

Transitivity is **not** a corollary of the above, and the reason is worth stating because it is
the same obstruction throughout. From `v ≤ w` one gets a reduced word `ω_w` for `w` with a
subword for `v`; `bruhatLe_reduced_witness` even makes that subword reduced. From `u ≤ v` one
gets a reduced word for `v` — but **some other one**, and nothing here says two reduced words for
the same element are interchangeable. That statement is the *subword property*, and it is
equivalent in strength to Matsumoto.

So the four split cleanly: antisymmetry needed only length bookkeeping and is done; transitivity,
the subword property and lifting all wait on Matsumoto.

✅ **Matsumoto is no longer open** (2026-09-06): `QOU.IwahoriHecke.Matsumoto.matsumoto` proves it,
and since 2026-09-07 with no hypothesis at all — `CoxeterDihedralOrder` discharged the rank-two
order data it used to carry.

✅ **And the subword property and transitivity followed the same day**, in
`QOU.IwahoriHecke.BruhatSubword` (`subword_property`, `bruhatLe_trans`, both hypothesis-free).
They live there rather than here because they need `BraidMove`, which is defined on
the Hecke side; this file cannot import them without a cycle. **Cite that file for them, not this
one** — the paragraph above stands as a description of what *this* file proves.

✅ **And lifting followed too**, in `QOU.IwahoriHecke.BruhatReflection`
(`bruhatLe_mul_simple_of_isRightDescent`, `lifting`). **All four of `CoxeterBruhat`'s deferred
properties are now proved** — antisymmetry here, subword + transitivity in `BruhatSubword`, lifting
in `BruhatReflection`. Only the last is in this file's own namespace; cite the other files for the
rest.

🛑 **Still open:** the equivalence between this subword `BruhatLe` and the *reflection-generated*
Bruhat order. `BruhatReflection.bruhatLe_of_reflLe` proves one direction; the converse does not
follow from lifting, and that file records the obstacle that actually remains.

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, §2.2
-- Ref: [leitner2026] beans qou-phir, qou-06h7
-/

namespace QOU.Machinery.CoxeterBruhatOrder

open CoxeterSystem List
open QOU.Machinery.CoxeterBruhat QOU.Machinery.CoxeterDeletion

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

/-! ## The witness can be taken reduced -/

/-- **A `BruhatLe` witness may be taken reduced.** A subword of a reduced word need not itself be
reduced; `exists_reduced_sublist'` replaces it by a reduced sublist with the same product, which
is still a sublist of the original by transitivity of `List.Sublist`. -/
theorem bruhatLe_reduced_witness {u w : W} (h : BruhatLe cs u w) :
    ∃ ω ω' : List B, cs.IsReduced ω ∧ cs.wordProd ω = w ∧ ω' <+ ω ∧
      cs.IsReduced ω' ∧ cs.wordProd ω' = u := by
  obtain ⟨ω, ω', hred, hw, hsub, hu⟩ := h
  obtain ⟨ω'', hsub'', hred'', hprod''⟩ := exists_reduced_sublist' cs ω'
  exact ⟨ω, ω'', hred, hw, hsub''.trans hsub, hred'', by rw [hprod'', hu]⟩

/-! ## The length squeeze, and antisymmetry -/

/-- **`u ≤ w` with `ℓ(w) ≤ ℓ(u)` forces `u = w`.**

A length squeeze and nothing else: `ℓ(u) ≤ |ω'| ≤ |ω| = ℓ(w) ≤ ℓ(u)` pins `|ω'| = |ω|`, and a
sublist of the same length as its host **is** its host. -/
theorem eq_of_bruhatLe_of_length_le {u w : W} (h : BruhatLe cs u w)
    (hlen : cs.length w ≤ cs.length u) : u = w := by
  obtain ⟨ω, ω', hred, hw, hsub, hu⟩ := h
  have h3 : cs.length w = ω.length := by rw [← hw]; exact hred
  have h4 : cs.length u ≤ ω'.length := by rw [← hu]; exact cs.length_wordProd_le ω'
  have h5 : ω'.length ≤ ω.length := hsub.length_le
  have h6 : ω'.length = ω.length := by omega
  have h7 : ω' = ω := hsub.eq_of_length h6
  rw [← hu, h7, hw]

/-- **Antisymmetry** — the first of `CoxeterBruhat`'s four deferred properties. -/
theorem bruhatLe_antisymm {u w : W} (h₁ : BruhatLe cs u w) (h₂ : BruhatLe cs w u) : u = w :=
  eq_of_bruhatLe_of_length_le cs h₁ (length_le_of_bruhatLe cs h₂)

/-- **`w ≤ 1` iff `w = 1`.** The identity is the bottom of the order and nothing sits below it. -/
theorem bruhatLe_one_iff {w : W} : BruhatLe cs w 1 ↔ w = 1 := by
  constructor
  · intro h
    exact bruhatLe_antisymm cs h (one_bruhatLe cs w)
  · rintro rfl
    exact bruhatLe_refl cs 1

/-- Contrapositive form, convenient downstream: a strictly longer element is never below. -/
theorem not_bruhatLe_of_length_lt {u w : W} (hlen : cs.length w < cs.length u) :
    ¬ BruhatLe cs u w := by
  intro h
  have := length_le_of_bruhatLe cs h
  omega

end QOU.Machinery.CoxeterBruhatOrder
