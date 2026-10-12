import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.LinearCombination
import QOU.BraidKnot.KeystoneModularTwist

/-!
# A twist splits the deuteron from the singlet only if it tells spin from isospin

Setting (bean `qou-ulj0`, stepping stone 4 of `qou-slz5`).  Six-quark Schur–Weyl: two-nucleon
spin `S` sits on the two-row block `(3+S, 3−S)` of `H₆(q)`, isospin `T` likewise.  The two
Pauli-allowed S-wave channels exchange the shapes between the two factors:

  deuteron `(S,T) = (1,0)`:  spin `(4,2)` ⊗ isospin `(3,3)`
  singlet  `(S,T) = (0,1)`:  spin `(3,3)` ⊗ isospin `(4,2)`

With one trace `tr` on both copies and block elements `p` (shape `(4,2)`), `p'` (shape `(3,3)`),
the two channels have the same trace `tr p · tr p'` — the Pauli lock of bean `qou-7zob`, and the
equal-trace case of `QOU.Hecke.ChannelSwapSplitting.tr_swap_sub`.

Insert a twist `θS` on the spin factor and `θI` on the isospin factor, each acting on the two
blocks by scalars (`θS p = s p`, `θS p' = s' p'`, `θI p = i p`, `θI p' = i' p'`; a central
element of a semisimple Hecke algebra acts this way).  Then (`twisted_split`)

  `tr(θS p)·tr(θI p') − tr(θS p')·tr(θI p) = (s i' − s' i) · tr p · tr p'`.

The split is the 2×2 determinant of the two factors' twist eigenvalues.  So:

* a twist that acts the same way on both factors (`θS = θI`, the ribbon structure of a single
  braided category applied to the whole tensor product) **never** splits the channels
  (`symmetric_twist_no_split`);
* a twist on the spin factor only (`θI = 1`) splits them by `(s − s')·tr p·tr p'`
  (`spin_only_twist_split`); over a domain with non-zero block traces, the split vanishes
  iff `s = s'` (`spin_only_twist_split_eq_zero_iff`).

For the ribbon twist `θ_λ = q^{c(λ)}` (`QOU.BraidKnot.Keystone.theta`), the content sum of a
two-row shape is a Casimir plus an `n`-dependent constant (`four_mul_contentSum_pair`):

  `4 c(a, b) = (a − b)(a − b + 2) + (a + b)(a + b − 4)`,   i.e.  `c = S(S+1) + n(n−4)/4`,

so between two shapes of the same size the twist ratio depends only on the spins
(`theta_pair_pow_four_ratio`).  At `n = 6`: `c(4,2) = 5`, `c(3,3) = 3`, `θ_{(4,2)} = q² θ_{(3,3)}`,
and the spin-only ribbon twist splits the channels by `(q⁵ − q³)·tr p·tr p'`
(`six_strand_spin_twist_split`).

## What this does and does not establish

Proved: the split identity, the symmetric-twist degeneracy (scope (b): the invariant is
`s i' = s' i`), and the Casimir form of the two-row twist ratio.

**Not** proved here, and not derived anywhere in the corpus as of this file: that the ribbon twist
acts on the spin factor and *not* on the isospin factor.  That asymmetry is the content of the
spin-statistics reading of framing; inside a single ribbon category it is false (the natural twist
acts on every object).  It is the hypothesis `θI = 1` of `spin_only_twist_split`, stated as such.

The base ring is generic (`CommRing` / `Field`, §7c).  No numerical value of `q` enters.
-/

namespace QOU.Hecke.TwistedChannelSplitting

open Finset QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.Keystone

section Split

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **Twisted channel split.**  With twists acting by scalars on the two blocks, the deuteron
minus the singlet is the 2×2 determinant of the twist eigenvalues times the two block traces. -/
theorem twisted_split (tr : A →ₗ[R] R) (θS θI p p' : A) (s s' i i' : R)
    (hS : θS * p = s • p) (hS' : θS * p' = s' • p')
    (hI : θI * p = i • p) (hI' : θI * p' = i' • p') :
    tr (θS * p) * tr (θI * p') - tr (θS * p') * tr (θI * p)
      = (s * i' - s' * i) * (tr p * tr p') := by
  rw [hS, hS', hI, hI', map_smul, map_smul, map_smul, map_smul]
  simp only [smul_eq_mul]
  ring

/-- **A twist acting the same way on both factors cannot split the channels.**  This is the
Pauli lock of bean `qou-7zob` surviving any twist that does not distinguish spin from isospin. -/
theorem symmetric_twist_no_split (tr : A →ₗ[R] R) (θ p p' : A) (s s' : R)
    (h : θ * p = s • p) (h' : θ * p' = s' • p') :
    tr (θ * p) * tr (θ * p') - tr (θ * p') * tr (θ * p) = 0 := by
  rw [twisted_split tr θ θ p p' s s' s s' h h' h h']
  ring

/-- **Spin-only twist.**  With the isospin factor untwisted, the split is `(s − s')·tr p·tr p'`. -/
theorem spin_only_twist_split (tr : A →ₗ[R] R) (θ p p' : A) (s s' : R)
    (h : θ * p = s • p) (h' : θ * p' = s' • p') :
    tr (θ * p) * tr p' - tr (θ * p') * tr p = (s - s') * (tr p * tr p') := by
  have := twisted_split tr θ 1 p p' s s' 1 1 h h' (by simp) (by simp)
  simpa using this

/-- Over a domain with non-zero block traces, a spin-only twist splits the channels exactly when
its two eigenvalues differ. -/
theorem spin_only_twist_split_eq_zero_iff [IsDomain R] (tr : A →ₗ[R] R) (θ p p' : A) (s s' : R)
    (h : θ * p = s • p) (h' : θ * p' = s' • p') (hp : tr p ≠ 0) (hp' : tr p' ≠ 0) :
    tr (θ * p) * tr p' - tr (θ * p') * tr p = 0 ↔ s = s' := by
  rw [spin_only_twist_split tr θ p p' s s' h h']
  constructor
  · intro hz
    rcases mul_eq_zero.mp hz with h0 | h0
    · exact sub_eq_zero.mp h0
    · exact absurd h0 (mul_ne_zero hp hp')
  · intro hss
    rw [hss, sub_self, zero_mul]

end Split

section Casimir

/-- `2 · Σ_{j<m} (j − i) = m(m−1) − 2 i m`. -/
theorem two_mul_sum_range_sub (m i : ℕ) :
    2 * ∑ j ∈ Finset.range m, ((j : ℤ) - (i : ℤ)) = (m : ℤ) * ((m : ℤ) - 1) - 2 * i * m := by
  induction m with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    push_cast
    ring

/-- **Two-row content sum.**  `2 c(a, b) = a(a−1) + b(b−3)`. -/
theorem two_mul_contentSum_pair (a b : ℕ) :
    2 * contentSum [a, b] = (a : ℤ) * ((a : ℤ) - 1) + (b : ℤ) * ((b : ℤ) - 3) := by
  rw [contentSum_eq_finset]
  simp only [List.length_cons, List.length_nil, Finset.sum_range_succ, Finset.sum_range_zero,
    zero_add, List.getD_cons_zero, List.getD_cons_succ, cellContent]
  have h0 := two_mul_sum_range_sub a 0
  have h1 := two_mul_sum_range_sub b 1
  push_cast at h0 h1 ⊢
  linear_combination h0 + h1

/-- **The two-row twist exponent is a Casimir plus a size constant.**
`4 c(a, b) = (a − b)(a − b + 2) + (a + b)(a + b − 4)`; with `2S = a − b`, `n = a + b`, this is
`c = S(S+1) + n(n−4)/4`. -/
theorem four_mul_contentSum_pair (a b : ℕ) :
    4 * contentSum [a, b]
      = ((a : ℤ) - b) * ((a : ℤ) - b + 2) + ((a : ℤ) + b) * ((a : ℤ) + b - 4) := by
  linear_combination 2 * two_mul_contentSum_pair a b

theorem contentSum_four_two : contentSum [4, 2] = 5 := by
  have := two_mul_contentSum_pair 4 2
  push_cast at this
  omega

theorem contentSum_three_three : contentSum [3, 3] = 3 := by
  have := two_mul_contentSum_pair 3 3
  push_cast at this
  omega

variable {R : Type*} [Field R]

/-- **Twist ratio between two shapes of the same size depends only on the spins.**
For `a + b = a' + b'`, `θ_{(a,b)}⁴ = θ_{(a',b')}⁴ · q^{(a−b)(a−b+2) − (a'−b')(a'−b'+2)}`. -/
theorem theta_pair_pow_four_ratio (q : R) (hq : q ≠ 0) (a b a' b' : ℕ) (hn : a + b = a' + b') :
    theta q [a, b] ^ 4 = theta q [a', b'] ^ 4
      * q ^ (((a : ℤ) - b) * ((a : ℤ) - b + 2) - ((a' : ℤ) - b') * ((a' : ℤ) - b' + 2)) := by
  unfold theta
  rw [← zpow_natCast, ← zpow_natCast, ← zpow_mul, ← zpow_mul, ← zpow_add₀ hq]
  congr 1
  have h := four_mul_contentSum_pair a b
  have h' := four_mul_contentSum_pair a' b'
  have hn' : ((a : ℤ) + b) = ((a' : ℤ) + b') := by exact_mod_cast hn
  push_cast
  rw [hn'] at h
  linear_combination h - h'

/-- At six strands the deuteron's spin shape is twisted by `q²` relative to the singlet's. -/
theorem theta_four_two (q : R) (hq : q ≠ 0) : theta q [4, 2] = q ^ 2 * theta q [3, 3] := by
  unfold theta
  rw [contentSum_four_two, contentSum_three_three,
    show (5 : ℤ) = 2 + 3 by norm_num, zpow_add₀ hq]
  norm_cast

/-- **Six-strand spin-only ribbon twist.**  If the ribbon twist `θ_λ = q^{c(λ)}` acts on the spin
factor only, the deuteron minus the singlet is `(q⁵ − q³)·tr p·tr p'`, where `p`, `p'` are the
`(4,2)` and `(3,3)` blocks. -/
theorem six_strand_spin_twist_split {A : Type*} [Ring A] [Algebra R A]
    (tr : A →ₗ[R] R) (θ p p' : A) (q : R)
    (h : θ * p = theta q [4, 2] • p) (h' : θ * p' = theta q [3, 3] • p') :
    tr (θ * p) * tr p' - tr (θ * p') * tr p = (q ^ 5 - q ^ 3) * (tr p * tr p') := by
  rw [spin_only_twist_split tr θ p p' _ _ h h']
  unfold theta
  rw [contentSum_four_two, contentSum_three_three]
  norm_cast

/-- The six-strand spin-only split vanishes (non-zero traces, `q ≠ 0`) iff `q² = 1`: it is a pure
`q`-deformation effect, absent at `q = 1`. -/
theorem six_strand_spin_twist_split_eq_zero_iff {A : Type*} [Ring A] [Algebra R A]
    (tr : A →ₗ[R] R) (θ p p' : A) (q : R) (hq : q ≠ 0)
    (h : θ * p = theta q [4, 2] • p) (h' : θ * p' = theta q [3, 3] • p')
    (hp : tr p ≠ 0) (hp' : tr p' ≠ 0) :
    tr (θ * p) * tr p' - tr (θ * p') * tr p = 0 ↔ q ^ 2 = 1 := by
  rw [six_strand_spin_twist_split tr θ p p' q h h']
  have hf : q ^ 5 - q ^ 3 = q ^ 3 * (q ^ 2 - 1) := by ring
  rw [hf]
  constructor
  · intro hz
    rcases mul_eq_zero.mp hz with h0 | h0
    · rcases mul_eq_zero.mp h0 with h1 | h1
      · exact absurd (pow_eq_zero_iff (by norm_num) |>.mp h1) hq
      · exact sub_eq_zero.mp h1
    · exact absurd h0 (mul_ne_zero hp hp')
  · intro h2
    rw [h2, sub_self, mul_zero, zero_mul]

end Casimir

end QOU.Hecke.TwistedChannelSplitting
