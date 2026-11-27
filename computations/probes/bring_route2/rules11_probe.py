#!/usr/bin/env python3
"""Route 2, option 1d (beans qou-99qc, qou-pzsi): rules A and B on every 11-letter braid.

Implements preregistration-rules11.md. No Q_beta / CODATA / mass input anywhere.
"""
import itertools
import json
import sys
from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bring_route2_probe as R2  # noqa: E402
import bring_loop_energy_probe as E  # noqa: E402
import option1_ropelength_probe as O1  # noqa: E402
import sameloop_probe as SL  # noqa: E402
import fibres_probe as F  # noqa: E402
import bring_route2_qdeformed_probe as QD  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

WORDLEN = 11
DIG = 40
SEEN = {k: "".join(map(str, v)) for k, v in R2.CANDIDATES.items() if len(v) == WORDLEN}


# ---- independent braid key checks (preregistration §4.4)
def gauss_cycle(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    if a + d < 0:
        a, b, c, d = -a, -b, -c, -d
    A, B, C = c, d - a, -b
    g = gcd(gcd(abs(A), abs(B)), abs(C))
    A, B, C = A // g, B // g, C // g
    D = B * B - 4 * A * C
    r = isqrt(D)

    def normB(Bv, Av):
        m = 2 * abs(Av)
        lo = -abs(Av) if abs(Av) > r else r - m
        Bp = Bv % m
        while Bp <= lo:
            Bp += m
        while Bp > lo + m:
            Bp -= m
        return Bp

    def rho(f):
        A_, B_, C_ = f
        Bp = normB(-B_, C_)
        return (C_, Bp, (Bp * Bp - D) // (4 * C_))

    def red(f):
        A_, B_, C_ = f
        return 0 < B_ <= r and r - B_ < 2 * abs(A_) <= r + B_

    f = (A, B, C)
    for _ in range(5000):
        if red(f):
            break
        f = rho(f)
    cyc = []
    while f not in cyc:
        cyc.append(f)
        f = rho(f)
    return (a + d, frozenset(cyc))


def parabolic_n(M):
    Mm = sp.Matrix(M)
    if Mm.trace() < 0:
        Mm = -Mm
    K = (Mm - sp.eye(2)).nullspace()[0]
    K = K * sp.ilcm(*[x.q for x in K])
    g0 = gcd(int(K[0]), int(K[1]))
    p, q = int(K[0]) // g0, int(K[1]) // g0
    x, y, _ = sp.gcdex(p, q)
    G = sp.Matrix([[p, -y], [q, x]])
    return int((G.inv() * Mm * G)[0, 1])


def main():
    checks = {}
    classes = {}
    for w in itertools.product((0, 1), repeat=WORDLEN):
        classes.setdefault(O1.canon(w), []).append(w)
    checks["class_count_is_94"] = len(classes) == 94
    q0 = mp.mpf(Q_50_DIGIT_STR, )
    rows = []
    for c in sorted(classes):
        w = "".join(map(str, c))
        M = R2.sl2z(list(c))
        with mp.workdps(60):
            q0h = Q_MP
            r = QD.classify(QD.evalm(QD.burau(list(c)), -q0h))
        rows.append({"word": w, "M": M, "S1": F.s1_key(M), "E": r["ell"], "type": r["type"],
                     "seen": sorted(k for k, v in SEEN.items() if O1.canon(tuple(map(int, v))) == c)})
    byw = {r["word"]: r for r in rows}

    # check 2: reproduction of seen E_q
    qd = json.loads((HERE / "results_qdeformed.json").read_text())["results"]["t=-q0"]
    rep = True
    for k, v in SEEN.items():
        cw = "".join(map(str, O1.canon(tuple(map(int, v)))))
        rep &= mp.nstr(byw[cw]["E"], 25) == qd[k]["ell"]
    checks["reproduce_seen_E_q_25_digits"] = rep

    # check 3: reversal is a class function
    m = defaultdict(set)
    for r in rows:
        rv = "".join(map(str, O1.canon(tuple(int(x) for x in r["word"][::-1]))))
        m[str(r["S1"])].add(str(byw[rv]["S1"]))
    checks["reversal_maps_classes_to_classes"] = all(len(v) == 1 for v in m.values())

    # check 4: independent keys give the same partition
    part_s1 = defaultdict(set)
    part_ind = defaultdict(set)
    for r in rows:
        kind = r["S1"][0]
        ind = gauss_cycle(r["M"]) if kind == "hyp" else (("par", parabolic_n(r["M"])) if kind == "par" else r["S1"])
        part_s1[str(r["S1"])].add(str(ind))
        part_ind[str(ind)].add(str(r["S1"]))
    checks["independent_key_same_partition"] = (all(len(v) == 1 for v in part_s1.values())
                                                and all(len(v) == 1 for v in part_ind.values()))

    # braids
    braids = defaultdict(list)
    for r in rows:
        braids[str(r["S1"])].append(r)
    key = lambda v: mp.nstr(v, DIG)  # noqa: E731
    E_of = {b: rs[0]["E"] for b, rs in braids.items()}
    checks["E_constant_on_braids"] = all(len({key(x["E"]) for x in rs}) == 1 for rs in braids.values())
    seen_of = {b: sorted({s for x in rs for s in x["seen"]}) for b, rs in braids.items()}
    ranked = sorted([b for b in braids if E_of[b] > 0], key=lambda b: E_of[b])
    zero = [b for b in braids if not E_of[b] > 0]

    def rule(cands):
        emin = min(E_of[b] for b in cands)
        win = [b for b in cands if key(E_of[b]) == key(emin)]
        return {"decided": len(win) == 1, "E_min": key(emin), "winners": win,
                "winner_is_seen_braid": [seen_of[b] for b in win],
                "winner_spellings": [len(braids[b]) for b in win]}

    ruleA = rule(ranked)

    # Rule B: shortest Bring loop, decided by the symmetry rule
    s_mp, u_mp = R2.delta245()
    s, u = E.from_mp(s_mp), E.from_mp(u_mp)
    rho, sigmas = R2.s5_epimorphisms()
    loops = []
    for r in rows:
        rr = O1.route2_row(tuple(int(x) for x in r["word"]))
        r["bring"] = rr["status"]
        if rr["status"] == "loop":
            r["L"] = rr["L"]
            r["_rr"] = rr
            loops.append(r)
    Lmin = min(r["L"] for r in loops)
    short = sorted([r for r in loops if mp.nstr(r["L"], 25) == mp.nstr(Lmin, 25)], key=lambda r: r["word"])
    geo = {}
    for r in short:
        st = E.loop_setup(r["word"], s_mp, u_mp, sigmas[0], rho, row=r["_rr"])
        geo[r["word"]] = SL.geometry(st)
    rep0 = short[0]["word"]
    matched = [r for r in short
               if SL.isometric(geo[rep0], geo[r["word"]], r["L"], s, u)[0] is not None]
    checks["shortest_length_is_one_loop"] = len(matched) == len(short)
    on_loop = sorted({str(r["S1"]) for r in matched})
    ruleB = rule([b for b in on_loop if E_of[b] > 0])
    ruleB.update({"shortest_L": mp.nstr(Lmin, 25), "word_classes_on_loop": len(matched),
                  "braids_on_loop": [[b, len([x for x in matched if str(x["S1"]) == b]),
                                      key(E_of[b]), seen_of[b]] for b in on_loop]})

    ranking = [{"rank": i + 1, "braid": b, "E_q": key(E_of[b]), "spellings": len(braids[b]),
                "seen": seen_of[b],
                "bring": Counter(x.get("bring") for x in braids[b]).most_common(1)[0][0]}
               for i, b in enumerate(ranked)]
    summary = {"classes": len(rows), "braids": len(braids), "zero_E_braids": zero,
               "rule_A": ruleA, "rule_B": ruleB,
               "seen_braid_ranks": {s_: [x["rank"] for x in ranking if s_ in x["seen"]] for s_ in SEEN},
               "ranking_top10": ranking[:10]}
    print(json.dumps(summary, indent=1, default=str))
    bad = [k for k, v in checks.items() if not v]
    for k in bad:
        print("FAIL " + k)
    print("checks:", len(checks) - len(bad), "/", len(checks), "pass")
    (HERE / "results_rules11.json").write_text(json.dumps(
        {"recipe": "preregistration-rules11.md", "q0": Q_50_DIGIT_STR, "summary": summary,
         "checks": checks, "ranking": ranking,
         "rows": [{"word": r["word"], "S1": str(r["S1"]), "E_q": key(r["E"]), "seen": r["seen"],
                   "bring": r.get("bring"), "L": mp.nstr(r["L"], 25) if "L" in r else None}
                  for r in rows]}, indent=1, default=str) + "\n")
    sys.exit(0 if not bad else 1)


if __name__ == "__main__":
    main()
