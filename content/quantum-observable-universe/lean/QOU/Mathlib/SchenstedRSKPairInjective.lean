import QOU.Mathlib.SchenstedRSKPairSurjective
import QOU.Mathlib.SchenstedRSKInjective

/-!
# QOU.Mathlib.SchenstedRSKPairInjective — `rskPair` is injective

Brick 39 of epic `qou-nrex` (RSK inverse).

`SchenstedRSKInjective` proves the RSK map injective **on words**: the pair `(P(w), Q(w))` of *list*
tableaux determines `w`. `rskPair` is stated **on permutations**, and its value is a `Σ` of Mathlib
standard Young tableaux. This file bridges that mismatch, which is the whole distance between the
two statements.

The bridge needs no `HEq` and no `subst`, and that is the point worth recording. Extracting the
second component of a `Σ`-equality normally needs a transport, because its type depends on the
first. But `fun X => X.2.1.entry i j` is a perfectly good **non-dependent** function on the `Σ`
type — a dependent projection followed by an `ℕ`-valued field — so `congrArg` hands over entry
equalities directly.

From there it is ordinary list combinatorics: `eq_of_shape_and_entries` turns "same shape, same
entries" into equality of list tableaux, `shiftT_injective` strips the `0`→`1` relabel, and
`word_eq_of_insertWordRec_eq` (the existing word-level injectivity) finishes.
`wordOfPerm_injective` takes the last step back to permutations.

## Scope

Injectivity. Together with brick 38 this is a bijection in substance, but the `Equiv` itself — and
`RSKBurnsideHolds` for general `n` past it — is not assembled here. `RSKBurnsideHolds` remains
proved only for `n ≤ 12`, by a route with no RSK correspondence in it.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.Schensted

open YoungDiagram

/-- **Same shape, same entries, same tableau.** -/
theorem eq_of_shape_and_entries {T T' : List (List ℕ)}
    (hs : tableauShape T = tableauShape T')
    (h : ∀ i j, (T.getD i []).getD j 0 = (T'.getD i []).getD j 0) : T = T' := by
  have hlen : T.length = T'.length := by
    have := congrArg List.length hs
    simpa [tableauShape] using this
  refine List.ext_getElem hlen (fun i h1 h2 => ?_)
  have hrow : (T.getD i []).length = (T'.getD i []).length := by
    rw [← getD_tableauShape T i, ← getD_tableauShape T' i, hs]
  rw [← getD_row_eq h1, ← getD_row_eq h2]
  refine List.ext_getElem hrow (fun j j1 j2 => ?_)
  have := h i j
  rwa [getD_eq_getElem_mem j1, getD_eq_getElem_mem j2] at this

/-- The `0`→`1` relabel is injective: it is a `map` of a `map` of an injective function. -/
theorem shiftT_injective : Function.Injective shiftT := by
  have hrow : Function.Injective (fun row : List ℕ => row.map (· + 1)) :=
    List.map_injective_iff.mpr (fun a b h => by simpa using h)
  intro Q Q' h
  exact List.map_injective_iff.mpr hrow h

/-- A permutation is determined by its word. -/
theorem wordOfPerm_injective {n : ℕ} : Function.Injective (wordOfPerm (n := n)) := by
  intro σ τ h
  simp only [wordOfPerm, List.map_inj_left] at h
  refine Equiv.coe_fn_injective (funext (fun i => Fin.ext ?_))
  have hval : ((σ i : ℕ)) + 1 = ((τ i : ℕ)) + 1 := h i (by simp)
  exact Nat.add_right_cancel hval

/-- **`rskPair` is injective.** Entry equalities come straight out of the `Σ`-equality by
`congrArg`; the rest is the word-level injectivity already in the corpus. -/
theorem rskPair_injective {n : ℕ} : Function.Injective (rskPair (n := n)) := by
  intro σ τ heq
  have hsh : pShape (wordOfPerm σ) = pShape (wordOfPerm τ) := congrArg Sigma.fst heq
  have hshape : tableauShape (insertWord (wordOfPerm σ))
      = tableauShape (insertWord (wordOfPerm τ)) := by
    have h1 := congrArg YoungDiagram.rowLens hsh
    rwa [pShape, pShape,
      rowLens_ofRowLens_eq_self (tableauShape_pos (insertWord_noEmptyRows (wordOfPerm σ))),
      rowLens_ofRowLens_eq_self (tableauShape_pos (insertWord_noEmptyRows (wordOfPerm τ)))] at h1
  have hP : insertWord (wordOfPerm σ) = insertWord (wordOfPerm τ) := by
    refine eq_of_shape_and_entries hshape (fun i j => ?_)
    exact congrArg (fun X : Σ μ : YoungDiagram, QOU.Mathlib.StandardYoungTableau μ ×
      QOU.Mathlib.StandardYoungTableau μ => X.2.1.entry i j) heq
  have hQs : shiftT (insertWordRec (wordOfPerm σ)).2 = shiftT (insertWordRec (wordOfPerm τ)).2 := by
    refine eq_of_shape_and_entries ?_ (fun i j => ?_)
    · rw [shiftT_shape, shiftT_shape, insertWordRec_shape_eq_P, insertWordRec_shape_eq_P, hshape]
    · have h2 := congrArg (fun X : Σ μ : YoungDiagram, QOU.Mathlib.StandardYoungTableau μ ×
        QOU.Mathlib.StandardYoungTableau μ => X.2.2.entry i j) heq
      simpa only [rskPair, rskPairWord, entry_cast] using h2
  have hrec : insertWordRec (wordOfPerm σ) = insertWordRec (wordOfPerm τ) := by
    refine Prod.ext_iff.mpr ⟨?_, shiftT_injective hQs⟩
    rw [insertWordRec_fst, insertWordRec_fst, hP]
  have hlen : (wordOfPerm σ).length = (wordOfPerm τ).length := by simp [wordOfPerm]
  exact wordOfPerm_injective
    (word_eq_of_insertWordRec_eq (wordOfPerm σ) (wordOfPerm τ) hlen hrec)

end QOU.Mathlib.Schensted
