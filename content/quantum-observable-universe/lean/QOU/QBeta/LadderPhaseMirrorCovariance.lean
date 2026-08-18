/-
Copyright (c) 2026 litlfred. All rights reserved.

# The ladder phase is mirror-covariant iff the Markov parameter is bar-invariant

Bean `qou-cds1` (convention C -> D re-derivation of the Q_beta precision
ladder). This file answers, structurally, why the asserted phase

  `alpha = (z - 1) * h / 2`,  `h = q - q⁻¹`

behaves so differently in the two Markov-parameter conventions, and what its
bar-odd part is in the frame where it is not already bar-odd.

## The argument

The Ocneanu / Markov trace on `H_n(q)` is NOT a link invariant on its own: the
two stabilisation loop values are distinct (`tr(x sigma_n) = z tr(x)` versus
`tr(x sigma_n⁻¹) = (z - h) tr(x)`), and invariance under both Markov moves is
restored by a **writhe-dependent prefactor outside the trace** (Jones 1987 §5;
`QOU.BraidKnot.jones_markov_trace` docstring; block
`prop:jones-markov-trace-stabilisation`).

Writhe is **odd under mirror image** — proved in this corpus, generically over
braid words, as
`QOU.StandardModel.WritheMarkovInvariance.writhe_inv : writhe (inv a) = -writhe a`
— and the mirror acts on the Hecke side as the bar involution `q ↦ q⁻¹`. So a
phase carried by the framing prefactor must be **bar-ODD**. That is the
constraint this file tests the two conventions against.

## What is proved (all sorry-free, all over a generic `CommRing`/`Field` — §7c)

1. `phaseTwice_bar_anomaly` — the completely general identity, pure `ring`:
   for `2*alpha = (z - 1) * h` with `h` bar-odd,
   `bar(2 alpha) + 2 alpha = h * (z - bar z)`.
   **The bar-anomaly of the phase is `h` times the bar-anomaly of `z`.**
2. `phaseTwice_bar_odd_iff_z_bar_fixed` — hence over a domain with `h ≠ 0`,
   the phase is bar-odd **iff** `z` is exactly bar-invariant. This is an iff,
   not a sufficient condition: bar-oddness of the phase *characterises*
   bar-invariance of the Markov parameter.
3. `zC_bar_fixed` — convention C (`z = √q/(1+q)`, in the half-power coordinate
   `s`, `s² = q`) is exactly bar-invariant, hence `phaseTwiceC_bar_odd`:
   **the C-frame phase is bar-odd, and it is so by structure.** (The
   bar-invariance itself is `QOU.QBeta.z_bar_invariant_field`, PR #3449; this
   file only draws the phase consequence.)
4. `zD_sub_bar_eq_h` — convention D (`z = q³/(q²+1)`) is **not** bar-invariant,
   and its anomaly is exactly `h`:  `z_D - bar(z_D) = q - q⁻¹`.
5. `phaseTwiceD_bar_anomaly` — therefore `bar(2 alpha_D) + 2 alpha_D = h²`
   (equivalently `bar(alpha_D) + alpha_D = h²/2`), and
6. `phaseTwiceD_sub_hsq_bar_odd` — the **bar-odd part** of the D-frame
   phase is `2 alpha_D - h²/2`, i.e. `alpha_D - h²/4`.

## Scope — what this does NOT do

Item 6 identifies a projection; it does not claim that projection reproduces
`Q_beta`. Numerically the projected D phase closes 92.03 % of the D-frame gap
in the amplifier-free coordinate and leaves a residual 41.94x the C-frame one
(`computations/qbeta/qbeta-eigenphase-branch-and-barodd-projection.witness.json`).
What this file changes is the *epistemic status* of that projection: it is the
unique mirror-covariant part of the asserted phase, forced by items 1-2, not a
seventh fitted ansatz. The residual is not addressed here and the standing
fence holds — searching for further phase corrections is fitting until one
lands with the structural standing of `c_2 = -1`.

No value is wired, no registry tier moves, and the convention ruling is
untouched: D remains canonical (owner ruling 2026-08-15). The C-frame
bar-oddness in item 3 is a fact about the *superseded* frame, recorded because
it is what makes the D-frame anomaly legible as an anomaly.

Sorry-free.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import QOU.QBeta.ZBarParity

namespace QOU.QBeta

/-! ## §1. The general identity: the phase anomaly is `h` times the `z` anomaly -/

variable {R : Type*} [CommRing R]

/-- The doubled ladder phase `2·alpha = (z - 1)·h`, carrying no division so
    the parity bookkeeping is available in any `CommRing` (including
    characteristic 2, where `alpha` itself would not be defined). -/
def phaseTwice (z h : R) : R := (z - 1) * h

/-- **The bar-anomaly of the phase is `h` times the bar-anomaly of `z`.**

    `h` is bar-ODD (`bar h = -h`, immediate for `h = q - q⁻¹`), so applying bar
    to `2 alpha = (z - 1) h` sends `z ↦ zb` and `h ↦ -h`. The sum with the
    unbarred phase is then

      `phaseTwice zb (-h) + phaseTwice z h = h * (z - zb)`.

    Everything downstream in this file is a specialisation of this one `ring`
    identity: the phase's failure to be mirror-covariant is *exactly* the
    Markov parameter's failure to be bar-invariant, amplified by `h`. -/
theorem phaseTwice_bar_anomaly (z zb h : R) :
    phaseTwice zb (-h) + phaseTwice z h = h * (z - zb) := by
  unfold phaseTwice; ring

/-- **Mirror-covariance of the phase characterises bar-invariance of `z`.**
    Over a domain with `h ≠ 0`, the doubled phase is bar-ODD (its bar image is
    its negative) **iff** `z` is exactly bar-fixed. The forward direction is
    the structural exclusion this file exists to state: a convention whose
    Markov parameter moves under bar cannot carry a mirror-covariant framing
    phase, whatever the size of the movement. -/
theorem phaseTwice_bar_odd_iff_z_bar_fixed {D : Type*} [CommRing D] [IsDomain D]
    (z zb h : D) (hh : h ≠ 0) :
    phaseTwice zb (-h) = -(phaseTwice z h) ↔ z = zb := by
  constructor
  · intro hodd
    have h0 : h * (z - zb) = 0 := by
      rw [← phaseTwice_bar_anomaly z zb h, hodd]; ring
    exact sub_eq_zero.mp ((mul_eq_zero.mp h0).resolve_left hh)
  · intro hz
    subst hz
    unfold phaseTwice; ring

/-! ## §2. Convention C (`z = √q/(1+q)`): bar-fixed, hence the phase is bar-odd -/

variable {F : Type*} [Field F]

/-- The convention-C Markov parameter in the half-power coordinate `s`
    (`s² = q`): `z_C = s/(1 + s²) = √q/(1+q)`. -/
noncomputable def zC (s : F) : F := s / (1 + s ^ 2)

/-- **`z_C` is exactly bar-fixed**: `z_C(s⁻¹) = z_C(s)`. This is
    `QOU.QBeta.z_bar_invariant_field` (PR #3449) restated on `zC`; only
    `s ≠ 0` is needed, since when `1 + s² = 0` both sides are `0` under
    Mathlib's division convention. -/
theorem zC_bar_fixed (s : F) (hs : s ≠ 0) : zC s⁻¹ = zC s :=
  z_bar_invariant_field s hs

/-- **The convention-C ladder phase is bar-ODD** — and by structure, not by
    coincidence: it is `phaseTwice_bar_odd_iff_z_bar_fixed` fed with
    `zC_bar_fixed`. A framing phase must be bar-odd (writhe is mirror-odd,
    `WritheMarkovInvariance.writhe_inv`), so convention C passes that test. -/
theorem phaseTwiceC_bar_odd (s h : F) (hs : s ≠ 0) :
    phaseTwice (zC s⁻¹) (-h) = -(phaseTwice (zC s) h) := by
  have hz := zC_bar_fixed s hs
  unfold phaseTwice
  rw [hz]; ring

/-! ## §3. Convention D (`z = q³/(q²+1)`): anomaly exactly `h`, phase anomaly `h²` -/

/-- The convention-D Markov parameter: `z_D = q³/(q² + 1)` (owner ruling
    2026-08-15, canonical). -/
noncomputable def zD (q : F) : F := q ^ 3 / (q ^ 2 + 1)

/-- **`z_D` is not bar-fixed, and its anomaly is exactly `h = q - q⁻¹`.**

    `z_D(q) - z_D(q⁻¹) = q - q⁻¹`, an exact identity, not an approximation:
    `q³/(q²+1) - q⁻¹/(1+q²)·... = (q⁴-1)/(q(1+q²)) = (q²-1)/q = q - q⁻¹`.

    This is the single fact that makes the whole D-frame phase story
    deterministic — combined with §1 it fixes the anomaly with no freedom. -/
theorem zD_sub_bar_eq_h (q : F) (hq : q ≠ 0) (hd : q ^ 2 + 1 ≠ 0) :
    zD q - zD q⁻¹ = q - q⁻¹ := by
  unfold zD
  have hd' : (1 : F) + q ^ 2 ≠ 0 := by rwa [add_comm]
  have hdi : q⁻¹ ^ 2 + 1 ≠ 0 := by
    intro hc
    apply hd
    have hx : (q⁻¹ ^ 2 + 1) * q ^ 2 = q ^ 2 + 1 := by field_simp; ring
    rw [← hx, hc, zero_mul]
  field_simp
  ring

/-- **The D-frame phase bar-anomaly is exactly `h²`** (for the doubled phase;
    equivalently `bar(alpha_D) + alpha_D = h²/2`). Immediate from §1 and
    `zD_sub_bar_eq_h`, with `h = q - q⁻¹`. The numerical value measured in
    `qbeta-eigenphase-branch-and-barodd-projection.witness.json` is this
    closed form. -/
theorem phaseTwiceD_bar_anomaly (q : F) (hq : q ≠ 0) (hd : q ^ 2 + 1 ≠ 0) :
    phaseTwice (zD q⁻¹) (-(q - q⁻¹)) + phaseTwice (zD q) (q - q⁻¹)
      = (q - q⁻¹) ^ 2 := by
  rw [phaseTwice_bar_anomaly, zD_sub_bar_eq_h q hq hd]; ring

/-- **The bar-odd part of the D-frame phase is `2 alpha_D - h²/2`**, i.e.
    `alpha_D - h²/4`.

    Subtracting half the anomaly is the unique shift that makes the phase
    mirror-covariant, so this projection is *forced* by §1 + `zD_sub_bar_eq_h`
    rather than chosen. Note `bar(h²) = h²` (`h` bar-odd ⇒ `h²` bar-even), so
    the same constant is subtracted on both sides — that is what makes the
    shift consistent, and it is why no freedom remains. -/
theorem phaseTwiceD_sub_hsq_bar_odd (q : F) (hq : q ≠ 0) (hd : q ^ 2 + 1 ≠ 0) :
    2 * phaseTwice (zD q⁻¹) (-(q - q⁻¹)) - (q - q⁻¹) ^ 2
      = -(2 * phaseTwice (zD q) (q - q⁻¹) - (q - q⁻¹) ^ 2) := by
  have hanom := phaseTwiceD_bar_anomaly q hq hd
  linear_combination 2 * hanom

end QOU.QBeta
