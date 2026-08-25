import QOU.Mathlib.SchenstedRSKInjective
import QOU.Mathlib.SchenstedPairingMap

/-!
# QOU.Mathlib.SchenstedPermInjective — RSK separates permutations (brick 8)

Brick 7 proved the RSK map injective on **words** of a fixed length. A permutation reaches that
statement through `wordOfPerm`, so this file supplies the missing half — `wordOfPerm` is itself
injective, and it has the length the brick-7 hypothesis wants — and composes the two:

> **distinct permutations of `Fin n` have distinct `(P, Q)` pairs.**

That is the injectivity half of the Robinson–Schensted correspondence, at the raw
`List (List ℕ)` level where the combinatorics lives.

## Why this rather than the typed `rskPair`

`SchenstedPairingMap.rskPair` is typed in `StandardYoungTableau`, built from the raw tableaux by
`listStandardYT`. Lifting brick 7 through that wrapper needs a typed→raw retraction, which the
corpus does not currently carry; and the *content* would be unchanged, since the wrapper is a
repackaging of the same data. So the honest statement to prove now is the raw one, and the typed
corollary can follow once a retraction exists. Nothing here claims `rskPair` itself is injective.

## Scope

Injectivity only. Surjectivity — the genuinely remaining half — and the cardinality identity
`RSKBurnsideHolds` are the rest of epic `qou-nrex`.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

open Equiv (Perm)

/-- `wordOfPerm σ` has one letter per point. -/
@[simp] theorem wordOfPerm_length {n : ℕ} (σ : Perm (Fin n)) : (wordOfPerm σ).length = n := by
  simp [wordOfPerm]

/-- **`wordOfPerm` is injective.** The word lists `σ`'s values in index order, shifted by one, so
reading it back recovers `σ` pointwise. -/
theorem wordOfPerm_injective {n : ℕ} : Function.Injective (wordOfPerm (n := n)) := by
  intro σ τ h
  refine Equiv.ext (fun i => Fin.ext ?_)
  have hmap : (List.finRange n).map (fun j => (σ j : ℕ) + 1)
      = (List.finRange n).map (fun j => (τ j : ℕ) + 1) := h
  have hget := List.map_inj_left.mp hmap i (List.mem_finRange i)
  omega

/-- **RSK separates permutations.** Distinct permutations of `Fin n` produce distinct
insertion/recording pairs.

Brick 7 needs the two words to have equal length; `wordOfPerm_length` supplies it, both being `n`.
-/
theorem insertWordRec_wordOfPerm_injective {n : ℕ} :
    Function.Injective (fun σ : Perm (Fin n) => insertWordRec (wordOfPerm σ)) := by
  intro σ τ h
  refine wordOfPerm_injective ?_
  exact word_eq_of_insertWordRec_eq (wordOfPerm σ) (wordOfPerm τ)
    (by rw [wordOfPerm_length, wordOfPerm_length]) h

/-- Contrapositive: distinct permutations are told apart by their `(P, Q)` pair. -/
theorem insertWordRec_wordOfPerm_ne {n : ℕ} {σ τ : Perm (Fin n)} (hne : σ ≠ τ) :
    insertWordRec (wordOfPerm σ) ≠ insertWordRec (wordOfPerm τ) :=
  fun h => hne (insertWordRec_wordOfPerm_injective h)

end QOU.Mathlib.Schensted
