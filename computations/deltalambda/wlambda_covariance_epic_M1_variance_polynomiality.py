#!/usr/bin/env python3
"""M_1>0 (qou-k5r5): is V_A(n) = Var(Sum|c|) an exact POLYNOMIAL in n? If it is, delta_A is exactly
computable and the one remaining analytic gap collapses. Decisive, cheap, exact -- and with a
positive control, so a negative result is about the corpus rather than about this script.

WHY THIS, NOW. PR #6602 narrowed the remaining work to a single target: a rigorous finite-n bound on
delta_A = (V_A/n^2 - v_A)/v_A. Before attacking that analytically (a Kerov-CLT-with-explicit-error
project), the formalize-first discipline says check whether the object has an exact closed form. A
polynomial V_A(n) would not merely bound delta_A -- it would give it exactly, at every n, and the
n >= 79 tail with it.

WHAT THE CORPUS ALREADY SAYS, and this probe does NOT re-derive it. The non-polynomiality of
M_1 = Cov(Sum h, Sum c^2) is established and explained:
  - docs/audits/2026-07-25-covariance-kernel-A2-odd-moment-structure.md: for EVEN k both weights are
    shifted-symmetric and M_{2j} is an exact polynomial in n; the odd weight Sum h^{2j+1} is NOT
    shifted-symmetric, so M_{2j+1} is non-polynomial.
  - docs/audits/2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md: "the non-polynomiality
    of M_1 is carried entirely by the non-shifted-symmetric" part; Sum c^2 is in the algebra.

Those are statements about the COVARIANCE family M_k. V_A = Var(Sum|c|) is a DIFFERENT object and
nothing in the corpus measures it. Sum|c| is not shifted-symmetric either (|.| is not a polynomial),
so the expectation is that V_A is non-polynomial too -- but "expected by analogy" is not measured,
and the payoff if the analogy fails is large enough to be worth one cheap check.

THE OBJECTS, named precisely (from the C-landscape probe's stats()):
    A = Sum_cells |c|        the first ABSOLUTE moment of the content distribution   (c = j - i)
    D = Sum_u d_u^2          d_u = #cells of content u; sum of squared diagonal multiplicities
    W = Sum_cells c^2 - C(n,2)                the second moment, recentred
    V_A = Var(A), V_D = Var(D), V_W = Var(W), P = Cov(A, W)      all under Plancherel

METHOD. For each quantity Q, exact Fraction values Q(n) are computed by summing over EVERY partition
of n. A degree-d polynomial is then fitted by exact Lagrange interpolation through the FIRST d+1
points and evaluated at every REMAINING point. Exact agreement on all held-out n is the test; a fit
that merely reproduces its own interpolation nodes proves nothing, which is why the held-out set is
the verdict and the nodes are excluded from it.

THE POSITIVE CONTROL, and it is the point of the design. Sum c^2 IS shifted-symmetric, so V_W should
come out an exact polynomial. If it does, the fitter works and a NONE verdict elsewhere is a fact
about the object. If V_W also comes out NONE, this script is broken and NO verdict here may be
quoted -- a negative from an unvalidated detector is the failure mode this corpus has paid for
repeatedly.

scope-(a); no fit to data (exact interpolation is not a fit in the anti-fit sense -- nothing is
tuned, and the verdict is exact agreement or none); nothing wired; no c_k; L2 unchanged.
Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import importlib.util
import pathlib

MAXDEG = 10


def _load_cl():
    """Import partitions()/stats()/fact() by explicit file path (not a bare name: the _path_bridge
    bootstrap trap -- this probe must run with PYTHONPATH unset)."""
    here = pathlib.Path(__file__).resolve().parent
    src = here / "wlambda_covariance_epic_M1_constant_C_landscape.py"
    spec = importlib.util.spec_from_file_location("_m1_cl", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def moments(mod, n):
    """Exact (V_A, V_D, V_W, P) at size n, as Fractions, over every partition of n."""
    nf = mod.fact(n)
    Cn2 = F(n * (n - 1), 2)
    ac = {k: F(0) for k in ("A", "D", "W", "AA", "DD", "WW", "AW")}
    for lam in mod.partitions(n):
        d, A, Dd, c2 = mod.stats(lam, n)
        w = F(d * d, nf)
        W = F(c2) - Cn2
        ac["A"] += w * A; ac["D"] += w * Dd; ac["W"] += w * W
        ac["AA"] += w * A * A; ac["DD"] += w * Dd * Dd; ac["WW"] += w * W * W
        ac["AW"] += w * A * W
    return (ac["AA"] - ac["A"] ** 2,
            ac["DD"] - ac["D"] ** 2,
            ac["WW"] - ac["W"] ** 2,
            ac["AW"] - ac["A"] * ac["W"])


def lagrange_at(nodes, values, x):
    """Exact Lagrange interpolation through (nodes, values), evaluated at x. All Fractions."""
    total = F(0)
    for i, xi in enumerate(nodes):
        term = values[i]
        for j, xj in enumerate(nodes):
            if i == j:
                continue
            term *= F(x - xj, xi - xj)
        total += term
    return total


def smallest_polynomial_degree(ns, vals, maxdeg=MAXDEG):
    """Smallest d <= maxdeg such that the degree-d interpolant through the first d+1 points
    reproduces EVERY held-out point exactly. Returns (d, n_heldout) or (None, n_heldout_at_maxdeg)."""
    for d in range(maxdeg + 1):
        if len(ns) < d + 2:                     # need at least one held-out point
            break
        nodes, values = ns[:d + 1], vals[:d + 1]
        held = ns[d + 1:]
        if all(lagrange_at(nodes, values, x) == vals[ns.index(x)] for x in held):
            return d, len(held)
    return None, max(0, len(ns) - (maxdeg + 1))


def main():
    mod = _load_cl()
    nmin, nmax = 2, 30
    print(f"# is V_A an exact polynomial in n?  exact Fraction arithmetic; NO float64 anywhere")
    print(f"#   window n = {nmin}..{nmax};  max degree tried = {MAXDEG}")
    print("#   A = Sum|c|   D = Sum_u d_u^2   W = Sum c^2 - C(n,2)   (Plancherel)")
    print("#")

    ns, rows = [], {"V_A": [], "V_D": [], "V_W": [], "P": []}
    for n in range(nmin, nmax + 1):
        vA, vD, vW, p = moments(mod, n)
        ns.append(n)
        rows["V_A"].append(vA); rows["V_D"].append(vD)
        rows["V_W"].append(vW); rows["P"].append(p)

    print(f"#   {'n':>3} {'V_A':>26} {'V_W':>20}")
    for i, n in enumerate(ns):
        if n <= 6 or n % 6 == 0:
            print(f"#   {n:>3} {str(rows['V_A'][i]):>26} {str(rows['V_W'][i]):>20}")
    print("#")

    verdicts = {}
    for key in ("V_W", "P", "V_A", "V_D"):
        d, held = smallest_polynomial_degree(ns, rows[key])
        verdicts[key] = d
        if d is None:
            print(f"#   {key:>4}: NOT a polynomial of degree <= {MAXDEG}   "
                  f"(every degree mispredicts held-out n)")
        else:
            print(f"#   {key:>4}: EXACT polynomial of degree {d}   "
                  f"(reproduces all {held} held-out n exactly)")
    print("#")

    # --- V_W's closed form, CHECKED at every n rather than read off the table by eye. The degree-3
    #     verdict plus the values 0, 2, 8, 20, 40, ... suggest 2*C(n,3); assert it exactly.
    wclosed = all(rows["V_W"][i] == F(n * (n - 1) * (n - 2), 3) for i, n in enumerate(ns))
    print("# V_W IN CLOSED FORM (checked exactly at every tabulated n, not fitted):")
    if wclosed:
        print(f"#   V_W = Var(Sum c^2) = n(n-1)(n-2)/3 = 2*C(n,3)   -- EXACT at all {len(ns)} values.")
        print("#   Consequence for the remaining bound: rho_P = P / sqrt(V_A V_W), so ONE of its three")
        print("#   ingredients carries NO finite-n error at all. Only P and V_A do. This is a small")
        print("#   simplification of the open target, not a step toward closing it.")
        print("#   (Classical for a shifted-symmetric weight; confirmed here, not claimed as new.)")
    else:
        bad = [n for i, n in enumerate(ns) if rows["V_W"][i] != F(n * (n - 1) * (n - 2), 3)]
        print(f"#   n(n-1)(n-2)/3 does NOT hold; first failures at n = {bad[:5]}. The degree-3 verdict")
        print("#   stands but the closed form guessed from the table does not -- do not quote it.")
    print("#")

    control_ok = verdicts["V_W"] is not None
    print("# POSITIVE CONTROL. Sum c^2 is shifted-symmetric, so V_W SHOULD be an exact polynomial.")
    if control_ok:
        print(f"#   V_W came out polynomial (degree {verdicts['V_W']}) => the fitter works, and a")
        print("#   NONE verdict below is a fact about the object, not about this script.")
    else:
        print("#   V_W did NOT come out polynomial. The control FAILED, so this script is broken and")
        print("#   NO verdict here may be quoted. Fix the fitter before reading anything else.")
    print("#")

    if not control_ok:
        result = ("CONTROL FAILED (V_W should be polynomial and was not) -- no verdict from this "
                  "probe may be quoted; the fitter is wrong, not the corpus")
    elif verdicts["V_A"] is None:
        result = (f"V_A is NOT an exact polynomial in n (degree <= {MAXDEG}), with the V_W control "
                  f"passing at degree {verdicts['V_W']}. So delta_A has no closed form by this route "
                  f"and the rigorous finite-n bound remains the only way through")
    else:
        result = (f"V_A IS an exact polynomial in n of degree {verdicts['V_A']} -- delta_A is then "
                  f"exactly computable at every n and the qou-k5r5 finite-n gap collapses; verify "
                  f"this independently before acting on it")
    print(f"# {result}.")
    print("#")
    print("# WHAT A NEGATIVE HERE DOES AND DOES NOT SETTLE. It rules out a polynomial in n up to")
    print(f"#   degree {MAXDEG} over n <= {nmax}. It does NOT rule out a closed form of another shape")
    print("#   (a polynomial divided by a falling factorial, a harmonic-augmented form, a two-term")
    print("#   recursion). The corpus has already tried several such shapes for M_1 and found none")
    print("#   (2026-08-21-…-antidiagonal-reformulation.md: poly_4 and n^2 H_n + poly_3 both fail);")
    print("#   this probe does not repeat those and does not extend them to V_A.")
    print(f"RESULT: {result}. Degrees: " +
          ", ".join(f"{k}={'NONE' if v is None else v}" for k, v in verdicts.items()) +
          ". qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
