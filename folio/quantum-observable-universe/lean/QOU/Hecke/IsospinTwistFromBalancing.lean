import QOU.Hecke.TwistedChannelSplitting
import QOU.BraidKnot.KeystoneJucysMurphyTwist

/-!
# The balancing axiom fixes the isospin twist by the isospin braiding

`TwistedChannelSplitting.spin_only_twist_split` assumes the twist acts on the spin factor and
**not** on the isospin factor (`θ_iso = 1`).  Nothing in the corpus derives that.  This file asks
whether the ribbon axioms can, and answers: they fix the isospin twist **up to one strand scalar**
from the isospin **braiding**, so the hypothesis is not free to be chosen.

## The balancing axiom, at block level

In a ribbon category the twist obeys `θ_{X⊗Y} = c_{Y,X} c_{X,Y} (θ_X ⊗ θ_Y)` (balancing).
Iterated over `n` strands of one object `V`, it reads `θ_{V^{⊗n}} = Δ² ∘ θ_V^{⊗n}`, where `Δ²` is
the full twist of `B_n` acting through the braiding.  On a block `λ` (an isotypic summand, where
the central `Δ²` acts by a scalar `f_λ`) the twist is therefore

    θ|_λ = τⁿ · f_λ,      τ := the scalar of θ_V on the strand.

We carry this as an explicit hypothesis shape (`i = τ⁶ f`, `i' = τ⁶ f'`) and cite it; it is the
standard consequence of the balancing axiom, not proved here from a ribbon-category structure,
since Mathlib carries no ribbon categories.

## What follows, proved here

* `balanced_split` — with both factors balanced, `D − S = σ⁶ τ⁶ (g f' − g' f) tr p tr p'`.  The
  strand scalars factor out; only the full-twist scalars of the two factors survive.
* `balanced_iso_eq_iff` — the isospin twist is the **same scalar on both channels** (`i = i'`,
  which is all a spin-only split needs: `D − S = i (s − s') tr p tr p'`) **iff** the isospin full
  twist does not tell `(4,2)` from `(3,3)`.  No strand twist `τ` can rescue it.
* `hecke_balanced_split` — if each factor braids by the corpus Hecke convention
  `(σ − x)(σ + x⁻¹) = 0` (spin at `x = q`, isospin at `x = t`), and the full twist acts on block
  `λ` by `θ_λ² = x^{2c(λ)}` (the Jucys–Murphy spectrum, the corpus's named open input
  `JucysMurphySpectrum`, `-- Ref: [wenzl1988]`), then

      D − S = σ⁶ τ⁶ · q⁶ t⁶ (q⁴ − t⁴) · tr p · tr p'.

* `hecke_same_parameter_no_split` — **at `t = q` the split vanishes.**  The corpus grades isospin
  by the Hecke projectors `P±` of the same `H_n(q₀)` (audit 2026-08-16, *interface graded by T₃*,
  §4), i.e. it puts isospin at `t = q`.  Under that structure balancing **forces** `D = S`: the
  hypothesis `θ_iso = 1` is not merely underived, it is inconsistent with the ribbon axioms.
* `hecke_iso_eq_iff` — the isospin twist is channel-blind iff `t⁴ = 1`.
* `transparent_iso_split` and `hecke_transparent_iff` — the Müger-centre route.  If isospin is
  transparent (trivial monodromy, so its full twist acts by `1` on every block), balancing gives
  `i = i' = τ⁶` and the split is `τ⁶ (s − s') tr p tr p'`: the spin-only form, **derived**.  But
  under the Hecke braiding transparency holds iff `t² = 1` — isospin at a classical point,
  braiding by the symmetric (`t = 1`) or super-symmetric (`t = −1`) permutation action.

## The convention point this exposes

`theta_four_two_sq_ratio`: with the corpus identification `Δ²|_λ = θ_λ²`
(`fullTwist_eq_theta_sq`, `theta_single_row_sq`), the balancing twist ratio between `(4,2)` and
`(3,3)` is `q⁴`, not the `q²` of `θ_λ = q^{c(λ)}`.  So if the twist of
`TwistedChannelSplitting.six_strand_spin_twist_split` is meant to be the **ribbon** twist of the
corpus Hecke braiding, the spin-only split is `σ⁶ (q¹⁰ − q⁶)`, ratio `D/S = q⁴`
(`hecke_spin_only_split`); `D/S = q²` corresponds to the half-twist convention `θ = q^{c}`.
This file does not decide which is meant; it records that the two differ.

## Verdict, scoped

* **Derived (conditional on the JM spectrum):** inside the corpus's own structure — one Hecke
  braiding at `q` on both factors — the balancing axiom forces `D = S`.  This is a scope-(b)
  exclusion of `θ_iso = 1` **for that structure**; the invariant is balancing plus
  `q⁴ − t⁴ = 0`.
* **Not derived:** a structure in which isospin braids at a classical point (`t² = 1`, e.g. a
  Deligne product `C_spin ⊠ Rep(SU(2))` with isospin Tannakian).  Such a structure *would* derive
  the spin-only split (`transparent_iso_split`), but the corpus does not contain it — and adopting
  it because it splits the channels would be selection against the target.

Base ring: generic `CommRing` for the split algebra (§7c); `Field` only where the Jucys–Murphy
class and `zpow` require it.  No numerical value of `q` enters.

Refs:
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors, §2.2 (balancing axiom).
- [turaev2010] Quantum Invariants of Knots and 3-Manifolds, I.1 (ribbon categories, twist).
- [deligne1990] Catégories tannakiennes (symmetric categories with trivial twist).
- [wenzl1988] Hecke algebra representations (Jucys–Murphy spectrum).
-/

namespace QOU.Hecke.IsospinTwistFromBalancing

open QOU.Hecke.TwistedChannelSplitting QOU.BraidKnot.Keystone QOU.MathlibExt.QPartitionCombinatorics

section Balanced

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **Both factors balanced.**  Spin twist eigenvalues `s = σ⁶ g`, `s' = σ⁶ g'` and isospin twist
eigenvalues `i = τ⁶ f`, `i' = τ⁶ f'` (balancing on six strands: strand scalar to the sixth times
the full-twist scalar on the block).  The strand scalars factor out of the split. -/
theorem balanced_split (tr : A →ₗ[R] R) (θS θI p p' : A) (σ τ g g' f f' : R)
    (hS : θS * p = (σ ^ 6 * g) • p) (hS' : θS * p' = (σ ^ 6 * g') • p')
    (hI : θI * p = (τ ^ 6 * f) • p) (hI' : θI * p' = (τ ^ 6 * f') • p') :
    tr (θS * p) * tr (θI * p') - tr (θS * p') * tr (θI * p)
      = σ ^ 6 * τ ^ 6 * (g * f' - g' * f) * (tr p * tr p') := by
  rw [twisted_split tr θS θI p p' _ _ _ _ hS hS' hI hI']
  ring

/-- **The isospin twist is channel-blind iff its full twist is.**  A spin-only split needs only
`i = i'` (then `D − S = i (s − s') tr p tr p'`).  Under balancing, `i = i'` holds exactly when the
isospin full-twist scalars agree; the strand scalar `τ` cannot supply it. -/
theorem balanced_iso_eq_iff [IsDomain R] (τ f f' : R) (hτ : τ ≠ 0) :
    τ ^ 6 * f = τ ^ 6 * f' ↔ f = f' := by
  constructor
  · intro h
    exact mul_left_cancel₀ (pow_ne_zero 6 hτ) h
  · intro h
    rw [h]

/-- **Transparent isospin derives the spin-only form.**  If the isospin monodromy is trivial, the
full twist acts by `1` on both isospin blocks; balancing then makes the isospin twist the single
scalar `τ⁶`, and the split is `τ⁶ (s − s') tr p tr p'` — the shape of `spin_only_twist_split`. -/
theorem transparent_iso_split (tr : A →ₗ[R] R) (θS θI p p' : A) (s s' τ : R)
    (hS : θS * p = s • p) (hS' : θS * p' = s' • p')
    (hI : θI * p = (τ ^ 6 * 1) • p) (hI' : θI * p' = (τ ^ 6 * 1) • p') :
    tr (θS * p) * tr (θI * p') - tr (θS * p') * tr (θI * p)
      = τ ^ 6 * (s - s') * (tr p * tr p') := by
  rw [twisted_split tr θS θI p p' _ _ _ _ hS hS' hI hI']
  ring

end Balanced

section Hecke

variable {R : Type*} [Field R]

/-- `θ_{(4,2)}² = x¹⁰`: the full-twist scalar on `(4,2)` under the JM spectrum. -/
theorem theta_four_two_sq (x : R) : theta x [4, 2] ^ 2 = x ^ 10 := by
  unfold theta
  rw [contentSum_four_two, ← zpow_natCast, ← zpow_mul,
    show (5 : ℤ) * ((2 : ℕ) : ℤ) = ((10 : ℕ) : ℤ) by norm_num, zpow_natCast]

/-- `θ_{(3,3)}² = x⁶`. -/
theorem theta_three_three_sq (x : R) : theta x [3, 3] ^ 2 = x ^ 6 := by
  unfold theta
  rw [contentSum_three_three, ← zpow_natCast, ← zpow_mul,
    show (3 : ℤ) * ((2 : ℕ) : ℤ) = ((6 : ℕ) : ℤ) by norm_num, zpow_natCast]

/-- **The balancing ratio is `q⁴`, not `q²`.**  With the corpus identification
`Δ²|_λ = θ_λ²`, the full-twist scalar on `(4,2)` is `q⁴` times that on `(3,3)`. -/
theorem theta_four_two_sq_ratio (x : R) :
    theta x [4, 2] ^ 2 = x ^ 4 * theta x [3, 3] ^ 2 := by
  rw [theta_four_two_sq, theta_three_three_sq]
  ring

variable {A : Type*} [Ring A] [Algebra R A]

/-- **Both factors braided by the Hecke relation, at parameters `q` (spin) and `t` (isospin).**
Given the Jucys–Murphy spectrum on each block (the corpus's named, cited open input), balancing
gives `D − S = σ⁶ τ⁶ q⁶ t⁶ (q⁴ − t⁴) tr p tr p'`. -/
theorem hecke_balanced_split (tr : A →ₗ[R] R) (θS θI p p' : A) (q t σ τ g g' f f' : R)
    (hq : q ≠ 0) (ht : t ≠ 0)
    [JucysMurphySpectrum R q [4, 2] 6 g] [JucysMurphySpectrum R q [3, 3] 6 g']
    [JucysMurphySpectrum R t [4, 2] 6 f] [JucysMurphySpectrum R t [3, 3] 6 f']
    (hS : θS * p = (σ ^ 6 * g) • p) (hS' : θS * p' = (σ ^ 6 * g') • p')
    (hI : θI * p = (τ ^ 6 * f) • p) (hI' : θI * p' = (τ ^ 6 * f') • p') :
    tr (θS * p) * tr (θI * p') - tr (θS * p') * tr (θI * p)
      = σ ^ 6 * τ ^ 6 * (q ^ 6 * t ^ 6 * (q ^ 4 - t ^ 4)) * (tr p * tr p') := by
  rw [balanced_split tr θS θI p p' σ τ g g' f f' hS hS' hI hI',
    fullTwist_eq_theta_sq q hq [4, 2] 6 g, fullTwist_eq_theta_sq q hq [3, 3] 6 g',
    fullTwist_eq_theta_sq t ht [4, 2] 6 f, fullTwist_eq_theta_sq t ht [3, 3] 6 f',
    theta_four_two_sq, theta_three_three_sq, theta_four_two_sq, theta_three_three_sq]
  ring

/-- **One Hecke braiding on both factors forces `D = S`.**  The corpus grades isospin by the
Hecke projectors of the same `H_n(q)` that carry spin; with `t = q`, balancing kills the split
whatever the strand scalars.  So `θ_iso = 1` is inconsistent with the ribbon axioms there. -/
theorem hecke_same_parameter_no_split (tr : A →ₗ[R] R) (θS θI p p' : A) (q σ τ g g' f f' : R)
    (hq : q ≠ 0)
    [JucysMurphySpectrum R q [4, 2] 6 g] [JucysMurphySpectrum R q [3, 3] 6 g']
    [JucysMurphySpectrum R q [4, 2] 6 f] [JucysMurphySpectrum R q [3, 3] 6 f']
    (hS : θS * p = (σ ^ 6 * g) • p) (hS' : θS * p' = (σ ^ 6 * g') • p')
    (hI : θI * p = (τ ^ 6 * f) • p) (hI' : θI * p' = (τ ^ 6 * f') • p') :
    tr (θS * p) * tr (θI * p') - tr (θS * p') * tr (θI * p) = 0 := by
  rw [hecke_balanced_split tr θS θI p p' q q σ τ g g' f f' hq hq hS hS' hI hI']
  ring

/-- **The isospin twist is channel-blind iff `t⁴ = 1`.**  Under the Hecke braiding at `t` and the
JM spectrum, `i = i'` (for a non-zero strand scalar) holds exactly when `t⁴ = 1`. -/
theorem hecke_iso_eq_iff (t τ f f' : R) (ht : t ≠ 0) (hτ : τ ≠ 0)
    [JucysMurphySpectrum R t [4, 2] 6 f] [JucysMurphySpectrum R t [3, 3] 6 f'] :
    τ ^ 6 * f = τ ^ 6 * f' ↔ t ^ 4 = 1 := by
  rw [balanced_iso_eq_iff τ f f' hτ, fullTwist_eq_theta_sq t ht [4, 2] 6 f,
    fullTwist_eq_theta_sq t ht [3, 3] 6 f', theta_four_two_sq, theta_three_three_sq]
  have h6 : t ^ 6 ≠ 0 := pow_ne_zero 6 ht
  constructor
  · intro h
    have : t ^ 6 * t ^ 4 = t ^ 6 * 1 := by rw [mul_one, ← pow_add]; exact h
    exact mul_left_cancel₀ h6 this
  · intro h
    rw [show t ^ 10 = t ^ 6 * t ^ 4 by ring, h, mul_one]

/-- **Transparency under the Hecke braiding is the classical point.**  The isospin full twist acts
trivially on both `(4,2)` and `(3,3)` iff `t² = 1`. -/
theorem hecke_transparent_iff (t f f' : R) (ht : t ≠ 0)
    [JucysMurphySpectrum R t [4, 2] 6 f] [JucysMurphySpectrum R t [3, 3] 6 f'] :
    (f = 1 ∧ f' = 1) ↔ t ^ 2 = 1 := by
  rw [fullTwist_eq_theta_sq t ht [4, 2] 6 f, fullTwist_eq_theta_sq t ht [3, 3] 6 f',
    theta_four_two_sq, theta_three_three_sq]
  constructor
  · rintro ⟨h10, h6⟩
    have h4 : t ^ 4 = 1 := by
      have : t ^ 6 * t ^ 4 = t ^ 6 * 1 := by
        rw [mul_one, ← pow_add]; norm_num [h10, h6]
      exact mul_left_cancel₀ (pow_ne_zero 6 ht) this
    have : t ^ 4 * t ^ 2 = t ^ 4 * 1 := by
      rw [mul_one, ← pow_add]; norm_num [h6, h4]
    exact mul_left_cancel₀ (pow_ne_zero 4 ht) this
  · intro h
    constructor
    · rw [show t ^ 10 = (t ^ 2) ^ 5 by ring, h, one_pow]
    · rw [show t ^ 6 = (t ^ 2) ^ 3 by ring, h, one_pow]

/-- **Spin-only, under balancing.**  Spin braided by the Hecke relation at `q`, isospin at the
classical point `t = 1`: the split is `σ⁶ τ⁶ (q¹⁰ − q⁶) tr p tr p'`, i.e. `D/S = q⁴` — not the
`q⁵ − q³` (`D/S = q²`) of the half-twist convention `θ_λ = q^{c(λ)}`. -/
theorem hecke_spin_only_split (tr : A →ₗ[R] R) (θS θI p p' : A) (q σ τ g g' f f' : R)
    (hq : q ≠ 0)
    [JucysMurphySpectrum R q [4, 2] 6 g] [JucysMurphySpectrum R q [3, 3] 6 g']
    [JucysMurphySpectrum R 1 [4, 2] 6 f] [JucysMurphySpectrum R 1 [3, 3] 6 f']
    (hS : θS * p = (σ ^ 6 * g) • p) (hS' : θS * p' = (σ ^ 6 * g') • p')
    (hI : θI * p = (τ ^ 6 * f) • p) (hI' : θI * p' = (τ ^ 6 * f') • p') :
    tr (θS * p) * tr (θI * p') - tr (θS * p') * tr (θI * p)
      = σ ^ 6 * τ ^ 6 * (q ^ 10 - q ^ 6) * (tr p * tr p') := by
  rw [hecke_balanced_split tr θS θI p p' q 1 σ τ g g' f f' hq one_ne_zero hS hS' hI hI']
  ring

end Hecke

end QOU.Hecke.IsospinTwistFromBalancing
