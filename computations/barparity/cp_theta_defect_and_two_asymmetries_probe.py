#!/usr/bin/env python3
"""sec:cp-violation-evidence rests on a theta-dependence that a sorry-free theorem excludes.

Beans `qou-fi93` (what does the bar-odd channel couple to?) and `qou-hjs8`
(is the theta_res^2 overshoot real?).  Lean, on `main`, sorry-free:
`folio/quantum-observable-universe/lean/QOU/Observations/CrossingDiscriminantThetaFree.lean`
  -> `crossingDisc_norm_theta_free`

WHY THIS EXISTS.  `qou-hjs8` established that the CP discriminant is
theta-FREE: the mirror inverts the MODULUS, not a phase, so

    delta_CP = (r^2 - 1)/(r^2 + 1) = tanh(ln|q|),    d/d(theta) = 0 identically

TWO content blocks on `main` still derive CP violation FROM theta, and
neither was corrected when that theorem landed (`7ecbd74fc6`):

  1. observations/cosmological-chirality-flip.md
     "This meets Sakharov's conditions: ... 2. Complex phase $\\theta$
      supplies CP violation."
  2. observations/cp-violation-evidence.md, lines 18-23 and 27
     "CP violation stems from a residual phase $\\theta_res$"
     "delta_CP ~ O(theta_res^2) for single-crossing systems"
     "delta_CP ~ n_c theta_res for multi-crossing composites"
     "If theta_res ~ tanh(ln q) . alpha_EM, then delta_CP ~ 10^-3.
      This matches kaon systems"

Block 2 is the quantitative one, and its arithmetic is what this probe
measures.  It uses tanh(ln q) as a SEED for a phase and then multiplies by
alpha_EM to land at 10^-3.  The theorem says tanh(ln q) IS the discriminant,
with no alpha_EM factor, so the predicted value is ~10^-1 -- and the stated
kaon match is lost by the factor 1/alpha_EM.

WHAT THIS PROBE DOES NOT DO.  It edits no content block and picks no reading.
`qou-hjs8` stays open per AGENTS.md 13a: which of the three readings the
author intends is an authoring decision, not a measurement.  Scope (a)
throughout -- the stated theta-dependence of these two blocks is refuted; no
ingredient is excluded, and a genuinely theta-dependent CP discriminant is
not ruled out.

PRIOR ART -- none of the following is claimed here as new:
  * delta_CP = tanh(ln q):  qou-hjs8, and the Lean above.
  * E_asym/E_sym = tanh(ln q) at n_- = 0, with multiplicity factor
    (n_+ + n_-)/(n_+ - n_-) otherwise:  prop:crossing-energy-decomposition
    item 4; knots-particles-confinement/coulomb-charge.md:25;
    observations/crossing-energy-interpretation.md:29; Lean
    `QOU.Braiding.coulomb_strong_ratio_q_rational` and
    `em_strong_ratio_tanh`.  So hjs8's delta_CP is that ratio identity
    read on the positive braid sigma_1^3 -- the SAME number, already
    published, reached by a second route.
  * count channel bar-odd / signed channel bar-even, and the parity
    forcing of the mass-vs-binding assignment:
    QOU.Mass.BrunnianBindingChannel (`countChannel_barOdd`,
    `signedChannel_barEven`, `brunnian_signedChannel_zero`).
  * delta_z = 0.07878466694:  docs/audits/2026-09-07-substrate-branch-and-
    the-q-eq-1-interface.md:513, and bean qou-ndt5.

NEW HERE, and it is small: the leading-order relation delta_CP/delta_z -> 4/3
between the two independently-derived ~10^-1 asymmetries, whose 3/4 is the
colour curve's own r'(0)/r(0); and the quantified size of block 2's defect.
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.codata import value_str  # noqa: E402

mp.mp.dps = 60


def hdr(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


Q0 = q_at(dps=60)
L = mp.log(Q0)

# ---------------------------------------------------------------- section 1
hdr("[1] The CP discriminant is theta-free, and it is the n_- = 0 channel ratio")

d_cp_tanh = mp.tanh(L)
d_cp_rat = (Q0 ** 2 - 1) / (Q0 ** 2 + 1)
print(f"  q0                     = {mp.nstr(Q0, 30)}")
print(f"  L = ln q0              = {mp.nstr(L, 30)}")
print(f"  tanh(ln q0)            = {mp.nstr(d_cp_tanh, 30)}")
print(f"  (q0^2-1)/(q0^2+1)      = {mp.nstr(d_cp_rat, 30)}")
assert abs(d_cp_tanh - d_cp_rat) < mp.mpf(10) ** -55

# the channel split of def:crossing-energy, E = n+ q - n- q^-1
qs, np_, nn_ = sp.symbols("q n_p n_m")
E = np_ * qs - nn_ / qs
signed = (np_ - nn_) * (qs + 1 / qs) / 2
count = (np_ + nn_) * (qs - 1 / qs) / 2
print(f"\n  E - (signed + count)   = {sp.simplify(E - signed - count)}   (exact)")
assert sp.simplify(E - signed - count) == 0

# at n_- = 0 the ratio is tanh(ln q) for EVERY n_+ -- not just a single crossing
ratio_pos = sp.simplify((count / signed).subs(nn_, 0))
print(f"  (count/signed)|_(n_-=0) = {ratio_pos}   -- n_+ cancels")
d_ratio = (Q0 - 1 / Q0) / (Q0 + 1 / Q0)
print(f"  numerically             = {mp.nstr(d_ratio, 30)}")
print(f"  |tanh(ln q0) - that|    = {mp.nstr(abs(d_cp_tanh - d_ratio), 5)}")
assert abs(d_cp_tanh - d_ratio) < mp.mpf(10) ** -55

# theta genuinely drops out of the MODULUS ratio
for th in ("1e-2", "1e-4", "1e-8"):
    theta = mp.mpf(th)
    qc = Q0 * mp.exp(1j * theta)
    dd = (abs(qc) ** 2 - 1) / (abs(qc) ** 2 + 1)
    assert abs(dd - d_cp_tanh) < mp.mpf(10) ** -55
print("  theta = 1e-2, 1e-4, 1e-8: discriminant unchanged to 1e-55  (theta-free)")

# ---------------------------------------------------------------- section 2
hdr("[2] cp-violation-evidence.md line 27: the stated 10^-3 is off by 1/alpha_EM")

# CODATA 2022 fine-structure constant, read from the vendored CODATA table
# rather than typed (witness-value copy ratchet).
ALPHA = mp.mpf(value_str("fine-structure constant"))
stated = d_cp_tanh * ALPHA           # the block's "theta_res ~ tanh(ln q).alpha_EM"
print("  block:  'If theta_res ~ tanh(ln q) . alpha_EM, then delta_CP ~ 10^-3.")
print("           This matches kaon systems'")
print(f"\n  tanh(ln q0) * alpha_EM = {mp.nstr(stated, 12)}   (the block's 10^-3)")
print(f"  theorem: delta_CP      = {mp.nstr(d_cp_tanh, 12)}   (theta-free, no alpha)")
print(f"  factor between them    = {mp.nstr(d_cp_tanh / stated, 12)}  = 1/alpha_EM")
assert abs(d_cp_tanh / stated - 1 / ALPHA) < mp.mpf(10) ** -40

KAON = mp.mpf("2e-3")                # K_L -> pi pi, the block's own comparison
print(f"\n  kaon eps (block's own) = {mp.nstr(KAON, 6)}")
print(f"  stated / kaon          = {mp.nstr(stated / KAON, 6)}   <- the claimed match")
print(f"  theorem / kaon         = {mp.nstr(d_cp_tanh / KAON, 6)}   <- the match is lost")

# ---------------------------------------------------------------- section 3
hdr("[3] Two independent ~10^-1 asymmetries, and they agree up to 4/3")

u0 = mp.sqrt(Q0)
z0 = u0 - 1 / u0
print(f"  z0 = sqrt(q0) - 1/sqrt(q0) = {mp.nstr(z0, 30)}")
print(f"  2 sinh(L/2)                = {mp.nstr(2 * mp.sinh(L / 2), 30)}")
assert abs(z0 - 2 * mp.sinh(L / 2)) < mp.mpf(10) ** -55

# colour curve r(x) = 5(4x^3 + 3x^2 + 3x + 4)   (27 * r, ColourCurveBarVsBranch)
xs = sp.Symbol("x")
r_sym = 5 * (4 * xs ** 3 + 3 * xs ** 2 + 3 * xs + 4)
odd_over_even = sp.simplify((r_sym - r_sym.subs(xs, -xs)) / (r_sym + r_sym.subs(xs, -xs)))
print(f"\n  delta_z(x) = (r(x)-r(-x))/(r(x)+r(-x)) = {odd_over_even}")


def r_num(t):
    return 5 * (4 * t ** 3 + 3 * t ** 2 + 3 * t + 4)


d_z = (r_num(z0) - r_num(-z0)) / (r_num(z0) + r_num(-z0))
print(f"  delta_z  at z0             = {mp.nstr(d_z, 30)}")
print(f"  delta_CP at q0             = {mp.nstr(d_cp_tanh, 30)}")

ratio = d_cp_tanh / d_z
print(f"\n  delta_CP / delta_z         = {mp.nstr(ratio, 20)}")
print(f"  4/3                        = {mp.nstr(mp.mpf(4) / 3, 20)}")
print(f"  relative deviation         = {mp.nstr(abs(ratio - mp.mpf(4) / 3) / (mp.mpf(4) / 3), 5)}")
assert abs(ratio - mp.mpf(4) / 3) / (mp.mpf(4) / 3) < mp.mpf("0.02")

print(f"\n  WHY 4/3.  r(0) = {r_num(0)}, r'(0) = 15, so delta_z = (r'(0)/r(0)).z + O(z^3)")
print("            = (3/4).z, while delta_CP = tanh L = L + O(L^3) and z = L + O(L^3).")
print(f"  series delta_CP(L) = {sp.series(sp.tanh(xs), xs, 0, 6).removeO()}")
zz = 2 * sp.sinh(xs / 2)
print(f"  series delta_z(L)  = {sp.simplify(sp.series(odd_over_even.subs(xs, zz), xs, 0, 4).removeO())}")
assert sp.Rational(15, 20) == sp.Rational(3, 4)

# ---------------------------------------------------------------- section 4
hdr("[4] The gap that is actually open: a suppression, not another asymmetry")

ETA = mp.mpf("6.1e-10")              # observed baryon-to-photon ratio
for name, d in (("delta_CP", d_cp_tanh), ("delta_z ", d_z)):
    print(f"  {name} / eta_obs = {mp.nstr(d / ETA, 8):>14s}   = {mp.nstr(mp.log10(d / ETA), 6)} dex")
print(f"\n  eta_obs = {mp.nstr(ETA, 4)}")
print(f"  required suppression f = eta / delta_CP = {mp.nstr(ETA / d_cp_tanh, 8)}")

print("""
  In the standard picture eta ~ epsilon . f, with epsilon the CP asymmetry per
  decay and f an entropy/washout suppression.  The corpus supplies
  epsilon-shaped objects at ~10^-1 and supplies NO f at all.

  qou-fi93's rank-one theorem (QOU.Observations.BarParityRankOne,
  `isBarOdd_iff`, sorry-free) says the bar-odd part of Z[q,q^-1] is FREE OF
  RANK ONE over the bar-even part, generated by q - q^-1.  So every bar-odd
  observable is (q - q^-1) times a bar-even factor: there is no second bar-odd
  SHAPE to look for.  That closes the search qou-fi93 was going to run, and it
  closes it negatively -- the missing object is not another asymmetry, it is a
  ratio of COUNTS, which is a different kind of quantity from an amplitude.

  Caveat, load-bearing: rank-one holds over Z[q,q^-1].  Over Z[q^(+-1/2)] the
  generator is u - u^-1 and q - q^-1 = (u - u^-1)(u + u^-1) is a proper
  multiple of it -- see bar_parity_rank_one_probe.py section 6.
""")

print("PROBE OK -- all symbolic and numerical assertions passed.")
