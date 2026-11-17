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

**PROVENANCE — most of §2 is a RE-DERIVATION, and saying so is the point.**
An earlier version of this docstring claimed the defect "was not formalised".
That is false, and a corpus-grep found the prior art after the file was written:

* `QOU.MassTheory.BondChargeRule.sumRule_like_pairs_differ` already proves the
  like-pair difference, in an abstract charge parameterisation
  (`sumRule c qi qj = (qi+qj−1)·c`, giving `2c`), and its own docstring cites
  bean `qou-1pig` and writes `f_pp − f_nn = h = 2·(h/2)`.  So
  `bondOfTz_pp_sub_nn` and the *magnitude* `h/2` of `bondOfTz_oddPart` are not
  new; this file restates them in the `T_z` variable.
* `computations/probes/pair-layer-isospin-parity.witness.json` already records
  the same thing as a measurement: "the charge-antisymmetric (isovector) part of
  the like-pair channel is `h/2`, **forced exactly by the Hecke skein relation**",
  together with a number this file does not produce — the isovector term is
  **1454×** the isoscalar one — and the observation that `bring_color_weighted`
  cannot repair it, since it touches only the self-conjugate p–n factor.

What is NOT in that prior art, and is what this file contributes:

1. **The `iff`, quantified over `q`** — `bondOfTz_even_iff` /
   `bondOfTz_even_iff_classical`.  The prior work computes the difference at the
   substrate; this characterises *when it vanishes at all*, and the answer is
   only `q = 1`.  That turns a measured defect into a structural exclusion.
2. **The energy level, including the writhe term** — `writheExponent_odd` shows
   the writhe normalisation is *itself* purely `T_z`-odd, so it adds a second odd
   term rather than cancelling the first; `bondL_pp_ne_nn` then follows from
   `bondL_strictMono`, already proved in the imported file and used rather than
   re-proved.
3. **The parity separation** — `multipletWeight_even` and
   `channels_opposite_parity`, against bean `qou-xwur`'s two-row channel.

**Related prior work that prices the obvious repair, and it LOSES.**  Bean
`qou-nial` proposes replacing the centred *sum* rule with a charge *product*
rule, under which `prodRule_like_pairs_are_strong_baseline` makes the strong
channel exactly charge-symmetric.  Measured over 12 nuclei ²H–⁵⁶Fe against
AME2020 (`bond_rule_dashboard_comparison_probe.py`), mean `|ln(model/AME)|` goes
**0.808 → 0.940**: worse.  Its A=3 mirror agreement is "a flat line crossing a
rising curve" — flat in `A`, identical at `A = 7` where the observed splitting
has doubled.  Its own recommendation is *do not switch*.  So evenness in `T_z` is
**not** by itself sufficient, and this file should not be read as arguing for that
substitution.

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

/-! ## §7. A charge-blind multiplier cannot change the `T_z` parity ratio

Added 2026-09-14 (bean `qou-vwu3`), and it generalises a measurement rather than
restating one.  The extensive-term arc's one surviving lead is the Markov trace's
failure of **bond-multiplicativity**: on an interleaved word class the trace of a
product of bond letters is not the product of their traces
(`docs/audits/2026-09-03-markov-trace-not-bond-multiplicative-n4.md`, bean
`qou-kru4`).  That defect reads the braid *word* beyond its linking data, which is
exactly what bean `qou-brng` leaves open after closing the Ocneanu trace family, the
magnitude, `μ̄₁₂₃` and the whole linking-data class.

Measured exactly this session with charge-**dressed** letters `b_i = σ_i + d_i·1`
(`computations/probes/dressed_interleaved_cross_term_charge_parity_probe.py`, 11/11,
sympy over `ℚ(q,d₀,d₁,d₂)`, with the bare limit reproducing the recorded closed form
as its control):

    Δ(d₀,d₁,d₂) = (z + d₂) · (z² − h z − 1)          exactly,

with `d₀` and `d₁` **absent** — the two interleaved bonds drop out, and only the
Markov-peeled bond survives.  So the defect *is* charge-sensitive, and its entire
charge dependence is one bond factor times the charge-blind scalar `z² − hz − 1`.

This section proves the consequence, and it is the general statement rather than
the instance: **multiplying by anything charge-blind cannot move a mirror odd/even
ratio.**  Any proposal of the shape "keep the bond factor, multiply it by a new
scalar" therefore inherits §3's exclusion verbatim, whatever the scalar is.

**🛑 SCOPE — the `n = 4` factorisation does NOT generalise, measured the same day.**
`parity_ratio_const_mul` is a theorem about a charge-blind multiplier and is
unconditional.  What is *word-specific* is the premise that the cross term HAS that
shape.  The same probe extended to `n = 5`, with two re-crossings
(`b₀b₁b₀b₂b₁b₃b₂` against `b₀²b₁²b₂²b₃`) and symbolic `q`, gives

    Δ₅ = f₃ · (z² − hz − 1) · ( f₀² + f₂² + (q⁴+1)/(q²+1)² )

— the *peeled* bond still factors out linearly, but the two **interleaved** bonds
now enter **quadratically** (additively, with no `f₀f₂` cross term), so the
mirror-even part becomes charge-dependent and the parity ratio is **no longer
forced**.  Measured: `Δ₅ odd/even ≠ f odd/even`.

So do **not** cite §7 as closing the word-class route.  It closes the `n = 4`
cross term, and the mechanism it closes — "bond factor × charge-blind scalar" —
whenever a construction actually has that shape.  At `n = 5` the route is open, and
the interesting object is the sum of squares.  Bean `qou-vwu3`. -/

/-- Mirror-even part of a function of the pair isospin projection. -/
noncomputable def evenPart (F : ℝ → ℝ) (tz : ℝ) : ℝ := (F tz + F (-tz)) / 2

/-- Mirror-odd part of a function of the pair isospin projection. -/
noncomputable def oddPart (F : ℝ → ℝ) (tz : ℝ) : ℝ := (F tz - F (-tz)) / 2

@[simp] theorem evenPart_const_mul (c : ℝ) (F : ℝ → ℝ) (tz : ℝ) :
    evenPart (fun t => c * F t) tz = c * evenPart F tz := by
  unfold evenPart; ring

@[simp] theorem oddPart_const_mul (c : ℝ) (F : ℝ → ℝ) (tz : ℝ) :
    oddPart (fun t => c * F t) tz = c * oddPart F tz := by
  unfold oddPart; ring

/-- **A charge-blind multiplier leaves the parity ratio exactly fixed.**

`c` is any nonzero scalar not depending on `T_z`.  Both parts scale by `c`, so the
ratio does not move at all — no choice of `c`, however large, however `q`-dependent,
changes it. -/
theorem parity_ratio_const_mul {c : ℝ} (hc : c ≠ 0) (F : ℝ → ℝ) (tz : ℝ) :
    oddPart (fun t => c * F t) tz / evenPart (fun t => c * F t) tz
      = oddPart F tz / evenPart F tz := by
  rw [evenPart_const_mul, oddPart_const_mul, mul_div_mul_left _ _ hc]

/-- The convention-D Markov defect `z² − hz − 1`.  It is a function of `q` alone, so
it is charge-blind by construction — that is the whole reason §7 applies to it. -/
noncomputable def markovDefect (q : ℝ) : ℝ := zD q ^ 2 - hq q * zD q - 1

/-- The `n = 4` interleaved cross term, as a function of the peeled bond's isospin
projection: `Δ(T_z) = f(T_z) · (z² − hz − 1)`, the identity measured above. -/
noncomputable def crossTerm (q tz : ℝ) : ℝ := bondOfTz q tz * markovDefect q

/-- **The cross term's parity ratio is the bond factor's own.**

So the interleaved word class changes the *magnitude* of the bond channel — which is
what `qou-kru4` wants it for, the defect being negative and hence extra binding — and
provably does **not** change its charge parity. -/
theorem crossTerm_parity_ratio_eq_bond {q : ℝ} (hd : markovDefect q ≠ 0) (tz : ℝ) :
    oddPart (crossTerm q) tz / evenPart (crossTerm q) tz
      = oddPart (bondOfTz q) tz / evenPart (bondOfTz q) tz := by
  have hfun : crossTerm q = fun t => markovDefect q * bondOfTz q t := by
    funext t; unfold crossTerm; ring
  rw [hfun, parity_ratio_const_mul hd]

/-- **The cross term is even in `T_z` iff the bond factor is** (given a nonvanishing
defect) — so §3's exclusion transfers: at every `q > 1` the cross term is odd too. -/
theorem crossTerm_even_iff {q : ℝ} (hd : markovDefect q ≠ 0) :
    (∀ tz : ℝ, crossTerm q tz = crossTerm q (-tz)) ↔ hq q = 0 := by
  constructor
  · intro hall
    refine (bondOfTz_even_iff q).mp ?_
    intro tz
    have := hall tz
    unfold crossTerm at this
    exact mul_right_cancel₀ hd this
  · intro h tz
    unfold crossTerm
    rw [(bondOfTz_even_iff q).mpr h tz]

/-- The defect does not vanish at any `q > 1`: `z² − hz − 1 = −(q⁴+q²+1)/(q²+1)²`,
which is strictly negative. -/
theorem markovDefect_ne_zero {q : ℝ} (hq0 : 0 < q) : markovDefect q ≠ 0 := by
  have hq2 : (0:ℝ) < q ^ 2 + 1 := by positivity
  have hne : (q ^ 2 + 1) ≠ 0 := ne_of_gt hq2
  have hq0' : q ≠ 0 := ne_of_gt hq0
  have key : markovDefect q = -((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) := by
    unfold markovDefect zD hq
    field_simp
    ring
  rw [key]
  have hnum : (0:ℝ) < q ^ 4 + q ^ 2 + 1 := by positivity
  have : (0:ℝ) < (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by positivity
  linarith [this]

/-- **The transfer, stated as the prune it is.**  At every `q > 1` the interleaved
cross term has a nonzero `T_z`-odd part, with the *same* odd/even ratio as the bond
factor it multiplies.  The word-class route can supply magnitude; it cannot supply a
different charge structure. -/
theorem crossTerm_oddPart_ne_zero {q : ℝ} (hq1 : 1 < q) :
    oddPart (crossTerm q) 1 ≠ 0 := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  have hd := markovDefect_ne_zero hq0
  have hfun : crossTerm q = fun t => markovDefect q * bondOfTz q t := by
    funext t; unfold crossTerm; ring
  rw [hfun, oddPart_const_mul]
  have hb : oddPart (bondOfTz q) 1 ≠ 0 := by
    unfold oddPart
    simpa using bondOfTz_oddPart_ne_zero hq1
  exact mul_ne_zero hd hb

/-! ## §8. The parity ratio is EXACTLY linear in `T_z`, with slope `(q⁴−1)/(q⁴+1)`

Added 2026-09-14 (bean `qou-vwu3`, second tranche).  §7 shows the `n = 4` cross
term inherits the bond factor's parity ratio; this computes that ratio in closed
form, and the answer is tighter than "inherits":

    oddPart / evenPart  =  ((q⁴ − 1)/(q⁴ + 1)) · T_z        exactly.

So on the physical range `|T_z| ≤ 1` the ratio is **capped** at `(q⁴−1)/(q⁴+1)`,
attained only at the pure like-pairs `T_z = ±1`.  Nothing in the interleaved
`n = 4` word can exceed it, for any bond assignment.

**Only algebra appears below.**  The comparison against a measured mirror
splitting is deliberately NOT formalised — it belongs in the probe and the bean,
not in a proof.  What Lean carries is the cap; what the cap is worth is an
empirical question asked elsewhere.

**And the cap is a statement about `n = 4` alone.**  Measured the same day, the
achievable `|ratio|` at the proton anchor grows with word length —
`0.2057` at `n = 4`, `0.3928` at `n = 5`, `0.4935` at `n = 6` — because more
dressings enter the kernel quadratically and the mirror image can be driven
closer to zero.  `ratio = (a − b)/(a + b)` with `a`, `b` the value and its
mirror, so `|ratio| < 1` exactly while `a` and `b` share a sign, and the
envelope approaches `1` as the slot count grows.  **A longer word can therefore
be made to bracket any target below 1, which is why reaching one by choosing `n`
is selection against the target and not a derivation.** -/

/-- The exact parity-ratio slope of the bond channel: `(q⁴ − 1)/(q⁴ + 1)`. -/
noncomputable def parityRatioSlope (q : ℝ) : ℝ := (q ^ 4 - 1) / (q ^ 4 + 1)

/-- **The parity ratio is exactly `slope · T_z`.**

Both parts were computed in §2: the odd part is `(h/2)·T_z` and the even part is
the constant `z_D − h/2 = (q⁴+1)/(2q(q²+1))`.  Their quotient collapses to
`(q⁴−1)/(q⁴+1)` times `T_z`, with the `2q(q²+1)` cancelling against `h = q − q⁻¹`. -/
theorem bondOfTz_parity_ratio_eq {q : ℝ} (hq0 : 0 < q) (tz : ℝ) :
    oddPart (bondOfTz q) tz / evenPart (bondOfTz q) tz = parityRatioSlope q * tz := by
  -- `hqne`, not `hq`: `hq` is the Hecke-parameter FUNCTION in this namespace, and a
  -- local hypothesis of that name shadows it, so `hq q` then elaborates as applying
  -- the hypothesis to `q`.  That is what the first draft of this proof did.
  have hqne : q ≠ 0 := ne_of_gt hq0
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  have h4 : q ^ 4 + 1 ≠ 0 := by positivity
  have hodd : oddPart (bondOfTz q) tz = hq q / 2 * tz := by
    unfold oddPart
    have := bondOfTz_oddPart q tz
    unfold oddPart at this
    linarith [this]
  have heven : evenPart (bondOfTz q) tz = zD q - hq q / 2 := by
    unfold evenPart
    have := bondOfTz_evenPart q tz
    unfold evenPart at this
    linarith [this]
  rw [hodd, heven]
  have hev : zD q - hq q / 2 = (q ^ 4 + 1) / (2 * q * (q ^ 2 + 1)) := by
    unfold zD hq; field_simp; ring
  rw [hev]
  unfold parityRatioSlope hq
  field_simp
  ring

/-- The slope is strictly positive for `q > 1`, and strictly below `1` for every
`q` — so the ratio is bounded by `1` in magnitude on `|T_z| ≤ 1`, whatever `q` is. -/
theorem parityRatioSlope_lt_one {q : ℝ} (hq0 : 0 < q) : parityRatioSlope q < 1 := by
  unfold parityRatioSlope
  rw [div_lt_one (by positivity)]
  linarith

/-- `1 ≤ q` forces `1 ≤ q⁴` — the step both bounds below need. -/
theorem one_le_pow_four {q : ℝ} (hq1 : 1 ≤ q) : 1 ≤ q ^ 4 := by
  have h2 : 1 ≤ q ^ 2 := by nlinarith
  nlinarith [sq_nonneg (q ^ 2 - 1)]

theorem parityRatioSlope_nonneg {q : ℝ} (hq1 : 1 ≤ q) : 0 ≤ parityRatioSlope q := by
  unfold parityRatioSlope
  apply div_nonneg _ (by positivity)
  linarith [one_le_pow_four hq1]

theorem parityRatioSlope_pos {q : ℝ} (hq1 : 1 < q) : 0 < parityRatioSlope q := by
  unfold parityRatioSlope
  apply div_pos _ (by positivity)
  have h2 : 1 < q ^ 2 := by nlinarith
  nlinarith [sq_nonneg (q ^ 2 - 1)]

/-- **THE CAP.**  On the physical range `|T_z| ≤ 1` the `n = 4` parity ratio
cannot exceed `(q⁴−1)/(q⁴+1)` in magnitude, for any bond assignment.

This is the scope-(b) content of the second tranche: it is not that the observed
ratio is missed by some amount, it is that the interleaved `n = 4` cross term has
no assignment reaching past this bound at all. -/
theorem bondOfTz_parity_ratio_cap {q : ℝ} (hq1 : 1 ≤ q) {tz : ℝ} (htz : |tz| ≤ 1) :
    |oddPart (bondOfTz q) tz / evenPart (bondOfTz q) tz| ≤ parityRatioSlope q := by
  have hq0 : 0 < q := lt_of_lt_of_le zero_lt_one hq1
  rw [bondOfTz_parity_ratio_eq hq0, abs_mul]
  have hs : |parityRatioSlope q| = parityRatioSlope q :=
    abs_of_nonneg (parityRatioSlope_nonneg hq1)
  rw [hs]
  calc parityRatioSlope q * |tz| ≤ parityRatioSlope q * 1 := by
        apply mul_le_mul_of_nonneg_left htz
        rw [← hs]; exact abs_nonneg _
    _ = parityRatioSlope q := by ring

/-- The same cap transfers to the `n = 4` interleaved cross term, by §7. -/
theorem crossTerm_parity_ratio_cap {q : ℝ} (hq1 : 1 ≤ q) (hd : markovDefect q ≠ 0)
    {tz : ℝ} (htz : |tz| ≤ 1) :
    |oddPart (crossTerm q) tz / evenPart (crossTerm q) tz| ≤ parityRatioSlope q := by
  rw [crossTerm_parity_ratio_eq_bond hd]
  exact bondOfTz_parity_ratio_cap hq1 htz


/-- **Classical vanishing `parityRatioSlope 1 = 0` and Cayley `q⁴` recovery identities (`qou-vwu3`).**
At `q = 1`, `parityRatioSlope 1 = 0`, and for every `q : ℝ`,
`(1 + parityRatioSlope q) * (q ^ 4 + 1) = 2 * q ^ 4` and `(1 - parityRatioSlope q) * (q ^ 4 + 1) = 2`. -/
theorem parityRatioSlope_at_one_and_cayley (q : ℝ) :
    parityRatioSlope 1 = 0 ∧
      (1 + parityRatioSlope q) * (q ^ 4 + 1) = 2 * q ^ 4 ∧
      (1 - parityRatioSlope q) * (q ^ 4 + 1) = 2 := by
  have h4 : (q ^ 4 + 1 : ℝ) ≠ 0 := by positivity
  refine ⟨by unfold parityRatioSlope; norm_num, ?_, ?_⟩
  · unfold parityRatioSlope; field_simp; ring
  · unfold parityRatioSlope; field_simp; ring

end QOU.MassTheory.BondChannelTzParity
