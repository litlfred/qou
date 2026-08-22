import QOU.Mathlib.SchenstedSYTRoundTrip
import QOU.Mathlib.SchenstedPairingMap

/-!
# QOU.Mathlib.SchenstedWordOfPermSurj — every permutation word comes from a permutation

Brick 36 of epic `qou-nrex` (RSK inverse).

`rskPairWord` accepts any word whose content is `{1, …, n}`; `rskPair` accepts a permutation and
reaches `rskPairWord` through `wordOfPerm`. Surjectivity of `rskPair` therefore needs the two entry
points to see the same words:

**`exists_wordOfPerm_eq`** — a word of content `{1, …, n}` *is* `wordOfPerm σ` for some `σ`.

The permutation is read straight off the word: `σ i = w[i] - 1`. It is injective because the word is
duplicate-free, and on a finite type injective is bijective — which is the only reason no inverse
has to be built by hand.

## Scope

One of the two gaps the epic bean records between brick 35 and `rskPair` surjectivity; the other is
threading brick 35's `Σ`-equality through `rskPair`'s definition. `rskPair` bijectivity is not
claimed here, and `RSKBurnsideHolds` for general `n` remains open — still proved only for `n ≤ 12`,
by a route with no RSK correspondence in it.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.Schensted

/-- A word of content `{1, …, n}` has length `n`, no repeats, and entries in `[1, n]`. -/
theorem length_nodup_mem_of_content {w : List ℕ} {n : ℕ}
    (hw : (↑w : Multiset ℕ) = (↑(List.range n) : Multiset ℕ).map (· + 1)) :
    w.length = n ∧ w.Nodup ∧ ∀ a ∈ w, 1 ≤ a ∧ a ≤ n := by
  have hinj : Function.Injective (fun x : ℕ => x + 1) := fun a b h => by simpa using h
  refine ⟨by simpa using congrArg Multiset.card hw, ?_, ?_⟩
  · have hnd : (↑w : Multiset ℕ).Nodup := by
      rw [hw, Multiset.map_coe, Multiset.coe_nodup]
      exact List.nodup_range.map hinj
    rwa [Multiset.coe_nodup] at hnd
  · intro a ha
    have hm : a ∈ (↑w : Multiset ℕ) := by simpa using ha
    rw [hw, Multiset.map_coe, Multiset.mem_coe, List.mem_map] at hm
    obtain ⟨b, hb, rfl⟩ := hm
    rw [List.mem_range] at hb
    omega

/-- **Every word of content `{1, …, n}` is a permutation word.** The permutation is `i ↦ w[i] - 1`;
duplicate-freeness makes it injective, and injective is bijective on a finite type. -/
theorem exists_wordOfPerm_eq {w : List ℕ} {n : ℕ}
    (hw : (↑w : Multiset ℕ) = (↑(List.range n) : Multiset ℕ).map (· + 1)) :
    ∃ σ : Equiv.Perm (Fin n), wordOfPerm σ = w := by
  obtain ⟨hlen, hnd, hmem⟩ := length_nodup_mem_of_content hw
  have hbound : ∀ i : Fin n, w.getD (i : ℕ) 0 - 1 < n := by
    intro i
    have hi : (i : ℕ) < w.length := by rw [hlen]; exact i.isLt
    have := hmem _ (getD_mem hi)
    omega
  have hinj : Function.Injective (fun i : Fin n => (⟨w.getD (i : ℕ) 0 - 1, hbound i⟩ : Fin n)) := by
    intro a b hab
    have h1 : w.getD (a : ℕ) 0 - 1 = w.getD (b : ℕ) 0 - 1 := congrArg Fin.val hab
    have ha : (a : ℕ) < w.length := by rw [hlen]; exact a.isLt
    have hb : (b : ℕ) < w.length := by rw [hlen]; exact b.isLt
    have hpa := hmem _ (getD_mem ha)
    have hpb := hmem _ (getD_mem hb)
    have heq : w.getD (a : ℕ) 0 = w.getD (b : ℕ) 0 := by omega
    rw [getD_eq_getElem_mem ha, getD_eq_getElem_mem hb] at heq
    exact Fin.ext (hnd.getElem_inj_iff.mp heq)
  refine ⟨Equiv.ofBijective _ (Finite.injective_iff_bijective.mp hinj), ?_⟩
  rw [wordOfPerm]
  refine List.ext_getElem (by simp [hlen]) (fun k h1 h2 => ?_)
  simp only [List.getElem_map, List.getElem_finRange, Equiv.ofBijective_apply, Fin.coe_cast,
    Fin.val_mk]
  have hk : k < w.length := h2
  have := hmem _ (getD_mem hk)
  rw [getD_eq_getElem_mem hk] at this ⊢
  omega

end QOU.Mathlib.Schensted
