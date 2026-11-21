import QOU.IwahoriHecke.BraidWordInvariance
import Mathlib.GroupTheory.Coxeter.Length

/-!
# 🛑 `exists_Tw_of_braidEquiv` cannot be applied to a Coxeter group — and the statement that can

`QOU.IwahoriHecke.BraidWordInvariance.exists_Tw_of_braidEquiv` presents itself as the honest
form of the `T_w` deferral: a conditional theorem naming Matsumoto as a hypothesis. Its own
docstring notes the hypothesis is *"stronger than Matsumoto (that speaks only of reduced
expressions)"*, and offers that strength as a feature — *"what a total `Tw : W → H` needs"*.

**It is not merely stronger. For the only instantiation anyone would want, it is false**, so the
theorem is vacuous there and reduces nothing.

## The refutation, in one line of arithmetic

A braid move replaces an alternating block of length `M i j` by one of length `M j i`. For a
Coxeter matrix those are equal, so **braid-equivalence preserves word length**
(`braidEquiv_length_eq`). But in a Coxeter group `s_i² = 1`, so `π [i, i] = π []` while the two
words have lengths `2` and `0`. Hence

> **`not_braidEquiv_hypothesis`** — for any Coxeter system with at least one generator, the
> hypothesis of `exists_Tw_of_braidEquiv` at `π := cs.wordProd` is **false**.

Nothing is wrong with `exists_Tw_of_braidEquiv` as a statement: it quantifies over an abstract
`π : List B → W` and is a true conditional. What is wrong is the claim that it "makes the
remaining gap exact". It makes a gap that cannot be filled.

## The statement that does work

`exists_Tw_of_matsumoto` takes the **real** Matsumoto hypothesis — braid-equivalence of two
**reduced** words with the same image — and delivers `Tw` agreeing with the word product on every
**reduced** word. That is satisfiable (it is exactly Matsumoto's theorem) and it is what the
`T_w` basis is actually stated about; a basis is indexed by `W` through reduced expressions, not
through arbitrary words.

The construction needs a choice of reduced word per element, which Mathlib supplies
(`CoxeterSystem.exists_reduced_word'`); `redWord` packages it.

## Status of the input

✅ **The input is now available.** `QOU.IwahoriHecke.Matsumoto` completes the chain — *exchange*
(`CoxeterReflectionCocycle.rightExchange`) → *deletion* (`CoxeterDeletion.exists_deletion`) →
*rank-two structure* (`CoxeterRankTwo`) → *dihedral descent* (`CoxeterDihedralDescent`) →
Matsumoto. `Matsumoto.exists_Tw` discharges `exists_Tw_of_matsumoto` outright, for **every**
Coxeter system — the order of `σᵢσⱼ` is settled in `CoxeterDihedralOrder`.

The conditional form below is kept: it is what `Matsumoto` feeds, and it names the input rather
than assuming it, which is what made the discharge auditable.

-- Ref: [matsumoto1964] DOI 10.1090/S0002-9904-1964-11211-9
-- Ref: [humphreys1990] §7.1, §7.4
-- Ref: [leitner2026] bean qou-06h7
-/

namespace QOU.IwahoriHecke.TwMatsumoto

open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.BraidWord

variable {B : Type*} {M : B → B → ℕ}

/-! ## Braid-equivalence preserves length -/

/-- A single braid move preserves word length, when `M` is symmetric — which it is for a Coxeter
matrix. The two alternating blocks have lengths `M i j` and `M j i`. -/
theorem braidMove_length_eq (hM : ∀ i j, M i j = M j i) {u v : List B}
    (h : BraidMove M u v) : u.length = v.length := by
  cases h with
  | move l₁ l₂ i j =>
    simp only [List.length_append, length_altWord]
    rw [hM i j]

/-- **Braid-equivalence preserves word length.** -/
theorem braidEquiv_length_eq (hM : ∀ i j, M i j = M j i) {u v : List B}
    (h : BraidEquiv M u v) : u.length = v.length := by
  induction h with
  | refl => rfl
  | tail _ hstep ih => rw [ih, braidMove_length_eq hM hstep]

/-! ## The hypothesis of `exists_Tw_of_braidEquiv` is unsatisfiable on a Coxeter group -/

variable {W : Type*} [Group W] {CM : CoxeterMatrix B} (cs : CoxeterSystem CM W)

/-- 🛑 **The all-words hypothesis is false for `cs.wordProd`.**

`π [i,i] = π []` because `s_i² = 1`, but braid-equivalence preserves length and `2 ≠ 0`. So
`exists_Tw_of_braidEquiv`, instantiated at the word product of a Coxeter system — the only
instantiation it exists for — has a hypothesis nothing can discharge, and proves nothing.

Stated for the Coxeter matrix's own entries, which are symmetric by `CoxeterMatrix.symmetric`. -/
theorem not_braidEquiv_hypothesis (i : B) :
    ¬ (∀ u v : List B, cs.wordProd u = cs.wordProd v → BraidEquiv (fun a b => CM a b) u v) := by
  intro hmat
  have hM : ∀ a b : B, (fun a b => CM a b) a b = (fun a b => CM a b) b a := fun a b => CM.symmetric a b
  have hprod : cs.wordProd [i, i] = cs.wordProd ([] : List B) := by
    simp [cs.wordProd_cons, cs.simple_mul_simple_self]
  have := braidEquiv_length_eq hM (hmat [i, i] [] hprod)
  simp at this

/-! ## The statement that works: `T_w` from Matsumoto proper -/

/-- A chosen reduced word for each element. -/
noncomputable def redWord (w : W) : List B := (cs.exists_reduced_word' w).choose

theorem redWord_isReduced (w : W) : cs.IsReduced (redWord cs w) :=
  (cs.exists_reduced_word' w).choose_spec.1

theorem wordProd_redWord (w : W) : cs.wordProd (redWord cs w) = w :=
  ((cs.exists_reduced_word' w).choose_spec.2).symm

variable {R : Type*} [CommRing R] (q : R)

/-- **`T_w` exists as soon as Matsumoto does — the satisfiable form.**

The hypothesis is Matsumoto's theorem verbatim: two **reduced** words with the same image in `W`
are braid-equivalent. The conclusion is a `Tw : W → H(M, q)` agreeing with the word product on
every **reduced** word, which is what the `T_w` basis means.

Contrast `exists_Tw_of_braidEquiv`, whose all-words hypothesis is refuted above. -/
theorem exists_Tw_of_matsumoto
    (hmat : ∀ u v : List B, cs.IsReduced u → cs.IsReduced v →
      cs.wordProd u = cs.wordProd v → BraidEquiv (fun a b => CM a b) u v) :
    ∃ Tw : W → HeckeAlgebra R q (fun a b => CM a b),
      ∀ l : List B, cs.IsReduced l →
        Tw (cs.wordProd l) = heckeWord q (fun a b => CM a b) l := by
  refine ⟨fun w => heckeWord q (fun a b => CM a b) (redWord cs w), fun l hl => ?_⟩
  refine heckeWord_eq_of_braidEquiv q (fun a b => CM a b)
    (hmat _ _ (redWord_isReduced cs _) hl ?_)
  exact wordProd_redWord cs (cs.wordProd l)

/-- The identity has `T_1 = 1`: the chosen reduced word for `1` is empty, since it is reduced and
`ℓ(1) = 0`. -/
theorem Tw_one_of_matsumoto
    (Tw : W → HeckeAlgebra R q (fun a b => CM a b))
    (hTw : ∀ l : List B, cs.IsReduced l →
      Tw (cs.wordProd l) = heckeWord q (fun a b => CM a b) l) :
    Tw 1 = 1 := by
  have h1 : cs.wordProd ([] : List B) = 1 := by simp
  rw [← h1, hTw [] (by simp [CoxeterSystem.IsReduced]), heckeWord_nil]

end QOU.IwahoriHecke.TwMatsumoto
