#!/usr/bin/env python3
"""⁴He with the γγ bond on all six pairs, exact in q (issue #9039; preregistration.md addendum 2).

Four formation routes × over/under transport, production order p p n n, plus the chain as a
control. The first nucleon factors out (towerTr_disjoint, proved): tr_atom = tr N₀ · tr(tail),
so the trace runs on 10 strands. Exact ℚ(q) via hecke_flint; exact Fractions at the proton pin.
No float in any computed quantity; mpmath only formats. AME is comparison only.
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "he4_closed_form"))
sys.path.insert(0, os.path.join(HERE, "..", "he4_all_pairs_formation"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools", "qou-substrate", "python"))
import flint  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import hecke_flint as F  # noqa: E402
from hecke_exact import Ring  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 40
T0 = time.time()
E0_MEV = Fraction("4.227483355629030550268056026587211153615")  # he4-gg-all-pairs.witness.json
AME_KEV = Fraction("28295.673")  # AME2020 ⁴He, comparison only
ORDER = "ppnn"
# ROUTES_HE4 of ../he4_all_pairs_formation/he4_all_pairs_formation_probe.py (copied: that
# module imports the mpmath stack at load time)
ROUTES = {
    "D+D pairing a": [(0, 2), (1, 3), (0, 1), (2, 3), (1, 2), (0, 3)],
    "D+D pairing b": [(1, 2), (0, 3), (0, 1), (2, 3), (0, 2), (1, 3)],
    "3H+p": [(1, 2), (2, 3), (1, 3), (0, 1), (0, 2), (0, 3)],
    "3He+n": [(0, 1), (1, 2), (0, 2), (2, 3), (1, 3), (0, 3)],
}
CHAIN = [(0, 1), (1, 2), (2, 3)]
qq, yy = sp.symbols("q y")
Qp = flint.fmpq_poly([0, 1])


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def to_y(P):
    """Even P(q) as a polynomial in y = q² − 1 (coefficients, constant first)."""
    c = [P[i] for i in range(P.degree() + 1)]
    assert all(c[i] == 0 for i in range(1, len(c), 2)), "not even"
    pe = flint.fmpq_poly(c[0::2])
    Py = pe(flint.fmpq_poly([1, 1]))
    return [Py[i] for i in range(Py.degree() + 1)]


def flint_to_sympy(P):
    return sum(sp.Rational(int(P[i].p), int(P[i].q)) * qq**i for i in range(P.degree() + 1))


DP = Qp**18 - 3*Qp**16 + 7*Qp**14 - 8*Qp**12 + 10*Qp**10 - 9*Qp**8 + 10*Qp**6 - 6*Qp**4 + 3*Qp**2 - 1
DN = Qp**14 - 3*Qp**12 + 4*Qp**10 - 4*Qp**8 + 5*Qp**6 - 4*Qp**4 + 3*Qp**2 - 1
DEN_OK = [Qp, Qp * Qp + 1, Qp**4 + 1, DP, DN]
SMALL = {"q-1": Qp - 1, "q+1": Qp + 1, "q^2-q+1": Qp * Qp - Qp + 1, "q^2+q+1": Qp * Qp + Qp + 1,
         "q": Qp, "q^2+1": Qp * Qp + 1, "q^4+1": Qp**4 + 1}

# ---- blocks and controls ------------------------------------------------------------------
tN = {k: F.tr(3, F.atom_word(k, [], "over")) for k in "pn"}
for k, v in tN.items():  # block traces: (q⁴+1)·Dp or (q⁴+1)·Dn up to q, q²+1 (Lean: positive)
    fac = v[0].factor()
    log(f"tr {k}: factors of degree {[int(f.degree()) for f, e in fac[1]]}, content {fac[0]}")
    assert fac[0] > 0
checks = {}
# P9: at A = 3, tr N₀ · tr(tail) equals the 9-strand trace, every cell
ok = True
for order in ("pnn", "npn", "nnp", "ppn", "pnp", "npp"):
    for v in ("over", "under"):
        b = [(0, 1), (1, 2), (0, 2)]
        ok &= F.same(F.tr(9, F.atom_word(order, b, v)),
                     F.mul(tN[order[0]], F.tr(7, F.atom_word(order, b, v, start=1))))
checks["P9_A3_first_nucleon_factors_out"] = bool(ok)
# hecke_flint against hecke_exact (independent code) on the ²H pn full word at q = 3/2
R = Ring(Fraction(3, 2))
w2 = F.atom_word("pn", [(0, 1)], "over")
m = {"S": R.S, "I": R.I, "A": R.Av}
v_exact = R.tr(6, [m[k](i) for k, i in w2])
v_flint = F.evalq(F.tr(6, w2), flint.fmpq(3, 2))
checks["flint_vs_hecke_exact_2H_q3/2"] = Fraction(int(v_flint.p), int(v_flint.q)) == v_exact
log(checks)

# ---- ⁴He ----------------------------------------------------------------------------------
free_tail = F.mul(F.mul(tN[ORDER[1]], tN[ORDER[2]]), tN[ORDER[3]])
qpin = flint.fmpq(*Fraction(Q_50_DIGIT_STR).as_integer_ratio())
W = json.load(open(os.path.join(HERE, "..", "he4_gg_all_pairs", "he4-gg-all-pairs.witness.json")))
ref = {(r["route"], r["variant"]): r for r in W["data"]["rows"] if r["atom"] == "4He"}


def fx(x):
    return mp.mpf(int(x.p)) / int(x.q)


cells = [("gg chain", "-", CHAIN)] + [(r, v, b) for r, b in ROUTES.items() for v in ("over", "under")]
sym, rows = {}, []
for route, variant, bonds in cells:
    t = time.time()
    tail = F.tr(10, F.atom_word(ORDER, bonds, "over" if variant == "-" else variant, start=1))
    num, den = F.div_num(tail, free_tail)          # ratio = num / den
    D = num - den                                  # ratio − 1 = D / den
    sden = den.factor()
    # denominator = Π block-trace numerators × q^a (q²+1)^b: factors q, q²+1, q⁴+1, Dp, Dn,
    # positive for q > 1 (LightNucleiGGChainSign: Dp, Dn > 0), positive content
    assert sden[0] > 0 and all(any(f == g for g in DEN_OK) for f, e in sden[1]), sden
    fl = D.factor()
    content = fl[0]
    small, big = {}, []
    for f, e in fl[1]:
        name = next((k for k, g in SMALL.items() if f == g), None)
        if name:
            small[name] = int(e)
        else:
            big.append((f, int(e)))
    # sign of ratio − 1 for q > 1 = sign(content) · Π sign(big factors) (small factors > 0 for q > 1)
    analysis = []
    for f, e in big:
        cy = to_y(f) if all(f[i] == 0 for i in range(1, f.degree() + 1, 2)) else None
        entry = {"degree_q": int(f.degree()), "multiplicity": e}
        P = sp.Poly(flint_to_sympy(f), qq)
        n_roots = P.count_roots(1, sp.oo) - (1 if P.eval(1) == 0 else 0)
        entry["real_roots_q_gt_1"] = int(n_roots)
        roots = []
        for (a, b), mlt in P.intervals(eps=sp.Rational(1, 10**22)):
            if b > 1:
                assert a > 1, "root interval straddles q = 1"
                mid = (a + b) / 2  # exact isolating interval of width ≤ 1e−22
                roots.append({"interval": [str(a), str(b)], "multiplicity": int(mlt),
                              "value": mp.nstr(mp.mpf(mid.p) / mid.q, 20)})
        entry["roots"] = roots
        if cy is not None:
            nz = [c for c in cy if c != 0]
            entry["sign_changes_in_y"] = sum(1 for a, b in zip(nz, nz[1:]) if a * b < 0)
            entry["value_at_y0_sign"] = int((cy[0] > 0) - (cy[0] < 0))
            entry["coeffs_in_y_const_first"] = [str(c) for c in cy]
        analysis.append(entry)
    k = small.get("q-1", 0)
    # leading coefficient at q = 1 of (ratio − 1) / y^k
    lead = None
    if k == small.get("q+1", 0):
        rest = D
        for _ in range(k):
            rest = rest // (Qp * Qp - 1)
        lead = rest(flint.fmpq(1)) / den(flint.fmpq(1))
    # pin
    t0p = F.evalq(tN[ORDER[0]], qpin)
    atom = t0p * F.evalq(tail, qpin)
    free = t0p * F.evalq(free_tail, qpin)
    E0 = flint.fmpq(*E0_MEV.as_integer_ratio())
    Bd = E0 * 1000 * (free - atom)
    Bl = fx(E0) * 1000 * mp.log(fx(free) / fx(atom))
    key = f"{route}:{variant}"
    rr = ref.get((route, variant))
    if rr is not None:
        checks[f"P8_{key}"] = bool(abs(fx(atom / free) - mp.mpf(rr["ratio_atom_over_free"])) < mp.mpf("1e-28"))
    sym[key] = {"small_factors": small, "content_sign": int((content > 0) - (content < 0)),
                "big_factors": analysis, "y_power_at_q1": k,
                "leading_coefficient_at_q1": None if lead is None else str(lead)}
    rows.append({"route": route, "variant": variant, "bonds": bonds,
                 "ratio_atom_over_free": mp.nstr(fx(atom / free), 30),
                 "B_diff_keV": mp.nstr(fx(Bd), 15), "B_log_keV": mp.nstr(Bl, 15),
                 "AME_keV_comparison_only": mp.nstr(fx(flint.fmpq(*AME_KEV.as_integer_ratio())), 10)})
    log(f"{key:20s} {time.time() - t:5.1f}s y^{k} lead {lead} | big "
        f"{[(a['degree_q'], a.get('sign_changes_in_y'), a['real_roots_q_gt_1'], [r['value'][:9] for r in a['roots']]) for a in analysis]}"
        f" | pin B_diff={mp.nstr(fx(Bd), 8)} keV B_log={mp.nstr(Bl, 8)} keV")
checks["P8_chain_-0.862_keV"] = abs(mp.mpf(rows[0]["B_diff_keV"]) + mp.mpf("0.8625")) < mp.mpf("0.0005")
log(checks)
assert all(checks.values())

out = {"q0Anchor": "proton", "q0AnchorReason": "exact Fractions at the proton 50-digit pin",
       "issue": 9039, "preregistration": "preregistration.md (addendum 2, ⁴He all pairs)",
       "rulings": "owner-rulings 2026-11-22: reading A, right-hand closure (bond enters newer nucleon)",
       "order": ORDER, "E0_MeV": str(E0_MEV), "symbolic": sym, "rows": rows, "checks": checks,
       "note": "PROBE, adopts nothing. AME values are comparison fields only."}
with open(os.path.join(HERE, "he4-all-pairs-exact.witness.json"), "w") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)
log("witness written")
