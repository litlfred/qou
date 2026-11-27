import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Prod
import Mathlib.Order.Fin.Basic

/-!
# Inversion count of a permutation of `Fin n` and its decrease under an adjacent descent swap

A small Mathlib-gap kernel for the Okounkov–Vershik exchange argument
(`QOU.BraidKnot.JucysMurphy.syt_all_connect_to_some`): the well-founded measure that drives the
walk of any standard Young tableau toward the row-superstandard base.

`invCount π` counts inversions `{(i, j) : i < j, π j < π i}`.  The key fact is that composing on
the right with the adjacent transposition `swap a (a+1)` at a **descent** (`π (a+1) < π a`) strictly
decreases the count (`invCount_mul_swap_lt`): the pair `(a, a+1)` is the *only* pair whose order is
reversed by an adjacent swap, so the inversion set of `π ∘ swap` injects into that of `π` while
missing the (now-resolved) inversion `(a, a+1)`.

Pure combinatorics on `Fin n`; §7c-clean; no fit.
-/

namespace QOU.Mathlib

open Finset

variable {n : ℕ}

/-- **Inversion count** of a permutation of `Fin n`: the number of pairs `i < j` with `π j < π i`. -/
def invCount (π : Equiv.Perm (Fin n)) : ℕ :=
  (Finset.univ.filter (fun p : Fin n × Fin n => p.1 < p.2 ∧ π p.2 < π p.1)).card

/-- An adjacent swap reverses the order of exactly the pair `(a, a+1)`; every other increasing pair
stays increasing. -/
theorem swap_lt_of_ne {a b : Fin n} (hb : (b : ℕ) = (a : ℕ) + 1) {i j : Fin n}
    (hij : i < j) (hne : (i, j) ≠ (a, b)) : Equiv.swap a b i < Equiv.swap a b j := by
  have hval : ∀ x : Fin n,
      (Equiv.swap a b x : Fin n).val
        = if x.val = a.val then b.val else if x.val = b.val then a.val else x.val := by
    intro x
    rw [Equiv.swap_apply_def]
    rcases eq_or_ne x a with h | h
    · subst h; simp
    · rcases eq_or_ne x b with h2 | h2
      · subst h2; rw [if_neg h, if_pos rfl, if_neg (by simpa [Fin.ext_iff] using h),
          if_pos rfl]
      · rw [if_neg h, if_neg h2, if_neg (by simpa [Fin.ext_iff] using h),
          if_neg (by simpa [Fin.ext_iff] using h2)]
  rw [Fin.lt_def, hval, hval]
  rw [Fin.lt_def] at hij
  have hnv : ¬ (i.val = a.val ∧ j.val = b.val) := by
    intro ⟨h1, h2⟩
    exact hne (Prod.ext (Fin.ext h1) (Fin.ext h2))
  split_ifs <;> omega

/-- **Descent swap strictly lowers the inversion count.**  If `b = a + 1` and `π b < π a`
(an adjacent descent), then `invCount (π * swap a b) < invCount π`. -/
theorem invCount_mul_swap_lt (π : Equiv.Perm (Fin n)) {a b : Fin n}
    (hb : (b : ℕ) = (a : ℕ) + 1) (hdesc : π b < π a) :
    invCount (π * Equiv.swap a b) < invCount π := by
  classical
  have hab : a < b := by rw [Fin.lt_def, hb]; omega
  unfold invCount
  set S : Finset (Fin n × Fin n) :=
    Finset.univ.filter (fun p : Fin n × Fin n => p.1 < p.2 ∧ π p.2 < π p.1) with hS
  set S' : Finset (Fin n × Fin n) :=
    Finset.univ.filter (fun p : Fin n × Fin n => p.1 < p.2 ∧
      (π * Equiv.swap a b) p.2 < (π * Equiv.swap a b) p.1) with hS'
  have hmemS : (a, b) ∈ S := by
    rw [hS, Finset.mem_filter]; exact ⟨Finset.mem_univ _, hab, hdesc⟩
  -- φ = swap on both components injects S' into S \ {(a,b)}
  have hmaps : ∀ p ∈ S', (Equiv.swap a b p.1, Equiv.swap a b p.2) ∈ S.erase (a, b) := by
    intro p hp
    rw [hS', Finset.mem_filter] at hp
    obtain ⟨_, hlt, hdlt⟩ := hp
    simp only [Equiv.Perm.mul_apply] at hdlt
    have hpne : p ≠ (a, b) := by
      rintro rfl
      simp only [Equiv.swap_apply_left, Equiv.swap_apply_right] at hdlt
      exact absurd hdlt (not_lt.mpr (le_of_lt hdesc))
    have hlt' : Equiv.swap a b p.1 < Equiv.swap a b p.2 :=
      swap_lt_of_ne hb hlt (by
        intro h; exact hpne (Prod.ext (congrArg Prod.fst h) (congrArg Prod.snd h)))
    rw [Finset.mem_erase]
    refine ⟨?_, ?_⟩
    · rintro heq
      have h1 : Equiv.swap a b p.1 = a := congrArg Prod.fst heq
      have h2 : Equiv.swap a b p.2 = b := congrArg Prod.snd heq
      have hp1 : p.1 = b := by
        have := congrArg (Equiv.swap a b) h1
        rwa [Equiv.swap_apply_self, Equiv.swap_apply_left] at this
      have hp2 : p.2 = a := by
        have := congrArg (Equiv.swap a b) h2
        rwa [Equiv.swap_apply_self, Equiv.swap_apply_right] at this
      rw [hp1, hp2] at hlt
      exact absurd hlt (not_lt.mpr (le_of_lt hab))
    · rw [hS, Finset.mem_filter]
      exact ⟨Finset.mem_univ _, hlt', hdlt⟩
  have hinj : Set.InjOn
      (fun p : Fin n × Fin n => (Equiv.swap a b p.1, Equiv.swap a b p.2)) S' := by
    intro x _ y _ h
    have h1 : Equiv.swap a b x.1 = Equiv.swap a b y.1 := congrArg Prod.fst h
    have h2 : Equiv.swap a b x.2 = Equiv.swap a b y.2 := congrArg Prod.snd h
    exact Prod.ext ((Equiv.swap a b).injective h1) ((Equiv.swap a b).injective h2)
  have hcard : S'.card ≤ (S.erase (a, b)).card := Finset.card_le_card_of_injOn _ hmaps hinj
  rw [Finset.card_erase_of_mem hmemS] at hcard
  have hSpos : 0 < S.card := Finset.card_pos.mpr ⟨(a, b), hmemS⟩
  omega

/-- A strictly monotone permutation of `Fin n` is the identity. -/
theorem eq_one_of_strictMono {π : Equiv.Perm (Fin n)} (hmono : StrictMono π) : π = 1 := by
  apply Equiv.ext
  intro i
  have h : ((⟨π, hmono.le_iff_le⟩ : Fin n ≃o Fin n) i : ℕ) = (i : ℕ) :=
    Fin.coe_orderIso_apply _ i
  rw [RelIso.coe_fn_mk] at h
  simpa using Fin.ext h

/-- Increasing on every adjacent pair implies strictly monotone (general `n`, by induction on the
gap). -/
theorem strictMono_of_adjacent {π : Equiv.Perm (Fin n)}
    (hadj : ∀ i : Fin n, ∀ h : (i : ℕ) + 1 < n, π i < π ⟨(i : ℕ) + 1, h⟩) : StrictMono π := by
  have key : ∀ d : ℕ, ∀ i j : Fin n, (j : ℕ) = (i : ℕ) + d → 0 < d → π i < π j := by
    intro d
    induction d with
    | zero => intro i j _ hd; omega
    | succ e IH =>
      intro i j hj _
      have hjlt := j.isLt
      rcases Nat.eq_zero_or_pos e with rfl | he
      · have h1 : (i : ℕ) + 1 < n := by omega
        have hstep := hadj i h1
        rwa [show j = (⟨(i : ℕ) + 1, h1⟩ : Fin n) from Fin.ext (by omega)]
      · have hk : (i : ℕ) + e < n := by omega
        have hk1 : ((i : ℕ) + e) + 1 < n := by omega
        have h1 : π i < π ⟨(i : ℕ) + e, hk⟩ := IH i ⟨(i : ℕ) + e, hk⟩ (by simp) he
        have hstep := hadj ⟨(i : ℕ) + e, hk⟩ (by simpa using hk1)
        have hb2 : (i : ℕ) + e + 1 < n := by omega
        have hjv : (j : ℕ) = (i : ℕ) + e + 1 := by omega
        have hjeq : j = (⟨(i : ℕ) + e + 1, hb2⟩ : Fin n) := Fin.ext hjv
        have h2 : π ⟨(i : ℕ) + e, hk⟩ < π j := by rw [hjeq]; exact hstep
        exact lt_trans h1 h2
  intro i j hij
  exact key (j.val - i.val) i j (by omega) (by omega)

/-- **`invCount π = 0 ⟹ π = 1`.**  No inversions means `π` is strictly monotone, hence the
identity. -/
theorem eq_one_of_invCount_eq_zero {π : Equiv.Perm (Fin n)} (h : invCount π = 0) : π = 1 := by
  apply eq_one_of_strictMono
  intro i j hij
  have hempty := Finset.card_eq_zero.mp h
  have hnm : (i, j) ∉ Finset.univ.filter
      (fun p : Fin n × Fin n => p.1 < p.2 ∧ π p.2 < π p.1) := by
    rw [hempty]; exact Finset.notMem_empty _
  rw [Finset.mem_filter] at hnm
  have hle : ¬ (π j < π i) := fun hlt => hnm ⟨Finset.mem_univ _, hij, hlt⟩
  rcases lt_or_eq_of_le (not_lt.mp hle) with h' | h'
  · exact h'
  · exact absurd (π.injective h') (ne_of_lt hij)

/-- **`π ≠ 1 ⟹` there is an adjacent descent** `π (a+1) < π a`. -/
theorem exists_adjacent_descent_of_ne_one {π : Equiv.Perm (Fin n)} (hπ : π ≠ 1) :
    ∃ a b : Fin n, (b : ℕ) = (a : ℕ) + 1 ∧ π b < π a := by
  by_contra hcon
  push_neg at hcon
  apply hπ
  apply eq_one_of_strictMono
  apply strictMono_of_adjacent
  intro i h
  have hle : ¬ (π ⟨(i : ℕ) + 1, h⟩ < π i) := by
    intro hlt
    exact absurd (hcon i ⟨(i : ℕ) + 1, h⟩ (by simp)) (not_le.mpr hlt)
  rcases lt_or_eq_of_le (not_lt.mp hle) with h' | h'
  · exact h'
  · exact absurd (π.injective h') (by intro heq; simp only [Fin.ext_iff] at heq; omega)

end QOU.Mathlib
