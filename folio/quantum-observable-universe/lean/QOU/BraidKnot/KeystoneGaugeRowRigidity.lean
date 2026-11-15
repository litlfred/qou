/-
Copyright (c) 2026 litlfred. All rights reserved.

# Attacking `bwS0_eq_hecke`: the gauge-row continuation is forced by interpolation rigidity

`bwS0_eq_hecke` (`KeystoneVerlindeSMatrixBridge.BWVacuumRowIsHecke`) is the single
open conjecture `loc_matches` reduces to: the Chern–Simons/WRT gauge vacuum row
`bwS0(λ)` equals the Hecke modular datum `d_q(λ)/√(Σ d_q²)` at real `q > 1`.

This file **attacks it honestly** — not by proving it (which rests on the TQFT
identification `WRT = BW-localization`, an input, per §Axiomatization-is-NOT-a-Proof),
but by proving the *structural* reduction:

> **If** the gauge row is a bounded-degree polynomial in the fold parameter
> `t = q + q⁻¹` (the **Habiro / quantum-modularity rigidity** property — a *cited*
> mathematical fact about WRT invariants, Habiro 2008 / Garoufalidis–Zagier),
> **and** it agrees with the value-map polynomial at enough fibre points (which
> `KeystoneLRAmplitudeReal`, PR #4365, supplies at the root of unity), **then** it
> equals the value map identically — hence at the substrate `q₀`.

So `bwS0_eq_hecke` is reduced from "one opaque identity at all real q" to
**"the gauge row is a bounded-degree Habiro object" + already-proved root agreement**.
The interpolation-rigidity engine is `eq_of_eval_agree_card`; the reduction is
`bwS0_eq_hecke_of_rigidity`.

**Honest scope (STRICT).** This does **not** prove `bwS0_eq_hecke`.  It proves the
implication; the antecedent (bwS0 is a bounded-degree polynomial equal to the
value-map polynomial at enough points) is the cited Habiro-rigidity input, carried
as an explicit hypothesis — *not* a fiat instance, *not* wired.  No `c_k`; no fit;
L2 unchanged.

Base ring: generic integral domain for the rigidity engine (the interpolation is
pure algebra); the physical statement specialises to `ℝ`.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-- Ref: [habiro2004] https://doi.org/10.1007/s00222-007-0071-0
-/
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Tactic

namespace QOU.BraidKnot.KeystoneGaugeRowRigidity

open Polynomial

variable {R : Type*} [CommRing R] [IsDomain R] [DecidableEq R]

/-- **Interpolation rigidity.** Two polynomials whose degrees are both `< s.card`
and which agree on a finset `s` of (distinct) points are equal.  A polynomial of
degree `< s.card` cannot have the `s.card` roots that their difference would carry
unless it is zero. -/
theorem eq_of_eval_agree_card
    (p q : R[X]) (s : Finset R)
    (hp : p.natDegree < s.card) (hq : q.natDegree < s.card)
    (h : ∀ x ∈ s, p.eval x = q.eval x) : p = q := by
  by_contra hne
  have h0 : p - q ≠ 0 := sub_ne_zero.mpr hne
  -- every point of `s` is a root of `p - q`, and the points are distinct
  have hsub : s ⊆ (p - q).roots.toFinset := by
    intro x hx
    rw [Multiset.mem_toFinset, mem_roots h0]
    show (p - q).eval x = 0
    rw [eval_sub, h x hx, sub_self]
  -- so `s.card ≤ #roots ≤ natDegree(p-q) < s.card`
  have h1 : s.card ≤ (p - q).roots.toFinset.card := Finset.card_le_card hsub
  have h2 : (p - q).roots.toFinset.card ≤ (p - q).natDegree :=
    le_trans (Multiset.toFinset_card_le _) (card_roots' _)
  have h3 : (p - q).natDegree < s.card :=
    lt_of_le_of_lt (natDegree_sub_le p q) (max_lt hp hq)
  omega

/-- **The reduction of `bwS0_eq_hecke` (honest, conditional).** Model the gauge row
and the value map as polynomials `bwPoly`, `valPoly` in the fold parameter.  If both
have degree `< s.card` for a finset `s` of fibre points, and they agree on `s` (the
root-of-unity agreement `KeystoneLRAmplitudeReal` proves), then they are equal — so
the gauge row equals the value map at **every** point, in particular at the
substrate `t₀ = q₀ + q₀⁻¹`.  The residual open content of `bwS0_eq_hecke` is exactly
the antecedent: *that the gauge row is such a bounded-degree polynomial* (Habiro
rigidity), and the finite root agreement — the latter already supplied at the root
by #4365. -/
theorem bwS0_eq_hecke_of_rigidity
    (bwPoly valPoly : R[X]) (s : Finset R) (t₀ : R)
    (hbw : bwPoly.natDegree < s.card) (hval : valPoly.natDegree < s.card)
    (hroot : ∀ x ∈ s, bwPoly.eval x = valPoly.eval x) :
    bwPoly.eval t₀ = valPoly.eval t₀ := by
  rw [eq_of_eval_agree_card bwPoly valPoly s hbw hval hroot]

end QOU.BraidKnot.KeystoneGaugeRowRigidity
