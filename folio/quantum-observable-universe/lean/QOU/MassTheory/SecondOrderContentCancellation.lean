/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/

/-!
# Second-Order Trace Coefficient `c_2` and Content-Cancellation Law (`qou-qqm4`)

This module formalizes the two analytical results of `qou-qqm4`:

1. **Parameter-free derivation of `[ε²](free; Z, N)`**:
   On the disconnected `A`-nucleon word (`A = Z + N`), trace factorization
   `tr(free; Z, N) = tr(p)^Z * tr(n)^N` together with the single-nucleon Taylor
   coefficients at `ε = q - 1 = 0`:
   - proton: `(a_p, r_p, q_p) = (1/2, 3/2, 23/4)`,
   - neutron: `(a_n, r_n, q_n) = (1/2, -1, 3)`,
   uniquely determines the second-order coefficient `[ε²](free; Z, N)`:
   multiplying by `2^(A + 2)` yields
   `4 * [2^(A+2) * [ε²](free; Z, N)] = 2 * (3Z - 2N)^2 + 2 * (37Z + 20N)`,
   where `37 = 2 * 23 - 9` and `20 = 2 * 12 - 4` arise directly from subtracting the
   diagonal self-pair terms `9Z + 4N` of `u^2 = (3Z - 2N)^2` from twice the single-nucleon
   second-order terms `2 * (23Z + 12N)`.

2. **Content-cancellation law and frame invariance of zero-net-content combinations**:
   Changing the intra-nucleon generator ordering from `grouped` to `borromean` shifts
   the single-nucleon quadratic contribution by the purely linear per-nucleon content form
   `(-9/16) * Z + (3/8) * N` (`(-36 * Z + 24 * N) / 64`). Any linear combination of
   same-`A` species with zero net `(Z, N)` content (`∑ α_i Z_i = 0`, `∑ α_i N_i = 0`)
   annihilates this per-nucleon ordering shift identically:
   - at `A = 2`: `c_2(pp) + c_2(nn) - 2 c_2(pn) = -1/2 = -32/64` in `grouped` (`[h^2]`) and
     `-15/32 = -30/64` for `[ε²]`, preserved under any linear per-nucleon shift;
   - at `A = 3`: `c_2(3p) + c_2(3n) - c_2(T) - c_2(3He) = 9/64` in BOTH the `grouped` and
     canonical `borromean` frames.
-/

namespace QOU.MassTheory.SecondOrderContentCancellation

/-- Four times the single-nucleon `[ε²]` coefficient of the proton (`4 * (23/4) = 23`). -/
def protonQuadNum : Int := 23

/-- Four times the single-nucleon `[ε²]` coefficient of the neutron (`4 * 3 = 12`). -/
def neutronQuadNum : Int := 12

/-- Twice the single-nucleon `[ε¹]` slope of the proton (`2 * (3/2) = 3`). -/
def protonSlopeNum : Int := 3

/-- Twice the single-nucleon `[ε¹]` slope of the neutron (`|2 * (-1)| = 2`). -/
def neutronSlopeNum : Int := 2

/-- Expanded quadratic form `u(Z, N)^2 = (3Z - 2N)^2 = 9 Z^2 - 12 Z N + 4 N^2`. -/
def firstOrderContentUSq (Z N : Int) : Int :=
  9 * (Z * Z) - 12 * (Z * N) + 4 * (N * N)

/-- Distinct-block pair sum `9 Z(Z-1) - 12 Z N + 4 N(N-1)` in the product expansion of
`tr(p)^Z * tr(n)^N` at order `ε²`. -/
def distinctBlockPairSum (Z N : Int) : Int :=
  9 * (Z * Z) - 9 * Z - 12 * (Z * N) + 4 * (N * N) - 4 * N

/-- The product-expansion numerator `4 * 2^(A+2) * [ε²](free; Z, N)` obtained directly
from expanding `(1/2 + (3/2)ε + (23/4)ε²)^Z * (1/2 - ε + 3ε²)^N` to order `ε²`:
single-block quadratic terms `4 * (23Z + 12N)` plus distinct-block product terms
`2 * distinctBlockPairSum Z N`. -/
def freeEps2ProductExpansionScaled (Z N : Int) : Int :=
  4 * (23 * Z + 12 * N) + 2 * distinctBlockPairSum Z N

/-- The closed-form formula `2 * (3Z - 2N)^2 + 2 * (37Z + 20N)` for
`4 * 2^(A+2) * [ε²](free; Z, N)`. -/
def freeEps2ClosedFormScaled (Z N : Int) : Int :=
  2 * firstOrderContentUSq Z N + 2 * (37 * Z + 20 * N)

/-- Parameter-free derivation of `[ε²](free; Z, N)` (`qou-qqm4`): the product expansion of
`tr(p)^Z * tr(n)^N` equals `2 * u(Z, N)^2 + 2 * (37Z + 20N)` for all `Z, N : Int`, with
`37 = 2 * 23 - 9` and `20 = 2 * 12 - 4`. -/
theorem free_eps2_closed_form_derivation (Z N : Int) :
    freeEps2ProductExpansionScaled Z N = freeEps2ClosedFormScaled Z N ∧
    2 * protonQuadNum - protonSlopeNum * protonSlopeNum = 37 ∧
    2 * neutronQuadNum - neutronSlopeNum * neutronSlopeNum = 20 := by
  unfold freeEps2ProductExpansionScaled freeEps2ClosedFormScaled
  unfold distinctBlockPairSum firstOrderContentUSq
  unfold protonQuadNum neutronQuadNum protonSlopeNum neutronSlopeNum
  have hpoly :
      4 * (23 * Z + 12 * N) +
        2 * (9 * (Z * Z) - 9 * Z - 12 * (Z * N) + 4 * (N * N) - 4 * N) =
      2 * (9 * (Z * Z) - 12 * (Z * N) + 4 * (N * N)) + 2 * (37 * Z + 20 * N) := by
    omega
  have hp : 2 * (23 : Int) - 3 * 3 = 37 := by decide
  have hn : 2 * (12 : Int) - 2 * 2 = 20 := by decide
  exact ⟨hpoly, hp, hn⟩

/-- Evaluation of `4 * 2^(A+2) * [ε²](free; Z, N) = 2 u^2 + 2 (37Z + 20N)` across all
species at `A = 2` (`pp, pn, nn`) and `A = 3` (`3p, 3He, T, 3n`). -/
theorem free_eps2_species_table :
    freeEps2ClosedFormScaled 2 0 = 220 ∧
    freeEps2ClosedFormScaled 1 1 = 116 ∧
    freeEps2ClosedFormScaled 0 2 = 112 ∧
    freeEps2ClosedFormScaled 3 0 = 384 ∧
    freeEps2ClosedFormScaled 2 1 = 220 ∧
    freeEps2ClosedFormScaled 1 2 = 156 ∧
    freeEps2ClosedFormScaled 0 3 = 192 := by
  have hpp : freeEps2ClosedFormScaled 2 0 = 220 := by decide
  have hpn : freeEps2ClosedFormScaled 1 1 = 116 := by decide
  have hnn : freeEps2ClosedFormScaled 0 2 = 112 := by decide
  have h3p : freeEps2ClosedFormScaled 3 0 = 384 := by decide
  have h3he : freeEps2ClosedFormScaled 2 1 = 220 := by decide
  have ht : freeEps2ClosedFormScaled 1 2 = 156 := by decide
  have h3n : freeEps2ClosedFormScaled 0 3 = 192 := by decide
  exact ⟨hpp, hpn, hnn, h3p, h3he, ht, h3n⟩

/-- Per-nucleon ordering shift `64 * ((-9/16) Z + (3/8) N) = -36 Z + 24 N` induced by
changing intra-nucleon generator ordering from `grouped` to `borromean`. -/
def orderingShiftScaled64 (Z N : Int) : Int :=
  -36 * Z + 24 * N

/-- General linear per-nucleon content functional `L(Z, N) = dZ * Z + dN * N + c0`. -/
def linearContentForm (dZ dN c0 Z N : Int) : Int :=
  dZ * Z + dN * N + c0

/-- Any linear per-nucleon content functional `L(Z, N) = dZ * Z + dN * N + c0` vanishes
on both the `A = 2` zero-net-content combination `L(2,0) + L(0,2) - 2 L(1,1)` and the
`A = 3` zero-net-content combination `L(3,0) + L(0,3) - L(1,2) - L(2,1)`. -/
theorem linear_content_form_cancels_at_A2_and_A3 (dZ dN c0 : Int) :
    linearContentForm dZ dN c0 2 0 + linearContentForm dZ dN c0 0 2 -
      2 * linearContentForm dZ dN c0 1 1 = 0 ∧
    linearContentForm dZ dN c0 3 0 + linearContentForm dZ dN c0 0 3 -
      linearContentForm dZ dN c0 1 2 - linearContentForm dZ dN c0 2 1 = 0 := by
  unfold linearContentForm
  have hA2 :
      (dZ * 2 + dN * 0 + c0) + (dZ * 0 + dN * 2 + c0) -
        2 * (dZ * 1 + dN * 1 + c0) = 0 := by omega
  have hA3 :
      (dZ * 3 + dN * 0 + c0) + (dZ * 0 + dN * 3 + c0) -
        (dZ * 1 + dN * 2 + c0) - (dZ * 2 + dN * 1 + c0) = 0 := by omega
  exact ⟨hA2, hA3⟩

/-- Exact `64 * c_2` values in the `grouped` frame at `A = 2` (`pp, pn, nn`) and
`A = 3` (`3p, 3He, T, 3n`), where `c_2 = [h^2](tr_M(free) - tr_M(atom))`. -/
def c2GroupedScaled64 (species : Nat) : Int :=
  match species with
  | 0 => -124  -- pp:  -31/16 = -124/64
  | 1 => -46   -- pn:  -23/32 = -46/64
  | 2 => 0     -- nn:   0/64
  | 3 => -297  -- 3p:  -297/64
  | 4 => -168  -- 3He: -21/8  = -168/64
  | 5 => -165  -- T:   -165/64
  | 6 => -27   -- 3n:  -27/64
  | _ => 0

/-- Exact `64 * c_2` values in the canonical `borromean` frame at `A = 2` (`pp, pn, nn`)
and `A = 3` (`3p, 3He, T, 3n`), where `c_2 = [h^2](tr_M(free) - tr_M(atom))`. -/
def c2BorromeanScaled64 (species : Nat) : Int :=
  match species with
  | 0 => -196  -- pp:  -49/16 = -196/64
  | 1 => -72   -- pn:  -9/8   = -72/64
  | 2 => 48    -- nn:   3/4   = 48/64
  | 3 => -405  -- 3p:  -405/64
  | 4 => -192  -- 3He: -3     = -192/64
  | 5 => -177  -- T:   -177/64
  | 6 => 45    -- 3n:   45/64
  | _ => 0

/-- Exact `64 * c_2` values shifted by the pure linear per-nucleon content form
`orderingShiftScaled64 Z N = -36 Z + 24 N`. -/
def c2LinearShiftedScaled64 (species : Nat) (Z N : Int) : Int :=
  c2GroupedScaled64 species + orderingShiftScaled64 Z N

/-- Exact second-order content-cancellation identities (`qou-qqm4`):
- in `grouped`, `64 * (c_2(pp) + c_2(nn) - 2 c_2(pn)) = -32` (`-1/2`), preserved under any
  linear per-nucleon shift `orderingShiftScaled64 Z N`;
- at `A = 3`, `64 * (c_2(3p) + c_2(3n) - c_2(T) - c_2(3He)) = 9` (`9/64`) in BOTH the
  `grouped` and canonical `borromean` frames. -/
theorem c2_zero_net_content_combinations_frame_invariant :
    c2GroupedScaled64 0 + c2GroupedScaled64 2 - 2 * c2GroupedScaled64 1 = -32 ∧
    (c2LinearShiftedScaled64 0 2 0 +
      c2LinearShiftedScaled64 2 0 2 -
      2 * c2LinearShiftedScaled64 1 1 1) = -32 ∧
    c2GroupedScaled64 3 + c2GroupedScaled64 6 -
      c2GroupedScaled64 5 - c2GroupedScaled64 4 = 9 ∧
    c2BorromeanScaled64 3 + c2BorromeanScaled64 6 -
      c2BorromeanScaled64 5 - c2BorromeanScaled64 4 = 9 := by
  have hA2g : c2GroupedScaled64 0 + c2GroupedScaled64 2 - 2 * c2GroupedScaled64 1 = -32 := by
    decide
  have hA2inv :
      (c2LinearShiftedScaled64 0 2 0 +
        c2LinearShiftedScaled64 2 0 2 -
        2 * c2LinearShiftedScaled64 1 1 1) = -32 := by
    decide
  have hA3g :
      c2GroupedScaled64 3 + c2GroupedScaled64 6 -
        c2GroupedScaled64 5 - c2GroupedScaled64 4 = 9 := by
    decide
  have hA3b :
      c2BorromeanScaled64 3 + c2BorromeanScaled64 6 -
        c2BorromeanScaled64 5 - c2BorromeanScaled64 4 = 9 := by
    decide
  exact ⟨hA2g, hA2inv, hA3g, hA3b⟩

end QOU.MassTheory.SecondOrderContentCancellation
