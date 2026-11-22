#!/usr/bin/env python3
"""³H, ³He with the γγ bond on all three pairs, exact (issue #9039; preregistration.md addendum).

Bonds (0,1), (1,2), (0,2), each V³ = (σ_{3j−1}σ_{3j}⁻¹)³ placed as in the chain (enters the
newer nucleon). The non-neighbour bond is transported by σ₂σ₃σ₄ · V³ · (σ₄σ₃σ₂)⁻¹ ("over")
or with the crossing signs reversed ("under"), as in ../he4_gg_all_pairs. Exact ℚ(q) on 9
strands for every order and both variants; exact Fractions at the proton pin. No float in any
computed quantity; mpmath only formats. AME is comparison only.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "he4_closed_form"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools", "qou-substrate", "python"))
from hecke_exact import Ring  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

mp.mp.dps = 40
T0 = time.time()
E0_MEV = Fraction("4.227483355629030550268056026587211153615")  # he4-gg-all-pairs.witness.json
AME_KEV = {"3H": Fraction("8481.798"), "3He": Fraction("7718.043")}  # AME2020, comparison only
NUCLEI = {"3H": "pnn", "3He": "ppn"}
PRODUCTION = {"3H": "pnn", "3He": "ppn"}  # atom_braid_word_3A order, the mpmath witness rows
qq, yy = sp.symbols("q y")


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def sh(L, k):
    return [(a, b, i + k) for a, b, i in L]


def tb(R, i, j, variant):
    gens = list(range(3 * i + 2, 3 * j - 1))
    up, down = (R.S, R.I) if variant == "over" else (R.I, R.S)
    return [up(g) for g in gens] + R.V3(3 * j - 1) + [down(g) for g in reversed(gens)]


def word(R, order, variant, appended=False):
    N = {"p": R.proton(), "n": R.neutron()}
    blocks = [N[order[0]], sh(N[order[1]], 3), sh(N[order[2]], 6)]
    bonds = {1: [tb(R, 0, 1, variant)], 2: [tb(R, 1, 2, variant), tb(R, 0, 2, variant)]}
    if appended:
        return blocks[0] + blocks[1] + blocks[2] + sum(bonds[1] + bonds[2], [])
    return blocks[0] + blocks[1] + bonds[1][0] + blocks[2] + bonds[2][0] + bonds[2][1]


def to_sym(x):
    return sp.sympify(str(x.as_expr())).subs("q", qq)


def roots_gt1(poly):
    """Real roots q > 1 of a polynomial, as isolating intervals (exact) plus a 30-digit value."""
    P = sp.Poly(poly, qq)
    out = []
    for (a, b), m in P.intervals(eps=sp.Rational(1, 10**12)):
        if b > 1:
            assert a > 1, "root interval straddles q = 1"
            r = sp.nsolve(P.as_expr(), qq, (a + b) / 2, prec=40)
            out.append({"interval": [str(a), str(b)], "value": mp.nstr(mp.mpf(str(r)), 30),
                        "multiplicity": int(m)})
    return out


# ---- 1. symbolic, every order and both variants ---------------------------------------
RS = Ring()
trS = {k: RS.tr(3, v) for k, v in (("p", RS.proton()), ("n", RS.neutron()))}
sym, cells = {}, []
for iso, comp in NUCLEI.items():
    for order in sorted(set("".join(o) for o in itertools.permutations(comp))):
        for variant in ("over", "under"):
            t = RS.tr(9, word(RS, order, variant))
            free = trS[order[0]] * trS[order[1]] * trS[order[2]]
            ratio = to_sym(t / free)
            m1 = sp.factor(ratio - 1)
            num_r, _den_r = sp.fraction(sp.factor(ratio))
            num_m1, den_m1 = sp.fraction(m1)
            # den_m1 is q^a (q²+1)^b times squares/products of Dp, Dn: positive for q > 1
            # (Dp, Dn positive: LightNucleiGGChainSign.lean). Sign of ratio − 1 = sign of num_m1.
            bind_roots = roots_gt1(sp.expand(num_m1))
            zero_roots = roots_gt1(sp.expand(num_r))
            # leading order at q = 1: ratio − 1 = c · y^k + O(y^(k+1)), y = q² − 1
            k = 0
            F = m1
            while sp.cancel(F).subs(qq, 1) == 0:
                F = sp.cancel(F / (qq**2 - 1))
                k += 1
            lead_coeff = sp.cancel(F).subs(qq, 1)
            # irreducible factors over Q of the numerator; the sign factor is the one of degree > 4
            fl = sp.factor_list(sp.expand(num_m1))
            sig = [f for f, e in fl[1] if sp.Poly(f, qq).degree() > 4]
            assert len(sig) == 1
            small = [f for f, e in fl[1] if sp.Poly(f, qq).degree() <= 4]
            # small factors must be q ± 1, q² ± q + 1 (no sign change for q > 1 except via q − 1 > 0)
            allowed = {sp.expand(qq - 1), sp.expand(qq + 1), sp.expand(qq**2 - qq + 1), sp.expand(qq**2 + qq + 1)}
            assert all(sp.expand(f) in allowed for f in small), small
            # denominator: q^a (q²+1)^b Dp^i Dn^j up to sign (Dp, Dn > 0 for q > 1, Lean)
            Dp = qq**18 - 3*qq**16 + 7*qq**14 - 8*qq**12 + 10*qq**10 - 9*qq**8 + 10*qq**6 - 6*qq**4 + 3*qq**2 - 1
            Dn = qq**14 - 3*qq**12 + 4*qq**10 - 4*qq**8 + 5*qq**6 - 4*qq**4 + 3*qq**2 - 1
            dl = sp.factor_list(sp.expand(den_m1))
            dallowed = {sp.expand(qq), sp.expand(qq**2 + 1), sp.expand(Dp), sp.expand(Dn)}
            assert all(sp.expand(f) in dallowed for f, e in dl[1]), dl
            key_pre = f"{iso}:{order}:{variant}"
            # Descartes in y: sign factor as a polynomial in y = q² − 1
            P = sig[0]
            assert sp.expand(P - P.subs(qq, -qq)) == 0, "sign factor not even"
            Py = sp.Poly(sp.expand(P.subs(qq, sp.sqrt(yy + 1))), yy)
            cy = Py.all_coeffs()[::-1]          # constant term first
            nz = [c for c in cy if c != 0]
            changes = sum(1 for a, b in zip(nz, nz[1:]) if a * b < 0)
            # hypothesis of LightNucleiGGChainSign.single_crossing: negative block first, then
            # nonnegative; constant term negative. Then P has exactly one root y* > 0
            # (P(0) < 0, P → +∞), with P < 0 below it and P > 0 above it.
            m_split = next(i for i, c in enumerate(cy) if c > 0)
            single_crossing_form = (cy[0] < 0 and all(c <= 0 for c in cy[:m_split])
                                    and all(c >= 0 for c in cy[m_split:]) and cy[-1] > 0)
            assert single_crossing_form, key_pre
            # overall sign: ratio − 1 = s · (positive for q > 1) · P, s = sign of the rest at q = 2
            rest = sp.cancel(m1 / P)
            s = int(sp.sign(rest.subs(qq, 2)))
            assert all(sp.sign(rest.subs(qq, sp.Rational(t, 100))) == s for t in range(101, 400, 7))
            # tr_atom = 0: same analysis on the numerator of the ratio
            zl = [f for f, e in sp.factor_list(sp.expand(num_r))[1] if sp.Poly(f, qq).degree() > 4]
            zy = [sp.Poly(sp.expand(f.subs(qq, sp.sqrt(yy + 1))), yy).all_coeffs()[::-1] for f in zl]
            zchanges = [sum(1 for a, b in zip([c for c in z if c], [c for c in z if c][1:]) if a * b < 0) for z in zy]
            metal = [(m + sp.sqrt(m * m + 4)) / 2 for m in range(1, 6)]
            hits = [str(v) for f, e in fl[1] + sp.factor_list(sp.expand(num_r))[1]
                    for v in metal + [sp.sqrt(t) for t in metal]
                    if sp.simplify(f.subs(qq, v)) == 0]
            key = f"{iso}:{order}:{variant}"
            sym[key] = {"ratio_minus_1": str(m1),
                        "leading_order_at_q1": {"y_power": k, "coefficient": str(lead_coeff)},
                        "numerator_factor_degrees": [[int(sp.Poly(f, qq).degree()), int(e)] for f, e in fl[1]],
                        "sign_factor_coeffs_in_y_const_first": [str(c) for c in cy],
                        "sign_factor_sign_changes_in_y": changes,
                        "single_crossing_form": bool(single_crossing_form),
                        "low_block_degree_m": m_split,
                        "overall_sign_of_rest": s,
                        "roots_of_ratio_minus_1_q_gt_1": bind_roots,
                        "tr_atom_numerator_sign_changes_in_y": zchanges,
                        "roots_of_tr_atom_q_gt_1": zero_roots,
                        "metallic_mean_roots_found": hits}
            cells.append((iso, order, variant))
            log(f"{key:16s} y^{k} coeff {lead_coeff}; Descartes {changes}; ratio=1 at q = "
                f"{[r['value'][:12] for r in bind_roots]}; tr_atom=0 at q = "
                f"{[r['value'][:12] for r in zero_roots]}")

# ---- 2. exact at the pin ------------------------------------------------------------------
R = Ring(Fraction(Q_50_DIGIT_STR))
trP = {k: R.tr(3, v) for k, v in (("p", R.proton()), ("n", R.neutron()))}
rows, checks = [], {}


def fx(x):
    return mp.mpf(x.numerator) / x.denominator


for iso, order, variant in cells:
    free = trP[order[0]] * trP[order[1]] * trP[order[2]]
    atom = R.tr(9, word(R, order, variant))
    Bd = E0_MEV * 1000 * (free - atom)
    Bl = fx(E0_MEV) * 1000 * mp.log(fx(free) / fx(atom))
    rows.append({"nucleus": iso, "order": order, "variant": variant,
                 "tr_free": mp.nstr(fx(free), 30), "tr_atom": mp.nstr(fx(atom), 30),
                 "ratio_atom_over_free": mp.nstr(fx(atom / free), 30),
                 "B_diff_keV": mp.nstr(fx(Bd), 15), "B_log_keV": mp.nstr(Bl, 15),
                 "AME_keV_comparison_only": mp.nstr(fx(AME_KEV[iso]), 10)})
    log(f"pin {iso:3s} {order} {variant:5s} ratio={mp.nstr(fx(atom / free), 15)} "
        f"B_diff={mp.nstr(fx(Bd), 8)} keV B_log={mp.nstr(Bl, 8)} keV")
    if order == PRODUCTION[iso]:
        checks[f"appended_eq_arranged_{iso}_{variant}"] = R.tr(9, word(R, order, variant, True)) == atom

# control against the mpmath witness of ../he4_gg_all_pairs
W = json.load(open(os.path.join(HERE, "..", "he4_gg_all_pairs", "he4-gg-all-pairs.witness.json")))
for r in W["data"]["rows"]:
    if r["atom"] in NUCLEI and r["route"] == "all pairs":
        mine = next(x for x in rows if x["nucleus"] == r["atom"] and x["order"] == PRODUCTION[r["atom"]]
                    and x["variant"] == r["variant"])
        gap = abs(mp.mpf(mine["ratio_atom_over_free"]) - mp.mpf(r["ratio_atom_over_free"]))
        checks[f"mpmath_witness_{r['atom']}_{r['variant']}"] = bool(gap < mp.mpf("1e-28"))
checks["all_pin_rows_unbind"] = all(mp.mpf(r["B_diff_keV"]) < 0 for r in rows)
log(checks)
assert all(checks.values())

out = {"q0Anchor": "proton", "q0AnchorReason": "exact Fractions at the proton 50-digit pin",
       "issue": 9039, "preregistration": "preregistration.md (addendum, all-pairs A = 3)",
       "rulings": "owner-rulings 2026-11-22: reading A, right-hand closure (bond enters newer nucleon)",
       "E0_MeV": str(E0_MEV), "symbolic": sym, "rows": rows, "checks": checks,
       "note": "PROBE, adopts nothing. AME values are comparison fields only."}
with open(os.path.join(HERE, "light-nuclei-a3-all-pairs.witness.json"), "w") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)
log("witness written")
