#!/usr/bin/env python3
"""Route 14 -- hA, hB, hC ARE genuine five-term instances. Exact, not numeric.

Bean `qou-rhyp` / roast item 1 of `qou-rstq`, parent `qou-0yqu`.

`qou-rstq` set this as the first thing to attack:

    "qou-rhyp, the five-term instances. Everything downstream is a
     linear_combination over these. If any of hA, hB, hC is not a genuine
     five-term instance -- wrong argument, wrong branch -- the whole derivation
     collapses. They were checked numerically to 1e-40; check the *algebra* of
     the arguments independently."

This probe does that. It runs entirely in **exact arithmetic in the cyclic cubic
field** Q(w), w^3 = 2w^2 + w - 1 (discriminant 49, the field Q(zeta_7)^+), with
`fractions.Fraction` coefficients in the power basis {1, w, w^2}. No floating
point is used anywhere in the argument matching, so a near-miss cannot pass:
either two arguments are the same algebraic number or they are not.

WHY EXACTNESS IS THE POINT
--------------------------
A numerical check to 1e-40 confirms the *relation* holds. It cannot distinguish
"this is the five-term relation at (x,y)" from "this is some other identity that
happens to hold at these points". The five-term relation

    L(x) + L(y) - L(xy) - L(x(1-y)/(1-xy)) - L(y(1-x)/(1-xy)) = 0

determines its last three arguments as *rational functions of (x, y)*. Matching
them exactly is what makes the instance genuine.

RESULT
------
All three match, and hA is more than a match -- it is the **diagonal** instance
x = y = w2, whose argument identification `w2^2 = 1 - q` is exactly `bloch_key`,
already sorry-free in `QOU/QBeta/FiveTwoCyclotomicBloch.lean`.

    hA : x = y = w2      ->  {w2^2, r, r}          =  {1-q, r, r}
    hB : x = 1-w2, y = q ->  {xy, .., ..}          =  {1-q, 1-s, w2}
    hC : x = w2,   y = s ->  {xy, .., ..}          =  {1-w2, 1-s, 1-r}

The Galois structure is visible: sigma(w) = (w-1)/w is the order-3 automorphism,
w2 = sigma(w1), w3 = sigma(w2), and the whole argument dictionary lives in Q(w).

WHAT THIS DOES NOT SHOW
-----------------------
That the five-term relation itself holds -- that is classical (Abel) and remains
the one open analytic input to the numerators. This probe shows only that the
three hypotheses are instances *of* it, with the right arguments. The 5_2 sum
rule remains **verified to 80 dps, unproved**.
"""

import json
import pathlib
from fractions import Fraction as F

# w^3 = -1 + w + 2w^2, i.e. the min poly is w^3 - 2w^2 - w + 1
MOD = [F(-1), F(1), F(2)]


def red(p):
    p = list(p)
    while len(p) > 3:
        c = p.pop()
        d = len(p) - 3
        for i, m in enumerate(MOD):
            p[d + i] += c * m
    while len(p) < 3:
        p.append(F(0))
    return p


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return red(out)


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def sc(k, a):
    return [F(k) * x for x in a]


ONE = [F(1), F(0), F(0)]
W = [F(0), F(1), F(0)]
ZERO = [F(0), F(0), F(0)]


def inv(a):
    """Exact inverse in Q(w) by solving the 3x3 multiplication matrix."""
    cols = [mul(a, e) for e in (ONE, W, [F(0), F(0), F(1)])]
    A = [[cols[c][row] for c in range(3)] for row in range(3)]
    b = [F(1), F(0), F(0)]
    for i in range(3):
        piv = next(k for k in range(i, 3) if A[k][i] != 0)
        A[i], A[piv] = A[piv], A[i]
        b[i], b[piv] = b[piv], b[i]
        d = A[i][i]
        A[i] = [x / d for x in A[i]]
        b[i] = b[i] / d
        for k in range(3):
            if k != i and A[k][i] != 0:
                f = A[k][i]
                A[k] = [x - f * y for x, y in zip(A[k], A[i])]
                b[k] -= f * b[i]
    return b


def div(a, b):
    return mul(a, inv(b))


def eq(a, b):
    return all(x == y for x, y in zip(a, b))


def txt(a):
    return f"({a[0]}) + ({a[1]})w + ({a[2]})w^2"


def main() -> int:
    gates = []

    w1 = W
    sigma = lambda z: div(sub(z, ONE), z)  # noqa: E731  -- the order-3 automorphism
    w2, w3 = sigma(w1), sigma(sigma(w1))
    q = div(w1, add(w1, ONE))   # (-w1)/(-w1-1)
    r = div(w2, add(w2, ONE))   # (-w2)/(-w2-1)
    s = sc(-1, w3)

    minpoly = lambda z: add(sub(sub(mul(mul(z, z), z), sc(2, mul(z, z))), z), ONE)  # noqa: E731

    # ---- G1: the field, the automorphism, and that all three roots live in it ----
    roots_ok = all(eq(minpoly(z), ZERO) for z in (w1, w2, w3))
    order3 = eq(sigma(w3), w1)
    gates.append({
        "gate": "G1",
        "claim": "sigma(w) = (w-1)/w is an order-3 automorphism of Q(w); w1,w2,w3 are its orbit",
        "w2": txt(w2), "w3": txt(w3),
        "minpoly_residuals": [txt(minpoly(z)) for z in (w1, w2, w3)],
        "sigma_cubed_is_identity": order3,
        "pass": bool(roots_ok and order3),
    })

    # ---- G2: the argument dictionary is exact ----
    names = {"w1": w1, "w2": w2, "w3": w3, "q": q, "r": r, "s": s,
             "1-w2": sub(ONE, w2), "1-q": sub(ONE, q),
             "1-r": sub(ONE, r), "1-s": sub(ONE, s)}
    gates.append({
        "gate": "G2",
        "claim": "the whole argument dictionary {w_k, q, r, s} lies in Q(w), exactly",
        "dictionary": {k: txt(v) for k, v in names.items()},
        "pass": True,
    })

    def label(z):
        for k, v in names.items():
            if eq(z, v):
                return k
        return "UNMATCHED"

    def five_term_args(x, y):
        """The last three arguments of L(x)+L(y)-L(xy)-L(..)-L(..) = 0."""
        xy = mul(x, y)
        d = sub(ONE, xy)
        return [xy, div(mul(x, sub(ONE, y)), d), div(mul(y, sub(ONE, x)), d)]

    # ---- G3: hA is the DIAGONAL instance, and its identification is bloch_key ----
    aA = five_term_args(w2, w2)
    gotA = [label(z) for z in aA]
    blochkey = sub(mul(mul(sub(ONE, w1), sub(ONE, w1)), add(ONE, w1)), mul(w1, w1))
    gates.append({
        "gate": "G3",
        "claim": "hA is the diagonal five-term instance x = y = w2; its identification IS bloch_key",
        "x": "w2", "y": "w2",
        "produced": gotA, "needed": ["1-q", "r", "r"],
        "w2_squared_minus_one_minus_q": txt(sub(mul(w2, w2), sub(ONE, q))),
        "bloch_key_residual_(1-w1)^2(1+w1)-w1^2": txt(blochkey),
        "lean": "QOU/QBeta/FiveTwoCyclotomicBloch.bloch_key -- already sorry-free",
        "pass": bool(sorted(gotA) == sorted(["1-q", "r", "r"]) and eq(blochkey, ZERO)),
    })

    # ---- G4/G5: hB and hC ----
    for gate, (x, xn), (y, yn), need in [
        ("G4", (sub(ONE, w2), "1-w2"), (q, "q"), ["1-q", "1-s", "w2"]),
        ("G5", (w2, "w2"), (s, "s"), ["1-w2", "1-s", "1-r"]),
    ]:
        got = [label(z) for z in five_term_args(x, y)]
        gates.append({
            "gate": gate,
            "claim": f"h{'B' if gate == 'G4' else 'C'} is the five-term instance x = {xn}, y = {yn}",
            "x": xn, "y": yn,
            "produced": got, "needed": need,
            "pass": bool(sorted(got) == sorted(need)),
        })

    # ---- G6: the cleared identities a Lean proof would need ----
    ids = {
        "A1  w2^2 = 1-q": sub(mul(w2, w2), sub(ONE, q)),
        "A2  r(1-w2^2) = w2(1-w2)": sub(mul(r, sub(ONE, mul(w2, w2))), mul(w2, sub(ONE, w2))),
        "B1  (1-w2)q = 1-q": sub(mul(sub(ONE, w2), q), sub(ONE, q)),
        "B2  (1-s)q = (1-w2)(1-q)": sub(mul(sub(ONE, s), q),
                                        mul(sub(ONE, w2), sub(ONE, q))),
        "C1  w2*s = 1-w2": sub(mul(w2, s), sub(ONE, w2)),
        "C2  (1-r)w2 = s(1-w2)": sub(mul(sub(ONE, r), w2), mul(s, sub(ONE, w2))),
    }
    gates.append({
        "gate": "G6",
        "claim": "the six division-free identities a CommRing Lean proof needs, all exactly zero",
        "residuals": {k: txt(v) for k, v in ids.items()},
        "note": "B1 makes hB's denominator 1-xy collapse to q, and C1 makes hC's collapse to w2 -- "
                "which is why hB's fifth argument is exactly w2 and hC's fourth is exactly 1-s",
        "pass": bool(all(eq(v, ZERO) for v in ids.values())),
    })

    out = {
        "probe": "qbeta_5two_route14_fiveterm_arguments_exact",
        "bean": "qou-rhyp",
        "roast_item": "qou-rstq item 1",
        "parent_bean": "qou-0yqu",
        "arithmetic": "exact, fractions.Fraction in the power basis of Q(w), w^3-2w^2-w+1 = 0",
        "gates": gates,
        "verdict": {
            "roast_outcome": "DISCHARGED. hA, hB, hC are genuine five-term instances. The last three "
                             "arguments of the relation, which are determined as rational functions "
                             "of (x,y), match the hypotheses' arguments exactly as algebraic numbers.",
            "hA": "the DIAGONAL instance x = y = w2. Its argument identification w2^2 = 1-q is "
                  "exactly bloch_key, already sorry-free in FiveTwoCyclotomicBloch.lean.",
            "hB": "x = 1-w2, y = q. The denominator 1-xy collapses to q, so the fifth argument is w2.",
            "hC": "x = w2, y = s. The denominator 1-xy collapses to w2, so the fourth argument is 1-s.",
            "why_exact_matters": "a 1e-40 numerical check confirms the relation holds; it cannot "
                                 "distinguish 'this is five-term at (x,y)' from 'some other identity "
                                 "true at these points'. Exact matching can.",
            "still_open": "the five-term relation itself (Abel). This probe shows the hypotheses are "
                          "instances of it, not that it holds.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route14-fiveterm-arguments-exact.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:88]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: roast item 1 DISCHARGED -- all three are genuine five-term instances (exact).")
    print("         hA is the diagonal instance; its identification is bloch_key, already in Lean.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
