#!/usr/bin/env python3
"""Route 2, recipe R-q (beans qou-99qc, qou-pzsi): reduced Burau at t = +q0 and t = -q0.

Implements preregistration-qdeformed.md exactly. Matrices are built symbolically in t
with exact integer coefficients (sympy), then evaluated with mpmath at 60 dps. No
float64, no selection, no Q_beta / CODATA / mass input.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools/qou-substrate/python"))
from bring_route2_probe import CANDIDATES, CONJUGATE_PAIRS, sl2z  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 60
TOL = mp.mpf("1e-40")
t = sp.Symbol("t")
S = {0: sp.Matrix([[-t, 1], [0, 1]]), 1: sp.Matrix([[1, 0], [t, -t]])}


def burau(word):
    M = sp.eye(2)
    for g in word:
        M = M * S[g]
    return M.applyfunc(sp.expand)


def evalm(M, tv):
    return [[mp.polyval([mp.mpf(int(c)) for c in sp.Poly(M[i, j], t).all_coeffs()], tv)
             for j in range(2)] for i in range(2)]


def classify(Mv):
    d = Mv[0][0] * Mv[1][1] - Mv[0][1] * Mv[1][0]
    tr = Mv[0][0] + Mv[1][1]
    x = abs(tr) / mp.sqrt(abs(d))
    out = {"det": d, "abs_tr": abs(tr), "x": x}
    if d < 0:
        out.update(type="glide reflection", ell=2 * mp.asinh(x / 2))
    elif abs(x - 2) < TOL:
        out.update(type="parabolic", ell=mp.mpf(0))
    elif x > 2:
        out.update(type="hyperbolic", ell=2 * mp.acosh(x / 2))
    else:
        out.update(type="elliptic", ell=mp.mpf(0), theta=2 * mp.acos(x / 2))
    return out


def main():
    q0 = Q_MP
    checks = {}
    # check 2: full twist is t^3 I
    tw = burau([0, 1] * 3)
    checks["full_twist_is_t3_I"] = bool(sp.simplify(tw - t**3 * sp.eye(2)) == sp.zeros(2))
    syms = {k: burau(w) for k, w in CANDIDATES.items()}
    # check 1: classical limit
    checks["classical_limit_matches_sl2z"] = all(
        [[int(syms[k][i, j].subs(t, -1)) for j in range(2)] for i in range(2)] == sl2z(w)
        for k, w in CANDIDATES.items())
    # check 4: determinant
    checks["det_is_(-t)^n"] = all(
        sp.expand(syms[k].det() - (-t) ** len(w)) == 0 for k, w in CANDIDATES.items())
    res = {}
    for label, tv in (("t=+q0", q0), ("t=-q0", -q0)):
        res[label] = {k: classify(evalm(syms[k], tv)) for k in CANDIDATES}
    # check 3: conjugation invariance
    checks["conjugate_pairs_equal_x"] = all(
        abs(res[L][a]["x"] - res[L][b]["x"]) < TOL for L in res for a, b in CONJUGATE_PAIRS)
    ok = all(checks.values())

    def s(v):
        return mp.nstr(v, 25)

    lines = ["# Route 2, recipe R-q: results", "",
             f"q0 = {Q_50_DIGIT_STR} (proton pin). mpmath {mp.mp.dps} dps. "
             "Recipe: preregistration-qdeformed.md. No ranking rule; nothing selected.", "",
             "## Checks", ""]
    lines += [f"- {k}: {'PASS' if v else 'FAIL'}" for k, v in checks.items()]
    lines += ["", "## Symbolic images (exact, in t)", ""]
    for k in CANDIDATES:
        lines.append(f"- {k}: tr = {sp.factor(syms[k].trace())}, det = {sp.factor(syms[k].det())}")
    for L in res:
        lines += ["", f"## {L}", "", "| word | det | x = abs(tr)/sqrt(abs(det)) | type | length |",
                  "|---|---|---|---|---|"]
        for k, r in res[L].items():
            extra = f" (rotation {s(r['theta'])})" if "theta" in r else ""
            lines.append(f"| {k} | {s(r['det'])} | {s(r['x'])} | {r['type']} | {s(r['ell'])}{extra} |")
    # Post-hoc (NOT pre-registered): the parabolic words get length exactly ln q0 at both t.
    # Reason: tr = t^5 (t - 1), det = -t^11, so x = |q0 -/+ 1| / sqrt(q0), and
    # 2 asinh((sqrt q - 1/sqrt q)/2) = 2 acosh((sqrt q + 1/sqrt q)/2) = ln q.
    lnq = mp.log(q0)
    post = {L: abs(res[L]["nuc11_interleaved"]["ell"] - lnq) < TOL for L in res}
    lines += ["", "## Post-hoc observation (not pre-registered)", "",
              "The three words that are parabolic at t = -1 (nuc11_interleaved = gluon_s0_s0, "
              "gluon_s0_s1) have length exactly ln q0 = " + s(lnq) + " at both t: "
              + ", ".join(f"{L} {'agrees' if v else 'DISAGREES'} to 1e-40" for L, v in post.items())
              + ". Exact reason: tr = t^5 (t - 1), det = -t^11."]
    here = Path(__file__).resolve().parent
    (here / "results_qdeformed.md").write_text("\n".join(lines) + "\n")
    (here / "results_qdeformed.json").write_text(json.dumps({
        "recipe": "preregistration-qdeformed.md", "q0": Q_50_DIGIT_STR, "dps": mp.mp.dps,
        "checks": checks, "selected": None,
        "post_hoc_parabolic_length_is_ln_q0": post,
        "symbolic": {k: {"trace": str(sp.factor(syms[k].trace())),
                         "det": str(sp.factor(syms[k].det()))} for k in CANDIDATES},
        "results": {L: {k: {kk: (s(vv) if isinstance(vv, mp.mpf) else vv)
                            for kk, vv in r.items()} for k, r in res[L].items()} for L in res},
    }, indent=2) + "\n")
    print("\n".join(lines))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
