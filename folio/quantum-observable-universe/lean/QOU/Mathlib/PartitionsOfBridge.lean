import QOU.Mathlib.PartitionListBridge
import QOU.Mathlib.IdentityIHLFBridge
import QOU.Mathlib.SchenstedRSKBurnside

/-!
# QOU.Mathlib.PartitionsOfBridge — `partitionsOf n` enumerates `Nat.Partition n`; RSK/Burnside `n ≤ 12`

The Identity I combinatorics run `decide` over the fuel-based list enumerator
`QOU.BraidKnot.IdentityI.partitionsOf n` (all weakly-decreasing positive `List ℕ` summing to
`n`), while the abstract Plancherel/RSK statements range over Mathlib's `Nat.Partition n`.
`PartitionListBridge` supplies the pointwise dictionary (`toList` / `ofList`); what was missing
is the **enumeration bridge**: that `partitionsOf n` lists *exactly* the image of `toList`,
each partition once.  This file proves it and cashes it out:

* `mem_partsFuel_sound` / `mem_partsFuel_complete` / `partsFuel_nodup` — soundness,
  completeness, and duplicate-freeness of the fuel-based enumerator, by induction on the fuel;
* `mem_partitionsOf` / `partitionsOf_nodup` — the corollaries at `fuel = target = cap = n`;
* `toFinset_partitionsOf` — `(partitionsOf n).toFinset = Finset.univ.image toList`;
* `sum_map_partitionsOf` — sum transport: `((partitionsOf n).map g).sum = Σ_{p ⊢ n} g (toList p)`;
* **`rskBurnsideHolds_le12`** — the RSK/Burnside identity `Σ_{p ⊢ n} dimSYT(p)² = n!` for all
  `n ≤ 12`, by feeding the `decide`-verified list-model data `dim_validated_le12` through
  `rskBurnsideHolds_iff_dimHLF` (which rests on the now-proved hook-length bridge
  `dimSYT_eq_dimHLF`).  This grounds the `n ≤ 12` Plancherel instances in the genuine `#SYT`
  count with **no** RSK correspondence and no SYT structure theory.

(A direct kernel `decide` on the `Nat.Partition n`-indexed sum is not possible: the `Fintype`
instance for `Nat.Partition n` does not reduce in the kernel — verified empirically.  The list
enumerator is the computable face; this bridge is what connects it to the abstract index.)

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.PartitionsOfBridge

open QOU.BraidKnot.IdentityI (partsFuel partitionsOf dimHLF dim_validated_le12)
open QOU.Mathlib.PartitionListBridge

/-! ## Soundness: members of `partsFuel f t cap` are sorted, positive, `≤ cap`, sum `t` -/

/-- Every member of `partsFuel f t cap` is a weakly-decreasing list of parts in `[1, cap]`
summing to `t`. -/
theorem mem_partsFuel_sound {f : ℕ} : ∀ {t cap : ℕ} {l : List ℕ}, l ∈ partsFuel f t cap →
    l.Sorted (· ≥ ·) ∧ (∀ a ∈ l, 0 < a ∧ a ≤ cap) ∧ l.sum = t := by
  induction f with
  | zero =>
    intro t cap l hl
    match t with
    | 0 => simp only [partsFuel, List.mem_singleton] at hl; subst hl; simp
    | t + 1 => simp [partsFuel] at hl
  | succ f ih =>
    intro t cap l hl
    match t with
    | 0 => simp only [partsFuel, List.mem_singleton] at hl; subst hl; simp
    | t + 1 =>
      simp only [partsFuel, List.mem_flatMap, List.mem_range, List.mem_map] at hl
      obtain ⟨i, hi, tail, htail, rfl⟩ := hl
      obtain ⟨hsort, hbound, hsum⟩ := ih htail
      have hp1 : 1 ≤ min cap (t + 1) - i := by omega
      have hpcap : min cap (t + 1) - i ≤ cap := by omega
      have hpt : min cap (t + 1) - i ≤ t + 1 := by omega
      refine ⟨?_, ?_, ?_⟩
      · rw [List.sorted_cons]
        exact ⟨fun b hb => (hbound b hb).2, hsort⟩
      · intro a ha
        rcases List.mem_cons.mp ha with rfl | ha
        · exact ⟨hp1, hpcap⟩
        · exact ⟨(hbound a ha).1, le_trans (hbound a ha).2 hpcap⟩
      · simp only [List.sum_cons, hsum]; omega

/-! ## Completeness: every valid partition list with enough fuel is enumerated -/

/-- Each entry of a positive list is at most the sum. -/
private theorem le_sum_of_mem {l : List ℕ} {a : ℕ} (ha : a ∈ l) : a ≤ l.sum := by
  induction l with
  | nil => cases ha
  | cons b l ih =>
    rcases List.mem_cons.mp ha with rfl | ha
    · simp
    · simpa using le_trans (ih ha) (Nat.le_add_left _ _)

/-- A list of positive entries is no longer than its sum. -/
private theorem length_le_sum {l : List ℕ} (h : ∀ a ∈ l, 0 < a) : l.length ≤ l.sum := by
  induction l with
  | nil => simp
  | cons b l ih =>
    have hb := h b (by simp)
    have := ih fun a ha => h a (List.mem_cons_of_mem b ha)
    simp only [List.length_cons, List.sum_cons]
    omega

/-- **Completeness.** Every weakly-decreasing list of parts in `[1, cap]` summing to `t`, of
length at most the fuel, appears in `partsFuel f t cap`. -/
theorem mem_partsFuel_complete {f : ℕ} : ∀ {t cap : ℕ} {l : List ℕ},
    l.Sorted (· ≥ ·) → (∀ a ∈ l, 0 < a ∧ a ≤ cap) → l.sum = t → l.length ≤ f →
    l ∈ partsFuel f t cap := by
  induction f with
  | zero =>
    intro t cap l _ _ hsum hlen
    have hnil : l = [] := List.length_eq_zero_iff.mp (Nat.le_zero.mp hlen)
    subst hnil
    simp only [List.sum_nil] at hsum
    subst hsum
    simp [partsFuel]
  | succ f ih =>
    intro t cap l hsort hbound hsum hlen
    match l, t with
    | [], t =>
      simp only [List.sum_nil] at hsum
      subst hsum
      simp [partsFuel]
    | p :: tail, 0 =>
      exact absurd hsum
        (by simp only [List.sum_cons]; have := (hbound p (by simp)).1; omega)
    | p :: tail, t + 1 =>
      simp only [partsFuel, List.mem_flatMap, List.mem_range, List.mem_map]
      obtain ⟨hp1, hpcap⟩ := hbound p (by simp)
      have hpt : p ≤ t + 1 := by
        have := le_sum_of_mem (l := p :: tail) (a := p) (by simp)
        omega
      have hplimit : p ≤ min cap (t + 1) := le_min hpcap hpt
      have hsorttail : tail.Sorted (· ≥ ·) := (List.sorted_cons.mp hsort).2
      have hheadge : ∀ b ∈ tail, b ≤ p := fun b hb => (List.sorted_cons.mp hsort).1 b hb
      refine ⟨min cap (t + 1) - p, by omega, tail, ?_, ?_⟩
      · have hcancel : min cap (t + 1) - (min cap (t + 1) - p) = p := by omega
        rw [hcancel]
        refine ih hsorttail
          (fun a ha => ⟨(hbound a (List.mem_cons_of_mem p ha)).1, hheadge a ha⟩) ?_ ?_
        · simp only [List.sum_cons] at hsum; omega
        · simpa using Nat.lt_succ_iff.mp (lt_of_lt_of_le (Nat.lt_succ_self _)
            (by simpa using hlen))
      · have hcancel : min cap (t + 1) - (min cap (t + 1) - p) = p := by omega
        rw [hcancel]

/-! ## No duplicates -/

/-- `partsFuel` enumerates without duplicates. -/
theorem partsFuel_nodup {f : ℕ} : ∀ {t cap : ℕ}, (partsFuel f t cap).Nodup := by
  induction f with
  | zero =>
    intro t cap
    match t with
    | 0 => simp [partsFuel]
    | t + 1 => simp [partsFuel]
  | succ f ih =>
    intro t cap
    match t with
    | 0 => simp [partsFuel]
    | t + 1 =>
      simp only [partsFuel]
      rw [List.nodup_flatMap]
      constructor
      · intro i _
        exact List.Nodup.map (fun a b h => (List.cons.injEq _ _ _ _).mp h |>.2) ih
      · have hlt := List.pairwise_lt_range (n := min cap (t + 1))
        refine hlt.imp_of_mem ?_
        intro i j hi hj hij x hxi hxj
        simp only [List.mem_range] at hi hj
        simp only [List.mem_map] at hxi hxj
        obtain ⟨_, _, rfl⟩ := hxi
        obtain ⟨_, _, hx⟩ := hxj
        have hhead : min cap (t + 1) - j = min cap (t + 1) - i :=
          ((List.cons.injEq _ _ _ _).mp hx).1
        omega

/-! ## `partitionsOf n` characterisation -/

/-- **Membership in the enumerator.** `partitionsOf n` lists exactly the weakly-decreasing
positive lists summing to `n` — the computable model of `Nat.Partition n`. -/
theorem mem_partitionsOf {n : ℕ} {l : List ℕ} :
    l ∈ partitionsOf n ↔ l.Sorted (· ≥ ·) ∧ (∀ a ∈ l, 0 < a) ∧ l.sum = n := by
  constructor
  · intro hl
    obtain ⟨hs, hb, hsum⟩ := mem_partsFuel_sound hl
    exact ⟨hs, fun a ha => (hb a ha).1, hsum⟩
  · rintro ⟨hs, hpos, hsum⟩
    subst hsum
    exact mem_partsFuel_complete hs (fun a ha => ⟨hpos a ha, le_sum_of_mem ha⟩) rfl
      (length_le_sum hpos)

/-- `partitionsOf n` has no duplicates. -/
theorem partitionsOf_nodup (n : ℕ) : (partitionsOf n).Nodup := partsFuel_nodup

/-! ## The enumeration bridge and sum transport -/

/-- **The enumeration bridge.** The finset underlying `partitionsOf n` is exactly the image of
`Nat.Partition n` under `toList`. -/
theorem toFinset_partitionsOf (n : ℕ) :
    (partitionsOf n).toFinset
      = Finset.univ.image (toList : Nat.Partition n → List ℕ) := by
  ext l
  simp only [List.mem_toFinset, Finset.mem_image, Finset.mem_univ, true_and, mem_partitionsOf]
  constructor
  · rintro ⟨hs, hpos, hsum⟩
    exact ⟨ofList l hpos hsum, toList_ofList l hpos hsum hs⟩
  · rintro ⟨p, rfl⟩
    exact ⟨toList_sorted p, toList_pos p, toList_sum p⟩

/-- **Sum transport.** A sum of any `g : List ℕ → M` over the enumerator `partitionsOf n`
equals the abstract sum over `Nat.Partition n`. -/
theorem sum_map_partitionsOf {M : Type*} [AddCommMonoid M] (n : ℕ) (g : List ℕ → M) :
    ((partitionsOf n).map g).sum = ∑ p : Nat.Partition n, g (toList p) := by
  rw [← sum_image_toList, ← toFinset_partitionsOf, List.sum_toFinset _ (partitionsOf_nodup n)]

/-! ## The RSK/Burnside discharge, `n ≤ 12` -/

/-- **RSK/Burnside for `n ≤ 12`, on the genuine SYT count.**  `Σ_{p ⊢ n} dimSYT(p)² = n!` —
the `decide`-verified list-model dimension certificate `dim_validated_le12`, transported to the
abstract `Nat.Partition` index through the enumeration bridge, and onto `dimSYT` through the
hook-length bridge `dimSYT_eq_dimHLF` (via `rskBurnsideHolds_iff_dimHLF`).  No RSK
correspondence is used. -/
theorem rskBurnsideHolds_le12 : ∀ n ∈ List.range 13, QOU.Mathlib.RSKBurnsideHolds n := by
  intro n hn
  rw [QOU.Mathlib.rskBurnsideHolds_iff_dimHLF]
  show ∑ p : Nat.Partition n, (dimHLF (toList p)) ^ 2 = n.factorial
  rw [← sum_map_partitionsOf n (fun l => (dimHLF l) ^ 2)]
  exact dim_validated_le12 n hn

/-- The concrete top instance, for downstream `uses`: `Σ_{p ⊢ 12} dimSYT(p)² = 12!`. -/
example : QOU.Mathlib.RSKBurnsideHolds 12 :=
  rskBurnsideHolds_le12 12 (by simp)

/-! ## The same identity in list-model form, for **every** `n` -/

/-- **`Σ_{λ ⊢ n} dimHLF(λ)² = n!` for every `n`** — the list-model dimension certificate that
`dim_validated_le12` establishes by `decide` at `n ≤ 12`, now available at every `n`.

This is `rskBurnsideHolds_le12` run backwards: that theorem transports the `decide`-verified list
identity *up* to the abstract `Nat.Partition` index; this one transports the Robinson–Schensted
theorem (`QOU.Mathlib.rskBurnsideHolds`) *down* to the list index, through the same two bridges —
`rskBurnsideHolds_iff_dimHLF` for the hook-length identification and `sum_map_partitionsOf` for the
enumeration.

Consumers that were capped at `n ≤ 12` only because `dim_validated_le12` was a finite check can use
this instead; `dim_validated_le12` remains the cheaper route inside its range. -/
theorem sum_map_dimHLF_sq (n : ℕ) :
    ((partitionsOf n).map (fun l => (dimHLF l) ^ 2)).sum = n.factorial := by
  rw [sum_map_partitionsOf n (fun l => (dimHLF l) ^ 2)]
  have h := QOU.Mathlib.rskBurnsideHolds n
  rwa [QOU.Mathlib.rskBurnsideHolds_iff_dimHLF] at h

end QOU.Mathlib.PartitionsOfBridge
