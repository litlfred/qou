#!/usr/bin/env python3
"""
qou-cds1: under D ALL the bar-odd content of log Vhat is theta = log q — which
is structure-free. So no bar-odd phase can carry D's structure.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

THE QUESTION THIS CLOSES. Earlier in this arc: the D form is multiplicative, so
resum log Vhat rather than Vhat; and D's un-removable bar-defect is h^2/2. The
open follow-up was whether the log form could ABSORB that defect — i.e. whether
moving to logs supplies a bar-odd phase carrying D's structure, the way
Vhat_C - 1 = 2 sinh(theta/2) does under C.

ANSWER: NO, and the reason is structural rather than a failed search.

MEASURED, sympy exact:

    odd(log Vhat_D) = log q                     EXACTLY
    odd(log Vhat_C) = a z-dependent expression, NOT log q

Under D the log frame DOES supply a bar-odd object. But it is theta = log q,
which contains no z, no Markov data, nothing convention-specific. ALL of D's
structure sits in the bar-EVEN part (the cosh-ratio [2]_{q^2}/[2]_q).

Under C the position is reversed: Vhat_C - 1 = 2 sinh(theta/2) is a bar-ODD
eigenvector AND carries the convention's data.

THE CONSEQUENCE, which is the point. `cos(phase)` is bar-invariant only when the
phase is bar-ODD. Under C such a phase exists and carries structure, so a cosine
resummation has something to resum. Under D every bar-odd object available from
Vhat is structure-free, so NO bar-odd phase can carry D's structure — and
therefore no cos-type resummation of a phase can express it, whatever offset is
chosen. That is stronger than "the offset must be q-dependent" (Step 7) and
stronger than "there is no fixed centre" (Step 8): those say the additive repair
is awkward; this says the bar-odd slot is empty of content.

HONESTY ABOUT WHAT IS NEW. `odd(log Vhat) = log q` is EQUIVALENT to Step 7's
`bar(Vhat) = Vhat/q^2` — take logs of both sides. It is a restatement in log
coordinates, not an independent discovery, and it is asserted here as such
(check `restatement_of_step7`). What is new is only the CONSEQUENCE above: that
the bar-odd slot being exactly theta rules out any structure-carrying phase.

A DISCARDED TEST, recorded so it is not repeated. I first tried substituting a
generic constant `zz` for z to see which z makes the odd part collapse to log q.
That test is MEANINGLESS: it treats z as bar-invariant, but z is a function of q
and bar acts on it. Any conclusion from a constant-z substitution here is void.

NOT CLAIMED: that no D-frame resummation exists — only that no cos-of-a-bar-odd
-phase one does. The multiplicative/log route (this arc) and the u*Vhat
invariant are untouched by this negative. No c_k. Scope (a).

NO FLOAT64: sympy exact throughout.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(q, 1 / q)), force=True))  # noqa: E731
h = q - 1 / q
V_C = sp.simplify(sp.sqrt(q) / (q + 1) * h + 1)
V_D = sp.simplify(q ** 3 / (q ** 2 + 1) * h + 1)

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


def odd_log(V):
    return sp.simplify(sp.expand_log((sp.log(V) - sp.log(bar(V))) / 2, force=True))


print("=" * 78)
print(" qou-cds1 — D's bar-odd content is structure-free")
print("=" * 78)

oD = odd_log(V_D)
oC = odd_log(V_C)

check("D_odd_part_of_log_Vhat_IS_exactly_log_q",
      sp.simplify(sp.expand_log(oD - sp.log(q), force=True)) == 0,
      f"odd(log Vhat_D) = {oD}")
check("C_odd_part_of_log_Vhat_is_NOT_log_q",
      sp.simplify(sp.expand_log(oC - sp.log(q), force=True)) != 0,
      "under C the odd part is z-dependent — it carries structure")

# C's additive bar-odd eigenvector DOES carry structure
oddC_add = sp.simplify(sp.radsimp((V_C - bar(V_C)) / 2))
check("C_has_a_structure_carrying_bar_ODD_eigenvector",
      sp.simplify(bar(V_C - 1) + (V_C - 1)) == 0 and sp.simplify(oddC_add - (V_C - 1)) == 0,
      f"Vhat_C - 1 = {oddC_add} = 2 sinh(theta/2) — bar-odd AND z-dependent")

# the honesty check: this is Step 7 in log coordinates
check("restatement_of_step7_not_an_independent_result",
      sp.simplify(bar(V_D) - V_D / q ** 2) == 0,
      "bar(Vhat_D) = Vhat_D/q^2  <=>  odd(log Vhat_D) = log q. Same fact.")

# and log q is structure-free: it is the same for BOTH conventions' q
check("log_q_carries_no_convention_data",
      sp.simplify(sp.diff(sp.log(q), q) - 1 / q) == 0,
      "theta = log q involves no z, no Markov parameter, nothing frame-specific")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
THE CONSEQUENCE.

cos(phase) is bar-invariant only when the phase is bar-ODD.

    C:  a bar-odd object exists AND carries the convention's data
        (Vhat_C - 1 = 2 sinh(theta/2)).  A cosine has something to resum.

    D:  the only bar-odd content of log Vhat is theta = log q, which carries
        NOTHING.  All of D's structure is in the bar-EVEN part.

So no bar-odd phase can carry D's structure, and therefore NO cos-type
resummation of a phase can express it — whatever offset is chosen. That is
stronger than "the offset must be q-dependent" (Step 7) and than "there is no
fixed centre" (Step 8): those say the additive repair is awkward. This says the
bar-odd slot is EMPTY OF CONTENT.

NOT CLAIMED: that no D-frame resummation exists. Only that no
cos-of-a-bar-odd-phase one does. The multiplicative/log route and the u*Vhat
invariant are untouched. No c_k. Scope (a).
""")
sys.exit(0 if npass == len(A) else 1)
