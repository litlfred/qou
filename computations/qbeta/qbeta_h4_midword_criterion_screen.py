#!/usr/bin/env python3
"""qbeta_h4_midword_criterion_screen.py — bean 8we6 follow-up: screen
mid-word-entangled sigma_2 candidates with the cheap O(u^4) criterion.

The Route-A gate-fail audit (2026-07-13-8we6-h4-route-a-three-framings-
gate-fail.md, PR #3769) left a checkable a-priori criterion: an H4 object
can contribute an independent c4 rung only if

    log( Delta(net)_4 / Delta(net)_3 )  has zero s^4 and s^6 coefficients
    (s = q-1; c_k lives at s^{2k}, so s^4 -> c2, s^6 -> c3),

which costs a rational-function series (seconds) instead of the full
trig/surd ladder (minutes). This probe generates SIX mid-word-entangled
sigma_2 candidates — constructions whose low-order content might cancel by
design (conjugations, commutators, straddling pairs) — and screens them.
Candidates passing the even-order screen get the full exact ladder run
(c2/c3 exact-match gate + c4^even extraction).

Candidate constructions (screening-only; any survivor is a DESIGN
CANDIDATE for owner review, never auto-wired):

  C1 conj_core        core = s2 . B3 . s2^-1, quark crossings as usual
  C2 conj_baryon      s2 . (B3 . crossings) . s2^-1  (whole baryon conjugated)
  C3 comm_12_append   baryon . [s1, s2]   ([a,b] = a b a^-1 b^-1)
  C4 comm_21inv_append baryon . [s2, s1^-1]
  C5 straddle_core    (s0 s1^-1) . s2 . (s0 s1^-1) . s2^-1 . (s0 s1^-1) as core
  C6 crossing_straddle B3 . cx(0,1) . s2 . cx(0,2) . s2^-1 . cx(1,2)

auditOnly; NO production wiring; NO fit (the screen and gate can only
falsify). Witness: qbeta-h4-midword-criterion-screen.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from qbeta_h4_route_a_gate_probe import (  # noqa: E402
    HA, q, s, reduce_quiet, mul_terms, crossing, baryon, net, ladder_cks,
)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

SCREEN_ORDER = 7  # series of log f through s^7; gate on s^4 and s^6


def inv(gen):
    """sigma_gen^-1 = sigma_gen - (q - q^-1)."""
    return {(gen,): sp.Integer(1), (): -HA}


def conj_s2(terms):
    """s2 . terms . s2^-1, reduced."""
    out = mul_terms({(2,): sp.Integer(1)}, terms)
    out = mul_terms(out, inv(2))
    return reduce_quiet(out)


def build_candidates():
    sig1_inv = inv(1)
    unit = reduce_quiet(mul_terms({(0,): sp.Integer(1)}, sig1_inv))
    b3 = reduce_quiet(mul_terms(reduce_quiet(mul_terms(unit, unit)), unit))

    comm12 = reduce_quiet(mul_terms(mul_terms({(1,): sp.Integer(1)}, {(2,): sp.Integer(1)}),
                                    mul_terms(inv(1), inv(2))))
    comm21i = reduce_quiet(mul_terms(mul_terms({(2,): sp.Integer(1)}, inv(1)),
                                     mul_terms(inv(2), {(1,): sp.Integer(1)})))
    core5 = reduce_quiet(mul_terms(mul_terms(mul_terms(mul_terms(
        unit, {(2,): sp.Integer(1)}), unit), inv(2)), unit))

    def baryon_c6(types):
        elem = dict(b3)
        pairs = [(0, 1), (0, 2), (1, 2)]
        for idx, (i, j) in enumerate(pairs):
            elem = reduce_quiet(mul_terms(elem, crossing(types[i], types[j], i)))
            if idx == 0:
                elem = reduce_quiet(mul_terms(elem, {(2,): sp.Integer(1)}))
            elif idx == 1:
                elem = reduce_quiet(mul_terms(elem, inv(2)))
        return elem

    n3, p3 = baryon(b3, ["u", "d", "d"]), baryon(b3, ["u", "u", "d"])

    cands = {}
    core1 = conj_s2(b3)
    cands["C1_conj_core"] = (baryon(core1, ["u", "d", "d"]), baryon(core1, ["u", "u", "d"]))
    cands["C2_conj_baryon"] = (conj_s2(n3), conj_s2(p3))
    cands["C3_comm_12_append"] = (reduce_quiet(mul_terms(n3, comm12)), reduce_quiet(mul_terms(p3, comm12)))
    cands["C4_comm_21inv_append"] = (reduce_quiet(mul_terms(n3, comm21i)), reduce_quiet(mul_terms(p3, comm21i)))
    cands["C5_straddle_core"] = (baryon(core5, ["u", "d", "d"]), baryon(core5, ["u", "u", "d"]))
    cands["C6_crossing_straddle"] = (baryon_c6(["u", "d", "d"]), baryon_c6(["u", "u", "d"]))
    dnet3 = sp.simplify(net(n3) - net(p3))
    return dnet3, cands


def screen(dnet3, dnet4):
    """Return (regularizable, coeffs s^1..s^SCREEN_ORDER of log(dnet4/dnet3), pass_even)."""
    if sp.simplify(dnet4.subs(q, 1)) != 0:
        return False, None, False
    f = sp.cancel(sp.together(dnet4) / sp.together(dnet3))
    ser = sp.series(sp.log(f.subs(q, 1 + s)), s, 0, SCREEN_ORDER + 1).removeO()
    coeffs = [sp.simplify(ser.coeff(s, i)) for i in range(1, SCREEN_ORDER + 1)]
    pass_even = (coeffs[3] == 0) and (coeffs[5] == 0)   # s^4, s^6
    return True, coeffs, pass_even


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    print("=" * 78)
    print(" H4 mid-word sigma_2 candidates — O(u^4) criterion screen (bean 8we6)")
    print("=" * 78)

    dnet3, cands = build_candidates()
    results, survivors = {}, []
    for name, (en, ep) in cands.items():
        dnet4 = sp.simplify(net(en) - net(ep))
        if sp.simplify(dnet4 - dnet3) == 0:
            print(f"\n  {name:22s}: TRIVIAL (Delta(net)_4 == Delta(net)_3; no sigma_2 content in net)")
            results[name] = {"verdict": "TRIVIAL", "delta_net4": str(dnet4)}
            continue
        reg, coeffs, ok = screen(dnet3, dnet4)
        if not reg:
            print(f"\n  {name:22s}: FAIL (not (q-1)-regularizable)")
            results[name] = {"verdict": "FAIL_regularizability", "delta_net4": str(dnet4)}
            continue
        c4s = {f"s^{i+1}": str(c) for i, c in enumerate(coeffs)}
        s4, s6 = coeffs[3], coeffs[5]
        print(f"\n  {name:22s}: [s^4]log f = {sp.nsimplify(s4)}   [s^6]log f = {sp.nsimplify(s6)}"
              f"   -> {'PASS' if ok else 'FAIL'}")
        results[name] = {"verdict": "PASS_screen" if ok else "FAIL_screen",
                         "log_f_coeffs": c4s, "delta_net4": str(dnet4)}
        if ok:
            survivors.append((name, dnet4))

    # full ladder only for screen survivors
    for name, dnet4 in survivors:
        print(f"\n  SURVIVOR {name}: running full exact ladder (KC=4) ...")
        cks, _ = ladder_cks(dnet4, label=name)
        c2n, c3n, c4n = (mp.mpf(str(sp.N(cks[k], 40))) for k in (2, 3, 4))
        print(f"    c2^even={mp.nstr(c2n,14)}  c3^even={mp.nstr(c3n,14)}  c4^even={mp.nstr(c4n,14)}")
        results[name]["full_ladder"] = {"c2_even": mp.nstr(c2n, 25), "c3_even": mp.nstr(c3n, 25),
                                        "c4_even": mp.nstr(c4n, 25), "c4_even_exact": str(cks[4])}

    witness = {
        "computation": "qbeta-h4-midword-criterion-screen",
        "description": (
            "Cheap O(u^4)-criterion screen (log(Delta(net)_4/Delta(net)_3) must have "
            "zero s^4 and s^6 coefficients) over six mid-word-entangled sigma_2 H4 "
            "candidates (conjugated core/baryon, two commutator appends, straddled "
            "core, straddled crossings), per the Route-A gate-fail audit's sharpened "
            "criterion. Full exact ladder run only for screen survivors. Screening "
            "can only falsify; survivors are design candidates for owner review, "
            "never auto-wired. auditOnly; no fit."
        ),
        "audit_only": True,
        "parameters": {"screen_order": SCREEN_ORDER, "criterion": "[s^4]=[s^6]=0 of log(dnet4/dnet3)"},
        "candidates": results,
        "n_survivors": len(survivors),
        "assertions": [
            {"label": "screen executed on all six candidates", "passed": len(results) == 6},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-h4-midword-criterion-screen.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall; survivors: {len(survivors)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
