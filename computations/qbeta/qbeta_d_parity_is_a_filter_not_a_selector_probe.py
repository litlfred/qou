#!/usr/bin/env python3
"""
qou-cds1: the parity condition ADMITS the whole symmetric-q-integer family, and
the Hankel gate is VACUOUS for rank-1 candidates. Two corrections to my own
proposed method.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

The previous entry derived that a D-frame single generator must be
bar-INVARIANT (not bar-odd), and I listed three gates for candidates: the
Hankel condition c_2*c_4 = c_3^2, weight-0 on every c_k, and reduction to
cos(alpha_eff) in the C limit. Testing what those gates actually do:

CORRECTION 1 — PARITY IS A FILTER, NOT A SELECTOR.
The corpus's `quantumInt n q = (q^n - q^-n)/(q - q^-1)` is the SYMMETRIC
convention, and every symmetric q-integer is bar-invariant:

    [2]_q, [3]_q, [4]_q, [5]_q   ->  bar-ratio 1, all of them

So the parity condition admits the ENTIRE q-integer family at once. It rules
out the docstring's bar-ODD "sinh partner" reading — which was the point, and
stands — but it does not pick a member. Anyone reading the previous entry as
"parity identifies the generator" would be over-reading it; it narrows the
class and stops.

CORRECTION 2 — THE HANKEL GATE IS VACUOUS FOR RANK-1 CANDIDATES.
I listed `c_2*c_4 = c_3^2` as a gate on candidates. But rank-1 means
c_3 = rho*c_2 and c_4 = rho^2*c_2, so

    c_2*c_4 = rho^2*c_2^2 = c_3^2       IDENTICALLY, for every rho

The condition is satisfied by construction. It EXCLUDES non-rank-1 menus (which
is exactly what `not_single_generator_of_hankel_ne` uses it for, against the
fitted c_2=-1, c_3=-2, c_4!=-4) but it cannot discriminate BETWEEN single
generators. Listing it as a gate on candidates was my error.

WHAT SURVIVES AS AN ACTUAL DISCRIMINATOR: the C-limit reduction, and the
numerical value of c_3 = rho*c_2. Only one gate of the three I named, plus one
I did not.

A WORKED NON-CANDIDATE, recorded so it is not mistaken for a refutation.
`habiroT25 = [3]_q/25` (MmuR9V9Closure.lean:76) IS bar-invariant, so it passes
the parity filter. With c_2 = -1 it would give c_3 = -[3]_q/25 = -0.1217 at the
proton pin, against the corpus's extracted c_3 = -2.0693. NOT a match — but
habiroT25 belongs to the m_mu R9/V9 closure, NOT the Q_beta ladder, so this
refutes nothing. It is a different object that shares a name. Recorded only to
show the parity filter passing something that the value test then rejects,
which is the shape of how the remaining gates work.

NOT CLAIMED: any generator, any c_k. Scope (a). NO FLOAT64: sympy exact.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q, rho, c2 = sp.symbols("q rho c_2", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(q, 1 / q)), force=True))  # noqa: E731
qi = lambda n: (q ** n - q ** (-n)) / (q - 1 / q)  # noqa: E731

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


print("=" * 78)
print(" qou-cds1 — what the gates actually do")
print("=" * 78)

for n in (2, 3, 4, 5):
    check(f"symmetric_[{n}]_q_is_bar_INVARIANT",
          sp.simplify(sp.radsimp(bar(qi(n)) / qi(n)) - 1) == 0)

check("parity_admits_the_WHOLE_q_integer_family",
      all(sp.simplify(sp.radsimp(bar(qi(n)) / qi(n)) - 1) == 0 for n in range(2, 8)),
      "a filter on the class, not a selector of a member")

# the Hankel gate is an identity for rank-1
c3 = rho * c2
c4 = rho ** 2 * c2
check("Hankel_c2c4_eq_c3sq_is_IDENTICAL_for_any_rank_1_rho",
      sp.simplify(c2 * c4 - c3 ** 2) == 0,
      "satisfied by construction — excludes non-rank-1 menus, cannot "
      "discriminate between single generators")

# the worked non-candidate
Q = sp.Float("1.1099785827513808076", 25)
t25 = qi(3) / 25
check("habiroT25_passes_the_parity_filter",
      sp.simplify(sp.radsimp(bar(t25) / t25) - 1) == 0,
      f"[3]_q/25 is bar-invariant; at the pin it gives c_3 = "
      f"{sp.N(-t25.subs(q, Q), 8)} vs extracted -2.06934258 — but habiroT25 is "
      "the m_mu R9/V9 object, NOT the Q_beta ladder, so this refutes nothing")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
TWO CORRECTIONS TO MY OWN PROPOSED METHOD.

  1. PARITY IS A FILTER, NOT A SELECTOR. Every symmetric q-integer is
     bar-invariant, so the condition admits the entire family at once. It rules
     out the bar-ODD "sinh partner" reading — that stands — but it does not
     pick a member.

  2. THE HANKEL GATE IS VACUOUS FOR RANK-1 CANDIDATES. c_2*c_4 = c_3^2 holds
     identically whenever c_{k+1} = rho*c_k. It excludes non-rank-1 menus, which
     is what the corpus uses it for; it cannot discriminate between single
     generators. Listing it as a candidate gate was my error.

SO OF THE THREE GATES I NAMED, ONE IS A CLASS FILTER, ONE IS VACUOUS, AND ONE
(the C-limit reduction) survives — joined by the numerical value of
c_3 = rho*c_2, which I had not listed.
""")
sys.exit(0 if npass == len(A) else 1)
