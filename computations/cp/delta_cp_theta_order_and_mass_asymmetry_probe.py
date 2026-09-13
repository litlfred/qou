#!/usr/bin/env python3
"""delta_CP: what order in theta is it, and is it a mass asymmetry?  (bean qou-hjs8)

`qou-hjs8` asks whether the "72x overshoot" of `theta_res^2` against the PDG
e+/e- mass split is real.  The bean's own CORRECTED note already renormalised
that to 282x and flagged the weakness: `delta_CP` is defined on CROSSING
ENERGY, not on mass, so the comparison is a quantity conflation.  Its stated
next step was "extend m(K) to complex q and compute (m+ - m-)/m_avg directly".

This probe does that, and finds the question is ill-posed one level earlier:
**`delta_CP` as the corpus defines it does not depend on theta at all.**  So
there is no theta^2 to compare, no theta small enough to rescue it, and the
overshoot factor is not 72x, 144x or 282x.

Everything here is EXACT: `sympy` for every identity, `mpmath.mpf` at 60 dps
for the one numerical evaluation.  No float64 anywhere (AGENTS.md
NO-FLOAT64, which binds probes as hard as producers).

Sources, all quoted rather than paraphrased:

  def:crossing-energy
      content/.../knots-particles-confinement/crossing-energy.md
      E_cross(H) = sum over crossings of  { q for L+,  -q^-1 for L- }
      -- a SUM of degree-(+-1) terms.

  prop:antiparticle-crossing-reversal  item 2
      content/.../predicted-spectra/antiparticle-crossing-reversal.md
      E_cross(H^sigma) = -E_cross(H) |_{q <-> q^-1}
      -- this FIXES the mirror; nothing is guessed.

  prop:antiparticle-crossing-reversal  item 4
      "Topological mass invariance ... m_top(H^sigma) = m_top(H)."

  conj:complex-chirality-rotation      items 1 and "Experimental discriminant"
      content/.../observations/complex-chirality-rotation.md
      item 1:  S_c(T; |q|e^{i.theta}) = S_c(T; |q|) e^{i.n_c.theta}
      discriminant:
        delta_CP = (|S_c(T)| - |S_c(T^sigma)|)/(|S_c(T)| + |S_c(T^sigma)|)
                 ~ O(theta^2),
        "This vanishes to first order, matching electron-positron mass
         equality."

  conj:cp-violation-spectral-form
      content/.../observations/cp-violation-spectral-form.md
      delta_CP = Im(chi_{(1^n)}/chi_{(n)}) ~ (n_{(1^n)} - n_{(n)}).theta_res,
      "recovering delta_CP ~ n_c theta_res."     <- LINEAR in theta.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402

mp.mp.dps = 60

# Exact symbols.  r = |q| > 1, theta real.
r = sp.Symbol("r", positive=True)
theta = sp.Symbol("theta", real=True)
q = r * sp.exp(sp.I * theta)


def hdr(n: str) -> None:
    print()
    print("=" * 78)
    print(n)
    print("=" * 78)


def rule(n: int = 78) -> None:
    print("-" * n)


# ---------------------------------------------------------------- section 1
hdr("[1] The two crossing energies, from the corpus's own two blocks")

# Trefoil T_{2,3} = sigma_1^3 in B_2: three POSITIVE crossings, none negative.
N_PLUS, N_MINUS = 3, 0
CROSSING_NUMBER = N_PLUS + N_MINUS       # n_c = 3
WRITHE = N_PLUS - N_MINUS                # w   = 3

# def:crossing-energy, applied literally: a SUM.
S_particle = N_PLUS * q - N_MINUS * q**-1

# prop:antiparticle-crossing-reversal item 2: negate, then swap q <-> 1/q.
S_anti = sp.simplify((-S_particle).subs(q, 1 / q).subs(1 / r, r**-1))
# do the substitution on the symbolic form directly to avoid q being a product
_Q = sp.Symbol("Q")
_S_sym = N_PLUS * _Q - N_MINUS * _Q**-1
S_anti = (-_S_sym).subs(_Q, 1 / _Q).subs(_Q, q)

print(f"  trefoil T_2,3 = sigma_1^3 :  n_+ = {N_PLUS}, n_- = {N_MINUS}, "
      f"n_c = {CROSSING_NUMBER}, writhe w = {WRITHE}")
print(f"  S_c(T)        = {sp.simplify(S_particle.subs(q, _Q))}      [def:crossing-energy]")
print(f"  S_c(T^sigma)  = {sp.simplify(S_anti.subs(q, _Q))}   "
      f"[prop:antiparticle-crossing-reversal item 2]")
print()
print("  The mirror does NOT merely conjugate a phase: it inverts the MODULUS,")
print("  q -> 1/q.  That is the whole result, and it is the corpus's own rule.")

# ---------------------------------------------------------------- section 2
hdr("[2] delta_CP is INDEPENDENT of theta -- exactly, to all orders")

absP = sp.simplify(sp.Abs(S_particle))
absA = sp.simplify(sp.Abs(S_anti))
print(f"  |S_c(T)|       = {absP}")
print(f"  |S_c(T^sigma)| = {absA}")

delta_cp = sp.simplify((absP - absA) / (absP + absA))
delta_cp = sp.simplify(sp.radsimp(delta_cp))
print(f"  delta_CP       = {delta_cp}")

d_dtheta = sp.simplify(sp.diff(delta_cp, theta))
print(f"  d(delta_CP)/d(theta) = {d_dtheta}")
assert d_dtheta == 0, "delta_CP should be theta-free"

# the closed form
closed = sp.simplify(delta_cp - (r**2 - 1) / (r**2 + 1))
print(f"  delta_CP - (r^2-1)/(r^2+1) = {closed}")
assert closed == 0

# and its hyperbolic form: rewrite tanh in exponentials, where ln r collapses
tanh_form = sp.simplify(
    ((r**2 - 1) / (r**2 + 1) - sp.tanh(sp.log(r))).rewrite(sp.exp)
)
print(f"  (r^2-1)/(r^2+1) - tanh(ln r) = {tanh_form}")
assert tanh_form == 0, "closed form should be exactly tanh(ln r)"

print()
print("  delta_CP = (|q|^2 - 1)/(|q|^2 + 1) = tanh(ln|q|).")
print("  It contains no theta.  Not O(theta^2); not O(theta) -- O(theta^0).")

# ---------------------------------------------------------------- section 3
hdr("[3] Its value at the substrate anchor (proton pin, per owner directive 2026-08-07)")

from qou_substrate.constants import q_at  # noqa: E402

q0 = q_at(dps=60)
r2 = q0 * q0
d_num = (r2 - 1) / (r2 + 1)
print(f"  q0 (proton pin, 60 dps) = {mp.nstr(q0, 40)}")
print(f"  delta_CP                = {mp.nstr(d_num, 30)}")
print(f"  tanh(ln q0)             = {mp.nstr(mp.tanh(mp.log(q0)), 30)}")
assert abs(d_num - mp.tanh(mp.log(q0))) < mp.mpf("1e-50")

PDG_EE_BOUND = mp.mpf("8e-9")   # PDG |m(e+)-m(e-)|/m_avg < 8e-9
print()
print(f"  PDG bound on |m(e+)-m(e-)|/m_avg : {mp.nstr(PDG_EE_BOUND, 3)}")
print(f"  ratio delta_CP / bound           : {mp.nstr(d_num / PDG_EE_BOUND, 6)}")
print()
print("  IF one accepts the block's identification of delta_CP with the e+/e-")
print("  mass asymmetry -- which the corpus ASSERTS and does not derive, and")
print("  which section [6] shows is the wrong mechanism -- the overshoot is")
print(f"  ~{mp.nstr(d_num / PDG_EE_BOUND, 4)}, not 72x / 144x / 282x.  And no choice of theta")
print("  reduces it, because theta does not appear.")

# ---------------------------------------------------------------- section 4
hdr("[4] conj:complex-chirality-rotation item 1: the exponent is 1, not n_c")

# item 1 claims  S_c(T; r e^{i.theta}) = S_c(T; r) . e^{i.n_c.theta}
S_at_r = N_PLUS * r - N_MINUS * r**-1
claimed = S_at_r * sp.exp(sp.I * CROSSING_NUMBER * theta)
actual = S_particle
resid = sp.simplify(actual - claimed)
print(f"  claimed  S_c(T;r).e^(i.n_c.theta) = {claimed}")
print(f"  actual   S_c(T; r e^(i.theta))    = {sp.simplify(actual)}")
print(f"  difference                        = {sp.simplify(resid)}")
print(f"  vanishes identically?             = {resid == 0}")

true_exp = sp.simplify(actual / S_at_r)
print(f"  actual phase factor               = {true_exp}")
print()
print("  E_cross is a SUM of terms each of degree +-1 in q, so an all-positive")
print("  braid carries e^{+i.theta} and an all-negative one e^{-i.theta}.  The")
print("  exponent is the degree, which is +-1 -- never the crossing number.")
print("  For a MIXED-sign braid it is not a pure phase at all: n_+ q - n_- q^-1")
print("  is inhomogeneous, so no e^{i.k.theta} can factor out.  Checked:")

for npos, nneg in ((3, 0), (2, 1), (1, 2), (0, 3)):
    S = npos * q - nneg * q**-1
    Sr = npos * r - nneg * r**-1
    ratio = sp.simplify(S / Sr) if Sr != 0 else None
    pure = (ratio is not None) and (sp.simplify(sp.Abs(ratio) - 1) == 0)
    print(f"    n_+={npos}, n_-={nneg}:  pure phase? {pure}")

# ---------------------------------------------------------------- section 5
hdr("[5] Item 1 and the discriminant contradict EACH OTHER, definition aside")

print("  Take item 1 at face value, whatever E_cross really is:")
print("     S_c(T)       = S_c(T;|q|) . e^{+i.n_c.theta}")
print("     S_c(T^sigma) = S_c(T;|q|) . e^{-i.n_c.theta}       (item 1, mirror)")
S0 = sp.Symbol("S0", positive=True)
a = sp.Abs(S0 * sp.exp(sp.I * CROSSING_NUMBER * theta))
b = sp.Abs(S0 * sp.exp(-sp.I * CROSSING_NUMBER * theta))
d_item1 = sp.simplify((a - b) / (a + b))
print(f"     |S_c(T)| = {sp.simplify(a)},  |S_c(T^sigma)| = {sp.simplify(b)}")
print(f"     => delta_CP = {d_item1}")
assert d_item1 == 0
print()
print("  A pure phase has modulus 1, so item 1 makes the two moduli EQUAL and")
print("  delta_CP identically 0 -- to all orders, not to first.  The block's")
print("  own item 1 therefore contradicts its own 'O(theta^2)'.  This holds")
print("  without reference to def:crossing-energy at all.")

# ---------------------------------------------------------------- section 6
hdr("[6] The sibling block says LINEAR, and it is a third value")

# cp-violation-spectral-form, via prop:antiparticle-crossing-reversal:
#   alternating block carries (-q)^{-w}; symmetric block carries q^{w}.
w = sp.Symbol("w", integer=True, positive=True)
chi_alt = (-q) ** (-WRITHE)
chi_sym = q ** WRITHE
ratio = sp.simplify(chi_alt / chi_sym)
im_part = sp.simplify(sp.im(sp.expand(sp.simplify(ratio.rewrite(sp.cos)))))
im_part = sp.simplify(sp.im(sp.expand_complex(sp.simplify(ratio))))
print(f"  chi_(1^n)/chi_(n) = (-q)^-w / q^w  with w = {WRITHE}")
print(f"                    = {sp.simplify(ratio)}")
print(f"  Im(.)             = {sp.simplify(im_part)}")

series = sp.series(im_part, theta, 0, 3).removeO()
print(f"  series at theta=0 : {sp.simplify(series)}")
lead = sp.simplify(sp.limit(im_part / theta, theta, 0))
print(f"  lim Im(.)/theta   = {lead}   (finite and nonzero => LINEAR)")
print()
print("  So cp-violation-spectral-form gives delta_CP ~ 2w.theta/r^(2w), i.e.")
print("  FIRST order, and says so explicitly ('recovering delta_CP ~ n_c.theta_res').")

# ---------------------------------------------------------------- section 7
hdr("[7] Three sources, three incompatible answers for ONE symbol")

rows = [
    ("conj:complex-chirality-rotation, as stated",
     "O(theta^2)", "-- (no value given)"),
    ("conj:complex-chirality-rotation item 1, taken literally",
     "identically 0", "0 exactly"),
    ("def:crossing-energy + prop:antiparticle-crossing-reversal",
     "O(theta^0)", mp.nstr(d_num, 12)),
    ("conj:cp-violation-spectral-form",
     "O(theta^1)", "2w.theta/r^(2w)"),
]
print(f"  {'source':<56} {'order in theta':<16} value")
rule()
for s, o, v in rows:
    print(f"  {s:<56} {o:<16} {v}")
print()
print("  These cannot all be true.  cp-violation-spectral-form cites")
print("  complex-chirality-rotation as its dependency, so the disagreement is")
print("  between a block and the block it rests on.")

# ---------------------------------------------------------------- section 8
hdr("[8] The mass question the bean actually asked")

print("  m(K) = m_e . Vol(K) . rho(K) / hbar_q^2      (AGENTS.md, the purged-")
print("  Geom_full form).  Under the mirror K -> K^sigma:")
print()
print("    Vol(K^sigma) = Vol(K)        -- hyperbolic volume is mirror-invariant;")
print("                                    a theorem of hyperbolic geometry, not")
print("                                    an assumption of this framework.")
print("    hbar_q                       -- no K-dependence, unchanged.")
print("    rho(K^sigma) = ?             -- THIS is what decides it.")
print()
print("  rho is built from the Markov trace, and the mirror sends a braid word")
print("  to its crossing-reversed image, so rho(K^sigma) = rho(K)|_{q -> 1/q}.")
print("  The mass asymmetry is therefore EXACTLY the mirror-asymmetry of rho:")
print()
print("      (m+ - m-)/m_avg  =  (rho(q) - rho(1/q)) / (rho(q) + rho(1/q))")
print()
print("  -- the same q <-> 1/q structure as delta_CP, and again with NO theta")
print("  in it.  Whether it vanishes is a question about rho's bar-parity at")
print("  real q, which is INDEPENDENT of the complex phase the block invokes.")
print()
print("  prop:antiparticle-crossing-reversal item 4 asserts m_top(H^sigma) =")
print("  m_top(H).  That assertion is sound for the Vol factor and UNPROVED")
print("  for the rho factor; this probe does not close it either way, and says")
print("  so rather than guessing.  What it does establish is that the e+/e-")
print("  mass equality, if it holds, holds because rho is bar-even -- NOT")
print("  because delta_CP is O(theta^2).  The block cites the wrong mechanism.")

# ---------------------------------------------------------------- section 9
hdr("[9] VERDICT -- scope (a), and the bean's question is ill-posed")

print("""
  ESTABLISHED (exact, sympy):

    1. delta_CP as the corpus defines it is theta-INDEPENDENT:
           delta_CP = (|q|^2 - 1)/(|q|^2 + 1) = tanh(ln|q|),
       because the mirror inverts the modulus (q <-> 1/q) rather than
       conjugating a phase.  At the proton pin it is""")
print(f"           {mp.nstr(d_num, 20)}")
print("""
    2. conj:complex-chirality-rotation item 1 is internally inconsistent
       with its own discriminant: a pure phase factor forces delta_CP = 0
       identically, not O(theta^2).

    3. Item 1's exponent is wrong for the definition it cites: E_cross is a
       SUM of degree-(+-1) terms, so the phase factor is e^{+-i.theta}, and
       a mixed-sign braid has no pure phase factor at all.

    4. conj:cp-violation-spectral-form gives a THIRD answer, linear in
       theta, while citing block (2) as its dependency.

  THEREFORE the bean's question -- "is the 72x overshoot real or
  higher-order?" -- has no theta^2 to be an overshoot OF.  It is neither:
  the quantity does not depend on theta.

  NOT ESTABLISHED, and not claimed:

    * That the framework predicts a 10.4% e+/e- mass asymmetry.  It does
      not: delta_CP is a CROSSING-ENERGY ratio, and the identification with
      a mass asymmetry is the conflation this bean already flagged.  Section
      [8] gives the mass asymmetry its own (theta-free) expression.

    * Which of the three readings the author intends.  That is an authoring
      decision, not a measurement.  All three are recorded rather than one
      being picked.

  Scope (a) throughout: this refutes the stated theta-dependence of these
  particular blocks.  It rules out no ingredient -- a genuinely
  theta-dependent CP discriminant may well exist in this framework; it is
  just not the modulus-ratio these blocks write down.
""")

print("PROBE OK -- all symbolic assertions passed.")
