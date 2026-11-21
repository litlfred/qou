import QOU.MathlibExt.IwahoriHeckeAlgebra
import Mathlib.Logic.Relation

/-!
# Word products in the Hecke algebra, and what Matsumoto's theorem is actually for

The `T_w` basis of an Iwahori–Hecke algebra is defined by picking a reduced expression
`w = s_{i₁} ⋯ s_{i_k}` and setting `T_w := T_{i₁} ⋯ T_{i_k}`. Whether that is well defined
is the standard hard point, and the corpus has repeatedly deferred it to "Matsumoto's
theorem". This file separates the two halves of that deferral, because only one of them is
hard and the corpus was treating both as unavailable.

**The algebra half is easy and is proved here.** Two words related by a *braid move* —
replacing an alternating subword `i j i ⋯` (`M i j` letters) by `j i j ⋯` (`M j i` letters)
— have the same product in `H(M, q)`, immediately from the defining braid relation
(`heckeWord_eq_of_braidMove`, and its closure `heckeWord_eq_of_braidEquiv`).

**The group half is the real Matsumoto theorem** and is about the *Coxeter group*, not the
algebra: any two reduced expressions for the same `w ∈ W` are related by a chain of braid
moves. **Mathlib** does not have it: `Mathlib/GroupTheory/Coxeter/` has `IsReduced`, the
length function, descents and inversion sequences, but no exchange property and no
Matsumoto.

🛑 **The claim that "nothing in this corpus proves it either" was wrong about the exchange
property, and it was mine** (corrected 2026-09-06).
`QOU.Machinery.CoxeterReflectionCocycle.rightExchange` proves `RightExchangeProp cs` for
every Coxeter system, sorry-free, off `strong_exchange` (Björner–Brenti Thm 1.4.3). What
remains open is **deletion → Matsumoto**; the exchange property is not part of the gap.

✅ **And that remainder is now closed too** (2026-09-06). `QOU.Machinery.CoxeterDeletion`
supplies deletion and `QOU.IwahoriHecke.Matsumoto` supplies Matsumoto — **for every Coxeter
system, with no hypothesis**, since `CoxeterDihedralOrder.dihedralExact_full` settles the order
of `σᵢσⱼ` and `bond_ne_zero_of_pow_eq_one` the infinite-bond case. So the
sentence below reading "not proved anywhere in this corpus or in Mathlib" is stale for this
corpus; it remains true of Mathlib.

`exists_Tw_of_braidEquiv` below is a conditional theorem naming its hypothesis rather than a
class asserting the conclusion.

🛑 **But do not read it as making the dependency exact — corrected 2026-09-06, and the earlier
wording here was mine.** Its hypothesis quantifies over *all* words, and at the only
instantiation anyone wants — `π := cs.wordProd` for a Coxeter system — that hypothesis is
**false**, so the theorem is vacuous there. Braid moves preserve word length (a Coxeter matrix
is symmetric), while `π [i,i] = π []` because `s_i² = 1`. Refuted in
`QOU.IwahoriHecke.TwMatsumoto.not_braidEquiv_hypothesis`; the satisfiable replacement, stated
against **reduced** words, is `TwMatsumoto.exists_Tw_of_matsumoto`.

## Relation to `QOU.IwahoriHecke.Tw`

That file's `wordProduct` is built over `QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot`,
which by its own scope note **imposes the quadratic relation only** and no braid relations.
Nothing of this file's content can hold there: with no braid relation, a braid move changes
the product. The word product belongs over
`QOU.MathlibExt.IwahoriHecke.HeckeAlgebra`, which imposes both families, and that is where
it is built here.

-- Ref: [matsumoto1964] DOI 10.1090/S0002-9904-1964-11211-9 (the group half)
-- Ref: [humphreys1990] §7.1, §7.4 (word products and the `T_w` basis)
-- Ref: [leitner2026] bean qou-k4oq
-/

namespace QOU.IwahoriHecke.BraidWord

open QOU.MathlibExt.IwahoriHecke

variable {R : Type*} [CommRing R] (q : R) {B : Type*} (M : B → B → ℕ)

/-! ## The word product -/

/-- The product `T_{i₁} ⋯ T_{i_k}` of the generators named by a word. -/
noncomputable def heckeWord : List B → HeckeAlgebra R q M
  | [] => 1
  | i :: l => T R q M i * heckeWord l

@[simp] theorem heckeWord_nil : heckeWord q M ([] : List B) = 1 := rfl

@[simp] theorem heckeWord_cons (i : B) (l : List B) :
    heckeWord q M (i :: l) = T R q M i * heckeWord q M l := rfl

@[simp] theorem heckeWord_singleton (i : B) : heckeWord q M [i] = T R q M i := by
  rw [heckeWord_cons, heckeWord_nil, mul_one]

/-- **Concatenation of words is multiplication.** The word product is a monoid map from the
free monoid on the generator index set. -/
theorem heckeWord_append (l₁ l₂ : List B) :
    heckeWord q M (l₁ ++ l₂) = heckeWord q M l₁ * heckeWord q M l₂ := by
  induction l₁ with
  | nil => simp
  | cons i l ih => rw [List.cons_append, heckeWord_cons, ih, heckeWord_cons, mul_assoc]

/-! ## Alternating words and braid moves -/

/-- The alternating word `i j i j ⋯` with `n` letters. Matches the recursion of
`QOU.MathlibExt.IwahoriHecke.altProd`, so that the two agree under `heckeWord`. -/
def altWord : B → B → ℕ → List B
  | _, _, 0 => []
  | i, j, (n + 1) => i :: altWord j i n

@[simp] theorem altWord_zero (i j : B) : altWord i j 0 = [] := rfl

@[simp] theorem altWord_succ (i j : B) (n : ℕ) :
    altWord i j (n + 1) = i :: altWord j i n := rfl

theorem length_altWord : ∀ (n : ℕ) (i j : B), (altWord i j n).length = n := by
  intro n
  induction n with
  | zero => intro i j; rfl
  | succ k ih => intro i j; rw [altWord_succ, List.length_cons, ih]

/-- **The word product of an alternating word is the alternating product.** This is the
bridge between the list-level and algebra-level statements of the braid relation. -/
theorem heckeWord_altWord :
    ∀ (n : ℕ) (i j : B),
      heckeWord q M (altWord i j n) = altProd (T R q M i) (T R q M j) n := by
  intro n
  induction n with
  | zero => intro i j; rfl
  | succ k ih => intro i j; rw [altWord_succ, heckeWord_cons, ih, altProd]

/-- **One braid move**: inside a word, replace the alternating block `i j i ⋯` of length
`M i j` by the alternating block `j i j ⋯` of length `M j i`. -/
inductive BraidMove : List B → List B → Prop
  | move (l₁ l₂ : List B) (i j : B) :
      BraidMove (l₁ ++ altWord i j (M i j) ++ l₂) (l₁ ++ altWord j i (M j i) ++ l₂)

/-- **Braid-equivalence**: the reflexive–transitive closure of `BraidMove`, i.e. any finite
chain of braid moves in either direction is generated by the symmetric closure. Since the
`BraidMove` constructor is symmetric in `(i, j)` — applying it with the pair swapped
reverses the move — the reflexive–transitive closure is already an equivalence. -/
abbrev BraidEquiv : List B → List B → Prop := Relation.ReflTransGen (BraidMove M)

/-- Braid moves are reversible: swapping the two indices runs the move backwards. -/
theorem braidMove_symm {u v : List B} (h : BraidMove M u v) : BraidMove M v u := by
  cases h with
  | move l₁ l₂ i j => exact BraidMove.move l₁ l₂ j i

/-- **The algebra half of Matsumoto.** A braid move does not change the word product,
directly from the defining braid relation of the Hecke algebra. -/
theorem heckeWord_eq_of_braidMove {u v : List B} (h : BraidMove M u v) :
    heckeWord q M u = heckeWord q M v := by
  cases h with
  | move l₁ l₂ i j =>
    rw [heckeWord_append, heckeWord_append, heckeWord_append, heckeWord_append,
      heckeWord_altWord, heckeWord_altWord, T_braid (R := R) (q := q) (M := M) i j]

/-- Braid-equivalent words have the same product. -/
theorem heckeWord_eq_of_braidEquiv {u v : List B} (h : BraidEquiv M u v) :
    heckeWord q M u = heckeWord q M v := by
  induction h with
  | refl => rfl
  | tail _ hstep ih => rw [ih, heckeWord_eq_of_braidMove q M hstep]

/-! ## What the missing group-theoretic half buys

The statement below is the whole content of the deferral. `π` is any way of reading a word
as a group element — for a Coxeter system, `CoxeterSystem.wordProd`. The hypothesis `hmat`
is **Matsumoto's theorem**, which is a fact about `W` and is not proved anywhere in this
corpus or in Mathlib. Everything else is discharged.

Note the hypothesis is stated for *all* pairs of words with the same image, which is
stronger than Matsumoto (that speaks only of *reduced* expressions).

🛑 **That extra strength is not a feature; it is fatal, and the sentence that used to stand
here calling it "what a total `Tw : W → H` needs" was wrong.** On a Coxeter group the
all-words hypothesis is refuted outright — see
`QOU.IwahoriHecke.TwMatsumoto.not_braidEquiv_hypothesis`. The statement one can actually
discharge is `TwMatsumoto.exists_Tw_of_matsumoto`, whose hypothesis is Matsumoto verbatim and
whose `Tw` agrees with the word product on every **reduced** word. This theorem remains true
as a statement about an abstract `π`; it is simply not applicable to the case it was written
for. -/

/-- **The `T_w` map exists as soon as the group half does.** If words with the same image
in `W` are braid-equivalent, the word product descends to a well-defined function on `W`
agreeing with it on every word.

This is a conditional theorem naming its hypothesis, which is the honest form of the
deferral — as opposed to a class that asserts the conclusion, or an instance that supplies
a placeholder. -/
theorem exists_Tw_of_braidEquiv {W : Type*} (π : List B → W) (hsurj : Function.Surjective π)
    (hmat : ∀ u v : List B, π u = π v → BraidEquiv M u v) :
    ∃ Tw : W → HeckeAlgebra R q M, ∀ l : List B, Tw (π l) = heckeWord q M l := by
  classical
  obtain ⟨g, hg⟩ := hsurj.hasRightInverse
  refine ⟨fun w => heckeWord q M (g w), fun l => ?_⟩
  exact heckeWord_eq_of_braidEquiv q M (hmat _ _ (hg (π l)))

/-- The descended map sends the empty word — hence the identity of `W`, whenever `π`
sends it there — to `1`. -/
theorem exists_Tw_one {W : Type*} [One W] (π : List B → W) (hone : π [] = 1)
    (Tw : W → HeckeAlgebra R q M) (hTw : ∀ l : List B, Tw (π l) = heckeWord q M l) :
    Tw 1 = 1 := by
  rw [← hone, hTw, heckeWord_nil]

end QOU.IwahoriHecke.BraidWord
