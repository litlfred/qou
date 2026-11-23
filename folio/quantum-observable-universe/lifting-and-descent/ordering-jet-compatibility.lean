import Mathlib.Data.Real.Basic
import Mathlib.Order.WellFounded
import Mathlib.Order.WellFoundedSet
import Mathlib.Data.List.Basic
import Mathlib.Data.List.Lex


/-!
# QOU.Torsion.ordering_jet_compatibility — Admissible ordering extends through jet tower

The braiding-induced ordering ≺_c on the Hecke basis of A₀
propagates through the recursive brane tower via jet prolongation.
At each level n, the ordering extends compatibly with multiplication
and remains well-founded.

LaTeX label: `prop:ordering-jet-compatibility`

## References
- [leitner2026] §3/ordering-jet-compatibility
-/

namespace QOU.Torsion

/-- A monomial basis element: a reduced positive braid word
    (list of generator indices). -/
-- Ref: [leitner2026] §3/ordering-jet-compatibility
abbrev MonomialBasis := List ℕ

/-- Degree-lexicographic ordering on braid monomials:
    compare by length first, then lexicographically. -/
-- Ref: [leitner2026] §2/quantum-observable-universe (axiom 5)
def degLex : MonomialBasis → MonomialBasis → Prop :=
  fun w w' =>
    w.length < w'.length ∨
    (w.length = w'.length ∧ w < w')

/-! ### Well-foundedness of `degLex`

`degLex` is well-founded.  Degree (= length) is bounded below by `0`, so the
length component is `Nat.lt` (well-founded); within a fixed length the words
form the finite lexicographic order on `ℕ`, which is well-founded.  The full
`List.Lex` order on `List ℕ` is *not* well-founded (`[1] > [0,1] > [0,0,1] >
…`), so the argument is factored through the equal-length restriction rather
than the (ill-founded) unrestricted lex order. -/

/-- Equal-length lexicographic order, packaged on the length-`n` subtype. -/
private def degLexRLen (n : ℕ) :
    {l : List ℕ // l.length = n} → {l : List ℕ // l.length = n} → Prop :=
  fun a b => List.Lex (· < ·) a.1 b.1

/-- Head/tail projection of a length-`(n+1)` word into `ℕ × (length-n word)`. -/
private def degLexFLen (n : ℕ) (w : {l : List ℕ // l.length = n + 1}) :
    ℕ × {l : List ℕ // l.length = n} :=
  (w.1.headI, ⟨w.1.tail, by simp [List.length_tail, w.2]⟩)

/-- Equal-length lex is well-founded, by induction on the common length: the
    base is the empty relation on `[]`; the step transports `Prod.Lex` on
    `ℕ × (length-n words)` along the head/tail projection. -/
private theorem degLexRLen_wf : ∀ n, WellFounded (degLexRLen n) := by
  intro n
  induction n with
  | zero =>
    refine ⟨fun a => Acc.intro a ?_⟩
    rintro b hrel
    have ha : a.1 = [] := List.length_eq_zero_iff.mp a.2
    have hb : b.1 = [] := List.length_eq_zero_iff.mp b.2
    simp only [degLexRLen, ha, hb] at hrel
    cases hrel
  | succ n ih =>
    have key : WellFounded (Prod.Lex (· < · : ℕ → ℕ → Prop) (degLexRLen n)) :=
      WellFounded.prod_lex (Nat.lt_wfRel.wf) ih
    have hsub : Subrelation (degLexRLen (n + 1))
        (InvImage (Prod.Lex (· < ·) (degLexRLen n)) (degLexFLen n)) := by
      rintro ⟨la, ha⟩ ⟨lb, hb⟩ hrel
      rcases la with _ | ⟨x, xs⟩
      · simp at ha
      rcases lb with _ | ⟨y, ys⟩
      · simp at hb
      simp only [degLexRLen] at hrel
      show Prod.Lex (· < ·) (degLexRLen n)
        (degLexFLen n ⟨x :: xs, ha⟩) (degLexFLen n ⟨y :: ys, hb⟩)
      simp only [degLexFLen, List.headI, List.tail_cons]
      cases hrel with
      | cons h => exact Prod.Lex.right _ h
      | rel h => exact Prod.Lex.left _ _ h
    exact Subrelation.wf hsub (InvImage.wf (degLexFLen n) key)

/-- Equal-length lex on all of `List ℕ` (carrying the length constraint as a
    conjunct, so it is globally well-founded — chains stay within one length). -/
private def degLexRList : List ℕ → List ℕ → Prop :=
  fun a b => a.length = b.length ∧ List.Lex (· < ·) a b

private theorem degLex_acc_rList_of_rLen : ∀ (n : ℕ) (p : {l : List ℕ // l.length = n}),
    Acc (degLexRLen n) p → Acc degLexRList p.1 := by
  intro n p hp
  induction hp with
  | intro p _ ih =>
    refine Acc.intro p.1 ?_
    rintro b ⟨hlen, hlex⟩
    exact ih ⟨b, hlen.trans p.2⟩ (by simpa [degLexRLen] using hlex)

private theorem degLexRList_wf : WellFounded degLexRList :=
  ⟨fun w => degLex_acc_rList_of_rLen w.length ⟨w, rfl⟩ ((degLexRLen_wf w.length).apply _)⟩

/-- **`degLex` is well-founded.**  Factored through the length-first embedding
    `w ↦ (w.length, w)` into `Prod.Lex Nat.lt degLexRList`; the length component
    is `Nat.lt` (well-founded) and the equal-length lex `degLexRList` is
    well-founded by `degLexRList_wf`. -/
-- Ref: [leitner2026] §2/quantum-observable-universe (axiom 5)
-- Ref: [leitner2026] §3/ordering-jet-compatibility
private theorem degLex_wf_unrestricted :
    WellFounded (fun (w w' : MonomialBasis) => degLex w w') := by
  have key : WellFounded (Prod.Lex (· < · : ℕ → ℕ → Prop) degLexRList) :=
    WellFounded.prod_lex (Nat.lt_wfRel.wf) degLexRList_wf
  have hsub : Subrelation (fun w w' : MonomialBasis => degLex w w')
      (InvImage (Prod.Lex (· < ·) degLexRList) (fun w : MonomialBasis => (w.length, w))) := by
    rintro a b (h | ⟨hlen, hlt⟩)
    · show Prod.Lex (· < ·) degLexRList (a.length, a) (b.length, b)
      exact Prod.Lex.left _ _ h
    · show Prod.Lex (· < ·) degLexRList (a.length, a) (b.length, b)
      rw [← hlen]
      exact Prod.Lex.right _ ⟨hlen, (List.lt_iff_lex_lt a b).mp hlt⟩
  exact Subrelation.wf hsub (InvImage.wf _ key)

theorem degLex_wellFounded (n : ℕ) (hn : 0 < n) :
    WellFounded (fun (w w' : MonomialBasis) =>
      degLex w w' ∧ ∀ g ∈ w, g < n) := by
  -- Our relation R w w' := degLex w w' ∧ (∀ g ∈ w, g < n)
  -- is a sub-relation of degLex (drop the second conjunct).
  -- A sub-relation of a well-founded relation is well-founded.
  exact Subrelation.wf (fun ⟨h, _⟩ => h) degLex_wf_unrestricted

/-- At brane level k, the jet prolongation introduces new generators
    (Ω¹ directions) ordered after all level-k generators. The
    resulting ordering on B_{k+1} extends B_k. -/
-- Ref: [leitner2026] §3/ordering-jet-compatibility
structure JetExtension where
  level : ℕ
  /-- Number of generators at this level. -/
  numGens : ℕ
  /-- Number of new Ω¹ directions per prolongation (= 3 for SU(2)). -/
  numNewDirs : ℕ := 3

/-- Lexicographic order on `ℕ`-words is preserved by any strictly monotone
    relabelling of the letters. -/
theorem lex_map_strictMono {φ : ℕ → ℕ} (hφ : StrictMono φ) :
    ∀ {a b : List ℕ}, List.Lex (· < ·) a b → List.Lex (· < ·) (a.map φ) (b.map φ)
  | _, _, List.Lex.nil => List.Lex.nil
  | _, _, List.Lex.cons h => List.Lex.cons (lex_map_strictMono hφ h)
  | _, _, List.Lex.rel h => List.Lex.rel (hφ h)

/-- **Ordering extends through the jet embedding.**

    The jet prolongation `ℓ_n : B_n → B_{n+1}` relabels each level-`n`
    generator index by a map `φ : ℕ → ℕ` on the alphabet; the new `Ω¹`
    directions are inserted without reordering the old generators, which is
    exactly the hypothesis that `φ` is strictly monotone. Under that
    hypothesis `a ≺_n b` implies `ℓ_n(a) ≺_{n+1} ℓ_n(b)`, with
    `ℓ_n(w) = w.map φ`.

    The hypothesis is load-bearing: a non-injective relabelling collapses
    `[0] ≺ [1]` to `[0] = [0]`, so the statement fails without it.

    History (bean qou-6qbv): until 2026-11-20 this declaration was
    `(hab : degLex a b) : degLex a b := hab`, a `P → P` in which neither the
    embedding nor the level index appeared. -/
-- Ref: [leitner2026] §3/ordering-jet-compatibility
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
theorem ordering_extends {φ : ℕ → ℕ} (hφ : StrictMono φ) {a b : MonomialBasis}
    (hab : degLex a b) : degLex (a.map φ) (b.map φ) := by
  rcases hab with h | ⟨hlen, hlt⟩
  · left; simpa using h
  · right
    refine ⟨by simpa using hlen, ?_⟩
    exact (List.lt_iff_lex_lt _ _).mpr
      (lex_map_strictMono hφ ((List.lt_iff_lex_lt a b).mp hlt))

/-- Equal-length lexicographic order is preserved by appending a common
    suffix (the difference lies inside the equal-length prefix). -/
theorem lex_append_right {d : List ℕ} : ∀ {a b : List ℕ}, a.length = b.length →
    List.Lex (· < ·) a b → List.Lex (· < ·) (a ++ d) (b ++ d)
  | _, _, _, List.Lex.nil => by simp_all
  | _ :: _, _ :: _, h, List.Lex.cons hl =>
      List.Lex.cons (lex_append_right (by simpa using h) hl)
  | _, _, _, List.Lex.rel h => List.Lex.rel h

/-- Lexicographic order is preserved by prepending a common prefix. -/
theorem lex_append_left (c : List ℕ) {a b : List ℕ} (h : List.Lex (· < ·) a b) :
    List.Lex (· < ·) (c ++ a) (c ++ b) := by
  induction c with
  | nil => simpa
  | cons x xs ih => exact List.Lex.cons ih

/-- Left and right compatibility with multiplication at each level:
    a ≺ b implies c·a·d ≺ c·b·d. Proved (was an `axiom` until 2026-11-20,
    bean qou-6qbv): a length difference survives concatenation, and an
    equal-length lex difference lives inside the middle factor. -/
-- Ref: [leitner2026] §3/ordering-jet-compatibility
-- Ref: [leitner2026] unital-groebner-bases/admissible-system
theorem ordering_compatible (a b c d : MonomialBasis)
    (hab : degLex a b) :
    degLex (c ++ a ++ d) (c ++ b ++ d) := by
  rcases hab with h | ⟨hlen, hlt⟩
  · left; simp only [List.length_append]; omega
  · right
    refine ⟨by simp [hlen], (List.lt_iff_lex_lt _ _).mpr ?_⟩
    simpa [List.append_assoc] using
      lex_append_left c (lex_append_right (d := d) hlen ((List.lt_iff_lex_lt a b).mp hlt))

/-- Well-foundedness at each level n: no infinite descending chains
    in B_n.  Immediate from `degLex_wellFounded`. -/
-- Ref: [leitner2026] §3/ordering-jet-compatibility
theorem wellfounded_at_level (n : ℕ) (hn : 0 < n) :
    WellFounded (fun (w w' : MonomialBasis) =>
      degLex w w' ∧ ∀ g ∈ w, g < n) :=
  degLex_wellFounded n hn

/-- The direct limit algebra A_∞ = colim End(A_n) carries a filtered
    admissible ordering ≺_∞ = ⋃_n ≺_n. The Gröbner reduction
    algorithm terminates on every element belonging to some finite
    level A_n. -/
-- Ref: [leitner2026] §3/ordering-jet-compatibility
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
theorem direct_limit_terminates (n : ℕ) (w : MonomialBasis)
    (_hw : ∀ g ∈ w, g < n) :
    Acc (fun (u v : MonomialBasis) => degLex u v ∧ ∀ g ∈ u, g < n) w :=
  -- Was `axiom … : ∃ w', ¬ degLex w' w`, which `w' := w` satisfies for every
  -- word (degLex is irreflexive) and so asserted nothing. Termination is
  -- accessibility: no infinite descending reduction chain starts at `w`.
  (Subrelation.wf (fun ⟨h, _⟩ => h) degLex_wf_unrestricted).apply w

/-- **Consequence for time**: the braiding-induced ordering ≺_c on
    A₀ propagates through the entire jet tower. Forward time
    (Gröbner reduction, braiding) and backward time (anti-involution,
    unbraiding) are well-defined at every brane level. -/
-- Ref: [leitner2026] §3/ordering-jet-compatibility
noncomputable def ordering_jet_compatibility : Prop :=
  ∀ n : ℕ, WellFounded (fun (w w' : MonomialBasis) =>
    degLex w w' ∧ ∀ g ∈ w, g < n)

end QOU.Torsion
