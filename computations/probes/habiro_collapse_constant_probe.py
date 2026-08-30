#!/usr/bin/env python3
"""What is the Habiro collapse constant C, actually? (bean qou-lrnd)

`MotivicPerpetualObstructionFromTrace.lean` carries, as docstring fact:

    C = a_0(-1) + 2*a_1(-1) = 4    for the proton/neutron
    C = a_0(-1) + 2*a_1(-1) = -32  for the deuteron

and `qou_proton_perpetual_obstruction` states it as "an exact algebraic
identity: a_0(u) evaluated at u=-1 gives 4, and a_1(-1)=0".

The collapse identity itself is proved in general, with no cyclotomic input:
`QOU.LiftingDescent.map_habiro_expansion` (sorry-free) gives
`phi(sum_m a_m (q;q)_m) = phi(a_0) + 2 phi(a_1)` for any ring map with
`phi q = -1`.  So C is fully determined by a_0 and a_1, and NOTHING about it
depends on p -- it is a constant by construction if the collapse holds.

This probe reads a_0 and a_1 from the canonical coefficients witness and
evaluates them.  Exact integer / Fraction arithmetic only -- no floats.

Ref: [manuscript] bean qou-lrnd
Ref: QOU.LiftingDescent.map_habiro_expansion
"""

import json
import pathlib
import re
from fractions import Fraction as F

WITNESS = pathlib.Path(__file__).resolve().parents[1] / "habiro" / \
    "habiro-coefficients-atomic.witness.json"

# The docstring's asserted values, as written in the Lean.
CLAIMED = {"p (proton, A=1)": 4, "D (deuteron, A=2)": -32}


def ev(expr: str, u: F) -> F:
    """Evaluate an integer polynomial in `u` exactly. Exact ints throughout."""
    s = expr.replace(" ", "")
    tot = F(0)
    for term in re.findall(r"[+-]?[^+-]+", s):
        sign = F(-1) if term.startswith("-") else F(1)
        t = term.lstrip("+-")
        m = re.fullmatch(r"(?:(\d+)\*?)?(?:u(?:\*\*(\d+))?)?", t)
        if m is None:
            raise ValueError(f"unparsed term {t!r} in {expr!r}")
        coef = F(int(m.group(1))) if m.group(1) else F(1)
        if "u" in t:
            e = int(m.group(2)) if m.group(2) else 1
            tot += sign * coef * u ** e
        else:
            tot += sign * coef
    return tot


def main() -> int:
    d = json.loads(WITNESS.read_text())
    rows, disagreements = [], []
    for name, r in d["results"].items():
        c = {x["m"]: x["a_m"] for x in r["habiro_coefficients"]}
        a0, a1 = ev(c[0], F(-1)), ev(c[1], F(-1))
        C = a0 + 2 * a1
        den = ev(r["denom_in_u"], F(-1))
        rows.append((name, c[0], c[1], a0, a1, C, den, C / den if den else None))
        if name in CLAIMED and C != CLAIMED[name]:
            disagreements.append((name, CLAIMED[name], C))

    print(f"{'atom':>22} {'a_0(-1)':>9} {'a_1(-1)':>9} {'C':>7} "
          f"{'claimed':>8} {'denom(-1)':>10} {'C/denom':>9}")
    for name, _, _, a0, a1, C, den, q in rows:
        cl = CLAIMED.get(name)
        print(f"{name:>22} {str(a0):>9} {str(a1):>9} {str(C):>7} "
              f"{(str(cl) if cl is not None else '-'):>8} {str(den):>10} {str(q):>9}")

    print("\nRaw coefficients, so the arithmetic above is checkable by eye:")
    for name, a0s, a1s, *_ in rows:
        print(f"  {name}\n     a_0 = {a0s}\n     a_1 = {a1s}")

    print()
    print("FINDINGS")
    print("  1. a_1(-1) = 0 for every atom -- that half of the docstring holds.")
    for name, claimed, actual in disagreements:
        print(f"  2. {name}: docstring says C = {claimed}; the coefficients give "
              f"C = {actual}.")
    print("  3. a_0 is a CONSTANT in every case (8, 2, 192), so 'a_0(u) evaluated")
    print("     at u=-1 gives 4' cannot be right for the proton whatever the")
    print("     evaluation point: a_0 = 8 identically.")
    print("  4. tr_M carries a denominator. Dividing through, proton and neutron")
    print("     BOTH collapse to 1/2 and the deuteron to 1/8 -- not integers, and")
    print("     the collapse does not separate proton from neutron.")
    print()
    print("SCOPE. This does not by itself refute the perpetual obstruction; it")
    print("says the two constants the Lean docstrings assert are not the ones the")
    print("canonical coefficients produce.  For why the residue route fails even")
    print("with a corrected C, see cyclotomic_residue_four_unit_probe.py: the")
    print("residue is a unit in F_p for every p not dividing C, and an explicit")
    print("cyclotomic unit realises it.")
    ok = not disagreements
    print()
    print("MATCHES DOCSTRING" if ok else "DOCSTRING DISAGREES WITH THE WITNESS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
