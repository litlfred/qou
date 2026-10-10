"""aomega_m3_gate3_determinant_ladder_probe.py

Route C M3, normalisation Part 10 / GATE 3 (bean qou-v1eu, issue #7376): the pretzel's
pairing determinant ladder, derived — and the SL-vs-GL rule it implies, calibrated against
GGM's own two printed choices.

Parts 1-9 fixed everything gate 3 needs: the Casoratian ratio (Part 1), the bar-involution
constant (Part 2), `det A . det Abar = 1` so a pairing is not excluded (Part 3's survivor),
the propagation law (Part 7), and — Part 9, from GGM Theorem 28 — that the pretzel's W is a
SINGLE definition holomorphic for |q| != 1, i.e. 4_1-style rather than 5_2-at-u=0's two-branch
(87).

The derivation.  G_{M,L} := W_M J Wbar_L^T, so det is multiplicative:

    det G_{M,L} = det W_M . det J . det Wbar_L
                = ratio^M . ratio_bar^L . det J . [det W_0(q) det W_0(q^-1)]
                = ratio^M . ratio_bar^L . det J . c                      (Part 2's c)

so the whole index dependence is `ratio^M ratio_bar^L` and nothing else.  That gives a rule:

    index dependence trivial  ->  det G constant  ->  SL is possible
    index dependence nontrivial -> det G a nonconstant unit monomial -> GL, never SL

Calibration, and it is two-for-two against GGM's PRINTED choices rather than assumed:

    4_1        ratio q/x   -> dependence (q/x)^{M-L}  -> GL   ... GGM (138) prints GL(2, Z[q,x])
    5_2 (u=0)  ratio 1     -> dependence trivial      -> SL   ... GGM  (93) prints SL(3, Z[q])

Applied to the pretzel (ratio q^4, Part 1):

    det G_{M,L} = q^{4(M-L)} . det J . c        ->  GL, NOT SL

Gates / tests
  G1  the rule reproduces GGM's printed GL for 4_1 and SL for 5_2 at u=0 — calibrated on two
      published statements before being applied
  G2  the pretzel's ladder is q^{4(M-L)} times a constant: a nonconstant unit monomial, so
      GL membership is automatic on determinant grounds and SL is IMPOSSIBLE off the diagonal
  T1  gate 3 closes completely, i.e. det J and c are individually determined.  It does NOT:
      the ladder fixes their PRODUCT's role, not either factor.  Recorded.
Exact sympy throughout; no mpmath, no q0, no float64.
"""
from __future__ import annotations

import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

q, x = sp.symbols("q x", positive=True)
M, L = sp.symbols("M L", integer=True)
c, dJ = sp.symbols("c dJ", nonzero=True)

RATIOS = {"4_1": q / x, "5_2_u0": sp.Integer(1), "pretzel": q**4}
GGM_PRINTED = {"4_1": "GL", "5_2_u0": "SL"}          # (138) and (93)


def dependence(ratio):
    rb = ratio.subs({q: 1 / q, x: 1 / x}, simultaneous=True)
    return sp.powsimp(sp.simplify(ratio**M * rb**L), force=True)


def predict(ratio):
    return "SL" if sp.simplify(dependence(ratio) - 1) == 0 else "GL"


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    rows = {}
    for k, r in RATIOS.items():
        d = dependence(r)
        rows[k] = {"ratio": str(r), "index_dependence": str(d), "predicted": predict(r),
                   "det_G": str(sp.simplify(d * dJ * c))}
        print(f"  {k:9s} ratio {str(r):6s}  dependence {str(d):22s}  -> {predict(r)}"
              f"   det G = {rows[k]['det_G']}")

    ok_cal = all(rows[k]["predicted"] == v for k, v in GGM_PRINTED.items())
    print(f"\n  calibration vs GGM printed: "
          f"4_1 {rows['4_1']['predicted']} vs {GGM_PRINTED['4_1']}, "
          f"5_2(u=0) {rows['5_2_u0']['predicted']} vs {GGM_PRINTED['5_2_u0']}")
    check("G1-the derived rule (index dependence trivial <=> SL possible) reproduces GGM's OWN two "
          "printed choices — GL(2, Z[q,x]) for 4_1 in (138) and SL(3, Z[q]) for 5_2 at u=0 in (93) "
          "— so it is calibrated on published statements before being applied at rank 6",
          ok_cal, predicted={k: rows[k]["predicted"] for k in GGM_PRINTED}, printed=GGM_PRINTED)

    dp = dependence(RATIOS["pretzel"])
    is_monomial = sp.simplify(dp - q**(4 * (M - L))) == 0
    check("G2-the pretzel's determinant ladder is q^{4(M-L)} times a constant: a NONCONSTANT unit "
          "monomial, so GL membership holds automatically on determinant grounds and SL is "
          "IMPOSSIBLE off the diagonal M = L", is_monomial and predict(RATIOS["pretzel"]) == "GL",
          ladder=str(dp), predicted="GL")

    check("T1-gate 3 closes COMPLETELY, i.e. det J and c are individually determined. It does NOT: "
          "the ladder constrains how they enter, not either factor. Closing them needs the explicit "
          "rank-6 blocks or a printed rank-6 pairing, and no held source prints one",
          False,
          what_is_closed="the determinant ladder q^{4(M-L)} and the GL-not-SL verdict",
          what_is_open="det J and c = det W_0(q) det W_0(q^-1) individually",
          searched="GGM secs 007/011/015/017 — pairings printed only at rank 2 (137)/(138) and "
                   "rank 3 (92)/(93); Theorem 28 gives the general operator and W but no pairing")

    verdict = (
        "GATE 3, partially closed and honestly bounded. det G_{M,L} = ratio^M ratio_bar^L det J c, "
        "so the entire index dependence is the Casoratian ratio and nothing else. That yields a "
        "rule — trivial dependence <=> SL possible, nontrivial => GL and never SL — which "
        "reproduces GGM's OWN two printed choices, GL for 4_1 in (138) and SL for 5_2 at u=0 in "
        "(93) (G1, two-for-two, calibrated before use). Applied to the pretzel with Part 1's ratio "
        "q^4: det G_{M,L} = q^{4(M-L)} det J c, a nonconstant unit monomial, so the rank-6 pairing "
        "is GL and CANNOT be SL off the diagonal (G2) — a derived prediction, since no held source "
        "prints a rank-6 pairing. Note the pretzel groups with 4_1 here (index-DEPENDENT "
        "determinant) exactly as it does on Part 9's branch structure: two independent groupings "
        "agreeing. What does NOT close (T1): det J and c individually, which need the explicit "
        "rank-6 blocks.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-gate3-determinant-ladder",
         "description": "The pretzel's pairing determinant ladder derived from the Casoratian ratio, the "
                        "SL-vs-GL rule it implies calibrated against GGM's two printed choices, and the "
                        "GL-not-SL prediction at rank 6.",
         "computation": "aomega-m3-gate3-determinant-ladder", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "parameters": {"identity": "det G_{M,L} = ratio^M ratio_bar^L det J c"},
         "data": {"knots": rows, "ggm_printed": GGM_PRINTED, "calibrated": bool(ok_cal),
                  "pretzel_verdict": "GL, not SL"},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-gate3-determinant-ladder.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
