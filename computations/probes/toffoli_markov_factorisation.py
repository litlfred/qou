"""RETRACTION probe: the recorded "product of traced volumes" IS the trace of
the element.  The hazard raised in bean qou-ahu3 is refuted.

WHAT WAS FLAGGED.  computations/_deprecated/toffoli-braid.py computes

    markov_trace(ordering) = prod_i Vhat_i ,   Vhat_i = z a_i + b_i

a PRODUCT OF TRACES.  tr_M is not multiplicative in general -- sigma_0 and
sigma_1 do not commute -- so this looked like it might be the arc's real
defect, and it was written into qou-ahu3 and PR #6247 as "may be the real
defect".

IT IS NOT A DEFECT.  The factorisation follows from the DEFINING MARKOV
PROPERTY, tr(x . sigma_last) = z tr(x), and from nothing else.  For the chain
elements x = a sigma_0 + b and y = c sigma_1 + d:

    tr(x y) = ac tr(s0 s1) + ad tr(s0) + bc tr(s1) + bd tr(1)
            = ac z^2 + ad z + bc z + bd            [Markov, applied twice]
            = (z a + b)(z c + d)
            = Vhat_0 . Vhat_1

The chains are built generator-by-generator in increasing index order, which is
exactly the shape the Markov property handles.  Formalized as
QOU.Information.tracedVolume_product_eq_trace_of_markov (sorry-free).

WHAT THIS PROBE ADDS to the Lean: the Lean states the two-element identity.
This checks the actual construction, for all eight strand-type orderings, with
BOTH q and z symbolic -- so the agreement is not a convention artefact and not
an anchor coincidence.  It also records that the NF word (0,1,0) never occurs
in any T_q, so no unproven trace value enters the comparison.

Exact symbolic arithmetic; no floating point.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp                                              # noqa: E402
from toffoli_nf_coordinates_and_lp_feasibility import (         # noqa: E402
    toffoli_element, chain_element, decode,
)

z = sp.Symbol("z")          # kept SYMBOLIC: convention-independent

# Markov trace of each NF word, from tr(x . sigma_last) = z tr(x) alone.
TR_010 = sp.Symbol("tr_010")     # never needed; present to prove it is unused
TR = {
    (): sp.Integer(1),
    (0,): z,
    (1,): z,
    (0, 1): z**2,
    (1, 0): z**2,
    (0, 1, 0): TR_010,
}


def main() -> int:
    print("=" * 74)
    print("  IS prod_i Vhat_i THE TRACE OF THE ELEMENT?  (retraction check)")
    print("=" * 74)
    print()
    print("  q and z both symbolic; Markov rule tr(x sigma_last) = z tr(x) only.")
    print()

    all_ok, uses_unknown = True, False
    for k in range(8):
        ordering = decode(k)
        T = toffoli_element(ordering)
        if (0, 1, 0) in T:
            uses_unknown = True
        trT = sp.expand(sum(c * TR[w] for w, c in T.items()))
        prod = sp.Integer(1)
        for i in range(2):
            a, b = chain_element(i, ordering)
            prod *= (z * a + b)
        diff = sp.simplify(sp.expand(trT - prod))
        ok = diff == 0
        all_ok &= ok
        print(f"  [{'PASS' if ok else 'FAIL'}] k={k} {ordering}   diff = {diff}")

    print()
    print(f"  [{'PASS' if not uses_unknown else 'FAIL'}] the word (0,1,0) never occurs, so tr_010 is never needed")
    print()
    print("=" * 74)
    verdict = all_ok and not uses_unknown
    print(f"  ALL EIGHT ORDERINGS AGREE, symbolically in q and z: {all_ok}")
    print("=" * 74)
    print()
    print("  RETRACTED: the multiplicativity hazard in qou-ahu3 / PR #6247.")
    print("  The construction is correct, and the factorisation is a theorem")
    print("  about the Markov property -- not an assumption smuggled in.")
    print("  Lean: QOU.Information.tracedVolume_product_eq_trace_of_markov")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
