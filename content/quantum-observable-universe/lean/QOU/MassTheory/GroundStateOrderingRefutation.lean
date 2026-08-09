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

## The readout, and why it is a two-parameter object

Write `q = t²` with `t > 1`.  The corpus builds, at each chain position
`i`, the product `M_i = Π_{j>i} T(d_ij)` of transfer factors

    T(d) = ![![h + d, 1], ![1, d]] = S + d • 1,   S = ![![h, 1], ![1, 0]],
    h = q - q⁻¹,

and reads off `V̂_i = z · (M_i) 1 0 + (M_i) 1 1` with `z = √q / (q+1)`.
Every `T(d)` is a polynomial in the single matrix `S`, so they all commute
(`QOU.MassTheory.TransferFactorCommute`) and `M_i` depends on the crossing
coefficients **only as a multiset**.  `S` has `tr S = h`, `det S = -1`,
hence eigenvalues `q` and `-q⁻¹` (`transferEigen_vieta` below), and
`S² = h • S + 1` collapses `M_i` to `α • 1 + β • S`, giving

    V̂_i = c₊ · μ₊ + c₋ · μ₋,      μ± = Π_{j>i} (λ± + d_ij),

with the two readout weights `c₊`, `c₋` defined below.  The three crossing
coefficients used by the corpus contribute the eigenfactor pairs

    d = 0     (pp)   :  μ₊ ·= q     μ₋ ·= -q⁻¹
    d = -h/2  (pn)   :  μ₊ ·= c     μ₋ ·= -c      ,  c = (q + q⁻¹)/2
    d = -h    (nn)   :  μ₊ ·= q⁻¹   μ₋ ·= -q

which is exactly what `cMix`, and the `μ±` arguments in
`sortedV0`…`sharedV3` below, encode.

## What is proved here

`sorted_lt_prescribed_A5` : for every `t > 1` at which the sign condition
`hU` holds — and the substrate anchor is such a `t` — the two chain
positions at which the two arrangements differ satisfy

    |V̂₀ · V̂₁| (sorted)  <  |V̂₀ · V̂₁| (prescribed).

The remaining two positions carry **identical** readouts
(`sharedV2`, `sharedV3`), so this is exactly `Φ_q(pnnnn) < Φ_q(npnnn)`, and
the prescribed arrangement is therefore **not** the minimiser.  Nothing
here is assumed: `hU` is a plain polynomial inequality on `t`, not an
axiomatised conclusion.

Scope note: this is a **scope-(b) structural exclusion for the clause**
— a counterexample, valid for a whole interval of `t` containing the
substrate anchor, not a "the numbers came out wrong" scope-(a) negative.

Reference: `docs/audits/2026-08-09-ground-state-ordering-truth-value.md`;
witness `computations/ground-state-ordering-argmin-sweep.witness.json`.
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

/-! ### The readout weights -/

/-- `K t = (t²+1)(t⁴+1)` — the common denominator of the two readout
weights, after clearing `z = √q/(q+1)` at `q = t²`. -/
noncomputable def K (t : ℝ) : ℝ := (t ^ 2 + 1) * (t ^ 4 + 1)

/-- `c₊`, the `λ₊ = q` readout weight: `(z + q⁻¹)/(q + q⁻¹)` at `q = t²`. -/
noncomputable def cPlus (t : ℝ) : ℝ := (t ^ 3 + t ^ 2 + 1) / K t

/-- `c₋`, the `λ₋ = -q⁻¹` readout weight: `(q - z)/(q + q⁻¹)` at `q = t²`. -/
noncomputable def cMinus (t : ℝ) : ℝ := (t ^ 6 + t ^ 4 - t ^ 3) / K t

/-- The mixed (`p`–`n`) eigenfactor `c = (q + q⁻¹)/2` at `q = t²`. -/
noncomputable def cMix (t : ℝ) : ℝ := (t ^ 4 + 1) / (2 * t ^ 2)

/-- The corpus vertex readout `V̂ = c₊·μ₊ + c₋·μ₋`. -/
noncomputable def vhat (t μp μm : ℝ) : ℝ := cPlus t * μp + cMinus t * μm

theorem K_pos {t : ℝ} (ht : 1 < t) : 0 < K t := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  unfold K; positivity

theorem cMix_pos {t : ℝ} (ht : 1 < t) : 0 < cMix t := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  unfold cMix; positivity

/-- The two weights sum to `1` — the `μ₊ = μ₋` positions are `z`-free. -/
theorem cPlus_add_cMinus {t : ℝ} (ht : 1 < t) : cPlus t + cMinus t = 1 := by
  have hK : K t ≠ 0 := ne_of_gt (K_pos ht)
  unfold cPlus cMinus K at *
  field_simp
  try ring

/-! ### The polynomial core -/

/-- `Ã = t³ + t² + 1` — the cleared numerator of `c₊`. -/
noncomputable def Anum (t : ℝ) : ℝ := t ^ 3 + t ^ 2 + 1

/-- `B̃ = t⁶ + t⁴ - t³` — the cleared numerator of `c₋`. -/
noncomputable def Bnum (t : ℝ) : ℝ := t ^ 6 + t ^ 4 - t ^ 3

theorem Anum_pos {t : ℝ} (ht : 1 < t) : 0 < Anum t := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  unfold Anum; positivity

theorem Bnum_pos {t : ℝ} (ht : 1 < t) : 0 < Bnum t := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  have h1 : 1 < t ^ 3 := one_lt_pow₀ ht (by norm_num)
  have : Bnum t = t ^ 3 * (t ^ 3 + t - 1) := by unfold Bnum; ring
  rw [this]
  have : (0:ℝ) < t ^ 3 + t - 1 := by nlinarith
  positivity

/-- **The polynomial certificate.**  For every `t > 1`,

    (Ã + B̃t¹²)(Ã - B̃)  >  (Ã - B̃t¹²)(t⁴+1)(t²+1).

Both sides are the cleared forms of the two arrangements' differing
readout products.  The difference factors as `(t-1)` times a polynomial
with **all coefficients positive** in the shifted variable `s = t - 1`,
which is why the counterexample survives on a whole interval above `1`
rather than only at one anchor.  (It degenerates to equality exactly at
`t = 1`, i.e. `q = 1`, where the deformation switches off.) -/
theorem A5_certificate {t : ℝ} (ht : 1 < t) :
    (Anum t - Bnum t * t ^ 12) * ((t ^ 4 + 1) * (t ^ 2 + 1))
      < (Anum t + Bnum t * t ^ 12) * (Anum t - Bnum t) := by
  have hs : (0:ℝ) < t - 1 := by linarith
  have key :
      (Anum t + Bnum t * t ^ 12) * (Anum t - Bnum t)
        - (Anum t - Bnum t * t ^ 12) * ((t ^ 4 + 1) * (t ^ 2 + 1))
      = (t - 1) *
        (72 + 1020 * (t - 1) + 6984 * (t - 1) ^ 2 + 31198 * (t - 1) ^ 3
          + 102036 * (t - 1) ^ 4 + 258454 * (t - 1) ^ 5
          + 523048 * (t - 1) ^ 6 + 861830 * (t - 1) ^ 7
          + 1170024 * (t - 1) ^ 8 + 1318330 * (t - 1) ^ 9
          + 1237418 * (t - 1) ^ 10 + 968058 * (t - 1) ^ 11
          + 629570 * (t - 1) ^ 12 + 338306 * (t - 1) ^ 13
          + 148678 * (t - 1) ^ 14 + 52600 * (t - 1) ^ 15
          + 14626 * (t - 1) ^ 16 + 3080 * (t - 1) ^ 17
          + 462 * (t - 1) ^ 18 + 44 * (t - 1) ^ 19
          + 2 * (t - 1) ^ 20) := by
    unfold Anum Bnum; ring
  have hpos :
      0 < (Anum t + Bnum t * t ^ 12) * (Anum t - Bnum t)
            - (Anum t - Bnum t * t ^ 12) * ((t ^ 4 + 1) * (t ^ 2 + 1)) := by
    rw [key]
    have hq : (0:ℝ) < t - 1 := hs
    positivity
  linarith

/-! ### The two arrangements at `A = 5`, `Z = 1`, `N = 4` -/

/-- The readout at position `0` of the **sorted** arrangement `p n n n n`:
a proton whose whole suffix is neutrons, so all four crossings are mixed
(`d = -h/2`), giving `μ₊ = μ₋ = c⁴`. -/
noncomputable def sortedV0 (t : ℝ) : ℝ := vhat t (cMix t ^ 4) (cMix t ^ 4)

/-- The readout at position `1` of `p n n n n`: a neutron with three
neutrons after it, so `μ₊ = q⁻³ = t⁻⁶` and `μ₋ = (-q)³ = -t⁶`. -/
noncomputable def sortedV1 (t : ℝ) : ℝ := vhat t (1 / t ^ 6) (-(t ^ 6))

/-- The readout at position `0` of the **prescribed** arrangement
`n p n n n` (rules (i)+(ii) at `Z = 1`, `N = 4`): a neutron with one
proton and three neutrons after it, so `μ₊ = c·q⁻³`, `μ₋ = (-c)(-q)³ = c·q³`. -/
noncomputable def prescribedV0 (t : ℝ) : ℝ :=
  vhat t (cMix t * (1 / t ^ 6)) (cMix t * t ^ 6)

/-- The readout at position `1` of `n p n n n`: a proton with three
neutrons after it, so `μ₊ = c³` and `μ₋ = (-c)³ = -c³`. -/
noncomputable def prescribedV1 (t : ℝ) : ℝ :=
  vhat t (cMix t ^ 3) (-(cMix t ^ 3))

/-- Position `2` of **both** arrangements: a neutron with two neutrons
after it (`μ₊ = q⁻² = t⁻⁴`, `μ₋ = (-q)² = t⁴`).  Identical in the two
arrangements, because at positions `2, 3` both suffixes are all-neutron. -/
noncomputable def sharedV2 (t : ℝ) : ℝ := vhat t (1 / t ^ 4) (t ^ 4)

/-- Position `3` of **both** arrangements: a neutron with one neutron
after it (`μ₊ = q⁻¹ = t⁻²`, `μ₋ = -q = -t²`). -/
noncomputable def sharedV3 (t : ℝ) : ℝ := vhat t (1 / t ^ 2) (-(t ^ 2))

theorem sortedV0_eq {t : ℝ} (ht : 1 < t) : sortedV0 t = cMix t ^ 4 := by
  unfold sortedV0 vhat
  have h := cPlus_add_cMinus ht
  have hfac : cPlus t * cMix t ^ 4 + cMinus t * cMix t ^ 4
      = (cPlus t + cMinus t) * cMix t ^ 4 := by ring
  rw [hfac, h, one_mul]

theorem sortedV1_eq {t : ℝ} (ht : 1 < t) :
    sortedV1 t = (Anum t - Bnum t * t ^ 12) / (K t * t ^ 6) := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  have hK : K t ≠ 0 := ne_of_gt (K_pos ht)
  have ht6 : (t:ℝ) ^ 6 ≠ 0 := by positivity
  unfold sortedV1 vhat cPlus cMinus Anum Bnum
  field_simp
  try ring

theorem prescribedV0_eq {t : ℝ} (ht : 1 < t) :
    prescribedV0 t = cMix t * ((Anum t + Bnum t * t ^ 12) / (K t * t ^ 6)) := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  have hK : K t ≠ 0 := ne_of_gt (K_pos ht)
  have ht6 : (t:ℝ) ^ 6 ≠ 0 := by positivity
  unfold prescribedV0 vhat cPlus cMinus Anum Bnum
  field_simp
  try ring

theorem prescribedV1_eq {t : ℝ} (ht : 1 < t) :
    prescribedV1 t = cMix t ^ 3 * ((Anum t - Bnum t) / K t) := by
  have hK : K t ≠ 0 := ne_of_gt (K_pos ht)
  unfold prescribedV1 vhat cPlus cMinus Anum Bnum
  field_simp
  try ring

/-! ### The refutation -/

/-- **The `A ≥ 4` clause of `prop:ground-state-ordering` is FALSE.**

At `A = 5`, `Z = 1`, `N = 4` the arrangement prescribed by rules (i)+(ii)
is `n p n n n`.  Under the hypothesis `hU` — a plain polynomial sign
condition on `t`, satisfied at the substrate anchor `t = √q₀` where
`Ã - B̃t¹² ≈ 0.604 > 0` — the **sorted** arrangement `p n n n n`, which the
proposition reserves for `A ≤ 3`, has a strictly smaller readout product
at the two positions where the arrangements differ:

    |V̂₀ V̂₁| (sorted)  <  |V̂₀ V̂₁| (prescribed).

Since positions `2, 3` agree (`sorted_shared_tail`), this is
`Φ_q(p n n n n) < Φ_q(n p n n n)`: the prescribed arrangement is not the
`Φ_q` minimiser. -/
theorem sorted_lt_prescribed_A5 {t : ℝ} (ht : 1 < t)
    (hU : 0 ≤ Anum t - Bnum t * t ^ 12) :
    |sortedV0 t * sortedV1 t| < |prescribedV0 t * prescribedV1 t| := by
  have h0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  have hK : 0 < K t := K_pos ht
  have hc : 0 < cMix t := cMix_pos ht
  have ht6 : (0:ℝ) < t ^ 6 := by positivity
  have hA : 0 < Anum t := Anum_pos ht
  have hB : 0 < Bnum t := Bnum_pos ht
  have hW : 0 < Anum t + Bnum t * t ^ 12 := by positivity
  have hcert := A5_certificate ht
  -- `R = Ã - B̃ > 0` is forced by the certificate, not assumed.
  have hR : 0 < Anum t - Bnum t := by
    by_contra hcon
    push_neg at hcon
    have h1 : (Anum t + Bnum t * t ^ 12) * (Anum t - Bnum t) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos (le_of_lt hW) hcon
    have h2 : 0 ≤ (Anum t - Bnum t * t ^ 12) * ((t ^ 4 + 1) * (t ^ 2 + 1)) := by
      have : (0:ℝ) ≤ (t ^ 4 + 1) * (t ^ 2 + 1) := by positivity
      exact mul_nonneg hU this
    linarith
  -- rewrite both sides
  rw [sortedV0_eq ht, sortedV1_eq ht, prescribedV0_eq ht, prescribedV1_eq ht]
  have hLHS :
      |cMix t ^ 4 * ((Anum t - Bnum t * t ^ 12) / (K t * t ^ 6))|
        = cMix t ^ 4 * ((Anum t - Bnum t * t ^ 12) / (K t * t ^ 6)) := by
    apply abs_of_nonneg
    have : (0:ℝ) < K t * t ^ 6 := by positivity
    have := div_nonneg hU (le_of_lt this)
    positivity
  have hRHSpos :
      0 < cMix t * ((Anum t + Bnum t * t ^ 12) / (K t * t ^ 6))
            * (cMix t ^ 3 * ((Anum t - Bnum t) / K t)) := by
    have h1 : (0:ℝ) < K t * t ^ 6 := by positivity
    positivity
  rw [hLHS, abs_of_pos hRHSpos, ← sub_pos]
  -- reduce to the certificate
  have hK_eq : K t = (t ^ 4 + 1) * (t ^ 2 + 1) := by unfold K; ring
  have hnum : 0 < (Anum t + Bnum t * t ^ 12) * (Anum t - Bnum t)
      - (Anum t - Bnum t * t ^ 12) * K t := by
    rw [hK_eq]; linarith [hcert]
  have hne : K t ≠ 0 := ne_of_gt hK
  have hne6 : (t:ℝ) ^ 6 ≠ 0 := by positivity
  have hgap :
      cMix t * ((Anum t + Bnum t * t ^ 12) / (K t * t ^ 6))
          * (cMix t ^ 3 * ((Anum t - Bnum t) / K t))
        - cMix t ^ 4 * ((Anum t - Bnum t * t ^ 12) / (K t * t ^ 6))
      = cMix t ^ 4 * ((Anum t + Bnum t * t ^ 12) * (Anum t - Bnum t)
            - (Anum t - Bnum t * t ^ 12) * K t) / (K t * K t * t ^ 6) := by
    field_simp
  rw [hgap]
  exact div_pos (mul_pos (by positivity) hnum) (by positivity)

/-- **`Φ_q` form of the refutation.**  Multiplying in the two shared
positions, the *full* four-position readout product of the sorted
arrangement `p n n n n` is strictly smaller in absolute value than that of
the prescribed `n p n n n`.  Taking `Real.log` of both sides, this is
`Φ_q(p n n n n) < Φ_q(n p n n n)`: rules (i)+(ii) do **not** select the
`Φ_q` minimiser at `A = 5`. -/
theorem sorted_lt_prescribed_A5_full {t : ℝ} (ht : 1 < t)
    (hU : 0 ≤ Anum t - Bnum t * t ^ 12)
    (h23 : sharedV2 t * sharedV3 t ≠ 0) :
    |sortedV0 t * sortedV1 t * (sharedV2 t * sharedV3 t)|
      < |prescribedV0 t * prescribedV1 t * (sharedV2 t * sharedV3 t)| := by
  rw [abs_mul (sortedV0 t * sortedV1 t), abs_mul (prescribedV0 t * prescribedV1 t)]
  exact mul_lt_mul_of_pos_right (sorted_lt_prescribed_A5 ht hU) (abs_pos.mpr h23)

/-- **The `A ≥ 4` clause of `prop:ground-state-ordering` is false.**  The
statement "the prescribed arrangement minimises `Φ_q`" fails at
`A = 5, Z = 1, N = 4`: there is a strictly better arrangement (the sorted
one), so no minimality claim about the prescribed arrangement can hold. -/
theorem prescribed_not_minimiser_A5 {t : ℝ} (ht : 1 < t)
    (hU : 0 ≤ Anum t - Bnum t * t ^ 12)
    (h23 : sharedV2 t * sharedV3 t ≠ 0) :
    ¬ (|prescribedV0 t * prescribedV1 t * (sharedV2 t * sharedV3 t)|
        ≤ |sortedV0 t * sortedV1 t * (sharedV2 t * sharedV3 t)|) := by
  exact not_le.mpr (sorted_lt_prescribed_A5_full ht hU h23)

end QOU.MassTheory.GroundStateOrderingRefutation
