#!/usr/bin/env python3
"""Route 40 -- the distribution (Kubert) route on the 5_2 saddle orbit:
what it DOES give, and a proof that it does not close the sum rule.

Bean `qou-0yqu`.  Pairs with QOU/QBeta/FiveTwoSaddleSumRule.lean section 7d
(twelve sorry-free theorems, standard axioms).

A RETRACTION FIRST
------------------
An earlier draft of this probe (never committed) claimed the distribution
family is **vacuous** on the Galois sum -- that `Li2(z^n) = n*sum_k Li2(zeta^k z)`
summed over the orbit degenerates to `A = A`, closing the family as a no-go.
That claim is FALSE and this probe retracts it.  Two independent errors
produced it:

  1. The generating polynomial was built by REVERSING the coefficient list.
     For monic `R` of degree `d`, `prod_i (1 - X_i z) = z^d * R(1/z)`, which is
     the highest-first coefficient list read low-to-high -- already in the right
     order.  Reversing it computes a different polynomial entirely.  G1 gates
     the convention and gates that the reversed one FAILS.
  2. Granting the change of variables `u = z^n` (which IS true: `S_n = A/n`),
     the conclusion "so the relation says `A = A`" assumed `S_n` is a single new
     unknown.  It is not: `X^9-2X^6+3X^3-1` and `X^6-X^4+2X^2-1` are both
     REDUCIBLE, so `S_n` splits along the factors.  G4 gates the split.

WHAT IS ACTUALLY TRUE
---------------------
The entire tower is powers of ONE generator.  Let `c` be a root of
`X^3+X^2-1` (`c = 1/rho`, `rho` the plastic number `rho^3 = rho+1`), and write
`C_m` for `sum Li2(c_i^m)` over the three conjugates.  Then (G3)

    c^1 -> X^3+X^2-1     c^2 -> X^3-X^2+2X-1 = Q     c^3 -> X^3-2X^2+3X-1 = P
    c^5 -> X^3-4X^2+5X-1   (the reflection: `1-c = c^5`)

so the two sum-rule unknowns are `B = C_2` and `A = C_3` in a single ladder,
and every minimal polynomial has discriminant `-23 * square` -- the same
cubic field throughout.  The four available relations are

    (i)   C_2 + C_3 = elementary        reflection at `y = c^3`, since `1-c^3 = c^2`
    (ii)  C_1 + C_5 = elementary        reflection at `c`,       since `1-c   = c^5`
    (iii) C_2 = 2*(C_1 + D)             duplication,   D = sum Li2(-c_i)
    (iv)  C_3 = 3*(C_1 + E)             triplication,  E over the sextic factor

G6 verifies (i) and (ii) to 50 dps; G5 verifies (iii) and (iv) at two working
precisions.  These are real relations between genuinely different quantities --
NOT `A = A`.

AND WHY IT STILL DOES NOT CLOSE
-------------------------------
Six unknowns `(C_1, C_2, C_3, C_5, D, E)`, four relations.  G7 settles it by
linear algebra rather than by impression: the coefficient matrix has rank 4,
but stacking the functional that reads off `C_3` raises the rank to 5.  So `A`
is **provably not in the span** -- no combination of these four relations
determines it.  That is a no-go with a proof, and it is the honest replacement
for the false one above.

It does NOT close the five-term relation, Landen (Route 3), or any relation
using a root NOT of the form `c^m`.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

import sympy as sp
from mpmath import fabs, log, mp, mpf, nstr, pi, polylog, polyroots, quad
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

X = sp.symbols('X')

# --- the tower, as monic integer coefficient lists (highest degree first) ----
R1 = [1, 1, 0, -1]        # X^3+X^2-1      minimal polynomial of c        -> C_1
Q = [1, -1, 2, -1]        # X^3-X^2+2X-1   minimal polynomial of c^2 = 1-y -> C_2 = B
P = [1, -2, 3, -1]        # X^3-2X^2+3X-1  minimal polynomial of c^3 = y   -> C_3 = A
P5 = [1, -4, 5, -1]       # X^3-4X^2+5X-1  minimal polynomial of c^5 = 1-c -> C_5
R2 = [1, -1, 0, 1]        # X^3-X^2+1      the negated orbit -c            -> D
R6 = [1, -1, 1, -2, 1, 0, 1]   # the sextic factor of P(X^3)               -> E
NINE = [1, 0, 0, -2, 0, 0, 3, 0, 0, -1]     # P(X^3)
SIX = [1, 0, -1, 0, 2, 0, -1]               # Q(X^2)

# negative controls for the hypothesis screen: these DO have a root in [1,inf)
CTRL_BAD = {"X^3-X-1 (plastic)": [1, 0, -1, -1], "X^4-X-1": [1, 0, 0, -1, -1]}


def gen_poly(coeffs, z):
    """`prod_i (1 - X_i z) = z^d R(1/z)`: the highest-first coefficient list of
    a monic `R`, read LOW-TO-HIGH.  No reversal -- see the module docstring."""
    return sum(coeffs[k] * z ** k for k in range(len(coeffs)))


def has_root_in_one_to_inf(coeffs):
    """The hypothesis both routes need: no root in `[1, inf)`, which is Li2's
    branch cut.  Equivalent to `gen_poly > 0` on `[0,1]` (it is 1 at `z=0`, and
    a real zero at `z` means `1/z >= 1` is a root), and that is how it is
    tested -- so the gate checks the equivalence, not just one side."""
    rs = polyroots(coeffs, maxsteps=500, extraprec=1500)
    by_roots = any(fabs(r.imag) < mpf(10) ** -30 and r.real >= 1 for r in rs)
    lo = min(gen_poly(coeffs, mpf(k) / 512) for k in range(513))
    return by_roots, bool(lo <= 0)


def galois_sum_li2(coeffs):
    """`sum_i Li2(X_i)` over the roots of monic `R`, via
    `sum_i Li2(X_i) = -int_0^1 log prod_i(1 - X_i z) / z dz`.

    Legitimate exactly when no root lies in `[1, inf)`: then `gen_poly` is
    positive on `[0,1]`, the logarithm is real and single-valued, and there is
    no interior singularity to split at."""
    def integrand(z):
        if z == 0:
            return mpf(coeffs[1])          # log(1 + a1 z + ...)/z -> a1
        return log(gen_poly(coeffs, z)) / z
    return -quad(integrand, [0, 1])


def direct_sum_li2(coeffs):
    """The same sum by an INDEPENDENT algorithm -- mpmath's `polylog` at each
    root (series / functional equation), not the integral representation."""
    return sum(polylog(2, r) for r in polyroots(coeffs, maxsteps=500, extraprec=1500))


def power_sums(coeffs, upto):
    """Exact integer power sums of the roots of a monic integer cubic, by
    Newton's identities.  No floating point anywhere."""
    a, b, c = coeffs[1], coeffs[2], coeffs[3]
    p = [3, -a, a * a - 2 * b]
    for k in range(3, upto + 1):
        p.append(-a * p[k - 1] - b * p[k - 2] - c * p[k - 3])
    return p


def minpoly_of_power(coeffs, m):
    """The monic integer cubic annihilating `c^m`, from exact power sums via
    Newton's identities.  Returns a highest-first coefficient list."""
    p = power_sums(coeffs, 3 * m)
    q1, q2, q3 = p[m], p[2 * m], p[3 * m]
    e1 = q1
    e2 = sp.Rational(q1 * q1 - q2, 2)
    e3 = sp.Rational(q1 ** 3 - 3 * q1 * q2 + 2 * q3, 6)
    assert e2.q == 1 and e3.q == 1, "non-integral elementary symmetric function"
    return [1, int(-e1), int(e2), int(-e3)]


def cubic_disc(coeffs):
    """Discriminant of `X^3 + aX^2 + bX + c`, exact integer arithmetic."""
    a, b, c = coeffs[1], coeffs[2], coeffs[3]
    return (18 * a * b * c - 4 * a ** 3 * c + a ** 2 * b ** 2
            - 4 * b ** 3 - 27 * c ** 2)


def poly_mul(u, v):
    """Exact integer polynomial product, highest-first lists."""
    out = [0] * (len(u) + len(v) - 1)
    for i, ui in enumerate(u):
        for j, vj in enumerate(v):
            out[i + j] += ui * vj
    return out


def as_expr(coeffs):
    d = len(coeffs) - 1
    return sum(coeffs[k] * X ** (d - k) for k in range(d + 1))


def main() -> int:
    set_compute_dps()
    gates = []

    # ---- G1: the generating-polynomial convention, and that reversing FAILS --
    ok_asis, ok_rev = True, True
    for coeffs in (P, Q, R1, R6):
        rs = polyroots(coeffs, maxsteps=500, extraprec=1500)
        for num in (37, 113, 251):
            z = mpf(num) / 512
            prod = 1
            for r in rs:
                prod *= (1 - r * z)
            ok_asis &= bool(fabs(prod - gen_poly(coeffs, z)) < mpf(10) ** -35)
            ok_rev &= bool(fabs(prod - gen_poly(list(reversed(coeffs)), z))
                           < mpf(10) ** -35)
    gates.append({
        "gate": "G1",
        "claim": "`prod_i (1 - X_i z) = z^d R(1/z)` IS the highest-first coefficient list read "
                 "low-to-high, with NO reversal -- checked against the literal product over "
                 "`polyroots` at three points on four polynomials. The second half is the "
                 "negative control: the reversed convention must FAIL, because reversing it is "
                 "the natural-looking error that produced the retracted no-go",
        "as_is_matches_product": ok_asis,
        "reversed_matches_product": ok_rev,
        "pass": bool(ok_asis and not ok_rev),
    })

    # ---- G2: integral route vs an INDEPENDENT algorithm, plus the screen -----
    worst_cross = mpf(0)
    screen_ok = True
    for coeffs in (P, Q, R1, R2, P5, R6, NINE, SIX):
        by_roots, by_positivity = has_root_in_one_to_inf(coeffs)
        screen_ok &= (by_roots == by_positivity) and not by_roots
        worst_cross = max(worst_cross,
                          fabs(galois_sum_li2(coeffs) - direct_sum_li2(coeffs)))
    ctrl_rejected = {}
    for name, coeffs in CTRL_BAD.items():
        by_roots, by_positivity = has_root_in_one_to_inf(coeffs)
        ctrl_rejected[name] = bool(by_roots and by_positivity)
    gates.append({
        "gate": "G2",
        "claim": "the integral route agrees with an INDEPENDENT computation (mpmath `polylog` at "
                 "the roots) on all eight polynomials in play, and the hypothesis it needs -- no "
                 "root in [1,inf), Li2's cut -- is verified two ways that must agree. The "
                 "negative controls X^3-X-1 and X^4-X-1 DO have such a root and must be "
                 "rejected, so the screen is not decoration",
        "worst_cross_check_residual": nstr(worst_cross, 12),
        "screen_consistent_and_clean": bool(screen_ok),
        "negative_controls_rejected": ctrl_rejected,
        "pass": bool(worst_cross < mpf(10) ** -30 and screen_ok
                     and all(ctrl_rejected.values())),
    })

    # ---- G3: the tower is the powers of ONE generator -----------------------
    expected = {1: R1, 2: Q, 3: P, 5: P5}
    tower, tower_ok = {}, True
    for m in range(1, 8):
        got = minpoly_of_power(R1, m)
        disc = cubic_disc(got)
        irred = sp.Poly(as_expr(got), X).is_irreducible
        # the field discriminant is -23; a power's minimal polynomial may carry
        # an index square, so require disc = -23 * (perfect square)
        ratio = sp.Rational(disc, -23)
        sq = ratio.q == 1 and sp.sqrt(int(ratio)).is_Integer
        tower[f"c^{m}"] = {"minpoly": str(as_expr(got)), "disc": int(disc),
                           "irreducible": bool(irred), "disc_is_-23*square": bool(sq)}
        tower_ok &= bool(irred and sq)
        if m in expected:
            tower_ok &= (got == expected[m])
    gates.append({
        "gate": "G3",
        "claim": "the whole ladder is the POWERS OF ONE GENERATOR `c` (root of X^3+X^2-1, "
                 "c = 1/rho with rho the plastic number): c^2 gives Q so B = C_2, c^3 gives P so "
                 "A = C_3, and c^5 gives the reflection since 1-c = c^5. Minimal polynomials "
                 "computed by exact integer Newton identities, and every discriminant is "
                 "-23*square -- one and the same cubic field",
        "tower": tower,
        "pass": bool(tower_ok),
    })

    # ---- G4: the two inflated polynomials are REDUCIBLE ----------------------
    # This is precisely what kills the retracted "A = A" reading.
    split_nine = poly_mul(R1, R6) == NINE
    split_six = poly_mul(R2, R1) == SIX
    nine_red = not sp.Poly(as_expr(NINE), X).is_irreducible
    six_red = not sp.Poly(as_expr(SIX), X).is_irreducible
    disc_factors = {"X^3+X^2-1": int(cubic_disc(R1)), "X^3-X^2+1": int(cubic_disc(R2))}
    gates.append({
        "gate": "G4",
        "claim": "P(X^3) = X^9-2X^6+3X^3-1 and Q(X^2) = X^6-X^4+2X^2-1 are BOTH REDUCIBLE, with "
                 "the stated exact integer factorizations. This is the fact that refutes the "
                 "retracted no-go: the Li2-sum over the nine (resp. six) numbers is not one new "
                 "unknown, it splits along the factors. Both cubic factors have discriminant "
                 "-23 -- the same field as y",
        "P(X^3) = (X^3+X^2-1)(X^6-X^5+X^4-2X^3+X^2+1)": bool(split_nine),
        "Q(X^2) = (X^3-X^2+1)(X^3+X^2-1)": bool(split_six),
        "nine_reducible": bool(nine_red), "six_reducible": bool(six_red),
        "disc_of_cubic_factors": disc_factors,
        "pass": bool(split_nine and split_six and nine_red and six_red
                     and set(disc_factors.values()) == {-23}),
    })

    # ---- G5: the two distribution relations, at TWO working precisions -------
    res = {}
    for dps in (40, 60):
        mp.dps = dps
        C1, C2, C3 = galois_sum_li2(R1), galois_sum_li2(Q), galois_sum_li2(P)
        D, E = galois_sum_li2(R2), galois_sum_li2(R6)
        res[dps] = (fabs(C3 - 3 * (C1 + E)), fabs(C2 - 2 * (C1 + D)))
    set_compute_dps()
    conv = bool(res[60][0] < res[40][0] * mpf(10) ** -10
                and res[60][1] <= res[40][1] * mpf(10) ** -10 + mpf(10) ** -55)
    gates.append({
        "gate": "G5",
        "claim": "the two distribution relations hold: A = C_3 = 3*(C_1 + E) (triplication) and "
                 "B = C_2 = 2*(C_1 + D) (duplication). Evaluated at dps 40 AND 60 so that a "
                 "single-precision quadrature coincidence cannot pass -- the residual must fall "
                 "with the working precision, not merely be small once",
        "residual_dps40": [nstr(res[40][0], 8), nstr(res[40][1], 8)],
        "residual_dps60": [nstr(res[60][0], 8), nstr(res[60][1], 8)],
        "falls_with_precision": conv,
        "pass": bool(res[40][0] < mpf(10) ** -35 and res[40][1] < mpf(10) ** -35 and conv),
    })

    # ---- G6: the two reflections --------------------------------------------
    refl = {}
    for tag, coeffs, lhs in (("y-orbit: C_2 + C_3", P, None), ("c-orbit: C_1 + C_5", R1, None)):
        rs = polyroots(coeffs, maxsteps=500, extraprec=1500)
        elem = pi ** 2 / 2 - sum(log(r) * log(1 - r) for r in rs)
        got = (galois_sum_li2(Q) + galois_sum_li2(P)) if "y-orbit" in tag \
            else (galois_sum_li2(R1) + galois_sum_li2(P5))
        refl[tag] = nstr(fabs(got - elem), 10)
    refl_ok = all(mpf(v) < mpf(10) ** -40 for v in refl.values())
    gates.append({
        "gate": "G6",
        "claim": "both reflections close in elementary terms with PRINCIPAL logs and no branch "
                 "correction: C_2 + C_3 = pi^2/2 - sum log y log(1-y) over the y-orbit, and "
                 "C_1 + C_5 = the same over the c-orbit. `1-c^3 = c^2` and `1-c = c^5` are why "
                 "these two land inside the tower instead of introducing fresh orbits",
        "residuals": refl,
        "pass": bool(refl_ok),
    })

    # ---- G7: the system provably does NOT determine A ------------------------
    # unknowns, in order: C_1, C_2, C_3, C_5, D, E
    M = sp.Matrix([[0, 1, 1, 0, 0, 0],      # (i)   C_2 + C_3 = elementary
                   [1, 0, 0, 1, 0, 0],      # (ii)  C_1 + C_5 = elementary
                   [-2, 1, 0, 0, -2, 0],    # (iii) C_2 = 2(C_1 + D)
                   [-3, 0, 1, 0, 0, -3]])   # (iv)  C_3 = 3(C_1 + E)
    read_off_A = sp.Matrix([[0, 0, 1, 0, 0, 0]])
    rank_M = M.rank()
    rank_aug = M.col_join(read_off_A).rank()
    gates.append({
        "gate": "G7",
        "claim": "THE ROUTE DOES NOT CLOSE, and this is a proof rather than an impression. Six "
                 "unknowns (C_1, C_2, C_3, C_5, D, E), four relations. The functional that reads "
                 "off A = C_3 lies in the row space iff rank is unchanged when it is stacked on. "
                 "It is not: rank goes 4 -> 5, so NO combination of reflection + duplication + "
                 "triplication over this tower determines A",
        "rank_of_relations": int(rank_M),
        "rank_with_target_stacked": int(rank_aug),
        "A_determined": bool(rank_M == rank_aug),
        "solution_family_dimension": int(6 - rank_M),
        "pass": bool(rank_M == 4 and rank_aug == 5),
    })

    # ---- G8: the retraction, gated ------------------------------------------
    # `S_9 = A/3` is TRUE (change of variables u = z^n).  What is FALSE is
    # reading that as `A = A`, which needs `S_9` to be a single new unknown.
    S9, C1, E = galois_sum_li2(NINE), galois_sum_li2(R1), galois_sum_li2(R6)
    A = galois_sum_li2(P)
    gates.append({
        "gate": "G8",
        "claim": "the retracted claim, isolated. The change of variables IS true: S_9 = A/3 to "
                 "40+ digits. The retracted step was reading that as `A = A`, which requires S_9 "
                 "to be one atomic new unknown. It is not -- S_9 = C_1 + E with BOTH parts "
                 "nonzero and C_1 far from S_9. So the relation connects genuinely different "
                 "quantities and the family is NOT vacuous",
        "change_of_variables_holds |A - 3*S9|": nstr(fabs(A - 3 * S9), 10),
        "S9_splits |S9 - (C1+E)|": nstr(fabs(S9 - (C1 + E)), 10),
        "C1": nstr(C1, 20), "E": nstr(E, 20), "S9": nstr(S9, 20),
        "|C1 - S9|": nstr(fabs(C1 - S9), 12),
        "pass": bool(fabs(A - 3 * S9) < mpf(10) ** -35
                     and fabs(S9 - (C1 + E)) < mpf(10) ** -35
                     and fabs(C1) > mpf(10) ** -3 and fabs(E) > mpf(10) ** -3
                     and fabs(C1 - S9) > mpf(10) ** -3),
    })

    out = {
        "probe": "qbeta_5two_route40_distribution_factors",
        "bean": "qou-0yqu", "dps": mp.dps,
        "pairs_with_lean": ["QOU/QBeta/FiveTwoSaddleSumRule.lean section 7d "
                            "(12 theorems, sorry-free, standard axioms)"],
        "retracts": "the never-committed claim that the distribution (Kubert) family is VACUOUS "
                    "on the Galois sum, i.e. that summing it gives `A = A`. False -- see G1 "
                    "(reversed generating polynomial) and G4/G8 (the inflated polynomials are "
                    "reducible, so the inflated sum is not one atomic unknown).",
        "gates": gates,
        "verdict": {
            "structure": "the tower is the powers of one generator c (root of X^3+X^2-1, "
                         "c = 1/rho, rho the plastic number): B = C_2, A = C_3, and the "
                         "reflection of C_1 is C_5 because 1-c = c^5. Every minimal polynomial "
                         "has discriminant -23*square: one cubic field throughout.",
            "relations": "four, all verified numerically here: C_2+C_3 and C_1+C_5 elementary "
                         "(reflection), C_2 = 2(C_1+D) (duplication), C_3 = 3(C_1+E) "
                         "(triplication).",
            "no_go": "six unknowns, four relations, and the functional reading off A is NOT in "
                     "the row space -- rank 4 -> 5 when stacked. So distribution + reflection "
                     "over this tower provably cannot determine A. Unlike the retracted claim, "
                     "this is a rank computation, not an integral identity.",
            "not_closed_by_this": "the five-term relation, Landen (Route 3), and any relation "
                                  "using a root not of the form c^m are all untouched.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route40-distribution-factors.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:78]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "distribution route MAPPED and bounded -- it gives four real relations and provably "
        "cannot determine A (rank 4 -> 5). The retracted 'A = A' no-go is refuted by G1/G4/G8. "
        "The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
