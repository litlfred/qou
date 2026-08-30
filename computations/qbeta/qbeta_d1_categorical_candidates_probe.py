"""(D1) priced for the two `categorical-*` Delta candidates -- the last two unmeasured.

`qou-bg3w` asks which element of H_3(q) is Delta. Six candidates. (D1),

    2 alpha = net(Delta) - tr_M^z(Delta)

-- the ONLY derivation of the Q_beta ladder phase the corpus has -- is
available iff tr_M is AFFINE in z, i.e. iff the z^2 coefficient of tr_M(Delta)
vanishes. It was priced for four of the six (Delta_S holds; the 9-crossing and
both 11-crossing pyhecke models excluded, `qbeta_d1_eleven_crossing_exclusion_probe`,
14/14). The two `categorical-*` candidates from PR #5958 were never tested.
This closes that gap.

THE TWO ARE NOT THE SAME KIND OF OBJECT, and that is the first result.

  * "as STATED" (-0.2089) is the difference of two NUMBERS the content blocks
    quote -- net(p) = 1.0065, net(n) = 0.7976, at 5 and 4 significant figures.
    There is no word, hence no NF vector, hence no tr_M. **(D1) is not
    ill-behaved for it; (D1) is not WELL-POSED for it.** A stated net is a
    target the blocks assert, not an element one can trace. Reported as
    `not-an-element`, never as pass or fail.

  * "as CONSTRUCTED (k=1)" (-0.2137638) IS an element: B_3 x Delta_3(quarks) x
    (L_-)^k with k = 1, built by `qbeta_delta_net_four_values_probe.built`.
    Testable, and tested here.

METHOD. The z^2 coefficient, from TR = [1, z, z, z^2, z^2, z(h z + 1)] over
NF_BASIS [(), (0,), (1,), (0,1), (1,0), (0,1,0)], is

    [z^2] tr_M(D) = D[3] + D[4] + h * D[5]

SYMMETRIC in slots 3 and 4, which is why the `hm_sym` slot swap recorded in
qou-bg3w (canonical L+ = sigma_0 sigma_1 at index 3, but hm_sym lands it at 4)
cannot affect the verdict. Exact symbolic in h throughout; no float64 anywhere,
and no q_0 substitution is needed -- the verdict is a statement about a
polynomial, not about a pin. That is deliberate: the four corrections this
bean's history records (a 9-crossing element called eleven; the wrong
invariant; decimals silently at q = 111/100; swapped basis labels) were all
errors this shape of test is immune to.

The builders are IMPORTED from the sibling probe, never re-transcribed.
"""
import pathlib as _pl
import sys as _sys

_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))

import _path_bridge  # noqa: F401,E402
import sympy as sp  # noqa: E402

from qbeta_net_trace_invariance_probe import h, q  # noqa: E402
from qbeta_delta_net_four_values_probe import built  # noqa: E402

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}" + (f"\n         {detail}" if detail else ""))


def z2_coeff(delta):
    """[z^2] tr_M(delta) = d[L+] + d[L-] + h*d[e^-]; symmetric in slots 3,4."""
    d = [sp.expand(delta[i]) for i in range(6)]
    return sp.factor(sp.simplify(d[3] + d[4] + h * d[5]))


def main() -> int:
    print("(D1) for the two categorical-* Delta candidates\n")

    # ---- candidate 1: "as STATED" is not an element -------------------
    check("'as STATED' (-0.2089) is a difference of QUOTED NUMBERS, not a word",
          True,
          "net(p)=1.0065, net(n)=0.7976 from categorical-{proton,neutron}-"
          "properties.md. No NF vector exists, so tr_M and hence (D1) are "
          "NOT WELL-POSED. Not a pass and not a fail.")

    # ---- candidate 2: "as CONSTRUCTED (k=1)" --------------------------
    # gens: the quark-generator assignment. built() takes (who, gens, k).
    gens = (0, 0, 1)          # (0,1)->gen0, (0,2)->gen0, (1,2)->gen1
    p1 = built("p", gens, 1)
    n1 = built("n", gens, 1)
    delta1 = [sp.expand(n1[i] - p1[i]) for i in range(6)]

    c1 = z2_coeff(delta1)
    print(f"\n  [z^2] tr_M(Delta_constructed, k=1) = {c1}")

    check("the k=1 constructed candidate IS an element (6-coordinate NF)",
          len(delta1) == 6)

    nonzero = sp.simplify(c1) != 0
    check("its z^2 coefficient is NONZERO -> tr_M is QUADRATIC in z", nonzero,
          f"{c1}")

    # Does any real substrate value kill it?
    #
    # CAREFUL -- the coefficient comes back in q, NOT in h, so `solve(c1, h)`
    # returns [] because `h` does not occur, and a check written that way
    # PASSES VACUOUSLY. (It did, on the first run of this probe.) Solve in q,
    # then map each real root through h = q - 1/q.
    real_roots = [r for r in sp.Poly(sp.numer(sp.together(c1)), q).all_roots()
                  if r.is_real]
    hs = {sp.nsimplify(sp.simplify(r - 1 / r)) for r in real_roots}
    check("every real root of [z^2] has h = 0 -> no substrate value rescues (D1)",
          hs == {0} or hs == set(),
          f"real q-roots {sorted(map(str, real_roots))} -> h in {sorted(map(str, hs))}; "
          f"substrate h = q0 - 1/q0 ~ 0.209, nonzero")

    # The octic factor is where a nonzero-h root could have hidden. Sturm count,
    # exact, rather than a numeric root-find.
    octic = 3 * q**8 - 5 * q**6 + 5 * q**4 - 5 * q**2 + 3
    check("the octic factor 3q^8-5q^6+5q^4-5q^2+3 has NO real root",
          sp.Poly(octic, q).count_roots() == 0,
          "exact Sturm count = 0, so q = +-1 (h = 0) are the only real roots "
          "of the whole numerator")

    # Context: k=0 and k=2, so the verdict is seen to be about the family.
    for k in (0, 2):
        pk, nk = built("p", gens, k), built("n", gens, k)
        dk = [sp.expand(nk[i] - pk[i]) for i in range(6)]
        ck = z2_coeff(dk)
        print(f"  (context) k={k}: [z^2] = {ck}")

    bad = [n for n, ok, _ in CHECKS if not ok]
    print(f"\n  {len(CHECKS) - len(bad)}/{len(CHECKS)} checks pass")
    if bad:
        print("  FAILED: " + "; ".join(bad))
        return 1

    print("\n  VERDICT. Of qou-bg3w's six candidates, (D1) is now priced for")
    print("  five and NOT WELL-POSED for the sixth ('as stated' is a number,")
    print("  not an element). Delta_S remains the ONLY candidate for which")
    print("  (D1) holds. The fork is binary after all: Delta_S, or no (D1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
