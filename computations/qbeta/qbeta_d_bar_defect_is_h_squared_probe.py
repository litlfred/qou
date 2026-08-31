#!/usr/bin/env python3
"""
qou-cds1: D's un-removable bar-defect IS h^2/2 — and it is built from the same
q^2-integer as the ladder's own expansion variable.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

FOLLOWS the order result (same PR): under D,
bar(alpha_eff)+alpha_eff carries a u-INDEPENDENT piece that no order of ladder
correction removes. That piece was left unidentified. This identifies it.

    bar(alpha_D) + alpha_D  =  h^2 / 2            EXACT

with h = q - 1/q the Hecke parameter. Equivalently, writing [3]_x = x + 1 + 1/x,

    bar(alpha_D) + alpha_D  =  ( [3]_{q^2} - 3 ) / 2

which is AGENTS.md's own identity h_A^2 = [3]_q - 3 read at argument q^2.

THE LINK. The Hoefsmit b, which defines the ladder variable u = b*hbar_q^2, is

    b = sqrt([3]_{q^2}) / [2]_q                   (established in this arc)

so (b*[2]_q)^2 = [3]_{q^2} and therefore

    bar(alpha_D) + alpha_D  =  ( (b*[2]_q)^2 - 3 ) / 2.

The SAME q^2-integer governs both the ladder's expansion variable and the defect
the ladder cannot remove. The obstruction is not foreign to the construction --
it is built out of the construction's own data.

WHY THAT IS WORTH RECORDING. The order result says the defect does not live in
the series. One might then expect it to be some object external to the ladder.
It is not: it is h^2/2, the most elementary invariant in the algebra, and it is
expressible in the ladder's own b. So the failure is not that D introduces
something alien; it is that the same ingredient enters at a place the series
cannot reach.

NOT CLAIMED. That this identification yields a repair, a replacement phase, or
any c_k. It names the obstruction; it does not remove it. Steps 7 and 8 are
untouched. Scope (a): symbolic, one convention pair.

A NOTATION TRAP, recorded because it caught me. AGENTS.md writes the identity as
h_A^2 = [3]_q - 3. With the symmetric convention [3]_x = x + 1 + 1/x that is
FALSE at argument q (it gives q - 2 + 1/q) and TRUE at argument q^2. Testing it
at the literal argument q is a false negative; check which argument is meant.

NO FLOAT64: sympy exact throughout.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(q, 1 / q)), force=True))  # noqa: E731
br2 = lambda x: x + 1 / x          # noqa: E731
br3 = lambda x: x + 1 + 1 / x      # noqa: E731

h = q - 1 / q
z_D = q ** 3 / (q ** 2 + 1)
z_C = sp.sqrt(q) / (q + 1)
b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
a_D = sp.simplify((z_D - 1) * h / 2)
a_C = sp.simplify((z_C - 1) * h / 2)
defect = sp.simplify(bar(a_D) + a_D)

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


print("=" * 78)
print(" qou-cds1 — the D bar-defect is h^2/2")
print("=" * 78)

check("D_defect_IS_h_squared_over_2",
      sp.simplify(defect - h ** 2 / 2) == 0,
      f"bar(alpha_D)+alpha_D = {defect} = h^2/2")
check("C_has_NO_such_defect", sp.simplify(bar(a_C) + a_C) == 0,
      "alpha_C is bar-ODD — the defect is D-specific")
check("h_squared_IS_[3]_{q^2}_minus_3",
      sp.simplify(h ** 2 - (br3(q ** 2) - 3)) == 0,
      "AGENTS.md's h_A^2 = [3]_q - 3, read at argument q^2")
check("defect_IS_([3]_{q^2}-3)/2",
      sp.simplify(defect - (br3(q ** 2) - 3) / 2) == 0)

# the notation trap, asserted as a NEGATIVE so it is on record
check("at_argument_q_the_identity_is_FALSE",
      sp.simplify(h ** 2 - (br3(q) - 3)) != 0,
      "[3]_q - 3 = q - 2 + 1/q != h^2 — check which argument is meant")

# the link to the ladder's own variable
check("b_IS_sqrt([3]_{q^2})_over_[2]_q",
      sp.simplify(b - sp.sqrt(br3(q ** 2)) / br2(q)) == 0)
check("b_times_[2]_q_all_squared_IS_[3]_{q^2}",
      sp.simplify((b * br2(q)) ** 2 - br3(q ** 2)) == 0,
      f"(b*[2]_q)^2 = {sp.simplify((b*br2(q))**2)}")
check("defect_IS_((b[2]_q)^2-3)/2",
      sp.simplify(defect - ((b * br2(q)) ** 2 - 3) / 2) == 0,
      "the defect is expressible in the LADDER'S OWN b")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
THE IDENTIFICATION.

    bar(alpha_D) + alpha_D  =  h^2/2  =  ([3]_{q^2} - 3)/2  =  ((b*[2]_q)^2 - 3)/2

The u-independent obstruction is h^2/2 — the most elementary invariant in the
algebra — and it is built from the SAME q^2-integer [3]_{q^2} that defines the
Hoefsmit b, hence the ladder variable u = b*hbar_q^2.

So the obstruction is not foreign to the construction. The same ingredient
enters at a place the correction series cannot reach. That is a sharper
statement of why the series is the wrong instrument than "the defect does not
live in the series": it says WHICH object it is and where it comes from.

NOT CLAIMED: a repair, a replacement phase, or any c_k. Naming an obstruction
is not removing it. Steps 7 and 8 untouched. Scope (a).
""")
sys.exit(0 if npass == len(A) else 1)
