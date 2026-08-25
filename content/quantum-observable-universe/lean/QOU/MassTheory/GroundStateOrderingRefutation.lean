import Mathlib.Tactic

/-!
# QOU.MassTheory.GroundStateOrderingRefutation

**Refutation of the `A ≥ 4` clause of
[`prop:ground-state-ordering`](../../mass-theory/ground-state-ordering.md).**

The proposition claims that the arrangement minimising the quantum
dilogarithm volume `Φ_q = Σ_i log|V̂_i|` is, for `A ≥ 4`, the
*interleaved + tail-packed* one:

    ordering[k] = proton  ⟺  k odd and k < 2Z.

This file **refutes** that clause at `A = 5`, `Z = 1`, `N = 4`, where the
prescribed arrangement is `n p n n n` and the *sorted* arrangement
`p n n n n` — the one the proposition reserves for `A ≤ 3` — is strictly
better.

## The readout, and where the Markov parameter enters

The corpus builds, at each chain position `i`, the product
`M_i = Π_{j>i} T(d_ij)` of transfer factors

    T(d) = ![![h + d, 1], ![1, d]] = S + d • 1,   S = ![![h, 1], ![1, 0]],
    h = q - q⁻¹,

and reads off `V̂_i = z · (M_i) 1 0 + (M_i) 1 1`, where `z` is the Markov
parameter.  Every `T(d)` is a polynomial in the single matrix `S`, so they
all commute (`QOU.MassTheory.TransferFactorCommute`) and `M_i` depends on
the crossing coefficients **only as a multiset**.  `S` has `tr S = h`,
`det S = -1`, hence eigenvalues `λ₊ = q` and `λ₋ = -q⁻¹`
(`transferEigen_vieta` below), and `S² = h • S + 1` collapses `M_i` to
`α • 1 + β • S`.  Since `S 1 0 = 1` and `S 1 1 = 0` we have `(M_i) 1 0 = β`
and `(M_i) 1 1 = α`, so

    V̂_i = c₊ · μ₊ + c₋ · μ₋,      μ± = Π_{j>i} (λ± + d_ij),
    c₊ = (z + q⁻¹)/(q + q⁻¹),     c₋ = (q - z)/(q + q⁻¹).

**`z` enters nowhere else.**  The three crossing coefficients used by the
corpus contribute the `z`-free eigenfactor pairs

    d = 0     (pp)   :  μ₊ ·= q     μ₋ ·= -q⁻¹
    d = -h/2  (pn)   :  μ₊ ·= c     μ₋ ·= -c      ,  c = (q + q⁻¹)/2
    d = -h    (nn)   :  μ₊ ·= q⁻¹   μ₋ ·= -q

which is what `cMix`, and the `μ±` arguments in `sortedV0`…`sharedV3`
below, encode.

## Convention independence (the point of this file)

This refutation was originally written in **convention C**,
`z = √q/(q+1)`, which the owner ruling of 2026-08-15 excises in favour of
**convention D**, `z = q³/(q²+1)`.  The argument does not depend on either:
it never reads `z`'s formula.  Two facts do all the work.

* `c₊ + c₋ = 1` **identically in `z`** (`cPlus_add_cMinus`) — the two
  weights are an affine partition of unity whatever `z` is.
* The whole `A = 5` comparison collapses to the single identity
  (`readout_gap`, `weight_prod`)

      V̂₀V̂₁(prescribed) - V̂₀V̂₁(sorted) = 2·c₊·c₋·c⁴·(q⁶ - 1)/q³,
      4·c₊·c₋ = 4q(q - z)(qz + 1)/(q² + 1)².

So for `q > 1` the refutation holds **exactly when both readout weights are
positive**, i.e. exactly when `-q⁻¹ < z < q`: the Markov parameter lies
strictly between the two eigenvalues of the transfer matrix.  Convention C
and convention D both lie in that window for every `q > 1`
(`zC_lt_self`, `zD_lt_self`), with room to spare — at the proton anchor
`q₀ ≈ 1.10998` the weights are `(0.6963, 0.3037)` under C and
`(0.7527, 0.2473)` under D.

This is the same disposition as `QOU.QBeta.BraidImageEigenphaseExclusion`:
generalise over `z` carrying the shared property as a hypothesis, rather
than re-derive.  Note that nothing here substitutes `z_D` into a C-frame
*conclusion* — the generalisation happens at the point where `z` first
enters the derivation, which is the readout itself.

## What is proved here

`sorted_lt_prescribed_A5` : for every `q > 1`, every `z` with both readout
weights positive, and every `q` at which the sign condition `hU` holds, the
two chain positions at which the two arrangements differ satisfy

    |V̂₀ · V̂₁| (sorted)  <  |V̂₀ · V̂₁| (prescribed).

The remaining two positions carry **identical** readouts (`sharedV2`,
`sharedV3`), so this is exactly `Φ_q(pnnnn) < Φ_q(npnnn)`, and the
prescribed arrangement is therefore **not** the minimiser.  Nothing here is
assumed: `hU` is a plain sign condition on the sorted readout, discharged
for convention D on `1 < q ≤ 6/5` (`sortedV1_zD_nonneg`, which contains the
substrate anchor) and for convention C in the committed polynomial form
(`sortedV1_zC_eq`).

Scope note: this is a **scope-(b) structural exclusion for the clause**
— a counterexample, valid for a whole interval of `q` containing the
substrate anchor and for every admissible Markov parameter, not a "the
numbers came out wrong" scope-(a) negative.

Reference: `docs/audits/2026-08-09-ground-state-ordering-truth-value.md`;
witness `computations/ground-state-ordering-argmin-sweep.witness.json`;
convention-independence probe
`computations/probes/ground_state_ordering_convention_independence_probe.py`
(8/8 exact).
-/

namespace QOU.MassTheory.GroundStateOrderingRefutation

/-! ### The transfer matrix and its Vieta pair -/

section Vieta

variable {R : Type*} [Field R]

/-- `q` and `-q⁻¹` are exactly the roots of the characteristic polynomial
`X² - hX - 1` of the corpus transfer matrix `S = ![![h,1],![1,0]]`, where
`h = q - q⁻¹`.  This is what collapses `M_i` to `α • 1 + β • S` and hence
gives the two-term readout `V̂ = c₊μ₊ + c₋μ₋`. -/
theorem transferEigen_isRoot {q x : R} (hq : q ≠ 0) (hx : x = q ∨ x = -q⁻¹) :
    x ^ 2 - (q - q⁻¹) * x - 1 = 0 := by
  rcases hx with rfl | rfl
  · field_simp; ring
  · field_simp; ring

/-- …and the right product, `λ₊ · λ₋ = -1` — the `det S = -1` conjunct of
`QOU.ParticleInteractions.ground_state_ordering`.  This is the **only**
conjunct of that proposition that survives; the two ordering conjuncts are
refuted by `sorted_lt_prescribed_A5`. -/
theorem transferEigen_vieta (q : R) (hq : q ≠ 0) :
    q * -q⁻¹ = -1 := by
  field_simp

end Vieta

/-! ### The readout weights, generic in the Markov parameter `z` -/

/-- `c₊`, the `λ₊ = q` readout weight. -/
noncomputable def cPlus (q z : ℝ) : ℝ := (z + q⁻¹) / (q + q⁻¹)

/-- `c₋`, the `λ₋ = -q⁻¹` readout weight. -/
noncomputable def cMinus (q z : ℝ) : ℝ := (q - z) / (q + q⁻¹)

/-- The mixed (`p`–`n`) eigenfactor `c = (q + q⁻¹)/2`.  It carries no `z`. -/
noncomputable def cMix (q : ℝ) : ℝ := (q + q⁻¹) / 2

/-- The corpus vertex readout `V̂ = c₊·μ₊ + c₋·μ₋`. -/
noncomputable def vhat (q z μp μm : ℝ) : ℝ := cPlus q z * μp + cMinus q z * μm

theorem cMix_pos {q : ℝ} (hq : 0 < q) : 0 < cMix q := by
  have h : 0 < q⁻¹ := inv_pos.mpr hq
  unfold cMix; linarith

theorem denom_pos {q : ℝ} (hq : 0 < q) : 0 < q + q⁻¹ := by
  have h : 0 < q⁻¹ := inv_pos.mpr hq
  linarith

/-- **The two weights sum to `1`, identically in `z`.**  This is the whole
reason the refutation is convention-independent: `z` is an affine parameter
on a partition of unity, so the `μ₊ = μ₋` positions are `z`-free outright,
and every other position sees `z` only through the product `c₊c₋`. -/
theorem cPlus_add_cMinus {q : ℝ} (hq : 0 < q) (z : ℝ) :
    cPlus q z + cMinus q z = 1 := by
  have h : q + q⁻¹ ≠ 0 := ne_of_gt (denom_pos hq)
  unfold cPlus cMinus
  field_simp
  ring

/-- The weight product, cleared: `4c₊c₋ = 4q(q - z)(qz + 1)/(q² + 1)²`.
Its sign is that of `(q - z)(qz + 1)`, so **both weights are positive
exactly when `-q⁻¹ < z < q`** — the Markov parameter strictly between the
two eigenvalues `λ₋ = -q⁻¹` and `λ₊ = q`. -/
theorem weight_prod {q : ℝ} (hq : 0 < q) (z : ℝ) :
    4 * (cPlus q z * cMinus q z) = 4 * q * (q - z) * (q * z + 1) / (q ^ 2 + 1) ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h : q + q⁻¹ ≠ 0 := ne_of_gt (denom_pos hq)
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  unfold cPlus cMinus
  field_simp

theorem cPlus_pos {q z : ℝ} (hq : 0 < q) (hz : -q⁻¹ < z) : 0 < cPlus q z := by
  unfold cPlus
  exact div_pos (by linarith) (denom_pos hq)

theorem cMinus_pos {q z : ℝ} (hq : 0 < q) (hz : z < q) : 0 < cMinus q z := by
  unfold cMinus
  exact div_pos (by linarith) (denom_pos hq)

/-! ### The two arrangements at `A = 5`, `Z = 1`, `N = 4` -/

/-- The readout at position `0` of the **sorted** arrangement `p n n n n`:
a proton whose whole suffix is neutrons, so all four crossings are mixed
(`d = -h/2`), giving `μ₊ = μ₋ = c⁴`. -/
noncomputable def sortedV0 (q z : ℝ) : ℝ := vhat q z (cMix q ^ 4) (cMix q ^ 4)

/-- The readout at position `1` of `p n n n n`: a neutron with three
neutrons after it, so `μ₊ = q⁻³` and `μ₋ = (-q)³ = -q³`. -/
noncomputable def sortedV1 (q z : ℝ) : ℝ := vhat q z (q ^ 3)⁻¹ (-(q ^ 3))

/-- The readout at position `0` of the **prescribed** arrangement
`n p n n n` (rules (i)+(ii) at `Z = 1`, `N = 4`): a neutron with one proton
and three neutrons after it, so `μ₊ = c·q⁻³`, `μ₋ = (-c)(-q)³ = c·q³`. -/
noncomputable def prescribedV0 (q z : ℝ) : ℝ :=
  vhat q z (cMix q * (q ^ 3)⁻¹) (cMix q * q ^ 3)

/-- The readout at position `1` of `n p n n n`: a proton with three
neutrons after it, so `μ₊ = c³` and `μ₋ = (-c)³ = -c³`. -/
noncomputable def prescribedV1 (q z : ℝ) : ℝ :=
  vhat q z (cMix q ^ 3) (-(cMix q ^ 3))

/-- Position `2` of **both** arrangements: a neutron with two neutrons
after it (`μ₊ = q⁻²`, `μ₋ = (-q)² = q²`).  Identical in the two
arrangements, because at positions `2, 3` both suffixes are all-neutron. -/
noncomputable def sharedV2 (q z : ℝ) : ℝ := vhat q z (q ^ 2)⁻¹ (q ^ 2)

/-- Position `3` of **both** arrangements: a neutron with one neutron after
it (`μ₊ = q⁻¹`, `μ₋ = -q`). -/
noncomputable def sharedV3 (q z : ℝ) : ℝ := vhat q z q⁻¹ (-q)

/-- The `μ₊ = μ₋` position is `z`-free: it collapses to `c⁴` by
`cPlus_add_cMinus`, whatever the Markov parameter is. -/
theorem sortedV0_eq {q : ℝ} (hq : 0 < q) (z : ℝ) : sortedV0 q z = cMix q ^ 4 := by
  unfold sortedV0 vhat
  have h := cPlus_add_cMinus hq z
  have hfac : cPlus q z * cMix q ^ 4 + cMinus q z * cMix q ^ 4
      = (cPlus q z + cMinus q z) * cMix q ^ 4 := by ring
  rw [hfac, h, one_mul]

/-! ### The polynomial core -/

/-- **The gap identity.**  The two arrangements' differing readout products
differ by an expression in which `z` survives only inside the product
`c₊c₋`:

    V̂₀V̂₁(prescribed) - V̂₀V̂₁(sorted) = 2·c₊·c₋·c⁴·(q⁶ - 1)/q³.

For `q > 1` the last two factors are positive, so the sign of the gap is
the sign of `c₊c₋`, which `weight_prod` computes.  It degenerates to
equality exactly at `q = 1`, where the deformation switches off. -/
theorem readout_gap {q : ℝ} (hq : 0 < q) (z : ℝ) :
    prescribedV0 q z * prescribedV1 q z - sortedV0 q z * sortedV1 q z
      = 2 * cPlus q z * cMinus q z * cMix q ^ 4 * (q ^ 6 - 1) / q ^ 3 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h : q + q⁻¹ ≠ 0 := ne_of_gt (denom_pos hq)
  unfold prescribedV0 prescribedV1 sortedV0 sortedV1 vhat cPlus cMinus cMix
  field_simp
  ring

/-! ### The refutation -/

/-- **The `A ≥ 4` clause of `prop:ground-state-ordering` is FALSE.**

At `A = 5`, `Z = 1`, `N = 4` the arrangement prescribed by rules (i)+(ii)
is `n p n n n`.  For every `q > 1`, every Markov parameter `z` whose two
readout weights are positive, and under the sign hypothesis `hU` on the
sorted readout, the **sorted** arrangement `p n n n n` — which the
proposition reserves for `A ≤ 3` — has a strictly smaller readout product
at the two positions where the arrangements differ:

    |V̂₀ V̂₁| (sorted)  <  |V̂₀ V̂₁| (prescribed).

Since positions `2, 3` agree, this is `Φ_q(p n n n n) < Φ_q(n p n n n)`:
rules (i)+(ii) do **not** select the `Φ_q` minimiser at `A = 5`. -/
theorem sorted_lt_prescribed_A5 {q z : ℝ} (hq : 1 < q)
    (hcp : 0 < cPlus q z) (hcm : 0 < cMinus q z)
    (hU : 0 ≤ sortedV1 q z) :
    |sortedV0 q z * sortedV1 q z| < |prescribedV0 q z * prescribedV1 q z| := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have hmix : 0 < cMix q := cMix_pos hq0
  have h6 : (0:ℝ) < q ^ 6 - 1 := by
    have : (1:ℝ) < q ^ 6 := one_lt_pow₀ hq (by norm_num)
    linarith
  -- the sorted product is non-negative: `V̂₀ = c⁴ > 0` and `hU` gives `V̂₁ ≥ 0`
  have hs : 0 ≤ sortedV0 q z * sortedV1 q z := by
    rw [sortedV0_eq hq0]
    exact mul_nonneg (le_of_lt (pow_pos hmix 4)) hU
  -- the gap is strictly positive: every factor of `readout_gap` is
  have hnum : 0 < 2 * cPlus q z * cMinus q z * cMix q ^ 4 * (q ^ 6 - 1) :=
    mul_pos (mul_pos (mul_pos (mul_pos (by norm_num) hcp) hcm) (pow_pos hmix 4)) h6
  have hgap : 0 < prescribedV0 q z * prescribedV1 q z
      - sortedV0 q z * sortedV1 q z := by
    rw [readout_gap hq0]
    exact div_pos hnum (pow_pos hq0 3)
  have hp : 0 ≤ prescribedV0 q z * prescribedV1 q z := by linarith
  rw [abs_of_nonneg hs, abs_of_nonneg hp]
  linarith

/-- **`Φ_q` form of the refutation.**  Multiplying in the two shared
positions, the *full* four-position readout product of the sorted
arrangement `p n n n n` is strictly smaller in absolute value than that of
the prescribed `n p n n n`.  Taking `Real.log` of both sides, this is
`Φ_q(p n n n n) < Φ_q(n p n n n)`. -/
theorem sorted_lt_prescribed_A5_full {q z : ℝ} (hq : 1 < q)
    (hcp : 0 < cPlus q z) (hcm : 0 < cMinus q z)
    (hU : 0 ≤ sortedV1 q z)
    (h23 : sharedV2 q z * sharedV3 q z ≠ 0) :
    |sortedV0 q z * sortedV1 q z * (sharedV2 q z * sharedV3 q z)|
      < |prescribedV0 q z * prescribedV1 q z * (sharedV2 q z * sharedV3 q z)| := by
  rw [abs_mul (sortedV0 q z * sortedV1 q z), abs_mul (prescribedV0 q z * prescribedV1 q z)]
  exact mul_lt_mul_of_pos_right (sorted_lt_prescribed_A5 hq hcp hcm hU) (abs_pos.mpr h23)

/-- **The `A ≥ 4` clause of `prop:ground-state-ordering` is false.**  The
statement "the prescribed arrangement minimises `Φ_q`" fails at
`A = 5, Z = 1, N = 4`: there is a strictly better arrangement (the sorted
one), so no minimality claim about the prescribed arrangement can hold.
Stated for an arbitrary Markov parameter whose readout weights are
positive — in particular for convention D, the canonical one. -/
theorem prescribed_not_minimiser_A5 {q z : ℝ} (hq : 1 < q)
    (hcp : 0 < cPlus q z) (hcm : 0 < cMinus q z)
    (hU : 0 ≤ sortedV1 q z)
    (h23 : sharedV2 q z * sharedV3 q z ≠ 0) :
    ¬ (|prescribedV0 q z * prescribedV1 q z * (sharedV2 q z * sharedV3 q z)|
        ≤ |sortedV0 q z * sortedV1 q z * (sharedV2 q z * sharedV3 q z)|) :=
  not_le.mpr (sorted_lt_prescribed_A5_full hq hcp hcm hU h23)

/-! ### Convention D — the canonical Markov parameter (owner ruling 2026-08-15) -/

/-- Convention D, `z = q³/(q²+1)`: the canonical Markov parameter. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

theorem zD_pos {q : ℝ} (hq : 0 < q) : 0 < zD q := by
  unfold zD; positivity

/-- `q - z_D = q/(q² + 1) > 0`: convention D lies below `λ₊ = q`. -/
theorem zD_lt_self {q : ℝ} (hq : 0 < q) : zD q < q := by
  have h : (0:ℝ) < q ^ 2 + 1 := by positivity
  unfold zD
  rw [div_lt_iff₀ h]
  nlinarith

theorem cPlus_zD_pos {q : ℝ} (hq : 0 < q) : 0 < cPlus q (zD q) :=
  cPlus_pos hq (lt_trans (neg_neg_iff_pos.mpr (inv_pos.mpr hq)) (zD_pos hq))

theorem cMinus_zD_pos {q : ℝ} (hq : 0 < q) : 0 < cMinus q (zD q) :=
  cMinus_pos hq (zD_lt_self hq)

/-- Under convention D the sorted position-`1` readout is
`(q⁴ + 1 - q⁶)/(q³(q² + 1))`. -/
theorem sortedV1_zD_eq {q : ℝ} (hq : 0 < q) :
    sortedV1 q (zD q) = (q ^ 4 + 1 - q ^ 6) / (q ^ 3 * (q ^ 2 + 1)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h : q + q⁻¹ ≠ 0 := ne_of_gt (denom_pos hq)
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  unfold sortedV1 vhat cPlus cMinus zD
  field_simp
  ring

/-- The sign hypothesis `hU`, discharged for convention D on `1 < q ≤ 6/5`
— an interval that contains the substrate anchor `q₀ ≈ 1.10998` (the exact
window is `q < 1.21060…`). -/
theorem sortedV1_zD_nonneg {q : ℝ} (hq : 1 < q) (hq5 : q ≤ 6/5) :
    0 ≤ sortedV1 q (zD q) := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  rw [sortedV1_zD_eq hq0]
  apply div_nonneg _ (by positivity)
  -- `q⁶ ≤ (36/25)·q⁴` since `q² ≤ 36/25`, and `(11/25)·q⁴ ≤ 1` since `q⁴ ≤ 1296/625`
  have h2 : q ^ 2 ≤ 36/25 := by nlinarith
  have h4 : q ^ 4 ≤ 1296/625 := by nlinarith
  nlinarith [pow_pos hq0 4]

/-- Under convention D the shared position-`2` readout is
`(q⁴ + 1)/(q²(q² + 1)) > 0`. -/
theorem sharedV2_zD_pos {q : ℝ} (hq : 0 < q) : 0 < sharedV2 q (zD q) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h : q + q⁻¹ ≠ 0 := ne_of_gt (denom_pos hq)
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  have he : sharedV2 q (zD q) = (q ^ 4 + 1) / (q ^ 2 * (q ^ 2 + 1)) := by
    unfold sharedV2 vhat cPlus cMinus zD
    field_simp
    ring
  rw [he]; positivity

/-- Under convention D the shared position-`3` readout collapses to
`1/(q(q² + 1)) > 0` — in particular it is never zero, so the shared tail
never degenerates. -/
theorem sharedV3_zD_pos {q : ℝ} (hq : 0 < q) : 0 < sharedV3 q (zD q) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have h : q + q⁻¹ ≠ 0 := ne_of_gt (denom_pos hq)
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  have he : sharedV3 q (zD q) = 1 / (q * (q ^ 2 + 1)) := by
    unfold sharedV3 vhat cPlus cMinus zD
    field_simp
    ring
  rw [he]; positivity

/-- **The refutation under the canonical convention D**, with every
hypothesis discharged except the `q`-range.  `1 < q ≤ 6/5` contains the
substrate anchor `q₀ ≈ 1.10998`. -/
theorem prescribed_not_minimiser_A5_conventionD {q : ℝ} (hq : 1 < q) (hq5 : q ≤ 6/5) :
    ¬ (|prescribedV0 q (zD q) * prescribedV1 q (zD q)
          * (sharedV2 q (zD q) * sharedV3 q (zD q))|
        ≤ |sortedV0 q (zD q) * sortedV1 q (zD q)
          * (sharedV2 q (zD q) * sharedV3 q (zD q))|) := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  exact prescribed_not_minimiser_A5 hq (cPlus_zD_pos hq0) (cMinus_zD_pos hq0)
    (sortedV1_zD_nonneg hq hq5)
    (ne_of_gt (mul_pos (sharedV2_zD_pos hq0) (sharedV3_zD_pos hq0)))

/-! ### Convention C — excised 2026-08-15, retained as a cross-check

The convention-C instance is kept so that the polynomial certificate this
file originally carried stays checkable, and so that the two conventions
can be compared.  It is **not** canonical; convention D above is.
-/

/-- Convention C, `z = √q/(q+1)`: excised by the owner ruling of
2026-08-15, retained here only as a cross-check. -/
noncomputable def zC (q : ℝ) : ℝ := Real.sqrt q / (q + 1)

theorem zC_nonneg {q : ℝ} (hq : 0 < q) : 0 ≤ zC q := by
  unfold zC
  exact div_nonneg (Real.sqrt_nonneg q) (by linarith)

/-- `z_C < q` for `q > 1`: convention C also lies below `λ₊ = q`. -/
theorem zC_lt_self {q : ℝ} (hq : 1 < q) : zC q < q := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have hs : Real.sqrt q ≤ q := by
    have h2 : q ≤ q ^ 2 := by nlinarith
    have := Real.sqrt_le_sqrt h2
    rwa [Real.sqrt_sq (le_of_lt hq0)] at this
  unfold zC
  rw [div_lt_iff₀ (by linarith)]
  nlinarith [hs]

theorem cPlus_zC_pos {q : ℝ} (hq : 1 < q) : 0 < cPlus q (zC q) := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  refine cPlus_pos hq0 (lt_of_lt_of_le ?_ (zC_nonneg hq0))
  simpa using inv_pos.mpr hq0

theorem cMinus_zC_pos {q : ℝ} (hq : 1 < q) : 0 < cMinus q (zC q) :=
  cMinus_pos (lt_trans zero_lt_one hq) (zC_lt_self hq)

/-- `Ã = t³ + t² + 1` — the cleared numerator of `c₊` under convention C at
`q = t²`. -/
noncomputable def Anum (t : ℝ) : ℝ := t ^ 3 + t ^ 2 + 1

/-- `B̃ = t⁶ + t⁴ - t³` — the cleared numerator of `c₋` under convention C
at `q = t²`. -/
noncomputable def Bnum (t : ℝ) : ℝ := t ^ 6 + t ^ 4 - t ^ 3

/-- `K t = (t²+1)(t⁴+1)` — their common denominator. -/
noncomputable def K (t : ℝ) : ℝ := (t ^ 2 + 1) * (t ^ 4 + 1)

theorem K_pos {t : ℝ} (ht : 1 < t) : 0 < K t := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  unfold K; positivity

/-- Under convention C at `q = t²`, the sorted position-`1` readout takes
the committed polynomial form `(Ã - B̃t¹²)/(K t⁶)`. -/
theorem sortedV1_zC_eq {t : ℝ} (ht : 1 < t) :
    sortedV1 (t ^ 2) (zC (t ^ 2)) = (Anum t - Bnum t * t ^ 12) / (K t * t ^ 6) := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  have hq0 : (0:ℝ) < t ^ 2 := by positivity
  have hsq : Real.sqrt (t ^ 2) = t := Real.sqrt_sq (le_of_lt h0)
  have hne : (t:ℝ) ≠ 0 := ne_of_gt h0
  have h : (t:ℝ) ^ 2 + (t ^ 2)⁻¹ ≠ 0 := ne_of_gt (denom_pos hq0)
  have hK : K t ≠ 0 := ne_of_gt (K_pos ht)
  unfold sortedV1 vhat cPlus cMinus zC Anum Bnum K
  rw [hsq]
  field_simp
  ring

/-- The sign hypothesis `hU` under convention C, in the committed
polynomial form. -/
theorem sortedV1_zC_nonneg {t : ℝ} (ht : 1 < t)
    (hU : 0 ≤ Anum t - Bnum t * t ^ 12) :
    0 ≤ sortedV1 (t ^ 2) (zC (t ^ 2)) := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  rw [sortedV1_zC_eq ht]
  exact div_nonneg hU (le_of_lt (mul_pos (K_pos ht) (by positivity)))

/-- **The refutation under convention C**, in the shape this file
originally carried: `q = t²` with `t > 1`, and `hU` the polynomial sign
condition `0 ≤ Ã - B̃t¹²` (satisfied at the substrate anchor
`t = √q₀`, where it evaluates to `≈ 0.604`; the exact window is
`q < 1.13699…`). -/
theorem prescribed_not_minimiser_A5_conventionC {t : ℝ} (ht : 1 < t)
    (hU : 0 ≤ Anum t - Bnum t * t ^ 12)
    (h23 : sharedV2 (t ^ 2) (zC (t ^ 2)) * sharedV3 (t ^ 2) (zC (t ^ 2)) ≠ 0) :
    ¬ (|prescribedV0 (t ^ 2) (zC (t ^ 2)) * prescribedV1 (t ^ 2) (zC (t ^ 2))
          * (sharedV2 (t ^ 2) (zC (t ^ 2)) * sharedV3 (t ^ 2) (zC (t ^ 2)))|
        ≤ |sortedV0 (t ^ 2) (zC (t ^ 2)) * sortedV1 (t ^ 2) (zC (t ^ 2))
          * (sharedV2 (t ^ 2) (zC (t ^ 2)) * sharedV3 (t ^ 2) (zC (t ^ 2)))|) := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  have hq : (1:ℝ) < t ^ 2 := by nlinarith
  exact prescribed_not_minimiser_A5 hq (cPlus_zC_pos hq) (cMinus_zC_pos hq)
    (sortedV1_zC_nonneg ht hU) h23

end QOU.MassTheory.GroundStateOrderingRefutation
