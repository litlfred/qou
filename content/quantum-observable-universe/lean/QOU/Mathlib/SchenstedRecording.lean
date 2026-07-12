import QOU.Mathlib.SchenstedInsertion
import Mathlib.Data.List.Range

/-!
# Content of the recording tableau — the RSK timestamps are `0, 1, …, |w|-1`

**Brick 8 keystone.**  The recording tableau `Q(w) = (insertWordRec w).2` fills
its cells with the step indices `0, 1, …, |w|-1` at which each box was added.
This file proves that its multiset `content` is exactly `List.range |w|` — every
timestamp occurs **exactly once** — and derives the `Nodup` consequence.

This is the combinatorial core the standard-tableau `bijOn` obligation rests on:
distinctness of the entries (injectivity of the filling) is `Nodup`, and coverage
of `{0, …, |w|-1}` is the `range` identity.  Both fall out of the single branch
lemma

    content (insertRec P Q x s).2 = content Q + {s}      (shape-aligned P, Q),

which says each insertion step contributes precisely its own index `s` to the
recording content, in every branch (new row, no-bump append, or bump-recursion).

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

open List

/-- **One step contributes one timestamp.**  Appending step index `s` to a
    shape-aligned recording tableau `Q` adds exactly `{s}` to its multiset
    content, in every insertion branch (base new-row, no-bump append, and
    bump-recursion). -/
theorem insertRec_snd_content :
    ∀ (P Q : List (List ℕ)) (x s : ℕ), tableauShape P = tableauShape Q →
      content (insertRec P Q x s).2 = content Q + {s}
  | [], Q, x, s => by
      intro h
      have hQ : Q = [] := by
        cases Q with
        | nil => rfl
        | cons q qs => simp [tableauShape] at h
      subst hQ
      simp [insertRec]
  | prow :: prest, Q, x, s => by
      intro h
      cases Q with
      | nil => simp [tableauShape] at h
      | cons qrow qrest =>
        simp only [tableauShape_cons] at h
        obtain ⟨hql, hqs⟩ := List.cons.injEq .. ▸ h
        rw [insertRec]
        cases hb : (rowInsert prow x).2 with
        | none =>
          simp only [List.headD_cons, List.tail_cons, content_cons]
          have hcoe : ((qrow ++ [s] : List ℕ) : Multiset ℕ) = (↑qrow : Multiset ℕ) + {s} := rfl
          rw [hcoe]; abel
        | some y =>
          simp only [List.headD_cons, List.tail_cons, content_cons]
          rw [insertRec_snd_content prest qrest y s hqs]; abel

/-- **Content of the recording fold.**  Folding the letters of `w` from step `s`
    adds the consecutive indices `s, s+1, …, s+|w|-1` (i.e. `List.range' s |w|`)
    to the recording content. -/
theorem insertWordRecAux_content :
    ∀ (w : List ℕ) (s : ℕ) (P Q : List (List ℕ)), tableauShape P = tableauShape Q →
      content (insertWordRecAux w s P Q).2 = content Q + ↑(List.range' s w.length)
  | [], s, P, Q => by intro _; simp [insertWordRecAux]
  | x :: rest, s, P, Q => by
      intro h
      rw [insertWordRecAux,
        insertWordRecAux_content rest (s + 1) _ _ (insertRec_shape P Q x s h).symm,
        insertRec_snd_content P Q x s h,
        List.length_cons, List.range'_succ, ← Multiset.cons_coe, ← Multiset.singleton_add]
      abel

/-- **The recording tableau's timestamps are exactly `0, 1, …, |w|-1`.**  Its
    multiset content is `List.range |w|`; each step index occurs exactly once. -/
theorem insertWordRec_snd_content (w : List ℕ) :
    content (insertWordRec w).2 = ↑(List.range w.length) := by
  rw [insertWordRec, insertWordRecAux_content w 0 [] [] rfl, content_nil, zero_add,
    List.range_eq_range']

/-- **The recording timestamps are distinct.**  Injectivity of the standard
    filling, in multiset form. -/
theorem insertWordRec_snd_content_nodup (w : List ℕ) :
    (content (insertWordRec w).2).Nodup := by
  rw [insertWordRec_snd_content, Multiset.coe_nodup]
  exact List.nodup_range

end QOU.Mathlib.Schensted
