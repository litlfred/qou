import QOU.MassTheory.DeuteronTwoBodyKernel
import QOU.MathlibExt.QIntegerFactorial

/-!
# The bond channel is odd in `T_z`; the multiplet channel is even

**What is decided here.**  The framework assigns each nucleon pair an *interface
factor* `f = z_D(q) − h(q)·t`, where `t` is the weight of the `σ⁻¹` branch:
`t = 0` for a p–p pair, `t = 1` for n–n, `t ≈ ½` for p–n
(`QOU.MassTheory.DeuteronKernel.interfaceFactor`).  Reading `t` against the pair
isospin projection `T_z` — `+1` for p–p, `0` for p–n, `−1` for n–n — gives
`t = (1 − T_z)/2`, so the bond factor is **affine in `T_z`**.

This file proves the consequence: the `T_z`-**odd** part of the bond factor is
exactly `(h/2)·T_z`, so the bond layer is charge-symmetric **iff `h(q) = 0`, iff
`q = 1`** — the classical limit.  For every `q > 1` the bond channel violates
charge symmetry, and no choice of `q` repairs it.

The contrast is the point.  The two-row isospin multiplet weight `[2T+1]_q` with
`T = |T_z|` is even in `T_z` **for every `q`**, trivially, because it sees only
`|T_z|`.  So the two channels carry opposite `T_z` parity and the bond channel is
the sole carrier of the violation.

**Why charge symmetry is the right demand.**  It is the statement that the
*strong* interaction does not distinguish p–p from n–n; the observed p–p / n–n
difference is attributed to the electromagnetic channel plus a small
charge-symmetry-breaking residual.  A strong-channel object is therefore required
to be **even** in `T_z`.  This is a symmetry demand, not a fitted constraint: no
measured number enters any statement below.

**What this does NOT prove.**  It does not show that an even-in-`T_z` bond factor
exists in the Hecke algebra, nor that `[2T+1]_q` is the right even object, nor
anything about magnitudes.  It is a **scope-(b) structural exclusion** of one
family — every `f` affine in the pair's neutron count — with the invariant cited:
the `T_z`-odd part of an affine function is its slope, and the slope here is
`h(q)/2`, which vanishes only at `q = 1`.

**Provenance.**  Bean `qou-1pig` measured the same defect numerically (`f_pn` is
the arithmetic mean of `f_pp` and `f_nn` to `1.4e-4`, so the factor is a linear
ramp in neutron count, "hence odd in `T_z`") and bean `qou-xwur` proposed the
two-row partition channel as the place isospin actually lives.  Neither was
formalised.  `bondL_strictMono` in the imported file already contained the energy
half of §4 and is used rather than re-proved.

No `sorry`, no axiom beyond Mathlib's, no fitted constant.
-/

namespace QOU.MassTheory.BondChannelTzParity

open QOU.MassTheory.DeuteronKernel
open QOU.MathlibExt

/-! ## §1. The colour weight as a function of the pair isospin projection -/

/-- The `σ⁻¹`-branch weight of a pair with isospin projection `T_z`:
`t(T_z) = (1 − T_z)/2`.

`T_z = +1` (p–p) ↦ `t = 0`; `T_z = 0` (p–n) ↦ `t = ½`; `T_z = −1` (n–n) ↦ `t = 1`,
matching `interfaceFactor`'s own reading of its second argument. -/
noncomputable def weightOfTz (tz : ℝ) : ℝ := (1 - tz) / 2

@[simp] theorem weightOfTz_one : weightOfTz 1 = 0 := by unfold weightOfTz; norm_num

@[simp] theorem weightOfTz_neg_one : weightOfTz (-1) = 1 := by
  unfold weightOfTz; norm_num

@[simp] theorem weightOfTz_zero : weightOfTz 0 = 1 / 2 := by
  unfold weightOfTz; norm_num

/-- The bond factor read as a function of the pair isospin projection. -/
noncomputable def bondOfTz (q tz : ℝ) : ℝ := interfaceFactor q (weightOfTz tz)

/-! ## §2. The exact even/odd split -/

/-- **The bond factor is affine in `T_z`**, with intercept `z_D − h/2` and slope
`h/2`:  `f(T_z) = (z_D − h/2) + (h/2)·T_z`. -/
theorem bondOfTz_eq (q tz : ℝ) :
    bondOfTz q tz = (zD q - hq q / 2) + (hq q / 2) * tz := by
  unfold bondOfTz weightOfTz interfaceFactor
  ring

/-- The `T_z`-**even** part is constant: it does not see `T_z` at all. -/
theorem bondOfTz_evenPart (q tz : ℝ) :
    (bondOfTz q tz + bondOfTz q (-tz)) / 2 = zD q - hq q / 2 := by
  rw [bondOfTz_eq, bondOfTz_eq]; ring

/-- **The `T_z`-odd part is exactly `(h/2)·T_z`.**  This is the whole content of
the file: the charge-symmetry violation of the bond layer *is* the Hecke
deformation parameter, with no other source and no other size. -/
theorem bondOfTz_oddPart (q tz : ℝ) :
    (bondOfTz q tz - bondOfTz q (-tz)) / 2 = (hq q / 2) * tz := by
  rw [bondOfTz_eq, bondOfTz_eq]; ring

/-- The p–p / n–n gap is exactly `h(q)`, for every `q`.  (Measured numerically at
the proton pin as `|f_pp − f_nn| = h = 0.20906029879563931543`.) -/
theorem bondOfTz_pp_sub_nn (q : ℝ) : bondOfTz q 1 - bondOfTz q (-1) = hq q := by
  rw [bondOfTz_eq, bondOfTz_eq]; ring

/-! ## §3. The exclusion -/

/-- **The bond factor is even in `T_z` iff the Hecke deformation vanishes.** -/
theorem bondOfTz_even_iff (q : ℝ) :
    (∀ tz : ℝ, bondOfTz q tz = bondOfTz q (-tz)) ↔ hq q = 0 := by
  constructor
  · intro h
    have h1 := h 1
    have : hq q = 0 := by
      have := bondOfTz_pp_sub_nn q
      rw [h1] at this
      linarith
    exact this
  · intro h tz
    rw [bondOfTz_eq, bondOfTz_eq, h]
    ring

/-- `h(q) = q − q⁻¹` vanishes exactly at `q = 1`, among positive `q`. -/
theorem hq_eq_zero_iff {q : ℝ} (hq0 : 0 < q) : hq q = 0 ↔ q = 1 := by
  unfold hq
  constructor
  · intro h
    have hne : q ≠ 0 := ne_of_gt hq0
    have : q * q = 1 := by field_simp at h; linarith [h]
    nlinarith
  · intro h; subst h; norm_num

/-- **The bond layer is charge-symmetric only in the classical limit.**

For every `q > 0`, the interface family is even in `T_z` iff `q = 1`.  So at any
genuine deformation — the substrate sits at `q₀ ≈ 1.10998` — the bond channel
carries a nonzero `T_z`-odd part, and it is the deformation itself that breaks
charge symmetry.  No choice of `q > 1` avoids this. -/
theorem bondOfTz_even_iff_classical {q : ℝ} (hq0 : 0 < q) :
    (∀ tz : ℝ, bondOfTz q tz = bondOfTz q (-tz)) ↔ q = 1 :=
  (bondOfTz_even_iff q).trans (hq_eq_zero_iff hq0)

/-- `1 < q` forces a strictly positive Hecke deformation. -/
theorem hq_pos_of_one_lt {q : ℝ} (hq1 : 1 < q) : 0 < hq q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  unfold hq
  have : q⁻¹ < 1 := by
    rw [inv_lt_one_iff₀]
    right; exact hq1
  linarith

/-- **Restated as the exclusion it is: at every `q > 1` the bond channel has a
nonzero `T_z`-odd part.** -/
theorem bondOfTz_oddPart_ne_zero {q : ℝ} (hq1 : 1 < q) :
    (bondOfTz q 1 - bondOfTz q (-1)) / 2 ≠ 0 := by
  rw [bondOfTz_oddPart]
  have := hq_pos_of_one_lt hq1
  positivity

/-! ## §4. The bond ENERGY, not merely the factor

`bondL` adds the writhe normalisation `−(t − ½)·log(1 − h)`.  Under
`t = (1 − T_z)/2` that term is `(T_z/2)·log(1 − h)` — itself purely `T_z`-odd, so
the writhe factor does not cancel the violation but adds a second odd term. -/

/-- The writhe exponent is purely `T_z`-odd:  `t(T_z) − ½ = −T_z/2`. -/
theorem writheExponent_odd (tz : ℝ) : weightOfTz tz - 1 / 2 = -tz / 2 := by
  unfold weightOfTz; ring

/-- **The p–p and n–n bond energies differ**, for every `q` whose deformation
lies in `(0,1)` — which includes the substrate, where `h(q₀) ≈ 0.209`.

This is the energy-level form of §3 and is a one-line consequence of
`bondL_strictMono`, already proved in the imported file: the bond energy is
strictly increasing in the colour weight, and p–p sits at `t = 0` while n–n sits
at `t = 1`.  Charge symmetry demands these be equal; strict monotonicity forbids
it. -/
theorem bondL_pp_ne_nn {q : ℝ} (hh0 : 0 < hq q) (hh1 : hq q < 1)
    (hpos : 0 < interfaceFactor q 1) :
    bondL q 0 ≠ bondL q 1 :=
  ne_of_lt (bondL_strictMono hh0 hh1 zero_lt_one hpos)

/-! ## §5. The even channel, for contrast -/

/-- The two-row isospin multiplet weight `[2T+1]_q` at `T = |T_z|`.

Two-row partitions `λ = (a,b) ⊢ A` are the isospin multiplets, with
`T = (a−b)/2` and `|N − Z| = a − b = 2T` (bean `qou-xwur`); the Wenzl weight of
the multiplet is the quantum dimension `[2T+1]_q`.  Indexed by the integer
projection here, since that is what a parity statement needs. -/
noncomputable def multipletWeight (q : ℝ) (tz : ℤ) : ℝ := qInt q (2 * tz.natAbs + 1)

/-- **The multiplet weight is even in `T_z`, for every `q`.**

Trivially so — it reads only `|T_z|`.  That triviality is the finding: evenness
costs the multiplet channel nothing, while the bond channel cannot have it at any
`q > 1`. -/
theorem multipletWeight_even (q : ℝ) (tz : ℤ) :
    multipletWeight q (-tz) = multipletWeight q tz := by
  unfold multipletWeight
  rw [Int.natAbs_neg]

/-! ## §6. The separation -/

/-- **The two channels carry opposite `T_z` parity.**

At every `q > 1`: the bond channel has a nonzero `T_z`-odd part, and the
multiplet channel has none.  So within this framework the charge-symmetry
violation is located entirely in the bond layer, it is exactly the Hecke
deformation, and it cannot be tuned away by any choice of `q`.

Read as guidance rather than as a result: a charge-symmetric strong channel has
to come from somewhere other than an interface factor affine in the neutron
count, and the multiplet weight is the corpus's standing candidate. -/
theorem channels_opposite_parity {q : ℝ} (hq1 : 1 < q) :
    ((bondOfTz q 1 - bondOfTz q (-1)) / 2 ≠ 0)
      ∧ (∀ tz : ℤ, multipletWeight q (-tz) = multipletWeight q tz) :=
  ⟨bondOfTz_oddPart_ne_zero hq1, multipletWeight_even q⟩

end QOU.MassTheory.BondChannelTzParity
