import Mathlib.GroupTheory.Coxeter.Length

/-!
# The Bruhat (subword) order on a Coxeter system

Mathlib has **no** Bruhat order. That is measured rather than grepped — a source grep is
worthless in this checkout, where `.lake/packages/mathlib` carries 6990 oleans and zero
`.lean` files — by enumerating the environment
([`scripts/lean-probes/`](../../../../../scripts/lean-probes/README.md)): of **439**
reachable `Coxeter` constants, **0** contain `ruhat` and **0** contain `ubword`.

It is wanted here for bean `qou-phir`. `TwInverseLength.TwInv_mem_spanLe` proves that
`T_w⁻¹` cannot escape upward in *length*; the sharper statement measured by
[`tw_inverse_support_probe.py`](../../../../../computations/hecke/tw_inverse_support_probe.py)
is that its support is the **interval `[e, w⁻¹]`** — and that cannot even be stated
without this order.

## The definition, and the one thing to know about it

`u ≤ w` iff **some** reduced word for `w` has a subword whose product is `u`.

The classical *subword property* says the choice of reduced word does not matter — for a
reduced `ω` with `wordProd ω = w`, every `u ≤ w` appears as a subword of **that** `ω`.
**It is not proved here**, and until it is, `BruhatLe` should be read as the existential
it literally is. The ingredient it needs is the exchange condition, which this repo does
have (`QOU.Machinery.CoxeterParabolic.rightExchange`, sorry-free for every Coxeter
system) — so this is unfinished work, not a blocked route.

## What is proved, and what is deliberately not

Proved: reflexivity, `1 ≤ w`, length monotonicity, and the two ascending-extension steps
that an induction along a reduced word actually consumes.

**Not proved, and not to be assumed by a consumer**: transitivity, antisymmetry, the
subword property above, and the lifting property. Each needs the exchange condition. A
downstream file that needs one of them should prove it from `rightExchange` rather than
quietly assume `BruhatLe` is a partial order — it is not yet known here to be one.
## 🟩 This file is on the Murphy-basis critical path — found 2026-09-06, after it was built

It was written as *"the subword order Mathlib has none of"*, with transitivity, antisymmetry,
the subword property and lifting **deliberately left unproved**.  All four are consumed by
Mathas' route to the Murphy basis, which was not known at the time:

* **Proposition 3.7 (Dipper–James)** — for row standard λ-tableaux, `s ⊵ t` **iff**
  `d(s) ⊵ d(t)`, the source noting that Bruhat–Chevalley *"agrees with the dominance ordering
  on row standard λ-tableaux"*.  Since `dOf` is a bijection
  (`TableauPerm.equivPerm`), `DominanceWellFounded.domGtOn` and the Bruhat order are **the
  same order transported**, so `MurphyInductionMeasure.murphyLex` is
  lex-on-shapes × **Bruhat**-on-permutations.
* **Corollary 3.8**, which 3.14's induction closes on, opens by invoking Mathas' Theorem
  1.1.11: `T_{d(v)} T_w = Σ r_x T_x` with `r_x ≠ 0` only for `x` whose reduced expression is a
  **subexpression** of `d(v)w`.  That is the **subword property**, i.e. exactly the lemma this
  file declines to prove.  `QOU.BraidKnot.TwInverseBruhat.TwInv_mem_spanBruhatLe` is the
  corpus's nearest existing instance of that shape.

🛑 **Two inequivalent definitions of the Bruhat order are now in play in this corpus and only
one is named.**  `BruhatLe` here is the **subword** definition.  Mathas' is
**reflection-generated with length increase** — `w = v t₁⋯t_k` with `ℓ(v t₁⋯t_j) = ℓ(v) + j`.
Their equivalence is a theorem, not an unfolding.  Do not let a second one accrete under this
name; that is the `dOf` collision (#6899) one level up.

Context: [`docs/audits/2026-09-06-tabloid-dominance-vs-the-column-word-measure.md`](../../../../../docs/audits/2026-09-06-tabloid-dominance-vs-the-column-word-measure.md).
-/

namespace QOU.Machinery.CoxeterBruhat

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

/-- **The Bruhat order**, by the subword criterion: `u ≤ w` when some reduced word for
`w` admits a subword multiplying to `u`. -/
def BruhatLe (u w : W) : Prop :=
  ∃ ω ω' : List B,
    cs.IsReduced ω ∧ cs.wordProd ω = w ∧ ω'.Sublist ω ∧ cs.wordProd ω' = u

theorem bruhatLe_refl (w : W) : BruhatLe cs w w := by
  obtain ⟨ω, hred, hw⟩ := cs.exists_reduced_word' w
  exact ⟨ω, ω, hred, hw.symm, List.Sublist.refl ω, hw.symm⟩

/-- **`1 ≤ w`** — the empty subword. -/
theorem one_bruhatLe (w : W) : BruhatLe cs 1 w := by
  obtain ⟨ω, hred, hw⟩ := cs.exists_reduced_word' w
  exact ⟨ω, [], hred, hw.symm, List.nil_sublist ω, cs.wordProd_nil⟩

/-- **Length is monotone** for the subword order: a subword is no longer than its word,
and a reduced word has the length of its product. -/
theorem length_le_of_bruhatLe {u w : W} (h : BruhatLe cs u w) :
    cs.length u ≤ cs.length w := by
  obtain ⟨ω, ω', hred, hw, hsub, hu⟩ := h
  have h1 : cs.length u ≤ ω'.length := by
    rw [← hu]; exact cs.length_wordProd_le ω'
  have h2 : ω'.length ≤ ω.length := hsub.length_le
  have h3 : cs.length w = ω.length := by rw [← hw]; exact hred
  omega

/-- Appending an ascending letter to a reduced word keeps it reduced. -/
theorem isReduced_append_singleton {ω : List B} {w : W} (i : B)
    (hred : cs.IsReduced ω) (hw : cs.wordProd ω = w)
    (hlen : cs.length (w * cs.simple i) = cs.length w + 1) :
    cs.IsReduced (ω ++ [i]) := by
  have hlenω : cs.length w = ω.length := by rw [← hw]; exact hred
  show cs.length (cs.wordProd (ω ++ [i])) = (ω ++ [i]).length
  rw [cs.wordProd_append, cs.wordProd_singleton, hw, hlen, hlenω]
  simp

/-- **`u ≤ w` ⇒ `u ≤ w·sᵢ`** when the length ascends: the same subword sits inside the
longer word. -/
theorem bruhatLe_mul_simple {u w : W} (i : B) (h : BruhatLe cs u w)
    (hlen : cs.length (w * cs.simple i) = cs.length w + 1) :
    BruhatLe cs u (w * cs.simple i) := by
  obtain ⟨ω, ω', hred, hw, hsub, hu⟩ := h
  refine ⟨ω ++ [i], ω', isReduced_append_singleton cs i hred hw hlen, ?_,
    hsub.trans (List.sublist_append_left ω [i]), hu⟩
  rw [cs.wordProd_append, cs.wordProd_singleton, hw]

/-- **`u ≤ w` ⇒ `u·sᵢ ≤ w·sᵢ`** when the length ascends: extend both words by the same
letter. -/
theorem bruhatLe_mul_simple_mul_simple {u w : W} (i : B) (h : BruhatLe cs u w)
    (hlen : cs.length (w * cs.simple i) = cs.length w + 1) :
    BruhatLe cs (u * cs.simple i) (w * cs.simple i) := by
  obtain ⟨ω, ω', hred, hw, hsub, hu⟩ := h
  refine ⟨ω ++ [i], ω' ++ [i], isReduced_append_singleton cs i hred hw hlen, ?_,
    hsub.append (List.Sublist.refl [i]), ?_⟩
  · rw [cs.wordProd_append, cs.wordProd_singleton, hw]
  · rw [cs.wordProd_append, cs.wordProd_singleton, hu]

/-- **The Bruhat order is inversion-invariant**: `u ≤ w ↔ u⁻¹ ≤ w⁻¹`.

This is the **handedness bridge**, and it is the reason this lemma is here rather than
in a consumer.  Three separate orders on this arc multiply on opposite sides:

* `Tw_mul_Tw : T_v · T_w = T_{w·v}` — the Hecke product is *anti*-multiplicative in the
  index, forced by `orbitMap`, not a typo;
* `TableauPerm.dOf_smul : dOf (w • t) = w * dOf t` — the tableau action puts the
  permutation on the **left**;
* `BruhatReflection.ReflStep v w := ∃ τ, IsReflection τ ∧ w = v * τ ∧ ℓ v < ℓ w` — the
  reflection order steps on the **right**.

A consumer that needs a left-handed statement of a right-handed lemma (or the reverse)
transports through this lemma rather than restating the lemma with the sides swapped.
The proof is the reversed word: `wordProd ω.reverse = (wordProd ω)⁻¹`, reversal preserves
reducedness, and `List.Sublist.reverse` carries the subword across. -/
theorem bruhatLe_inv {u w : W} (h : BruhatLe cs u w) : BruhatLe cs u⁻¹ w⁻¹ := by
  obtain ⟨ω, ω', hred, hw, hsub, hu⟩ := h
  refine ⟨ω.reverse, ω'.reverse, hred.reverse, ?_, hsub.reverse, ?_⟩
  · rw [cs.wordProd_reverse, hw]
  · rw [cs.wordProd_reverse, hu]

/-- The `↔` form of `bruhatLe_inv`, by applying it twice. -/
theorem bruhatLe_inv_iff {u w : W} : BruhatLe cs u⁻¹ w⁻¹ ↔ BruhatLe cs u w :=
  ⟨fun h => by simpa using bruhatLe_inv cs h, bruhatLe_inv cs⟩

/-- **`u ≤ w` ⇒ `sᵢ·u ≤ sᵢ·w`** when the length ascends on the **left** — the mirror of
`bruhatLe_mul_simple_mul_simple`, obtained by transporting through `bruhatLe_inv`. -/
theorem bruhatLe_simple_mul_simple_mul {u w : W} (i : B) (h : BruhatLe cs u w)
    (hlen : cs.length (cs.simple i * w) = cs.length w + 1) :
    BruhatLe cs (cs.simple i * u) (cs.simple i * w) := by
  have hlen' : cs.length (w⁻¹ * cs.simple i) = cs.length w⁻¹ + 1 := by
    have h1 : cs.length (w⁻¹ * cs.simple i) = cs.length (cs.simple i * w) := by
      rw [← cs.length_inv (w⁻¹ * cs.simple i), mul_inv_rev, cs.inv_simple, inv_inv]
    rw [h1, hlen, cs.length_inv]
  have h2 := bruhatLe_inv cs (bruhatLe_mul_simple_mul_simple cs i (bruhatLe_inv cs h) hlen')
  simpa [mul_inv_rev, cs.inv_simple] using h2


end QOU.Machinery.CoxeterBruhat
