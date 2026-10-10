#!/usr/bin/env python3
"""The bar is NOT the full involution (CPT): two involutions, and only one grades the theory.

Beans `qou-fi93` (matter/antimatter asymmetry -> number density) and `qou-brng`
(linking vs self-energy).

WHY THIS EXISTS.  qou-fi93 records a scope-(b) exclusion: every counting measure
the framework defines is exactly bar-even, so the colour-curve asymmetry cannot
reach a number density.  Its constructive consequence has been read as "find a
bar-ODD counting object".  This probe asks whether bar-parity is the right
grading for that question at all, and finds that it is NOT.

🛑 NAMING, CORRECTED 2026-09-13 AFTER A CORPUS-GREP.  An earlier draft of this
file called the full involution "C" / "the full involution (CPT)".  THE CORPUS SAYS
OTHERWISE and the label is what makes this file's argument land or miss:

  * full:c-from-color-flavor-swap (brings-surface/) -- "The bar-involution
    q -> q^-1, sigma_i -> sigma_i^-1 acts as the COMPOSITE CPT in this
    categorisation, NOT as C alone."  It assigns C to a colour-sheet flavour
    swap, P to the braid-diagram mirror, T to trace reversal.
  * prop:c-equals-bar-iff-all-1dim (knots-particles-confinement/) uses C for
    the DIAGRAM HALF alone (sigma_i -> sigma_i^-1), and settles when that
    equals the bar: iff every irrep of H_n(q) is 1-dimensional (so C = bar at
    H_2, leptons; C != bar at H_3, mesons and baryons).
  * The notation register reserves calligraphic \mathcal{C} for the
    charge-conjugation operator.

So this file uses the corpus's own vocabulary from computations/
bar_parity_involution_atlas_probe.py (on main since #7060) -- ONE involution
def:bar-involution with two independently-applicable HALVES:

    B     coefficient half   q -> q^-1,   (n_+, n_-) FIXED
    FULL  the whole thing    (n_+, n_-; q) -> (n_-, n_+; q^-1)   [= CPT]

FULL is prop:antiparticle-crossing-reversal item 2.  B is what
QOU/Mass/BrunnianBindingChannel.lean and QOU/Observations/
CrossingEnergyBarSplit.lean grade by.  The two halves induce DIFFERENT
parities on the same objects.

🛑 PRIOR ART -- NOTHING IN SECTIONS 1-4 IS NEW.  Cite, do not re-derive:

  * prop:crossing-energy-decomposition item 2 already states the crossover in
    prose: "This inverts the parity of the weight functions themselves, where
    cosh is even and sinh is odd in lambda, because under sigma the
    multiplicity flips as well."
  * computations/bar_parity_involution_atlas_probe.py (ON MAIN, a week before
    this file) is a four-way atlas of these gradings and already concludes:
    "Under the FULL involution -- the one def:bar-involution actually defines
    -- BOTH crossing-energy channels are ODD."
  * QOU/Observations/CrossingEnergyBarSplit.mirror_swaps (sorry-free) gives
    FULL E = -E after substituting q -> q^-1.
  * The value tanh(ln q0) = 0.103963710052410145676652858536 is already in
    beans qou-hjs8 and qou-fi93, and prop:crossing-energy-decomposition item 4
    already gives E_asym/E_sym = tanh(ln q) independent of crossing number.

This file RE-DERIVES those symbolically in one place and adds only the
consequence spelled out in the verdict.

Exact `sympy` throughout; one `mpmath.mpf` block at 60 dps.  No float64.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402

mp.mp.dps = 60

q = sp.Symbol("q", positive=True)
npos, nneg = sp.symbols("n_plus n_minus", integer=True, nonnegative=True)


def simp(e):
    return sp.simplify(sp.expand(e))


def bar(e):
    """B: the COEFFICIENT bar, q -> q^-1, multiplicities fixed."""
    return simp(e.subs(q, 1 / q))


def full(e):
    """FULL (= CPT, NOT C): (n_+, n_-) swapped AND q -> q^-1.
    prop:antiparticle-crossing-reversal item 2."""
    a, b = sp.Dummy(), sp.Dummy()
    return simp(e.subs({npos: a, nneg: b}, simultaneous=True)
                 .subs({a: nneg, b: npos}, simultaneous=True)
                 .subs(q, 1 / q))


def hdr(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


E = npos * q - nneg / q                      # def:crossing-energy
w = npos - nneg                              # writhe        (signedMultiplicity)
nc = npos + nneg                             # crossing no.  (countMultiplicity)
cosh_ch = q + 1 / q                          # the bar-even scalar
sinh_ch = q - 1 / q                          # the bar-odd scalar (Hecke constant)

# ---------------------------------------------------------------- section 1
hdr("[1] The crossing energy is PURELY FULL-odd -- it has NO FULL-even part")

print(f"  E              = {E}")
print(f"  B E            = {bar(E)}")
print(f"  FULL E            = {full(E)}")
print()
print(f"  FULL E + E        = {simp(full(E) + E)}      <- identically zero")
assert simp(full(E) + E) == 0
print(f"  B E + E        = {sp.factor(simp(bar(E) + E))}   <- NOT zero")
assert simp(bar(E) + E) != 0
print("""
  So under the bar there is a genuine even/odd GRADING, and under charge
  conjugation there is NOT: E is entirely FULL-odd, its FULL-even part is 0.

  CONSEQUENCE, and it is the point of this probe.  A number DENSITY (a count
  of things, n + nbar) must be FULL-EVEN.  The crossing energy has no FULL-even
  part at all, so it cannot supply one -- not because its bar-parity is
  wrong, but because it is purely FULL-odd.

  SCOPE OF THAT, because the unscoped form is false.  Reading bar-parity as
  FULL-parity is only an error for quantities that CARRY n_+/n_-.  On a
  purely q-dependent quantity the coefficient half and the full involution
  act identically, so QOU/BringsSurface/ColourCurveBarVsBranch.lean -- which
  says "matter and antimatter are related by the bar ... so a bar-invariant
  quantity cannot distinguish them" about r(z), a quantity with no
  multiplicity dependence -- is SOUND, and is not an instance of this.""")

# ---------------------------------------------------------------- section 2
hdr("[2] The parities CROSS OVER between multiplicity and scalar")

rows = [
    ("writhe        w = n_+ - n_-", w, "multiplicity"),
    ("crossing no. n_c = n_+ + n_-", nc, "multiplicity"),
    ("cosh scalar    q + q^-1", cosh_ch, "scalar"),
    ("sinh scalar    q - q^-1", sinh_ch, "scalar"),
]
print(f"  {'object':<30s} {'under B  ':<12s} {'under FULL':<12s}")
print(f"  {'-'*30} {'-'*12} {'-'*12}")


def parity(e, f):
    if simp(f(e) - e) == 0:
        return "EVEN"
    if simp(f(e) + e) == 0:
        return "ODD"
    return "neither"


table = {}
for name, obj, _kind in rows:
    pb, pc = parity(obj, bar), parity(obj, full)
    table[name.split()[0]] = (pb, pc)
    print(f"  {name:<30s} {pb:<12s} {pc:<12s}")

# a multiplicity does not involve q, so B fixes it; a scalar has no n, so C
# acts on it through q alone.  The CROSSOVER is the content:
assert parity(w, full) == "ODD" and parity(nc, full) == "EVEN"
assert parity(cosh_ch, bar) == "EVEN" and parity(sinh_ch, bar) == "ODD"
print("""
  Read the two columns against each other.  Under the BAR the grading sits in
  the SCALAR (cosh even, sinh odd); the multiplicities carry no q at all, so
  B FIXES them and they are bar-even only trivially -- the bar cannot tell
  the writhe from the crossing number.  Under C the grading sits in the
  MULTIPLICITY (crossing number even, writhe odd) and C separates them.

  So the framework DOES have a FULL-even counting integer and a FULL-odd one:

      FULL-EVEN   n_c = n_+ + n_-    total crossings      <- the "n + nbar" slot
      FULL-ODD    w   = n_+ - n_-    writhe               <- the "n - nbar" slot

  qou-fi93's survey asked for a bar-odd counting measure.  The counting
  integers are not graded by the bar at all (it fixes them); they are graded
  by C, and BOTH parities are already present.""")

# ---------------------------------------------------------------- section 3
hdr("[3] The two corpus channels pair a multiplicity with the OPPOSITE scalar")

signed_ch = w * cosh_ch / 2        # QOU.Mass.BrunnianBindingChannel.signedChannel
count_ch = nc * sinh_ch / 2        # QOU.Mass.BrunnianBindingChannel.countChannel

print(f"  signedChannel = w   (q+q^-1)/2   B:{parity(signed_ch, bar):<5s} C:{parity(signed_ch, full)}")
print(f"  countChannel  = n_c (q-q^-1)/2   B:{parity(count_ch, bar):<5s} C:{parity(count_ch, full)}")
print(f"  sum - E       = {simp(signed_ch + count_ch - E)}")
assert simp(signed_ch + count_ch - E) == 0
print("""
  Each channel pairs a FULL-ODD object with a FULL-EVEN one, so BOTH channels come
  out FULL-odd -- which is section 1 again, now term by term.  The bar separates
  them; C does not.  Mass (bar-even, signed) and binding (bar-odd, count) are
  therefore NOT a matter/antimatter pair, and the proved assignment
  QOU.Mass.BrunnianBindingChannel.binding_not_mass_sector is a statement about
  B, not about C.""")

# ---------------------------------------------------------------- section 4
hdr("[4] The FULL-odd / FULL-even ratio EXISTS, and it is delta_CP")

ratio_mult = sp.simplify(w / nc)
ratio_energy = sp.simplify((E - full(E)) / (E + bar(E)))
print(f"  unweighted   w / n_c                    = {ratio_mult}")
print(f"  energy-weighted (E - CE)/(E + BE)       = {sp.simplify(ratio_energy)}")
print()
deg1 = sp.simplify(sinh_ch / cosh_ch)
print(f"  degree-one channel ratio (q-q^-1)/(q+q^-1) = {deg1} = tanh(ln q)")
tanh_exp = sp.tanh(sp.log(q)).rewrite(sp.exp)
chk = simp(sp.cancel(sp.together(deg1 - tanh_exp)))
print(f"  tanh(ln q) rewritten in exp                = {sp.simplify(tanh_exp)}")
print(f"  difference                                 = {chk}")
assert chk == 0
print("""
  A FULL-odd numerator over a FULL-even denominator is exactly the shape of a
  baryon asymmetry eta = (n_B - n_Bbar)/n_gamma.  The framework HAS one, and
  it is the object qou-hjs8 already computed as delta_CP.""")

# ---------------------------------------------------------------- section 5
hdr("[5] The number, and the gap (mpmath, 60 dps -- no float64)")

from qou_substrate.constants import q_at  # noqa: E402

q0 = q_at(dps=60)
delta_cp = (q0 - 1 / q0) / (q0 + 1 / q0)
eta_obs = mp.mpf("6.1e-10")          # PDG 2024 baryon-to-photon ratio, order only

print(f"  q0                          = {mp.nstr(q0, 30)}")
print(f"  delta_CP = tanh(ln q0)      = {mp.nstr(delta_cp, 30)}")
print(f"  tanh(log(q0)) cross-check   = {mp.nstr(mp.tanh(mp.log(q0)), 30)}")
assert abs(delta_cp - mp.tanh(mp.log(q0))) < mp.mpf("1e-55")
print()
print(f"  observed eta (PDG, order)   = {mp.nstr(eta_obs, 3)}")
print(f"  delta_CP / eta              = {mp.nstr(delta_cp / eta_obs, 6)}")
print(f"  log10 of that ratio         = {mp.nstr(mp.log10(delta_cp / eta_obs), 6)}")
print("""
  Eight and a half orders of magnitude.  qou-fi93 already rules that this is a
  DISCONNECTION, not a suppression to be found -- and section 1 says why in
  structural terms: the quantity that would have to do the suppressing is a
  ratio of POPULATIONS, and populations are not what a single braid word has.""")

# ---------------------------------------------------------------- verdict
hdr("VERDICT")

print("""
  RE-DERIVED HERE (exact symbolic).  NONE of this is new -- see the PRIOR ART
  block in the module docstring.  What this file adds is one place where all
  four facts are checked together, and the consequence below.

    * The crossing energy is PURELY FULL-odd: FULL E + E = 0 identically.
      (Already: prop:antiparticle-crossing-reversal item 2;
      CrossingEnergyBarSplit.mirror_swaps; bar_parity_involution_atlas_probe.)
    * The coefficient half B and the full involution induce different
      parities.  B grades the SCALAR (cosh/sinh); FULL grades the
      MULTIPLICITY (crossing number even, writhe odd).
      (Already: prop:crossing-energy-decomposition item 2.)
    * Both corpus channels are FULL-odd, each pairing a FULL-odd factor with
      a FULL-even one.  So BrunnianBindingChannel.binding_not_mass_sector is
      a statement about the COEFFICIENT HALF and carries no matter/antimatter
      content -- mass and binding are not a particle/antiparticle pair.
    * The FULL-odd/FULL-even ratio is tanh(ln q).
      (Already: prop:crossing-energy-decomposition item 4; qou-hjs8.)

  THE ONE CONSEQUENCE THAT IS WORTH RECORDING.  qou-fi93's append specifies
  its own next step as "find a bar-ODD counting measure".  That search is
  mis-specified, and the two bullets above say why: the counting integers
  carry no q, so the coefficient half FIXES them and no counting integer is
  bar-odd or bar-even in any useful sense; and under the involution that
  actually relates matter to antimatter both parities are already present --
  n_c = n_+ + n_- is FULL-even (the n + nbar slot), w = n_+ - n_- is FULL-odd
  (the n - nbar slot).  The framework is not missing a bar-odd counting
  object.

  WHAT IS MISSING is the denominator's PHYSICS, not its parity.  eta is a
  ratio of number densities in a thermal ensemble; the corpus has a
  per-configuration asymmetry on a single braid word and no step converting a
  per-process asymmetry into a population ratio -- no ensemble, no Boltzmann
  equation, no freeze-out.  NOTE THE NARROW WORDING: the corpus DOES have a
  thermodynamic layer (beta = ln q dictionary, Markov-trace Gibbs free
  energy, information-theory/boltzmann-constant, hydrogen-partition-function,
  bond-log-ratio-is-a-free-energy).  The gap is the ENSEMBLE step, not
  thermodynamics as such.

  NOT CLAIMED HERE.  Reading baryon-number violation off the skein relation
  L_+ - L_- = (q - q^-1) L_0 is an INTERPRETATION, not a derivation -- the
  final append of qou-fi93 refuses exactly that move, and the corpus's
  prevailing stance is baryon number CONSERVED (hadron-proton-example.md runs
  the isotopy argument in the opposite direction, for proton stability).

  Scope (a) throughout: nothing excluded, no route refuted, no number wired.
  The tanh(ln q0)/eta ratio is the SIZE OF A GAP, not a prediction, and
  qou-fi93 already rules that the gap is a DISCONNECTION rather than a
  suppression to be found.
""")

print("PROBE OK -- all symbolic and numerical assertions passed.")
