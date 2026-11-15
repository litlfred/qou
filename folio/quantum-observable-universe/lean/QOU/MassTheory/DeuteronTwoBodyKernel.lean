import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.GCongr

/-!
# QOU.MassTheory.DeuteronTwoBodyKernel

**The two-body Markov-trace kernel over-binds the deuteron, and no admissible
colour weight in the derived neighbourhood rescues it.**

## What this file is about

The production binding form `B_sym` (`computations/mass_binding_dashboard.py`,
`_bond_type_L`) computes the deuteron — the `A = 2`, `Z = N = 1` nucleus, a
*single* p–n bond with no coordination topology, no cluster structure and no
Coulomb term — as

  `B_sym(²H) = E₀ · L_pn`,
  `E₀ = mₑ / (q₀(q₀−1))`,
  `L_pn = −log(z_D(q₀) − h(q₀)·t) − (t − ½)·log(1 − h(q₀))`,

where `z_D(q) = q³/(q²+1)` is the **convention-D** Markov parameter (owner
ruling R1, 2026-08-15), `h(q) = q − q⁻¹` is the Hecke skein parameter, the
second term is the Lean-proved writhe normalisation
(`QOU.QBeta.WritheNormalisation`, `(1−h)^(Δe/2)`), and `t` is the weight of the
`σ⁻¹` branch in the p–n colour superposition `(1−t)·σ + t·σ⁻¹`.  The
`bring_color_weighted` convention (owner ruling R3) fixes

  `t = ½ − δ(q)/4`,  `δ(q) = (q−1)²(1−q⁻⁴)/3`

— the *bar-symmetric* weight `½`, split by the leading flavour asymmetry
`δ = Δm/M_N` proved in `prop:flavor-split-substrate`.

Numerically (mpmath, 60 dps, no float64), at the canonical proton pin
`q₀ = 1.109978582751380807…` and CODATA `mₑ = 0.51099895069 MeV`:

| quantity | value |
|---|---|
| `E₀` | `4.185981363294475896945 MeV` |
| `z_D(q₀)` | `0.6126880371464652515958` |
| `h(q₀)` | `0.2090602987956393154308` |
| `δ(q₀)` | `0.001375710807027096009` |
| `t = ½ − δ/4` | `0.4996560722982432259979` |
| `E₀·L_pn` | **`2.832824919934573065733 MeV`** |
| `B_AME(²H)` | `2.2245662 MeV` |
| overshoot | **`+27.34 %`** |

`²H` is the **only** negative residual in the low-isotope table
(`R(²H) = −0.61`; every other isotope has `R > 0`), which is why it is
logically prior to the additive-term programme: a correction that is
non-negative for all `A` cannot simultaneously repair `⁴He` (which
*under*-binds) and `²H` (which *over*-binds).

## What is proved here, sorry-free

* `interfaceFactor_half` — the **exact** algebraic identity
  `z_D(q) − h(q)/2 = (q⁴+1)/(2q(q²+1))`: the bar-symmetric p–n interface factor
  is a rational function of `q` with no free constant in it.
* `bondL_strictMono` — `t ↦ L(q,t)` is **strictly increasing** on the
  admissible weight range.  Hence the whole one-parameter interface family is
  swept monotonically by `t`, and a single evaluation at either endpoint bounds
  every weight on that side.
* `overshoot_core` / `deuteron_overbinds` — for `q` in the proton-pin interval,
  `mₑ` in the CODATA interval, and **any** near-balanced weight `t ∈ [0.499, ½]`,
  `E₀·L(q,t) > 1.25 · B_AME(²H)`.  A strict, falsifiable numerical inequality:
  the two-body kernel over-binds the deuteron by more than 25 %.
* `required_weight_far_from_balanced` — conversely, **any** `t` reproducing a
  deuteron binding `≤ 2.4 MeV` satisfies `t ≤ 0.4`.
* `derived_weight_near_balanced` — the derived weight satisfies
  `t = ½ − δ/4 ≥ 0.4996`.
* `no_flavour_split_rescue` — combining the last two: the departure from
  balance that the deuteron demands exceeds `250 ×` the derived flavour split
  `δ/4`.  The colour weighting is a `10⁻³`-scale correction; the deuteron needs
  a `10⁻¹`-scale one.

## Scope of the negative — scope (a), NOT scope (b)

Per AGENTS.md §"Before declaring refuted / ruled out / dead end", the result
proved here is a **scope-(a) scope-limited negative**:

> *The two-body Markov-trace kernel `B_sym`, with the convention-D Markov
> parameter and the derived `bring_color_weighted` interface, does not
> reproduce `B_AME(²H)`; it over-binds by `+27 %`, and no interface weight
> within `250 ×` the derived flavour split closes the gap.*

It is **not** a scope-(b) structural exclusion of the `B_sym` construction.
Two invariants would be needed for that and neither is in hand:

1. The admissible interface family is `d ∈ [0, −h]`, i.e. `t ∈ [0, 1]`, and
   `B_AME(²H)` **is inside** the band — `interfaceFactor` reaches it at
   `t ≈ 0.268` (`required_weight_far_from_balanced` bounds this by `0.4`).
   So no reachability invariant excludes the target; what is excluded is
   reaching it *at the derived weight*.
2. `t` enters only through the interface factor.  A term entering
   **additively** (rather than by re-weighting the interface) is untouched by
   everything proved here.

Under the *excised* convention C (`z = √q/(q+1)`) the band was
`[2.907, 5.178] MeV` and `B_AME(²H) = 2.225` sat **below all of it** — under C
the deuteron was genuinely unreachable.  The convention-D ruling reversed that.
Do not carry the older impossibility claim forward.

## Convention-C staleness note (measured 2026-08-26)

`QOU.Hecke.ClosedFormInterfaceFactors` — the only other Lean formalisation of
the three named bond factors `f_pp`, `f_nn`, `f_pn` — defines its Markov
parameter as `markovZ s = s/(s²+1)` in the square-root variable `q = s²`, i.e.
`z = √q/(q+1)`: **convention C**, which owner ruling R1 excised.  That spelling
is invisible to every convention-C detector in the tree (none of them scan a
square-root-variable rational form), which is why it survived the 2026-08-10
drain that AGENTS.md records as having cleared `.lean` to zero.  This module
therefore does **not** import it, and states `zD` afresh; the two are not
interchangeable.  Tracked separately — do not "reconcile" them by substitution.

## References

- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] prop:flavor-split-substrate (leading `δ(q)`)
- [leitner2026] `QOU.QBeta.WritheNormalisation` (writhe factor, sorry-free)
- docs/audits/2026-08-25-low-isotope-binding-error-staleness-vs-gap.md §6 GAP-1
- computations/mass_binding_dashboard.py `_bond_type_L` (production form)
- computations/deuteron_two_body_kernel_overshoot_probe.py (the mpf numbers)
-/

namespace QOU.MassTheory.DeuteronKernel

open Real

/-! ## §1. The kernel, written out -/

/-- **Convention-D** Markov parameter `z_D(q) = q³/(q²+1)` (owner ruling R1,
2026-08-15).  NOT the excised convention-C `√q/(q+1)`. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- Hecke skein parameter `h(q) = q − q⁻¹`. -/
noncomputable def hq (q : ℝ) : ℝ := q - q⁻¹

/-- Leading flavour split `δ(q) = (q−1)²·(1 − q⁻⁴)/3`
(`prop:flavor-split-substrate`, `_li_2_q_util.flavor_split_leading`). -/
noncomputable def flavorDelta (q : ℝ) : ℝ := (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3

/-- Interface factor of the p–n bond at colour weight `t`:
`f(q,t) = z_D(q) − h(q)·t`.

`t` is the weight of the `σ⁻¹` branch in the superposition `(1−t)·σ + t·σ⁻¹`;
using the Hecke skein relation `σ⁻¹ = σ − h·1` this superposition is
`σ − h·t·1`, so `t` is exactly the scalar dressing in units of `−h`.
`t = 0` is the p–p bond (`σ`), `t = 1` the n–n bond (`σ⁻¹`). -/
noncomputable def interfaceFactor (q t : ℝ) : ℝ := zD q - hq q * t

/-- The derived colour weight `t = ½ − δ(q)/4` (`bring_color_weighted`,
owner ruling R3, 2026-08-15). -/
noncomputable def tDerived (q : ℝ) : ℝ := 1 / 2 - flavorDelta q / 4

/-- The CAL-1 × CAL-2 energy unit `E₀ = mₑ/(q(q−1))`.  `mₑ` is CAL-1 (it fixes
the MeV scale); `q` is pinned by CAL-2 through its proton proxy. -/
noncomputable def E0 (me q : ℝ) : ℝ := me / (q * (q - 1))

/-- Writhe-normalised per-bond log-suppression
`L(q,t) = −log f(q,t) − (t − ½)·log(1 − h(q))`.

The second term is the writhe normalisation `(1−h)^(Δe/2)` forced by Markov
invariance (`QOU.QBeta.WritheNormalisation`, sorry-free, unique up to sign);
for the colour superposition the exponent-sum expectation is `Δe = 2t − 1`. -/
noncomputable def bondL (q t : ℝ) : ℝ :=
  -Real.log (interfaceFactor q t) - (t - 1 / 2) * Real.log (1 - hq q)

/-- The two-body deuteron binding `B_sym(²H) = E₀ · L(q,t)`. -/
noncomputable def BSymDeuteron (me q t : ℝ) : ℝ := E0 me q * bondL q t

/-! ## §2. Two elementary logarithm bounds

Both are consequences of `Real.log_le_sub_one_of_pos`; they are what turns the
numerical claims below into rational arithmetic. -/

/-- `−log x ≥ log 2 + 1 − 2x` for `x > 0`.  Tight near `x = ½`, which is where
the deuteron interface factor sits — the bound loses only `1.7 × 10⁻⁴` there. -/
theorem neg_log_lower {x : ℝ} (hx : 0 < x) :
    Real.log 2 + 1 - 2 * x ≤ -Real.log x := by
  have h2 : Real.log (2 * x) ≤ 2 * x - 1 := Real.log_le_sub_one_of_pos (by linarith)
  rw [Real.log_mul (by norm_num) (ne_of_gt hx)] at h2
  linarith

/-- `log x ≥ 1 − x⁻¹` for `x > 0`. -/
theorem log_ge_one_sub_inv {x : ℝ} (hx : 0 < x) : 1 - x⁻¹ ≤ Real.log x := by
  have h := Real.log_le_sub_one_of_pos (inv_pos.mpr hx)
  rw [Real.log_inv] at h
  linarith

/-! ## §3. The bar-symmetric interface factor is an exact rational function -/

/-- **The bar-symmetric p–n interface factor has a closed rational form.**

At the bar-symmetric weight `t = ½` the writhe exponent `Δe = 2t − 1` vanishes,
so the writhe factor is exactly `1` and the entire bond energy is
`E₀ · log(1 / f)` with

  `f = z_D(q) − h(q)/2 = (q⁴+1) / (2q(q²+1))`.

Every constant on the right-hand side is fixed: there is no scale, no
normalisation and no fitted coefficient anywhere in it. -/
theorem interfaceFactor_half {q : ℝ} (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    interfaceFactor q (1 / 2) = (q ^ 4 + 1) / (2 * q * (q ^ 2 + 1)) := by
  unfold interfaceFactor zD hq
  field_simp
  ring

/-- The writhe factor is exactly trivial at the bar-symmetric weight. -/
theorem bondL_half (q : ℝ) :
    bondL q (1 / 2) = -Real.log (interfaceFactor q (1 / 2)) := by
  unfold bondL
  norm_num

/-! ## §4. Monotonicity of the bond energy in the colour weight -/

/-- **The bond energy is strictly increasing in the colour weight `t`.**

Both terms increase with `t`: the interface factor `z − h·t` decreases (so
`−log` of it increases), and `−(t − ½)·log(1 − h)` increases because
`log(1 − h) < 0`.  Consequently the admissible interface family is swept
monotonically, `t = 0` (p–p) is its minimum and `t = 1` (n–n) its maximum, and
a bound at one weight bounds every weight on that side. -/
theorem bondL_strictMono {q : ℝ} (hh0 : 0 < hq q) (hh1 : hq q < 1)
    {t₁ t₂ : ℝ} (hlt : t₁ < t₂) (hpos : 0 < interfaceFactor q t₂) :
    bondL q t₁ < bondL q t₂ := by
  have hpos₁ : 0 < interfaceFactor q t₁ := by
    unfold interfaceFactor at hpos ⊢
    nlinarith [mul_lt_mul_of_pos_left hlt hh0]
  have hlt' : interfaceFactor q t₂ < interfaceFactor q t₁ := by
    unfold interfaceFactor
    nlinarith [mul_lt_mul_of_pos_left hlt hh0]
  have hlog : Real.log (interfaceFactor q t₂) < Real.log (interfaceFactor q t₁) :=
    Real.log_lt_log hpos hlt'
  have hlw : Real.log (1 - hq q) < 0 := Real.log_neg (by linarith) (by linarith)
  have hw : (t₂ - 1 / 2) * Real.log (1 - hq q) < (t₁ - 1 / 2) * Real.log (1 - hq q) := by
    exact mul_lt_mul_of_neg_right (by linarith) hlw
  unfold bondL
  linarith

/-! ## §5. The overshoot

The numerical core is stated on abstract reals with interval hypotheses, so
that the arithmetic is separated from the substrate instantiation and each half
is checkable on its own. -/

/-- **Numerical core of the deuteron overshoot.**

For a Markov parameter, skein parameter and energy unit inside the intervals
that the proton-pinned substrate and CODATA `mₑ` actually determine, and for
**any** near-balanced colour weight `t ∈ [0.499, ½]`, the two-body bond energy
exceeds `1.25 ×` the experimental deuteron binding.

The bound is proved through the rational chain

  `f ≤ 0.5083671`,
  `−log f ≥ log 2 + 1 − 2f ≥ 0.6764130`,
  `(½ − t)·log(1 − h) ≥ 0.001 · (1 − (1 − h)⁻¹) ≥ −0.0002644`,
  `E · L ≥ 4.185980 × 0.6761486 = 2.83034 > 2.78071 = 1.25 × 2.2245666`. -/
theorem overshoot_core {z hh E t B : ℝ}
    (hzlo : (0.6126879 : ℝ) ≤ z) (hzhi : z ≤ 0.6126881)
    (hhlo : (0.2090601 : ℝ) ≤ hh) (hhhi : hh ≤ 0.2090604)
    (hE : (4.185980 : ℝ) ≤ E)
    (htlo : (0.499 : ℝ) ≤ t) (hthi : t ≤ 1 / 2)
    (hB : B ≤ 2.2245666) :
    1.25 * B < E * (-Real.log (z - hh * t) - (t - 1 / 2) * Real.log (1 - hh)) := by
  -- the interface factor, bracketed
  have hht : (0.2090601 : ℝ) * 0.499 ≤ hh * t :=
    mul_le_mul hhlo htlo (by norm_num) (by linarith)
  have hht' : hh * t ≤ 0.2090604 * (1 / 2) :=
    mul_le_mul hhhi hthi (by linarith) (by norm_num)
  have hfhi : z - hh * t ≤ 0.5083672 := by nlinarith
  have hflo : (0.5081577 : ℝ) ≤ z - hh * t := by nlinarith
  have hfpos : 0 < z - hh * t := by linarith
  -- lower bound on −log f, via `log 2 + 1 − 2f ≤ −log f`
  have h1 : Real.log 2 + 1 - 2 * (z - hh * t) ≤ -Real.log (z - hh * t) :=
    neg_log_lower hfpos
  have h2 : (0.6931471803 : ℝ) < Real.log 2 := Real.log_two_gt_d9
  have hneg : (0.6764129 : ℝ) ≤ -Real.log (z - hh * t) := by linarith
  -- lower bound on the writhe term, via `1 − x⁻¹ ≤ log x`
  have hone : (0 : ℝ) < 1 - hh := by linarith
  have hipos : 0 < (1 - hh)⁻¹ := inv_pos.mpr hone
  have hcan : (1 - hh) * (1 - hh)⁻¹ = 1 := mul_inv_cancel₀ (ne_of_gt hone)
  have hinv : (1 - hh)⁻¹ ≤ 1.2643191 := by nlinarith
  have hlw : (-0.2643191 : ℝ) ≤ Real.log (1 - hh) := by
    have hlog := Real.log_le_sub_one_of_pos hipos
    rw [Real.log_inv] at hlog
    linarith
  have hlwn : Real.log (1 - hh) ≤ 0 := Real.log_nonpos (by linarith) (by linarith)
  have hwrithe : (-0.0002644 : ℝ) ≤ -(t - 1 / 2) * Real.log (1 - hh) := by
    nlinarith
  -- assemble
  have hbond : (0.6761485 : ℝ) ≤
      -Real.log (z - hh * t) - (t - 1 / 2) * Real.log (1 - hh) := by linarith
  have hprod : (4.185980 : ℝ) * 0.6761485 ≤
      E * (-Real.log (z - hh * t) - (t - 1 / 2) * Real.log (1 - hh)) :=
    mul_le_mul hE hbond (by norm_num) (by linarith)
  nlinarith

/-- **The two-body Markov-trace kernel over-binds the deuteron by more than
25 %.**

Stated at the canonical proton pin `q₀ ∈ [1.1099785, 1.1099786]` and CODATA
`mₑ ∈ [0.5109989, 0.5109990]`, for any near-balanced colour weight.  The
measured value is `+27.34 %`; `1.25` is the margin that survives the rational
bounding chain above. -/
theorem deuteron_overbinds {me q t B : ℝ}
    (hzlo : (0.6126879 : ℝ) ≤ zD q) (hzhi : zD q ≤ 0.6126881)
    (hhlo : (0.2090601 : ℝ) ≤ hq q) (hhhi : hq q ≤ 0.2090604)
    (hE : (4.185980 : ℝ) ≤ E0 me q)
    (htlo : (0.499 : ℝ) ≤ t) (hthi : t ≤ 1 / 2)
    (hB : B ≤ 2.2245666) :
    1.25 * B < BSymDeuteron me q t := by
  unfold BSymDeuteron bondL interfaceFactor
  exact overshoot_core hzlo hzhi hhlo hhhi hE htlo hthi hB

/-! ## §6. The weight the deuteron would demand -/

/-- **Any colour weight reproducing a deuteron binding of at most `2.4 MeV`
lies at or below `0.4`.**

Contrapositive of the same bounding chain evaluated at `t = 0.4`, where the
bond energy is already `≥ 2.547 MeV`.  Since `B_AME(²H) = 2.2246 < 2.4`, the
experimental deuteron is reachable in this family only at `t ≤ 0.4` — a
departure of at least `0.0996` from the bar-symmetric weight `½`. -/
theorem required_weight_far_from_balanced {me q t : ℝ}
    (hzlo : (0.6126879 : ℝ) ≤ zD q) (hzhi : zD q ≤ 0.6126881)
    (hhlo : (0.2090601 : ℝ) ≤ hq q) (hhhi : hq q ≤ 0.2090604)
    (hE : (4.185980 : ℝ) ≤ E0 me q)
    (hthi : t ≤ 1 / 2)
    (hbind : BSymDeuteron me q t ≤ 2.4) :
    t ≤ 0.4 := by
  by_contra hcon
  push_neg at hcon
  set hh := hq q with hhdef
  set z := zD q with hzdef
  set E := E0 me q with hEdef
  have hht : (0.2090601 : ℝ) * 0.4 ≤ hh * t :=
    mul_le_mul hhlo (le_of_lt hcon) (by norm_num) (by linarith)
  have hht' : hh * t ≤ 0.2090604 * (1 / 2) :=
    mul_le_mul hhhi hthi (by linarith) (by norm_num)
  have hfhi : z - hh * t ≤ 0.5290641 := by nlinarith
  have hfpos : (0 : ℝ) < z - hh * t := by nlinarith
  have h1 : Real.log 2 + 1 - 2 * (z - hh * t) ≤ -Real.log (z - hh * t) :=
    neg_log_lower hfpos
  have h2 : (0.6931471803 : ℝ) < Real.log 2 := Real.log_two_gt_d9
  have hneg : (0.6350190 : ℝ) ≤ -Real.log (z - hh * t) := by linarith
  have hone : (0 : ℝ) < 1 - hh := by linarith
  have hipos : 0 < (1 - hh)⁻¹ := inv_pos.mpr hone
  have hcan : (1 - hh) * (1 - hh)⁻¹ = 1 := mul_inv_cancel₀ (ne_of_gt hone)
  have hinv : (1 - hh)⁻¹ ≤ 1.2643191 := by nlinarith
  have hlw : (-0.2643191 : ℝ) ≤ Real.log (1 - hh) := by
    have hlog := Real.log_le_sub_one_of_pos hipos
    rw [Real.log_inv] at hlog
    linarith
  have hlwn : Real.log (1 - hh) ≤ 0 := Real.log_nonpos (by linarith) (by linarith)
  have hwrithe : (-0.0264320 : ℝ) ≤ -(t - 1 / 2) * Real.log (1 - hh) := by
    nlinarith
  have hbond : (0.6085870 : ℝ) ≤
      -Real.log (z - hh * t) - (t - 1 / 2) * Real.log (1 - hh) := by linarith
  have hprod : (4.185980 : ℝ) * 0.6085870 ≤
      E * (-Real.log (z - hh * t) - (t - 1 / 2) * Real.log (1 - hh)) :=
    mul_le_mul hE hbond (by norm_num) (by linarith)
  unfold BSymDeuteron bondL interfaceFactor at hbind
  rw [← hhdef, ← hzdef, ← hEdef] at hbind
  nlinarith

/-! ## §7. The derived colour weight is not the demanded one -/

/-- The derived weight `t = ½ − δ(q)/4` is near-balanced: on the proton-pin
interval `δ(q)/4 < 3.45 × 10⁻⁴`, so `t ≥ 0.4996`. -/
theorem flavorDelta_small {q : ℝ}
    (hq1 : (1.1099785 : ℝ) ≤ q) (hq2 : q ≤ 1.1099786) :
    0 ≤ flavorDelta q ∧ flavorDelta q ≤ 0.001377 := by
  have hq0 : (0 : ℝ) ≤ q := by linarith
  have hq4pos : (0 : ℝ) < q ^ 4 := by positivity
  have hq4hi : q ^ 4 ≤ 1.5180 := by
    calc q ^ 4 ≤ (1.1099786 : ℝ) ^ 4 := by gcongr
      _ ≤ 1.5180 := by norm_num
  have hipos : 0 < (q ^ 4)⁻¹ := inv_pos.mpr hq4pos
  have hcan : q ^ 4 * (q ^ 4)⁻¹ = 1 := mul_inv_cancel₀ (ne_of_gt hq4pos)
  have hinvlo : (0.6587 : ℝ) ≤ (q ^ 4)⁻¹ := by nlinarith
  have hq4lo : (1 : ℝ) ≤ q ^ 4 := one_le_pow₀ (by linarith)
  have hinvhi : (q ^ 4)⁻¹ ≤ 1 := by nlinarith
  have hsq : (q - 1) ^ 2 ≤ 0.01209530 := by nlinarith
  have hsq0 : (0 : ℝ) ≤ (q - 1) ^ 2 := sq_nonneg _
  constructor
  · unfold flavorDelta; nlinarith
  · unfold flavorDelta; nlinarith

/-- **The derived colour weight is bar-balanced to one part in a thousand.**

`t = ½ − δ(q)/4 ∈ [0.4996, ½]` on the proton-pin interval: the
`bring_color_weighted` convention displaces the p–n interface from the
bar-symmetric superposition by less than `3.5 × 10⁻⁴`. -/
theorem derived_weight_near_balanced {q : ℝ}
    (hq1 : (1.1099785 : ℝ) ≤ q) (hq2 : q ≤ 1.1099786) :
    (0.4996 : ℝ) ≤ tDerived q ∧ tDerived q ≤ 1 / 2 := by
  obtain ⟨hd0, hdhi⟩ := flavorDelta_small hq1 hq2
  constructor
  · unfold tDerived; linarith
  · unfold tDerived; linarith

/-- **The flavour split cannot rescue the deuteron.**

The derived colour weight sits within `δ/4 < 3.5 × 10⁻⁴` of the bar-symmetric
value `½`; any weight reproducing a deuteron binding of at most `2.4 MeV` lies
at or below `0.4`, i.e. at least `0.0996` below balance.  The departure the
deuteron demands therefore exceeds `250 ×` the entire derived flavour split.

This is the sharp form of the negative.  The p–n colour weighting is a
`10⁻³`-scale structure and the deuteron gap is a `10⁻¹`-scale one, so no
refinement of `δ` — subleading corrections included — reaches it. -/
theorem no_flavour_split_rescue {me q t : ℝ}
    (hq1 : (1.1099785 : ℝ) ≤ q) (hq2 : q ≤ 1.1099786)
    (hzlo : (0.6126879 : ℝ) ≤ zD q) (hzhi : zD q ≤ 0.6126881)
    (hhlo : (0.2090601 : ℝ) ≤ hq q) (hhhi : hq q ≤ 0.2090604)
    (hE : (4.185980 : ℝ) ≤ E0 me q)
    (hthi : t ≤ 1 / 2)
    (hbind : BSymDeuteron me q t ≤ 2.4) :
    250 * (flavorDelta q / 4) < tDerived q - t := by
  have hle : t ≤ 0.4 :=
    required_weight_far_from_balanced hzlo hzhi hhlo hhhi hE hthi hbind
  have hd := (derived_weight_near_balanced hq1 hq2).1
  have hdhi := (flavorDelta_small hq1 hq2).2
  linarith

end QOU.MassTheory.DeuteronKernel
