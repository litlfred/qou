#!/usr/bin/env python3
"""Route 2, option 1c (beans qou-99qc, qou-pzsi): where do 13-letter words collapse along
route 2, and does the q-length at t = -q0 split them?

Implements preregistration-fibres.md. No Q_beta / CODATA / mass input anywhere.
Exact integer / sympy arithmetic for the stage keys; mpmath at 60 dps for q-lengths.
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
sys.path.insert(0, str(HERE.parents[2] / "tools/qou-substrate/python"))
import bring_route2_probe as R2  # noqa: E402
import option1_ropelength_probe as O1  # noqa: E402
import bring_route2_qdeformed_probe as QD  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 60
WORDLEN = 13
DIG = 40


def raw_period(M):
    """Continued-fraction period (not canonicalised) of the attracting fixed point."""
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    D = (d - a) ** 2 + 4 * b * c
    sgn = 1 if a + d > 0 else -1
    P, Q = (a - d) * sgn, 2 * c * sgn
    if (D - P * P) % Q:
        P, Q, D = P * abs(Q), Q * abs(Q), D * Q * Q
    seen, terms = {}, []
    rD = isqrt(D)
    for i in range(100000):
        k = (P, Q)
        if k in seen:
            # after j CF steps the point is mapped by a GL(2,Z) matrix of det (-1)^j; start
            # the cycle at the first EVEN step j >= seen[k] so the tail is SL(2,Z)-equivalent
            i0 = seen[k]
            per = terms[i0:]
            off = (i0 % 2) % len(per) if per else 0
            return per[off:] + per[:off], i0
        seen[k] = i
        aa = (P + rD) // Q if Q > 0 else -((P + rD) // (-Q)) - 1
        terms.append(aa)
        P = aa * Q - P
        Q = (D - P * P) // Q
    raise RuntimeError("period not found")


def s1_key(M):
    """B3 conjugacy class for a fixed word length = PSL(2,Z) conjugacy class of the image."""
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    if a + d < 0:
        a, b, c, d = -a, -b, -c, -d
    tr = a + d
    if tr > 2:
        if c == 0:
            raise RuntimeError("hyperbolic with c = 0 cannot occur in SL(2,Z)")
        per, _ = raw_period([[a, b], [c, d]])
        if len(per) % 2:
            per = per * 2
        shifts = [tuple(per[k:] + per[:k]) for k in range(0, len(per), 2)]
        return ("hyp", tr, min(shifts))
    if tr == 2:
        n = gcd(gcd(abs(a - 1), abs(b)), abs(c))
        sgn = (1 if b > 0 else -1) if b != 0 else (1 if -c > 0 else -1) if c != 0 else 0
        return ("par", sgn * n)
    if tr == 0:
        return ("ell", 0)
    return ("ell", tr, 1 if c > 0 else -1)


def main():
    checks = {}
    classes = {}
    for w in itertools.product((0, 1), repeat=WORDLEN):
        classes.setdefault(O1.canon(w), []).append(w)
    checks["class_count_is_316"] = len(classes) == 316
    sl = json.loads((HERE / "results_sameloop.json").read_text())
    loop_of = {}
    for i, cl in enumerate(sl["isometry_classes"]):
        for w in cl:
            loop_of[w] = i  # 0 = shortest loop (classes sorted by L)
    top = set(sl["isometry_classes"][0])
    checks["top_loop_has_90"] = len(top) == 90

    q0 = Q_MP
    t = QD.t
    rows = []
    for c in sorted(classes):
        w = "".join(map(str, c))
        M = R2.sl2z(list(c))
        B = QD.burau(list(c))
        trp = sp.expand(B.trace())
        rec = {"word": w, "S1": s1_key(M), "S1p": str(trp), "S2": O1.gl2z_class(M),
               "S3": loop_of.get(w, "none"), "sl2z_trace": M[0][0] + M[1][1]}
        checks.setdefault("classical_limit", True)
        checks["classical_limit"] &= int(trp.subs(t, -1)) == rec["sl2z_trace"]
        for lab, tv in (("m", -q0), ("p", q0)):
            r = QD.classify(QD.evalm(B, tv))
            rec[f"ell_{lab}"] = r["ell"]
            rec[f"type_{lab}"] = r["type"]
        rows.append(rec)

    # invariance checks
    by1 = defaultdict(set)
    by1_2 = defaultdict(set)
    for r in rows:
        by1[str(r["S1"])].add(r["S1p"])
        by1_2[str(r["S1"])].add(str(r["S2"]))
    checks["same_S1_same_burau_trace"] = all(len(v) == 1 for v in by1.values())
    checks["S1_finer_than_S2"] = all(len(v) == 1 for v in by1_2.values())

    # reproduction against results_qdeformed.json (stored to 25 digits)
    qd = json.loads((HERE / "results_qdeformed.json").read_text())
    Bq = QD.burau(R2.CANDIDATES["gluon_s1_s0"])
    ellA = QD.classify(QD.evalm(Bq, -q0))["ell"]
    stored = qd["results"]["t=-q0"]["gluon_s1_s0"]["ell"]
    checks["reproduce_classA_ell_minus_q0_to_stored_25_digits"] = mp.nstr(ellA, 25) == stored

    def census(sub):
        return {k: len({str(r[k]) for r in sub}) for k in ("S1", "S1p", "S2", "S3")}

    topr = [r for r in rows if r["word"] in top]
    summary = {"classes": len(rows), "census_all": census(rows), "census_top_loop_90": census(topr),
               "S1p_equals_S1_partition_all": len({r["S1p"] for r in rows}) == len({str(r["S1"]) for r in rows}),
               "type_at_minus_q0": Counter(r["type_m"] for r in rows),
               "type_at_plus_q0": Counter(r["type_p"] for r in rows)}

    key = lambda v: mp.nstr(v, DIG)  # noqa: E731

    def energy_test(sub):
        pos = [r for r in sub if r["ell_m"] > 0]
        excl = [r["word"] for r in sub if not r["ell_m"] > 0]
        emin = min(r["ell_m"] for r in pos)
        win = [r for r in pos if key(r["ell_m"]) == key(emin)]
        wcl = sorted({str(r["S1"]) for r in win})
        mult = Counter()
        seen_cls = {}
        for r in pos:
            seen_cls.setdefault(str(r["S1"]), key(r["ell_m"]))
        mult = sorted(Counter(seen_cls.values()).items(), key=lambda kv: mp.mpf(kv[0]))
        return {"E_min": key(emin), "minimiser_words": [r["word"] for r in win],
                "minimiser_B3_classes": wcl, "PASS": len(wcl) == 1,
                "excluded_ell_zero": excl, "B3_classes_ranked": len(seen_cls),
                "value_multiplicities_by_B3_class": mult[:12]}

    summary["test_A_all_316"] = energy_test(rows)
    summary["test_B_top_loop_90"] = energy_test(topr)

    print(json.dumps(summary, indent=1, default=str))
    bad = [k for k, v in checks.items() if not v]
    for k in bad:
        print("FAIL " + k)
    print("checks:", len(checks) - len(bad), "/", len(checks), "pass")

    def ser(r):
        return {k: (mp.nstr(v, DIG) if isinstance(v, mp.mpf) else str(v) if isinstance(v, tuple) else v)
                for k, v in r.items()}

    (HERE / "results_fibres.json").write_text(json.dumps(
        {"recipe": "preregistration-fibres.md", "q0": Q_50_DIGIT_STR, "mp_dps": mp.mp.dps,
         "summary": summary, "checks": checks, "rows": [ser(r) for r in rows]},
        indent=1, default=str) + "\n")
    sys.exit(0 if not bad else 1)


if __name__ == "__main__":
    main()
