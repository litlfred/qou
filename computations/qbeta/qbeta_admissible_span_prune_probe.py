#!/usr/bin/env python3
"""Track 3 (`qou-99qc`): can a DERIVED weight close the admissible bracket?

`qou-99qc` records that the two functionals admissible under convention D
bracket the measured Q-value (+12.470 % and -43.157 %), so *some* convex
combination reproduces CODATA exactly, and names the trap: that is one
parameter against one anchor, and any weight must be derived from the
representation rather than fitted.

This probe asks the prior structural question, in the formalize-first spirit
of narrowing a class before searching it.

  Matching on `Delta` alone is ONE equation.
  Agreeing as FUNCTIONALS on H_3(q) is SIX.

A functional on H_3(q) is a covector in a 6-dimensional space. The question
"is there a weight w with w*aug + (1-w)*tr_M(z_D) = net?" is therefore a
LINEAR ALGEBRA question with a definite answer, not a search:

    is  net  in  span{ aug, tr_M(z_D) }  over  Q(q)?

If it is not, then NO weight — derived, fitted, convex or affine — produces
the coordinate sum the ansatz evaluates. The bracket would then be a
statement about one number on one element, not about the functionals, and
track 3 is closed by exclusion rather than left open.

Writes no witness, edits no number, proposes no c_k. Exact symbolic in Q(q)
throughout; the one numeric print is display-only via mpmath.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, N, LEFT, ONE, basis_vec, vec, length, net, q, h,
)

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if not ok:
        FAILED.append(name)


def main() -> int:
    set_compute_dps()
    Z = sp.Symbol("z")
    Z_D = q**3 / (q**2 + 1)

    # --- the three functionals, as covectors over Q(q) --------------------
    # net: the coordinate sum sigma -> 1 (what the ansatz evaluates)
    co_net = sp.Matrix([[sp.Integer(1)] * N])
    # aug: the augmentation sigma -> q (the unique admissible multiplicative one)
    co_aug = sp.Matrix([[q ** length(BASIS[i]) for i in range(N)]])
    # the Markov trace, at the descent root z_D
    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]
    co_tr = sp.Matrix([[sp.simplify(TR[i].subs(Z, Z_D)) for i in range(N)]])

    # CONTROL: these covectors really are the functionals they claim to be.
    check("control_co_net_reproduces_net_on_every_basis_element",
          all(sp.simplify((co_net * basis_vec(i))[0] - net(basis_vec(i))) == 0
              for i in range(N)))
    check("control_co_aug_is_multiplicative_on_the_generators",
          all(sp.simplify((co_aug * (LEFT[a] * basis_vec(b)))[0]
                          - (co_aug * basis_vec(a))[0] * (co_aug * basis_vec(b))[0]) == 0
              for a in (1, 2) for b in (1, 2)),
          "(so it is an algebra map, not merely a vector of powers)")
    check("control_the_three_covectors_are_pairwise_distinct",
          sp.simplify(co_net - co_aug) != sp.zeros(1, N)
          and sp.simplify(co_net - co_tr) != sp.zeros(1, N)
          and sp.simplify(co_aug - co_tr) != sp.zeros(1, N))

    # --- THE PRUNE -------------------------------------------------------
    M2 = sp.Matrix.vstack(co_aug, co_tr)
    M3 = sp.Matrix.vstack(co_aug, co_tr, co_net)
    r2, r3 = M2.rank(), M3.rank()

    check("the_two_admissible_functionals_are_independent",
          r2 == 2, f"rank{{aug, tr_M(z_D)}} = {r2}")
    check("THE_COORDINATE_SUM_IS_NOT_IN_THEIR_SPAN",
          r3 == 3,
          f"rank{{aug, tr_M(z_D), net}} = {r3} > {r2}. So NO weight — derived, "
          "fitted, convex or affine — gives a combination equal to `net` AS A "
          "FUNCTIONAL. The bracket matches one number on one element; it does "
          "not reconstruct the functional the ansatz evaluates")

    # Where the failure lives: exhibit a basis element the best-fit misses.
    w = sp.Symbol("w")
    combo = w * co_aug + (1 - w) * co_tr
    delta = vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)
    w_delta = sp.solve(sp.Eq(sp.simplify((combo * delta)[0]),
                             sp.simplify(net(delta))), w)
    check("a_weight_matching_Delta_EXISTS_and_is_unique",
          len(w_delta) == 1,
          "(this is the bracket — it is exactly the one anchor being fitted)")

    w_star = sp.simplify(w_delta[0])
    combo_star = sp.simplify(combo.subs(w, w_star))
    resid = [sp.simplify((combo_star * basis_vec(i))[0] - net(basis_vec(i)))
             for i in range(N)]
    nz = [i for i, r in enumerate(resid) if sp.simplify(r) != 0]
    check("but_that_SAME_weight_then_MISSES_on_other_basis_elements",
          len(nz) > 0,
          f"disagrees on {len(nz)} of {N} basis elements "
          f"(indices {nz}) — fitting Delta does not make the functionals agree")

    q0 = Q_MP
    print()
    print(f"  w* (the weight that reproduces Delta) = {sp.simplify(w_star)}")
    print(f"  w* at q0                              = "
          f"{sp.lambdify(q, w_star, 'mpmath')(q0)}")
    print(f"  basis elements where w* then fails    = {len(nz)} of {N}")

    print()
    if FAILED:
        print(f"FAILED {len(FAILED)}/8: {', '.join(FAILED)}")
        return 1
    print("8/8 assertions hold.")
    print()
    print("READING: track 3 is closed by EXCLUSION, not left open. The two")
    print("admissible functionals span a 2-dimensional space of covectors on")
    print("H_3(q); the coordinate sum the ansatz evaluates lies OUTSIDE it.")
    print("So the bracket cannot be closed by any weight, however derived —")
    print("there is no weight to derive. A weight fitted to reproduce Delta")
    print("exists and is unique (that IS the one-parameter-one-anchor fit")
    print("qou-99qc names), and it then disagrees with `net` elsewhere in the")
    print("algebra. This does NOT show the Q-value wrong: it shows the")
    print("convex-combination repair is unavailable, so the honest options")
    print("remain (i) adopt an admissible functional and accept its error, or")
    print("(ii) derive a different element for it to act on. Scope-(b): the")
    print("exclusion is a rank computation, not a failed search.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
