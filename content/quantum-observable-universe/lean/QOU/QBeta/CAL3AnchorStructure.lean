/-
Copyright (c) 2026 litlfred. All rights reserved.

# The CAL-3 anchor structure for the Q_β c_3 coefficient

What it would mean to CAL-3-anchor `c_3` (the Q_β precision-ladder rung that is a
near-match, not a derivation — registry §3). The odd channel of `c_3` factors as

    c_3^odd  =  κ_(2,1)(q_0) · S ,

a **derived, pure-q, bar-odd fibre carrier** `κ_(2,1)(q) = (q−1)³(q+1)/q²`
(`QOU.QBeta.kappa21_bar_odd`, ZBarParity §3) times a **single archimedean scalar
`S`** — "the single archimedean leak" the whole ladder carries. Numerically (this
session): `κ_(2,1)(q_0) ≈ 0.00228` (anchor-rigid), `S ≈ −908` (proton) / `−887`
(muon), and the entire c_3 cross-anchor swing (2.42 %) lives in `S`, not `κ`.

**This file proves what is provable about that structure; it does NOT close the
keystone.** The open, un-formalized content is the identification `S = g(P_avg^π)` —
that `S` is fixed by the CAL-3 datum (the pion/meson scale) rather than read off
Q_β. That link is a conjecture; per the anti-laundering discipline (§"Conditional-
proved ≠ premise-established") it is deliberately **not** axiomatised as a Lean
class here — doing so would be vacuous (any `S` is trivially `g(P_avg^π)` for some
`g`). The genuine open question is cross-anchor rigidity of a single categorical
`g`, which no Lean scaffold establishes.

Provable pieces (all sorry-free):
1. `kappa21`, `kappa21_ne_zero` — the carrier is nonzero away from `q ∈ {0,1,−1}`,
   so the factorization `S := c_3^odd / κ` is well-defined.
2. `c3odd_bar_odd_of_factor` — `κ·S` with `κ` bar-odd and `S` bar-fixed (an
   archimedean constant) is bar-odd: the factorization sits in the odd channel
   (standing reading, KC6/KC10), inheriting its parity from `κ`, not `S`.
3. `c3_swing_factorization` — the cross-anchor ratio `(κa·Sa)/(κb·Sb)` factors
   into the pure-q carrier ratio `κa/κb` times the scalar ratio `Sa/Sb`: the
   swing is isolated in `S`.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta.CAL3Anchor

variable {R : Type*}

/-- The derived bar-odd fibre carrier of the `c_3` odd channel:
    `κ_(2,1)(q) = (q−1)³(q+1)/q²`. (Same object as `QOU.QBeta.kappaNum/kappaDen`;
    packaged here as a single field element for the factorization.) -/
def kappa21 [Field R] (q : R) : R := (q - 1) ^ 3 * (q + 1) / q ^ 2

/-- **The carrier is nonzero away from `q ∈ {0, 1, −1}`.** Hence
    `S := c_3^odd / κ_(2,1)(q_0)` is well-defined at the substrate anchor
    (`q_0 ≈ 1.11 ∉ {0,1,−1}`). -/
theorem kappa21_ne_zero [Field R] (q : R) (h0 : q ≠ 0) (h1 : q ≠ 1)
    (hm1 : q ≠ -1) : kappa21 q ≠ 0 := by
  unfold kappa21
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 h0
  refine div_ne_zero (mul_ne_zero (pow_ne_zero 3 ?_) ?_) hq2
  · exact sub_ne_zero.mpr h1
  · intro hcontra
    exact hm1 (add_eq_zero_iff_eq_neg.mp hcontra)

/-- **The odd-channel factorization sits in the bar-odd part.** If the `c_3` odd
    channel is `κ·S` with `κ` bar-odd (`σ κ = −κ`, the carrier) and `S` bar-fixed
    (`σ S = S`, an archimedean constant), then it is bar-odd. The parity is
    inherited from the carrier `κ`, NOT from the archimedean scalar `S` — so
    anchoring `S` cannot change the channel's parity (consistent with the
    standing reading KC6/KC10: parity gates test the odd part). -/
theorem c3odd_bar_odd_of_factor [CommRing R] (σ : R →+* R) (κ S : R)
    (hκ : σ κ = -κ) (hS : σ S = S) : σ (κ * S) = -(κ * S) := by
  rw [map_mul, hκ, hS]; ring

/-- **The cross-anchor swing is isolated in `S`.** For nonzero carriers, the ratio
    of the factorized odd channel at two anchors factors into the pure-q carrier
    ratio times the scalar ratio: `(κa·Sa)/(κb·Sb) = (κa/κb)·(Sa/Sb)`. Since `κ`
    is a pure-q function (anchor-rigid to the ppb the anchors differ by), the
    entire c_3 cross-anchor swing lives in `Sa/Sb`. -/
theorem c3_swing_factorization [Field R] (κa κb Sa Sb : R)
    (hκb : κb ≠ 0) (hSb : Sb ≠ 0) :
    (κa * Sa) / (κb * Sb) = (κa / κb) * (Sa / Sb) := by
  field_simp

/-- **`S` is the single archimedean leak (not derived).** The identity
    `S = c_3^odd / κ_(2,1)(q_0)` merely *defines* `S`; it carries no content until
    `S` is fixed independently. The open keystone is the identification of `S`
    with a CAL-3-class quantity `g(P_avg^π)` — deliberately not axiomatised (a class
    `S = g P_avg^π` is vacuously satisfiable; the real content is cross-anchor
    rigidity of a single categorical `g`, which is unproved). This lemma records
    only the trivial well-definedness of the defining ratio. -/
theorem S_welldefined [Field R] (c3odd κ : R) (hκ : κ ≠ 0) :
    κ * (c3odd / κ) = c3odd := by
  field_simp

end QOU.QBeta.CAL3Anchor
