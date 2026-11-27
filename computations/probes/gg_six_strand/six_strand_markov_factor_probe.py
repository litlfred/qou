#!/usr/bin/env python3
"""Identify the step-2 scalar c(q) as the Markov trace of the Borromean core (bean qou-cds1).

Exact over Q(q), convention D. Checks:
  1. c(q) recorded in six-strand-h3-residue.witness.json equals tr_M(V^3),
     tr_M(x) = sum_lambda y_lambda chi_lambda(x) on H3, V = s0 s1^-1.
  2. E_{6->3}(V_j^3) = tr_M(V^3) * 1 for j = 2, 3 (scalar on both two-row blocks).
  3. E_{6->3}(V_1^3) is not a scalar.
  4. E_{6->3}(V_0^3 V_3^3) = tr_M(V^3) * V_0^3 (Markov factorisation of a disjoint product).
No measured value enters; q0 is printed only for reading.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gg_ntower"))
import gg_ntower_probe as g  # noqa: E402
import sympy as sp  # noqa: E402

q = g.q
OUT = HERE / "six-strand-markov-factor.witness.json"


def V(i, k):
    return [(i, 1), (i + 1, -1)] * k


def lvl3(letters):
    ch = g.level_chars(letters, 6)
    return {mu: sp.cancel(ch[(3, mu)]) for mu in g.two_row_shapes(3)}


def main():
    core = V(0, 3)
    trM = sp.factor(sp.cancel(sum(g.y_lambda(l) * g.tr(g.rep(l).word(core)) for l in g.two_row_shapes(3))))
    dims = {l: g.rep(l).word([]).shape[0] for l in g.two_row_shapes(3)}
    corech = {l: sp.cancel(g.tr(g.rep(l).word(core))) for l in g.two_row_shapes(3)}
    checks = {}
    res = json.loads((HERE / "six-strand-h3-residue.witness.json").read_text())
    rec = next(r for r in res["rows"] if r["V_indices"] == [2, 2, 2])["level3_over_core"]["(3, 0)"]
    checks["c_equals_trM_V3"] = sp.cancel(sp.sympify(rec, locals={"q": q}) - trM) == 0
    for j in (2, 3):
        e = lvl3(V(j, 3))
        checks[f"E(V{j}^3)_is_trM_times_1"] = all(sp.cancel(e[l] - trM * dims[l]) == 0 for l in e)
    e1 = lvl3(V(1, 3))
    checks["E(V1^3)_not_scalar"] = sp.cancel(e1[(3, 0)] / dims[(3, 0)] - e1[(2, 1)] / dims[(2, 1)]) != 0
    e03 = lvl3(V(0, 3) + V(3, 3))
    checks["E(V0^3 V3^3)_eq_trM_V0^3"] = all(sp.cancel(e03[l] - trM * corech[l]) == 0 for l in e03)
    ok = all(checks.values())
    for k, v in checks.items():
        print(("PASS" if v else "FAIL"), k)
    w = {
        "computation": "six-strand-markov-factor",
        "scriptFile": "computations/probes/gg_six_strand/six_strand_markov_factor_probe.py",
        "kind": "probe",
        "beans": ["qou-cds1"],
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 used only for the printed value; all checks are exact in Q(q)",
        "markov_convention": "D",
        "trM_V3": str(trM),
        "trM_V3_at_q0": str(sp.N(trM.subs(q, g.Q0_RAT), 25)),
        "checks": checks,
        "all_pass": ok,
    }
    OUT.write_text(json.dumps(w, indent=1) + "\n")
    print("tr_M(V^3) =", trM, "  at q0:", w["trM_V3_at_q0"])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
