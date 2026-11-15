#!/usr/bin/env python3
"""bring_descending_tower_probe.py — which cyclic quotients of Bring's curve are unramified, exactly.
Bean `qou-6082` (owner 2026-10-12, option 3: the derived descending tower). Companion to
`QOU/Brings/BringDescendingTower.lean`.

Bring's curve B: Σx = Σx² = Σx³ = 0 in ℙ⁴, S₅ permuting coordinates. For one representative g of each
non-identity conjugacy class, the fixed points of g on B are the points of B lying on the projectivised
eigenspaces of the permutation matrix. Each eigenspace is parametrised exactly (sympy, over ℚ(ζ_n)), the three
equations are restricted to it, and the projective solutions are counted.

Then, for each cyclic subgroup ⟨g⟩, Riemann–Hurwitz 2·4 − 2 = |G|(2h − 2) + Σ_x (|Stab x| − 1) gives the
quotient genus h; it must come out a non-negative integer (a check on the counts). Expected (Lean): only
3-cycles act freely, giving h = 2; the order-6 element is free itself, but its subgroup contains a
transposition. A free subgroup has every non-identity element of order 3, so it is a 3-group, and 9 ∤ 120, so it
is a C₃: the forced unramified descending tower is Σ₄ → C₂ (genus 2), and genus 2 has no non-trivial unramified
quotient. Exact arithmetic throughout; no floats. Nothing fitted.
-- Ref: [manuscript] Braden–Disney-Hogg 2024 §4 (library s40879-023-00706-0); bean qou-6082
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

X = sp.symbols("x0:5")
EQS = [sum(X), sum(v ** 2 for v in X), sum(v ** 3 for v in X)]
CLASSES = {  # cycle type -> one representative as an image list (i -> perm[i])
    "(12)": [1, 0, 2, 3, 4],
    "(12)(34)": [1, 0, 3, 2, 4],
    "(123)": [1, 2, 0, 3, 4],
    "(1234)": [1, 2, 3, 0, 4],
    "(12345)": [1, 2, 3, 4, 0],
    "(123)(45)": [1, 2, 0, 4, 3],
}


def perm_matrix(p):
    M = sp.zeros(5, 5)
    for i, j in enumerate(p):
        M[j, i] = 1
    return M


def compose(p, q):
    return [p[q[i]] for i in range(5)]


def order(p):
    k, r = 1, list(p)
    while r != list(range(5)):
        r, k = compose(p, r), k + 1
    return k


def fixed_points(p):
    """Exact fixed points of p on B, as a list of normalised coordinate tuples."""
    M = perm_matrix(p)
    pts = []
    for lam, _mult, vecs in M.eigenvects():
        c = sp.symbols(f"c0:{len(vecs)}")
        point = sum((ci * v for ci, v in zip(c, vecs)), sp.zeros(5, 1))
        polys = [sp.expand(e.subs(dict(zip(X, list(point))))) for e in EQS]
        # projective solutions: try each chart c_k = 1 with c_j = 0 for j < k
        for k in range(len(c)):
            sub = {c[j]: 0 for j in range(k)}
            sub[c[k]] = 1
            sys_ = [sp.expand(q.subs(sub)) for q in polys]
            free = [ci for ci in c[k + 1:]]
            if not free:
                if all(sp.simplify(q) == 0 for q in sys_):
                    pts.append(tuple(sp.nsimplify(sp.simplify(e.subs(sub))) for e in point))
                continue
            sols = sp.solve([q for q in sys_ if q != 0], free, dict=True)
            for s in sols:
                full = {**sub, **s}
                pts.append(tuple(sp.simplify(e.subs(full)) for e in point))
    return pts


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    counts = {}
    for name, p in CLASSES.items():
        pts = fixed_points(p)
        on = all(all(sp.simplify(e.subs(dict(zip(X, pt)))) == 0 for e in EQS) for pt in pts)
        counts[name] = len(pts)
        print(f"  {name:<10} order {order(p)}  fixed points on B: {len(pts)}  (all on curve: {on})")
        check(f"fixed_points_of_{name}_lie_on_curve", on, "exact substitution")
    check("only_3_cycles_and_order_6_are_fixed_point_free",
          {k for k, v in counts.items() if v == 0} == {"(123)", "(123)(45)"}, "Lean threeCycle_* / *_fixed_point")
    check("5_cycle_has_4_fixed_points", counts["(12345)"] == 4, "BringConjugationChirality rotExp")

    # Riemann–Hurwitz for each cyclic subgroup <g>
    rh = {}
    for name, p in CLASSES.items():
        n = order(p)
        powers, r = [], list(p)
        for _ in range(n - 1):
            powers.append(r)
            r = compose(p, r)
        fix_sets = [set(fixed_points(q)) for q in powers]
        allpts = set().union(*fix_sets)
        ram = 0
        for x in allpts:
            stab = 1 + sum(1 for fs in fix_sets if x in fs)
            ram += stab - 1
        two_h_minus_2 = sp.Rational(2 * 4 - 2 - ram, n)
        h = (two_h_minus_2 + 2) / 2
        rh[name] = {"order": n, "ramification": ram, "quotient_genus": str(h)}
        print(f"  B/<{name}>: |G| = {n}, Σ(|Stab|−1) = {ram}, quotient genus h = {h}")
        check(f"quotient_genus_by_{name}_is_a_nonnegative_integer", h.is_integer and h >= 0, "Riemann–Hurwitz")
    check("B_mod_C3_is_unramified_of_genus_2", rh["(123)"]["ramification"] == 0 and rh["(123)"]["quotient_genus"] == "2",
          "Lean free_quotient_genus; BDH24 §4 genus-2 curve C₂")
    check("order_6_subgroup_is_ramified_(contains_a_transposition)", rh["(123)(45)"]["ramification"] > 0, "power (45)")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("bring-descending-tower", engine="sympy")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "independent",
        "q0_anchor_reason": "pure algebraic geometry of Bring curve; no q",
        "q0AnchorReason": "pure algebraic geometry of Bring curve (S5 action on Sigma x = Sigma x^2 = Sigma x^3 = 0); imports only sympy and the witness builder, never q",
        "description": ("PROBE (bean qou-6082): exact fixed-point counts of each S5 conjugacy class on Bring's curve and "
                        "Riemann–Hurwitz for the cyclic quotients. Only 3-cycles generate a free subgroup; B/C3 is an "
                        "unramified genus-2 curve; the descending unramified tower is Σ4 → C2 and stops."),
        "fixed_point_counts": counts,
        "cyclic_quotients": rh,
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
