import QOU.Hecke.TwistedChannelSplitting

/-!
# The sign of the spin-only twist split, as a function of the two unfixed conventions

`TwistedChannelSplitting` proves that a twist acting on the spin factor only splits the deuteron
channel `D = tr(θ p)·tr p'` from the singlet channel `S = tr(θ p')·tr p` by
`D − S = (s − s')·tr p·tr p'`, where `p`, `p'` are the `(4,2)` and `(3,3)` blocks and `s`, `s'`
the twist's eigenvalues on them.  Whether the deuteron then binds **more** than the singlet
depends on two inputs that the corpus does **not** fix (corpus-grep, 2026-10-11):

1. **The twist orientation.**  The corpus fixes that the *positive* full twist
   `Δ² = (σ₁⋯σ_{n−1})ⁿ` — a positive braid word under the convention `σᵢ = L₊`,
   `(σᵢ − q)(σᵢ + q⁻¹) = 0` — acts on the block `λ` by `q^{2c(λ)}`
   (`QOU.BraidKnot.Hecke.fullTwist_smul_eq_theta_sq`, conditional on the per-element
   Jucys–Murphy eigenvalue hypothesis `IsJMWeight` for `dim V_λ > 1`; checked exactly on the
   seminormal matrices of `(4,2)` and `(3,3)` by `framing_twist_channel_split_probe.py`).  It does
   **not** fix whether the spin-only insertion is `Δ²` or `Δ⁻²` (`θ` or `θ⁻¹`): the per-strand
   framing of `strand-twist-datum` is a free integer label of either sign, negated by the bar
   involution.  Here the orientation is an explicit choice between `θ^k` and `(θ⁻¹)^k`.
2. **The trace → energy map.**  No block derives one.  The working forms — `B = −α·log μ`
   (`QOU.QBeta.InterfaceScalar`), the dashboard's `B_sym = α·ln(tr_free/tr_atom)` (tagged
   `POSITED` by its own producer: "no block in the corpus licenses `α·ln(ratio)` as an energy"),
   and the mass facade `m ∝ |tr_M|` — all make binding **decrease** as the trace grows; none is
   derived.  Here the map is an explicit hypothesis: a binding functional `B` that is either
   strictly monotone or strictly antitone on the positive traces.

The four cells (`q > 1`, positive block traces, `k ≥ 1`):

| orientation | `B` antitone (working forms) | `B` monotone |
|---|---|---|
| `θ^k` (positive twist)   | deuteron binds **less** | deuteron binds **more** |
| `(θ⁻¹)^k` (negative)     | deuteron binds **more** | deuteron binds **less** |

So the sign is the product of two unfixed signs.  This file states the dictionary; it selects
no cell.  Agreement with nature (deuteron bound, singlet unbound) is a comparison, never a
criterion for choosing a cell — doing so would be selection against the target.

Base ring: a generic linearly ordered field (§7c — the ordering `1 < q` and positivity of the
block traces are the only order-theoretic inputs).  No numerical value of `q` enters.
-/

namespace QOU.Hecke.TwistSplitSignDictionary

open QOU.Hecke.TwistedChannelSplitting QOU.BraidKnot.Keystone

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

section SplitSign

variable {A : Type*} [Ring A] [Algebra R A]

/-- If the twist's eigenvalue on the deuteron's spin block exceeds that on the singlet's, and the
block traces have positive product, then `D > S`. -/
theorem split_pos_of_lt (tr : A →ₗ[R] R) (θ p p' : A) (s s' : R)
    (h : θ * p = s • p) (h' : θ * p' = s' • p') (hs : s' < s) (htr : 0 < tr p * tr p') :
    tr (θ * p') * tr p < tr (θ * p) * tr p' := by
  have := spin_only_twist_split tr θ p p' s s' h h'
  have hpos : 0 < (s - s') * (tr p * tr p') := mul_pos (sub_pos.mpr hs) htr
  linarith

/-- If the twist's eigenvalue on the deuteron's spin block is the smaller one, then `D < S`. -/
theorem split_neg_of_lt (tr : A →ₗ[R] R) (θ p p' : A) (s s' : R)
    (h : θ * p = s • p) (h' : θ * p' = s' • p') (hs : s < s') (htr : 0 < tr p * tr p') :
    tr (θ * p) * tr p' < tr (θ * p') * tr p := by
  have := spin_only_twist_split tr θ p p' s s' h h'
  have hneg : (s - s') * (tr p * tr p') < 0 := mul_neg_of_neg_of_pos (sub_neg.mpr hs) htr
  linarith

end SplitSign

section Eigenvalues

theorem theta_three_three_pos (q : R) (hq : 0 < q) : 0 < theta q [3, 3] := by
  unfold theta
  exact zpow_pos hq _

/-- For `q > 1`, the ribbon eigenvalue on `(4,2)` exceeds that on `(3,3)`, and so does every
positive power `k` of it (`k = 1` ribbon, `k = 2` full twist). -/
theorem theta_pow_lt (q : R) (hq : 1 < q) (k : ℕ) (hk : k ≠ 0) :
    theta q [3, 3] ^ k < theta q [4, 2] ^ k := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have ht := theta_three_three_pos q hq0
  rw [theta_four_two q hq0.ne']
  have hq2 : 1 < q ^ 2 := one_lt_pow₀ hq (by norm_num)
  have hlt : theta q [3, 3] < q ^ 2 * theta q [3, 3] := by
    nlinarith
  exact pow_lt_pow_left₀ hlt ht.le hk

/-- For `q > 1`, the inverse (negative-orientation) twist reverses the order. -/
theorem theta_inv_pow_lt (q : R) (hq : 1 < q) (k : ℕ) (hk : k ≠ 0) :
    (theta q [4, 2])⁻¹ ^ k < (theta q [3, 3])⁻¹ ^ k := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have h33 := theta_three_three_pos q hq0
  have h42 : 0 < theta q [4, 2] := by
    rw [theta_four_two q hq0.ne']; positivity
  have hlt1 : theta q [3, 3] < theta q [4, 2] := by
    simpa using theta_pow_lt q hq 1 one_ne_zero
  have hinv : (theta q [4, 2])⁻¹ < (theta q [3, 3])⁻¹ := (inv_lt_inv₀ h42 h33).mpr hlt1
  exact pow_lt_pow_left₀ hinv (inv_pos.mpr h42).le hk

end Eigenvalues

section Orientation

variable {A : Type*} [Ring A] [Algebra R A]

/-- **Positive orientation.**  A spin-only twist acting by `θ_λ^k` (`k ≥ 1`) makes the deuteron
channel trace the larger: `S < D`. -/
theorem positive_twist_D_gt_S (tr : A →ₗ[R] R) (θ p p' : A) (q : R) (hq : 1 < q)
    (k : ℕ) (hk : k ≠ 0)
    (h : θ * p = theta q [4, 2] ^ k • p) (h' : θ * p' = theta q [3, 3] ^ k • p')
    (htr : 0 < tr p * tr p') :
    tr (θ * p') * tr p < tr (θ * p) * tr p' :=
  split_pos_of_lt tr θ p p' _ _ h h' (theta_pow_lt q hq k hk) htr

/-- **Negative orientation.**  A spin-only twist acting by `θ_λ^{−k}` makes the deuteron channel
trace the smaller: `D < S`. -/
theorem negative_twist_D_lt_S (tr : A →ₗ[R] R) (θ p p' : A) (q : R) (hq : 1 < q)
    (k : ℕ) (hk : k ≠ 0)
    (h : θ * p = (theta q [4, 2])⁻¹ ^ k • p) (h' : θ * p' = (theta q [3, 3])⁻¹ ^ k • p')
    (htr : 0 < tr p * tr p') :
    tr (θ * p) * tr p' < tr (θ * p') * tr p :=
  split_neg_of_lt tr θ p p' _ _ h h' (theta_inv_pow_lt q hq k hk) htr

end Orientation

section Dictionary

/-! ## From traces to binding: the four cells

`B : R → R` is a binding functional of the channel trace (larger `B` = more bound), with the
deuteron and singlet traces `D`, `S` positive.  Its monotonicity is a hypothesis: the corpus
fixes neither direction. -/

omit [IsStrictOrderedRing R] in
/-- Antitone binding (the direction of every working form in the corpus): the larger trace binds
less. -/
theorem binds_less_of_antitone (B : R → R) (hB : StrictAntiOn B (Set.Ioi 0)) {D S : R}
    (hD : 0 < D) (hS : 0 < S) (hSD : S < D) : B D < B S :=
  hB hS hD hSD

omit [IsStrictOrderedRing R] in
/-- Monotone binding: the larger trace binds more. -/
theorem binds_more_of_monotone (B : R → R) (hB : StrictMonoOn B (Set.Ioi 0)) {D S : R}
    (hD : 0 < D) (hS : 0 < S) (hSD : S < D) : B S < B D :=
  hB hS hD hSD

variable {A : Type*} [Ring A] [Algebra R A]

/-- Cell (positive twist, antitone `B`): the deuteron binds **less** than the singlet. -/
theorem positive_antitone_deuteron_binds_less (B : R → R) (hB : StrictAntiOn B (Set.Ioi 0))
    (tr : A →ₗ[R] R) (θ p p' : A) (q : R) (hq : 1 < q) (k : ℕ) (hk : k ≠ 0)
    (h : θ * p = theta q [4, 2] ^ k • p) (h' : θ * p' = theta q [3, 3] ^ k • p')
    (htr : 0 < tr p * tr p') (hD : 0 < tr (θ * p) * tr p') (hS : 0 < tr (θ * p') * tr p) :
    B (tr (θ * p) * tr p') < B (tr (θ * p') * tr p) :=
  binds_less_of_antitone B hB hD hS (positive_twist_D_gt_S tr θ p p' q hq k hk h h' htr)

/-- Cell (negative twist, antitone `B`): the deuteron binds **more** than the singlet. -/
theorem negative_antitone_deuteron_binds_more (B : R → R) (hB : StrictAntiOn B (Set.Ioi 0))
    (tr : A →ₗ[R] R) (θ p p' : A) (q : R) (hq : 1 < q) (k : ℕ) (hk : k ≠ 0)
    (h : θ * p = (theta q [4, 2])⁻¹ ^ k • p) (h' : θ * p' = (theta q [3, 3])⁻¹ ^ k • p')
    (htr : 0 < tr p * tr p') (hD : 0 < tr (θ * p) * tr p') (hS : 0 < tr (θ * p') * tr p) :
    B (tr (θ * p') * tr p) < B (tr (θ * p) * tr p') :=
  binds_less_of_antitone B hB hS hD (negative_twist_D_lt_S tr θ p p' q hq k hk h h' htr)

/-- Cell (positive twist, monotone `B`): the deuteron binds **more** than the singlet. -/
theorem positive_monotone_deuteron_binds_more (B : R → R) (hB : StrictMonoOn B (Set.Ioi 0))
    (tr : A →ₗ[R] R) (θ p p' : A) (q : R) (hq : 1 < q) (k : ℕ) (hk : k ≠ 0)
    (h : θ * p = theta q [4, 2] ^ k • p) (h' : θ * p' = theta q [3, 3] ^ k • p')
    (htr : 0 < tr p * tr p') (hD : 0 < tr (θ * p) * tr p') (hS : 0 < tr (θ * p') * tr p) :
    B (tr (θ * p') * tr p) < B (tr (θ * p) * tr p') :=
  binds_more_of_monotone B hB hD hS (positive_twist_D_gt_S tr θ p p' q hq k hk h h' htr)

/-- Cell (negative twist, monotone `B`): the deuteron binds **less** than the singlet. -/
theorem negative_monotone_deuteron_binds_less (B : R → R) (hB : StrictMonoOn B (Set.Ioi 0))
    (tr : A →ₗ[R] R) (θ p p' : A) (q : R) (hq : 1 < q) (k : ℕ) (hk : k ≠ 0)
    (h : θ * p = (theta q [4, 2])⁻¹ ^ k • p) (h' : θ * p' = (theta q [3, 3])⁻¹ ^ k • p')
    (htr : 0 < tr p * tr p') (hD : 0 < tr (θ * p) * tr p') (hS : 0 < tr (θ * p') * tr p) :
    B (tr (θ * p) * tr p') < B (tr (θ * p') * tr p) :=
  binds_more_of_monotone B hB hS hD (negative_twist_D_lt_S tr θ p p' q hq k hk h h' htr)

end Dictionary

end QOU.Hecke.TwistSplitSignDictionary
