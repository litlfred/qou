import QOU.MassTheory.StaircaseTopCoeff
import Mathlib.Algebra.Polynomial.Monic
import Mathlib.RingTheory.Polynomial.Basic

/-!
# Top terms of the `q`-hook quotient

Third step of the partition count behind `conj:cyclotomic-boundary-at-keystone`.

For a Young diagram `s` (a finite lower set of `ℕ × ℕ`) with `n` cells, write
`[k] = 1 + X + ⋯ + X^{k-1}` (`qint`), `[n]! = ∏_{k ≤ n} [k]` (`qfact`) and
`H(s) = ∏_{c ∈ s} [hook c]` (`hookProd`). The `q`-hook formula says `H(s)` divides `[n]!`
(Stanley, EC2, §7.21; `[stanley1999]`); its quotient `g_s` is `dim_q s` up to the substitution `X = q²`
and a power of `q`. This file does **not** prove that divisibility. It proves, for any `g` with
`[n]! = g · H(s)`:

* `sum_hook`: `∑_{c ∈ s} hook c = n + N(s)` (arms and legs counted by double counting);
* `qHook_top_of_eq`: `g` is monic of degree `C(n,2) - N(s)`, and `N(s) ≤ C(n,2)`;
* `qHook_nextCoeff_of_eq`: the next coefficient of `g` is `corners(s) - 1`, where a corner is a
  cell with hook `1`;
* `coeff_sum_qHook_of_eq`: with `n = T_m + r`, `1 ≤ r ≤ m + 1`, the coefficient of
  `∑_s g_s` at degree `C(n,2) - N_min` is `C(m+1, r)`;
* `top_exponent_gap`: when `2m < n - 1`, the shapes with `n - 1` and `n - 2` cells stay strictly
  below the top exponent of `S(n)`, also after the factor `[n-1]`. So inside
  `D(n) = S(n) - S(n-1) - [n-1] S(n-2)` the top coefficient is that of `S(n)`.

The divisibility is a hypothesis of each statement (`_of_eq`), not an axiom.
-/

namespace QOU.Mass.StaircaseMinimisers

open Finset Polynomial

/-- Cells to the right of `c` in its row. -/
def arm (s : Finset (ℕ × ℕ)) (c : ℕ × ℕ) : ℕ := (s.filter (fun d => d.1 = c.1 ∧ c.2 < d.2)).card

/-- Cells below `c` in its column. -/
def leg (s : Finset (ℕ × ℕ)) (c : ℕ × ℕ) : ℕ := (s.filter (fun d => d.2 = c.2 ∧ c.1 < d.1)).card

/-- The hook length of `c` in `s`. -/
def hook (s : Finset (ℕ × ℕ)) (c : ℕ × ℕ) : ℕ := arm s c + leg s c + 1

/-- Double counting: `∑_c #{d : P c d} = ∑_d #{c : P c d}`. -/
private theorem sum_card_filter_comm (s : Finset (ℕ × ℕ)) (P : ℕ × ℕ → ℕ × ℕ → Prop)
    [∀ c d, Decidable (P c d)] :
    ∑ c ∈ s, (s.filter (fun d => P c d)).card = ∑ d ∈ s, (s.filter (fun c => P c d)).card := by
  simp only [card_eq_sum_ones, sum_filter]
  exact sum_comm

theorem sum_arm {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    ∑ c ∈ s, arm s c = ∑ d ∈ s, d.2 := by
  unfold arm
  rw [sum_card_filter_comm s (fun c d => d.1 = c.1 ∧ c.2 < d.2)]
  refine sum_congr rfl (fun d hd => ?_)
  have : s.filter (fun c => d.1 = c.1 ∧ c.2 < d.2) = (range d.2).image (fun j => (d.1, j)) := by
    ext c
    simp only [mem_filter, mem_image, mem_range]
    constructor
    · rintro ⟨-, h1, h2⟩; exact ⟨c.2, h2, by ext <;> simp [h1]⟩
    · rintro ⟨j, hj, rfl⟩
      refine ⟨hs (show ((d.1, j) : ℕ × ℕ) ≤ d from ⟨le_rfl, hj.le⟩) hd, rfl, hj⟩
  rw [this, card_image_of_injective _ (fun a b h => by simpa using h), card_range]

theorem sum_leg {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    ∑ c ∈ s, leg s c = ∑ d ∈ s, d.1 := by
  unfold leg
  rw [sum_card_filter_comm s (fun c d => d.2 = c.2 ∧ c.1 < d.1)]
  refine sum_congr rfl (fun d hd => ?_)
  have : s.filter (fun c => d.2 = c.2 ∧ c.1 < d.1) = (range d.1).image (fun i => (i, d.2)) := by
    ext c
    simp only [mem_filter, mem_image, mem_range]
    constructor
    · rintro ⟨-, h1, h2⟩; exact ⟨c.1, h2, by ext <;> simp [h1]⟩
    · rintro ⟨i, hi, rfl⟩
      refine ⟨hs (show ((i, d.2) : ℕ × ℕ) ≤ d from ⟨hi.le, le_rfl⟩) hd, rfl, hi⟩
  rw [this, card_image_of_injective _ (fun a b h => by simpa using h), card_range]

/-- **Hook sum.** For a Young diagram, `∑ hook = n + N(s)`. -/
theorem sum_hook {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    ∑ c ∈ s, hook s c = s.card + N s := by
  simp only [hook, sum_add_distrib, sum_arm hs, sum_leg hs, sum_const, smul_eq_mul, mul_one, N, val]
  ring

/-- `[k] = 1 + X + ⋯ + X^{k-1}`. -/
noncomputable def qint (k : ℕ) : ℤ[X] := ∑ i ∈ range k, X ^ i

/-- `[n]! = [1][2]⋯[n]`. -/
noncomputable def qfact (n : ℕ) : ℤ[X] := ∏ k ∈ range n, qint (k + 1)

/-- `H(s) = ∏_{c ∈ s} [hook c]`. -/
noncomputable def hookProd (s : Finset (ℕ × ℕ)) : ℤ[X] := ∏ c ∈ s, qint (hook s c)

theorem qint_monic {k : ℕ} (hk : k ≠ 0) : (qint k).Monic := monic_geom_sum_X hk

theorem qint_natDegree (k : ℕ) : (qint k).natDegree = k - 1 := by
  rcases k with _ | k
  · simp [qint]
  · rw [qint, sum_range_succ, Nat.add_sub_cancel]
    rcases k with _ | k
    · simp
    · rw [natDegree_add_eq_right_of_natDegree_lt, natDegree_X_pow]
      rw [natDegree_X_pow]
      calc (∑ i ∈ range (k + 1), (X : ℤ[X]) ^ i).natDegree ≤ k := by
            apply natDegree_sum_le_of_forall_le
            intro i hi
            rw [natDegree_X_pow]
            exact Nat.lt_succ_iff.1 (mem_range.1 hi)
        _ < k + 1 := Nat.lt_succ_self k

/-- The next coefficient of `[k]` is `1` for `k ≥ 2` and `0` for `k ≤ 1`. -/
theorem qint_nextCoeff (k : ℕ) : (qint k).nextCoeff = if 2 ≤ k then 1 else 0 := by
  rw [nextCoeff, qint_natDegree]
  rcases k with _ | _ | k
  · simp
  · simp
  · simp only [show 2 ≤ k + 2 from by omega, if_true, show k + 2 - 1 = k + 1 from by omega,
      Nat.add_one_ne_zero, if_false, qint, finset_sum_coeff, coeff_X_pow]
    rw [sum_ite_eq]
    simp only [mem_range, if_pos (show k + 1 - 1 < k + 2 by omega)]

theorem qfact_monic (n : ℕ) : (qfact n).Monic :=
  monic_prod_of_monic _ _ (fun k _ => qint_monic (Nat.succ_ne_zero k))

theorem qfact_natDegree (n : ℕ) : (qfact n).natDegree = n * (n - 1) / 2 := by
  rw [qfact, natDegree_prod_of_monic _ _ (fun k _ => qint_monic (Nat.succ_ne_zero k))]
  simp only [qint_natDegree]
  exact sum_range_id n

theorem hook_pos (s : Finset (ℕ × ℕ)) (c : ℕ × ℕ) : 1 ≤ hook s c := by
  simp [hook]

theorem hookProd_monic (s : Finset (ℕ × ℕ)) : (hookProd s).Monic :=
  monic_prod_of_monic _ _ (fun c _ => qint_monic (by have := hook_pos s c; omega))

theorem hookProd_natDegree {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    (hookProd s).natDegree = N s := by
  rw [hookProd, natDegree_prod_of_monic _ _
    (fun c _ => qint_monic (by have := hook_pos s c; omega))]
  simp only [qint_natDegree]
  have h := sum_hook hs
  have h2 : ∑ c ∈ s, (hook s c - 1) + ∑ c ∈ s, 1 = ∑ c ∈ s, hook s c := by
    rw [← sum_add_distrib]
    exact sum_congr rfl (fun c _ => Nat.sub_add_cancel (hook_pos s c))
  simp only [sum_const, smul_eq_mul, mul_one] at h2
  omega

/-- **Top term of the `q`-hook quotient.** If `[n]! = g · H(s)` for a Young diagram `s` with
`n` cells, then `g` is monic of degree `C(n,2) - N(s)`. -/
theorem qHook_top_of_eq {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ)))
    {g : ℤ[X]} (hg : qfact s.card = g * hookProd s) :
    g.Monic ∧ g.natDegree = s.card * (s.card - 1) / 2 - N s ∧ N s ≤ s.card * (s.card - 1) / 2 := by
  have hgm : g.Monic := (hookProd_monic s).of_mul_monic_right (hg ▸ qfact_monic _)
  have hd := congrArg natDegree hg
  rw [qfact_natDegree, hgm.natDegree_mul (hookProd_monic s), hookProd_natDegree hs] at hd
  exact ⟨hgm, by omega, by omega⟩

/-- **Next coefficient of the `q`-hook quotient.** Under the same hypothesis, the coefficient of
`g` one below the top is `corners(s) - 1`, where the corners are the cells with hook `1`. -/
theorem qHook_nextCoeff_of_eq {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ)))
    (hne : s.Nonempty) {g : ℤ[X]} (hg : qfact s.card = g * hookProd s) :
    g.nextCoeff = ((s.filter (fun c => hook s c = 1)).card : ℤ) - 1 := by
  have hgm := (qHook_top_of_eq hs hg).1
  have h := congrArg nextCoeff hg
  rw [hgm.nextCoeff_mul (hookProd_monic s), qfact, hookProd,
    Monic.nextCoeff_prod _ _ (fun k _ => qint_monic (Nat.succ_ne_zero k)),
    Monic.nextCoeff_prod _ _ (fun c _ => qint_monic (by have := hook_pos s c; omega))] at h
  simp only [qint_nextCoeff] at h
  have hcard : 1 ≤ s.card := card_pos.2 hne
  have h1 : ∑ k ∈ range s.card, (if 2 ≤ k + 1 then (1 : ℤ) else 0) = (s.card : ℤ) - 1 := by
    rw [← sum_filter, sum_const, nsmul_eq_mul, mul_one]
    have : (range s.card).filter (fun k => 2 ≤ k + 1) = (range s.card).erase 0 := by
      ext k; simp only [mem_filter, mem_range, mem_erase]; omega
    rw [this, card_erase_of_mem (mem_range.2 hcard), card_range]
    push_cast [hcard]; ring
  have h2 : ∑ c ∈ s, (if 2 ≤ hook s c then (1 : ℤ) else 0) =
      (s.card : ℤ) - (s.filter (fun c => hook s c = 1)).card := by
    rw [← sum_filter, sum_const, nsmul_eq_mul, mul_one]
    have := filter_card_add_filter_neg_card_eq_card (s := s) (fun c => hook s c = 1)
    have e : s.filter (fun c => 2 ≤ hook s c) = s.filter (fun c => ¬ hook s c = 1) := by
      ext c
      simp only [mem_filter]
      have := hook_pos s c
      constructor <;> rintro ⟨h1, h2⟩ <;> exact ⟨h1, by omega⟩
    rw [e]; push_cast [← this]; ring
  rw [h1, h2] at h
  linarith

/-- **Leading coefficient of `∑_s g_s`.** For `n = T_m + r` with `1 ≤ r ≤ m + 1`, if
`[n]! = g_s · H(s)` for every Young diagram `s` with `n` cells, then the coefficient of
`∑_s g_s` at degree `C(n,2) - N_min` is `C(m+1, r)`. -/
theorem coeff_sum_qHook_of_eq {m r : ℕ} (hr1 : 1 ≤ r) (hr : r ≤ m + 1)
    (g : Finset (ℕ × ℕ) → ℤ[X])
    (hg : ∀ s ∈ shapes ((stair m).card + r), qfact ((stair m).card + r) = g s * hookProd s) :
    (∑ s ∈ shapes ((stair m).card + r), g s).coeff
        (((stair m).card + r) * ((stair m).card + r - 1) / 2 - (N (stair m) + r * m)) =
      ((m + 1).choose r : ℤ) := by
  have key : ∀ s ∈ shapes ((stair m).card + r), (g s).Monic ∧
      (g s).natDegree = ((stair m).card + r) * ((stair m).card + r - 1) / 2 - N s ∧
      N s ≤ ((stair m).card + r) * ((stair m).card + r - 1) / 2 := by
    intro s hs
    obtain ⟨-, hcard, hlow⟩ := mem_shapes.1 hs
    have := qHook_top_of_eq hlow (g := g s) (by rw [hcard]; exact hg s hs)
    rwa [hcard] at this
  refine coeff_sum_shapes_of_top hr1 hr g _ (fun s hs => (key s hs).2.2)
    (fun s hs => (key s hs).2.1.le) (fun s hs => ?_)
  rw [← (key s hs).2.1]
  exact (key s hs).1.leadingCoeff

end QOU.Mass.StaircaseMinimisers

namespace QOU.Mass.StaircaseMinimisers

open Finset

/-- **Degree check inside `D(n)`.** Let `n = k + 2 = T_m + r` with `1 ≤ r ≤ m + 1` and
`2m < k + 1`. In the balanced variable `q`, `dim_q λ` has top exponent `C(|λ|, 2) - N(λ)`.
Every shape `s'` with `n - 1` cells and every shape `s''` with `n - 2` cells stays strictly
below the top exponent `C(n,2) - N_min(n)` of `S(n)`, also after the factor `[n-1]`, whose top
exponent is `n - 2 = k`. So `S(n-1)` and `[n-1] S(n-2)` do not reach the top degree of `S(n)`. -/
theorem top_exponent_gap {m r k : ℕ} (hr1 : 1 ≤ r) (hr : r ≤ m + 1)
    (hn : (stair m).card + r = k + 2) (hm : 2 * m < k + 1)
    {s' s'' : Finset (ℕ × ℕ)} (hs' : s'.card = k + 1) (hs'' : s''.card = k) :
    ((k + 1).choose 2 : ℤ) - N s' < ((k + 2).choose 2 : ℤ) - (N (stair m) + r * m) ∧
      (k : ℤ) + (k.choose 2 : ℤ) - N s'' < ((k + 2).choose 2 : ℤ) - (N (stair m) + r * m) := by
  have c2 : ((k + 2).choose 2 : ℤ) = (k + 1 : ℤ) + ((k + 1).choose 2 : ℤ) := by
    rw [Nat.choose_succ_succ, Nat.choose_one_right]; push_cast; ring
  have c1 : ((k + 1).choose 2 : ℤ) = (k : ℤ) + (k.choose 2 : ℤ) := by
    rw [Nat.choose_succ_succ, Nat.choose_one_right]; push_cast; ring
  -- `N s' ≥ N(stair m) + (r - 1) m`
  have h1 : N (stair m) + (r - 1) * m ≤ N s' :=
    le_N_of_card (by omega) (by omega)
  -- `N s'' ≥ N(stair m) + r m - 2m`
  have h2 : (N (stair m) : ℤ) + r * m - 2 * m ≤ N s'' := by
    rcases Nat.lt_or_ge r 2 with hr2 | hr2
    · -- `r = 1`: `s''` has `T_{m-1} + (m - 1)` cells
      have hr1' : r = 1 := by omega
      subst hr1'
      rcases m with _ | m
      · simp [stair] at hn
      · have hc : (stair (m + 1)).card = (stair m).card + (m + 1) := by
          have := two_mul_card_stair m
          have := two_mul_card_stair (m + 1)
          nlinarith
        have := le_N_of_card (m := m) (r := m) (by omega) (s := s'') (by omega)
        have hst := N_stair_succ m
        push_cast at this hst ⊢
        nlinarith
    · have := le_N_of_card (m := m) (r := r - 2) (by omega) (s := s'') (by omega)
      have e : ((r - 2 : ℕ) : ℤ) = r - 2 := by push_cast [Nat.cast_sub hr2]; ring
      have := (Nat.cast_le (α := ℤ)).2 this
      push_cast [e] at this
      nlinarith
  have h1' := (Nat.cast_le (α := ℤ)).2 h1
  have e1 : ((r - 1 : ℕ) : ℤ) = r - 1 := by push_cast [Nat.cast_sub hr1]; ring
  push_cast [e1] at h1'
  have hm' : (2 * m : ℤ) < k + 1 := by exact_mod_cast hm
  constructor <;> nlinarith

end QOU.Mass.StaircaseMinimisers
