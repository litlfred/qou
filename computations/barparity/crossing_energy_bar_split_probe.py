#!/usr/bin/env python3
"""The crossing energy's bar-split: writhe is bar-EVEN, crossing number bar-ODD.

Beans `qou-fi93` (the bar-defect / matter-antimatter asymmetry) and `qou-hjs8`
(the delta_CP theta-independence, which is what pointed here).

WHY THIS EXISTS.  `qou-fi93` establishes a scope-(b) exclusion: every counting
object the framework defines is EXACTLY bar-even, so the 7.878 % colour-curve
asymmetry cannot reach a number density.  Measured there: `[n]_q` bar-even
exactly, `d_q(lambda)` bar-even (worst 1.378e-40 at dps 40), the Plancherel
measure `d_q^2/D^2` bar-even (3.444e-41), `sum_lambda y_lambda` bar-even to 40
digits.  Its constructive consequence is stated as: *baryogenesis in QOU needs
a counting measure NOT built from q-integers -- a new structural object, not a
tuning.*

`qou-hjs8` then established, for a different reason, that the CROSSING ENERGY
is not such an object: `def:crossing-energy` makes it a SUM of degree-(+-1)
terms, `E_cross = n_+ q - n_- q^-1`, and the mirror sends `q <-> q^-1` rather
than conjugating a phase.  A sum of `q` and `q^-1` with unequal coefficients
is not bar-even.

So the question this probe asks is `qou-fi93`'s own question, aimed at an
object it did not examine: **what is the crossing energy's bar-parity, and
what does each part carry?**

THE ANSWER, and it is exact and clean:

    E_cross(q) + E_cross(1/q) = (n_+ - n_-)(q + q^-1) = w   (q + q^-1)
    E_cross(q) - E_cross(1/q) = (n_+ + n_-)(q - q^-1) = n_c (q - q^-1)

  bar-EVEN part carries the WRITHE           w   = n_+ - n_-
  bar-ODD  part carries the CROSSING NUMBER  n_c = n_+ + n_-

Both are topological counting integers, and they land on OPPOSITE bar-parities.
The bar-odd channel `qou-fi93` says the framework lacks is therefore not
absent from the corpus -- it is the crossing number, and it is carried by an
object that is not a q-integer.

AND WHY THE q-INTEGERS LOSE IT.  `[n]_q = (q^n - q^-n)/(q - q^-1)` is bar-even
*because it is a ratio of two bar-ODD objects*: numerator and denominator each
negate under the bar, and the signs cancel.  The bar-odd content is not missing
from the q-integers; it is DIVIDED OUT, and the same factor `(q - q^-1)` that
the crossing energy keeps is the one `[n]_q` cancels.  That is a mechanism, not
a coincidence, and it makes the obvious constructive candidate explicit:

    q^n - q^-n  =  [n]_q * (q - q^-1)

is bar-odd, indexed by an integer n, and is not a q-integer -- exactly the
shape `qou-fi93` asks for.

Exact `sympy` throughout; one `mpmath.mpf` evaluation at 60 dps.  No float64.
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
n = sp.Symbol("n", integer=True, positive=True)


def bar(e):
    """The bar involution q -> 1/q."""
    return sp.simplify(e.subs(q, 1 / q))


def bar_even_part(e):
    return sp.simplify((e + bar(e)) / 2)


def bar_odd_part(e):
    return sp.simplify((e - bar(e)) / 2)


def hdr(t: str) -> None:
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ---------------------------------------------------------------- section 1
hdr("[1] The crossing energy is NOT bar-even, and its two parts count different things")

npos, nneg = sp.symbols("n_plus n_minus", integer=True, nonnegative=True)
E = npos * q - nneg / q

print(f"  E_cross          = {E}                [def:crossing-energy]")
print(f"  bar(E_cross)     = {bar(E)}")
print()

s = sp.simplify(E + bar(E))
d = sp.simplify(E - bar(E))
print(f"  E + bar(E)       = {sp.factor(s)}")
print(f"  E - bar(E)       = {sp.factor(d)}")

w = npos - nneg            # writhe
nc = npos + nneg           # crossing number

chk_even = sp.simplify(sp.expand(s - w * (q + 1 / q)))
chk_odd = sp.simplify(sp.expand(d - nc * (q - 1 / q)))
print()
print(f"  (E + bar E) - w*(q + 1/q)    = {chk_even}")
print(f"  (E - bar E) - n_c*(q - 1/q)  = {chk_odd}")
assert chk_even == 0 and chk_odd == 0

print("""
  So, exactly:

      bar-EVEN part  =  w   (q + q^-1) / 2     w   = n_+ - n_-   the WRITHE
      bar-ODD  part  =  n_c (q - q^-1) / 2     n_c = n_+ + n_-   the CROSSING NUMBER

  Two topological counting integers, on OPPOSITE bar-parities.  The bar-odd
  one is the crossing number -- and E_cross is not a q-integer.""")

# ---------------------------------------------------------------- section 2
hdr("[2] Bar-parity is EXCHANGED by the mirror, which is why qou-hjs8 saw what it saw")

E_mirror = sp.simplify(-E.subs(q, 1 / q))     # prop:antiparticle-crossing-reversal item 2
print(f"  E_cross(mirror)  = {sp.simplify(E_mirror)}    [prop:antiparticle-crossing-reversal]")
print(f"  = E with n_+ <-> n_-?  {sp.simplify(E_mirror - (nneg * q - npos / q)) == 0}")
print()
print("  The mirror SWAPS n_+ and n_-, hence negates the writhe and fixes the")
print("  crossing number.  So under particle -> antiparticle:")
print("      bar-even part (writhe)          -> NEGATED")
print("      bar-odd  part (crossing number) -> PRESERVED")
print()
print("  That is the structural reason qou-hjs8's delta_CP is theta-free: it")
print("  compares MODULI, which see the q <-> 1/q inversion, not a phase.")

# ---------------------------------------------------------------- section 3
hdr("[3] Why the q-integers have no bar-odd content: it is DIVIDED OUT")

num = q ** n - q ** -n
den = q - 1 / q
qint = num / den

print(f"  [n]_q = ({num}) / ({den})")
print()
for label, e in (("numerator  q^n - q^-n", num), ("denominator q - q^-1", den)):
    b = sp.simplify(bar(e) + e)          # bar-ODD  <=>  bar(e) = -e  <=>  bar(e)+e = 0
    print(f"  {label:<26} bar(e) + e = {sp.simplify(b)}   -> bar-ODD: {sp.simplify(b) == 0}")

be = sp.simplify(bar(qint) - qint)       # bar-EVEN <=>  bar(e) = e
print(f"  [n]_q                      bar(e) - e = {be}   -> bar-EVEN: {be == 0}")

print("""
  A ratio of two bar-ODD objects is bar-EVEN -- the signs cancel.  So the
  bar-evenness qou-fi93 measured across every counting object is not an
  absence of bar-odd structure in the framework; it is the SAME bar-odd
  factor (q - q^-1) appearing twice and cancelling.

  The crossing energy keeps that factor undivided.  That is the whole
  difference between the two objects.""")

# ---------------------------------------------------------------- section 4
hdr("[4] The constructive candidate qou-fi93 asks for, made explicit")

cand = sp.simplify(sp.expand(qint * den - num))
print(f"  [n]_q * (q - q^-1) - (q^n - q^-n) = {cand}")
assert cand == 0
print()
print("  So  q^n - q^-n  =  [n]_q * (q - q^-1)  is:")
print("    * bar-ODD                     (verified in section [3])")
print("    * indexed by an integer n     (it counts)")
print("    * NOT a q-integer             (it is [n]_q times the bar-odd factor)")
print()
print("  which is exactly the shape qou-fi93 specifies: 'a counting measure")
print("  NOT built from q-integers -- a new structural object, not a tuning'.")
print("  It is obtained by NOT dividing, so it introduces no free parameter.")

# ---------------------------------------------------------------- section 5
hdr("[5] Numbers at the substrate anchor")

from qou_substrate.constants import q_at  # noqa: E402

q0 = q_at(dps=60)
print(f"  q0 (proton pin)   = {mp.nstr(q0, 30)}")
print(f"  q0 - 1/q0         = {mp.nstr(q0 - 1 / q0, 30)}   <- the bar-odd factor")
print(f"  q0 + 1/q0         = {mp.nstr(q0 + 1 / q0, 30)}   <- the bar-even factor")
print()
print("  For the trefoil (n_+ = 3, n_- = 0, w = 3, n_c = 3):")
tre_even = 3 * (q0 + 1 / q0) / 2
tre_odd = 3 * (q0 - 1 / q0) / 2
print(f"    bar-even part   = {mp.nstr(tre_even, 20)}")
print(f"    bar-odd  part   = {mp.nstr(tre_odd, 20)}")
print(f"    odd / even      = {mp.nstr(tre_odd / tre_even, 20)}")
print()
print("  Note odd/even = (q0-1/q0)/(q0+1/q0) = tanh(ln q0) -- the SAME quantity")
print(f"  qou-hjs8 computed as delta_CP: {mp.nstr(mp.tanh(mp.log(q0)), 20)}")
assert abs(tre_odd / tre_even - mp.tanh(mp.log(q0))) < mp.mpf("1e-50")

# ---------------------------------------------------------------- section 6
hdr("[6] VERDICT -- a channel, NOT a derivation of the asymmetry")

print(f"""
  ESTABLISHED (exact, sympy):

    1. E_cross(q) +- E_cross(1/q) splits the crossing energy into a bar-EVEN
       part carrying the WRITHE and a bar-ODD part carrying the CROSSING
       NUMBER.  Both are topological counting integers, on opposite parities.

    2. The mirror swaps n_+ and n_-, so it NEGATES the writhe and PRESERVES
       the crossing number -- the bar-odd part is the mirror-invariant one.

    3. [n]_q is bar-even BECAUSE it is a ratio of two bar-odd objects.  The
       framework's bar-odd content is divided out, not absent.

    4. q^n - q^-n = [n]_q (q - q^-1) is bar-odd, integer-indexed, and not a
       q-integer -- the shape qou-fi93 specifies, obtained by NOT dividing,
       hence with no free parameter introduced.

  WHAT THIS DOES NOT DO, and the bean stays open for it:

    * It does NOT derive the baryon asymmetry, or eta, or any number density.
      It exhibits a bar-ODD object carrying a counting integer.  qou-fi93's
      scope-(b) exclusion was that every counting measure the framework
      DEFINES is bar-even; this adds an object that is not, it does not
      construct the coupling to a density that the bean says is missing.

    * It does NOT show this object is the RIGHT one.  `q^n - q^-n` is the
      most obvious bar-odd companion to [n]_q, not a derived selection, and
      picking it because it has the wanted parity would be selection against
      the target.  What is derived here is the MECHANISM (division by a
      bar-odd factor destroys bar-odd content), not the choice.

    * The 7.878 % colour-curve asymmetry is untouched.  Nothing here connects
      it to the crossing number.

  So this RE-SCOPES qou-fi93's constructive consequence rather than
  discharging it: the needed object is not missing from the framework, and
  the reason the counting measures are bar-even is now a mechanism rather
  than an observation.  Scope (a) on the positive claim; qou-fi93's
  scope-(b) exclusion is untouched and still stands.
""")

print("PROBE OK -- all symbolic assertions passed.")
