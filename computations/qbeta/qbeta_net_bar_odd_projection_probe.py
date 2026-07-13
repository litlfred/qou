#!/usr/bin/env python3
"""
Bar-ODD projection of the H_3 GS categorical net == KC20's odd-channel cubic.

Follows the W2 kill (docs/audits/2026-07-07-qbeta-gs-net-vs-cos-ladder-w2-kill.md):
the FULL categorical net Delta(net) is cosh-like (bar-even dominated), so the
Q_beta decay observable is not read off the full net. This probe strips the
bar-EVEN growth and keeps the bar-ODD projection -- the genuine decay carrier --
and finds it is EXACTLY (h/4) times KC20's irreducible odd-channel cubic.

Objects (exact, symbolic in q; NO CODATA, NO fit, NO anchor):
  Delta(net)(q)   = augmentation(nucleon_nf(u,d,d)) - augmentation(nucleon_nf(u,u,d))
  Delta(net)_odd  = (Delta(net)(q) - Delta(net)(1/q)) / 2   (bar involution q -> 1/q)
  h               = q - 1/q   (bar-ODD)
  y               = q^2 + q^-2 (bar-EVEN KC20 variable)
  C(y)            = y^3 - 4y^2 + 3y - 2          (KC20 cubic)
  C_Hopf(y)       = y^3 - 6y^2 + 10y - 6         (KC20 Hopf sector)
  C_unknot(y)     = 2y^2 - 7y + 4                (KC20 identity/unknot sector)

RESULT (all exact):
  W-odd-1  Delta(net)_odd = (h/4) * C(q^2 + q^-2)                 [the identity]
  W-odd-2  C = C_Hopf + C_unknot                                 [KC20 sector split]
  W-odd-3  C, C_Hopf irreducible over Q (no rational root)       [degree-3 field]
  W-odd-4  no quadratic anchor (golden y=3, silver y=6, classical y=2) is a root
           of C  => real-q/quadratic c_3 closures structurally excluded (KC20)
  W-odd-5  Delta(net)_odd vanishes at q=1 (bar-ODD; consistent with h(1)=0)

SIGNIFICANCE: KC20 (sibling, landed on main) derived C(y) from the cyclotomic /
Hopf-sector analysis of the bar-odd carrier. This probe derives the SAME cubic,
completely independently, as the bar-odd projection of the H_3 GS augmentation.
Two independent categorical routes to the identical irreducible cubic. NO c_k
value; nothing wired (registry section 8).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (
    _ROOT,
    os.path.join(_ROOT, "tools", "pyhecke", "python"),
    os.path.join(_ROOT, "tools", "qou-substrate", "python"),
    os.path.join(_ROOT, "tools", "pyhecke-native", "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import computations.qbeta.qbeta_h4_nucleon_assembly as h4  # noqa: E402


def _repo_head_sha():
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_HERE, text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha -- refusing to emit witness")
    return sha


def main():
    q = h4.q
    h = q - 1 / q
    y = sp.symbols("y")
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    dnet = sp.cancel(
        h4.augmentation(h4.nucleon_nf(["u", "d", "d"]))
        - h4.augmentation(h4.nucleon_nf(["u", "u", "d"]))
    )
    dnet_odd = sp.cancel((dnet - dnet.subs(q, 1 / q)) / 2)

    C = y ** 3 - 4 * y ** 2 + 3 * y - 2
    C_Hopf = y ** 3 - 6 * y ** 2 + 10 * y - 6
    C_unknot = 2 * y ** 2 - 7 * y + 4
    y_of_q = q ** 2 + 1 / q ** 2

    # W-odd-1: Delta(net)_odd = (h/4) * C(q^2 + q^-2)  (the identity)
    check("W_odd_1_projection_equals_KC20_cubic",
          sp.simplify(dnet_odd - (h / 4) * C.subs(y, y_of_q)) == 0,
          "Delta(net)_odd = (h/4) * C(q^2+q^-2), C(y)=y^3-4y^2+3y-2")

    # confirm dnet_odd is bar-ODD (flips sign under q->1/q)
    check("W_odd_bar_odd",
          sp.simplify(dnet_odd + dnet_odd.subs(q, 1 / q)) == 0,
          "Delta(net)_odd is exactly bar-odd")

    # W-odd-2: KC20 sector split
    check("W_odd_2_sector_split",
          sp.expand(C - (C_Hopf + C_unknot)) == 0,
          "C = C_Hopf + C_unknot")

    # W-odd-3: irreducibility over Q (degree-3 field)
    check("W_odd_3_C_irreducible", sp.Poly(C, y).is_irreducible, "C irreducible over Q")
    check("W_odd_3_C_Hopf_irreducible", sp.Poly(C_Hopf, y).is_irreducible,
          "C_Hopf irreducible over Q")

    # W-odd-4: no quadratic anchor is a root of C
    anchors = {"golden": 3, "silver": 6, "classical": 2}
    no_anchor_root = all(C.subs(y, v) != 0 for v in anchors.values())
    check("W_odd_4_no_quadratic_anchor_root", no_anchor_root,
          f"C(y) at {anchors} = "
          + ", ".join(f"{k}:{C.subs(y, v)}" for k, v in anchors.items())
          + " (none 0) => quadratic-anchor c_3 closures excluded")

    # W-odd-5: vanishes at q=1 (bar-odd)
    check("W_odd_5_vanishes_at_q1",
          sp.simplify(sp.limit(dnet_odd, q, 1)) == 0,
          "Delta(net)_odd -> 0 as q -> 1 (h(1)=0)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CONFIRMED: the bar-ODD projection of the H_3 GS categorical net is EXACTLY "
        "Delta(net)_odd = (h/4) * C(q^2+q^-2) with C(y)=y^3-4y^2+3y-2 -- the SAME "
        "irreducible odd-channel cubic KC20 derived independently from the cyclotomic / "
        "Hopf-sector analysis. C = C_Hopf + C_unknot reproduces KC20's sector split; C "
        "and C_Hopf are irreducible over Q; no quadratic anchor (golden/silver/classical) "
        "is a root, so real-q/quadratic c_3 closures are structurally excluded (second "
        "independent witness for KC20). The full net's cosh-likeness (W2 kill) is the "
        "bar-EVEN part; the decay carrier is this bar-ODD cubic. NO c_k value; nothing wired."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-net-bar-odd-projection",
        "description": "Bar-odd projection of the H_3 GS categorical net Delta(net) equals "
                       "(h/4)*C(q^2+q^-2) with C(y)=y^3-4y^2+3y-2 -- an INDEPENDENT "
                       "categorical derivation of KC20's irreducible odd-channel Hopf cubic.",
        "auditOnly": True,
        "tier": "symbolic-exact (sympy; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "Delta_net_odd": str(sp.simplify(dnet_odd)),
            "identity": "Delta(net)_odd = (h/4) * C(q^2+q^-2)",
            "C": "y^3 - 4y^2 + 3y - 2",
            "C_Hopf": "y^3 - 6y^2 + 10y - 6",
            "C_unknot": "2y^2 - 7y + 4",
            "verdict": verdict,
        },
        "context": {
            "follows": "W2 kill (docs/audits/2026-07-07-qbeta-gs-net-vs-cos-ladder-w2-kill.md)",
            "independent_of": "KC20 (registry §9) -- derived C from cyclotomic/Hopf-sector; "
                              "this derives it from the GS augmentation bar-odd projection",
            "gs_reducer": "computations/qbeta/qbeta_h4_nucleon_assembly.py",
            "flip_flop_guard": "registry section 8 -- no c_k wired",
        },
    }
    out = os.path.join(_HERE, "qbeta-net-bar-odd-projection.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("=== bar-odd projection of the GS net == KC20 cubic ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
