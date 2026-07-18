#!/usr/bin/env python3
"""qbeta_h4_screen_calibration_verify.py — bean qou-tti3 (8we6 critical-eye):
adversarial re-verification of the O(u^4) screen machinery BEFORE building on
its nine negatives.

The Route-A gate-fail audit (2026-07-13) and the mid-word screen rest on an
UNSTATED calibration identity between the cheap criterion and the full ladder:

    Delta(net)_4 = f(q) * Delta(net)_3,   phi_i := [s^i] log f(1+s)
    =>  Dc2 = phi_4 / U2[4]                      (U2 = s-series of u^2)
        Dc3 = (phi_6 - Dc2 * U2[6]) / U3[6]      (U3 = s-series of u^3)

with u = b*hbar_q^2, b = sqrt(q^4+q^2+1)/(q^2+1), hbar_q = (q-1)/q, so
U2[4] = b(1)^2 = 3/4 and U3[6] = b(1)^3 = 3*sqrt(3)/8. If this identity is
wrong, the screen's FAIL verdicts are miscalibrated and the nine negatives
are unreliable. This probe verifies it three independent ways:

  [1] SYMBOLIC: derive U2/U3 series from the ladder's own u(q), state the
      identity exactly.
  [2] SYNTHETIC TEST VECTORS: run the actual ladder solver (ladder_cks) on
      dnet3 * g(q) for three constructed g with known log-series (t^4, t^2,
      t^3 seeds; t = q-1) and check the predicted Dc2/Dc3 EXACTLY. These are
      machinery test vectors, not physics candidates — nothing is tuned.
  [3] CROSS-PROBE + INDEPENDENT ENGINE: recompute phi_4/phi_6 for all nine
      published candidates (three Route-A framings + six mid-word) with
      (i) the sympy screen method and (ii) an independent Cauchy-integral
      engine (mpmath.taylor method='quad' — no sympy series), then check the
      Route-A full-ladder c2 shifts (+12, +13/6, -40 exactly) against
      Dc2 = (4/3)*phi_4.

Also reports the screen's documented blind spot: the odd coefficients
[s^5], [s^7] of log f (odd-ladder leakage) for all nine candidates, which
the even-only criterion never inspects.

auditOnly; NO production wiring; NO fit. Scope-(a) throughout.
Witness: qbeta-h4-screen-calibration-verify.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath
from mpmath import mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

from qbeta_h4_route_a_gate_probe import (  # noqa: E402
    HA, q, s, reduce_quiet, mul_terms, baryon, net, ladder_cks,
)
from qbeta_h4_midword_criterion_screen import (  # noqa: E402
    build_candidates, inv,
)

NS = 8  # series order for the calibration algebra


def log_f_coeffs_sympy(dnet3, dnet4, order=7):
    """Exact [s^1..s^order] of log(dnet4/dnet3) — the screen's own method."""
    f = sp.cancel(sp.together(dnet4) / sp.together(dnet3))
    ser = sp.series(sp.log(f.subs(q, 1 + s)), s, 0, order + 1).removeO()
    return [sp.simplify(ser.coeff(s, i)) for i in range(1, order + 1)]


def log_f_coeffs_numeric(dnet3, dnet4, order=7, radius="0.08"):
    """Independent engine: extract [s^1..s^order] of log(f(1+s)) by a Cauchy
    contour integral (mpmath.taylor method='quad') — well-conditioned and
    genuinely independent of sympy's symbolic series algorithm.

    f = dnet4/dnet3; both vanish to first order at q=1 so f(1)=L (finite,
    nonzero) and g(s)=log(f(1+s)) is analytic on a disk about 0 (as long as
    f has no zero inside). We integrate g on the complex circle |s|=radius;
    the principal-branch log is single-valued there when f is zero-free in
    the disk. The constant coefficient (log L, branch-dependent) is discarded;
    only s^1..s^order are compared. (The quad method is well-conditioned at
    order 8, unlike a Vandermonde fit on clustered points.)
    """
    f3 = sp.lambdify(q, dnet3, modules="mpmath")
    f4 = sp.lambdify(q, dnet4, modules="mpmath")

    def g(sv):
        return mpmath.log(f4(1 + sv) / f3(1 + sv))

    coeffs = mpmath.taylor(g, 0, order, method="quad", radius=mp.mpf(radius))
    return [coeffs[i] for i in range(1, order + 1)]


def main() -> int:
    t0 = time.monotonic()
    mp.dps = 60
    print("=" * 78)
    print(" 8we6 critical-eye: screen-calibration verification (bean qou-tti3)")
    print("=" * 78)

    # ── [0] rebuild H3 baseline + candidates via the screen's own builders ──
    dnet3, cands = build_candidates()
    print(f"\n[0] rebuilt H3 Delta(net) + six mid-word candidates "
          f"({time.monotonic()-t0:.1f}s)")

    # ── [1] symbolic calibration identity from the ladder's own u(q) ──
    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    u_ser = sp.series(u.subs(q, 1 + s), s, 0, NS + 1).removeO()
    u2_ser = sp.expand(u_ser * u_ser)
    u3_ser = sp.expand(u2_ser * u_ser)
    U2 = [sp.simplify(sp.nsimplify(u2_ser.coeff(s, i))) for i in range(NS + 1)]
    U3 = [sp.simplify(sp.nsimplify(u3_ser.coeff(s, i))) for i in range(NS + 1)]
    ok_u24 = sp.simplify(U2[4] - sp.Rational(3, 4)) == 0
    ok_u36 = sp.simplify(U3[6] - 3 * sp.sqrt(3) / 8) == 0
    print(f"\n[1] U2[4] = {U2[4]}  (== 3/4: {ok_u24})")
    print(f"    U2[6] = {U2[6]}")
    print(f"    U3[6] = {U3[6]}  (== 3*sqrt(3)/8: {ok_u36})")
    print("    identity: Dc2 = (4/3)*phi_4 ;  Dc3 = (phi_6 - Dc2*U2[6]) / U3[6]")

    # ── [2] synthetic test vectors through the REAL ladder solver ──
    t = q - 1
    vectors = {
        "V1_t4_seed": 1 + t**4,      # phi_4 = 1, phi_6 = 0
        "V2_t2_seed": 1 + t**2,      # phi_2 = 1, phi_4 = -1/2, phi_6 = 1/3
        "V3_t3_seed": 1 + t**3,      # odd seed: phi_3 = 1, phi_4 = 0, phi_6 = -1/2
    }
    print("\n[2] synthetic test vectors (real ladder_cks run on dnet3*g):")
    c_base, _ = ladder_cks(dnet3, label="H3-baseline")
    vec_results = {}
    for name, g in vectors.items():
        phis = log_f_coeffs_sympy(dnet3, sp.expand(dnet3 * g))
        pred_dc2 = sp.simplify(phis[3] * sp.Rational(4, 3))
        pred_dc3 = sp.simplify((phis[5] - pred_dc2 * U2[6]) / U3[6])
        c_syn, _ = ladder_cks(sp.expand(dnet3 * g), label=name)
        dc2 = sp.simplify(c_syn[2] - c_base[2])
        dc3 = sp.simplify(c_syn[3] - c_base[3])
        ok2 = sp.simplify(dc2 - pred_dc2) == 0
        ok3 = sp.simplify(dc3 - pred_dc3) == 0
        if not ok2:  # exact simplify can miss surds; confirm numerically
            ok2 = abs(mp.mpf(str(sp.N(dc2 - pred_dc2, 40)))) < mp.mpf("1e-30")
        if not ok3:
            ok3 = abs(mp.mpf(str(sp.N(dc3 - pred_dc3, 40)))) < mp.mpf("1e-30")
        print(f"    {name}: phi_4={phis[3]}  phi_6={phis[5]}  "
              f"Dc2 pred={pred_dc2} meas={sp.nsimplify(dc2)} [{ok2}]  "
              f"Dc3 pred≈{sp.N(pred_dc3, 12)} meas≈{sp.N(dc3, 12)} [{ok3}]")
        vec_results[name] = {
            "g": str(g), "phi_4": str(phis[3]), "phi_6": str(phis[5]),
            "dc2_pred": str(pred_dc2), "dc2_measured": str(sp.nsimplify(dc2)),
            "dc3_pred": str(sp.N(pred_dc3, 30)), "dc3_measured": str(sp.N(dc3, 30)),
            "dc2_match": bool(ok2), "dc3_match": bool(ok3),
        }

    # ── [3] nine published candidates: two-engine phi + cross-probe check ──
    print("\n[3] nine published candidates — sympy vs independent numeric phi:")
    # rebuild the three Route-A framings exactly as published
    sig1_inv = inv(1)
    unit = reduce_quiet(mul_terms({(0,): sp.Integer(1)}, sig1_inv))
    b3 = reduce_quiet(mul_terms(reduce_quiet(mul_terms(unit, unit)), unit))
    elem_n3 = baryon(b3, ["u", "d", "d"])
    elem_p3 = baryon(b3, ["u", "u", "d"])
    e_word = {(1, 2, 1): sp.Integer(1)}
    sig2 = {(2,): sp.Integer(1)}
    unit4 = reduce_quiet(mul_terms(mul_terms(unit, sig2), sig1_inv))
    b4 = reduce_quiet(mul_terms(reduce_quiet(mul_terms(unit4, unit4)), unit4))
    framings = {
        "A1_brane_hopf_strand": (baryon(b3, ["u", "d", "d", "b"]),
                                 baryon(b3, ["u", "u", "d", "b"])),
        "A2_lepton_strand": (reduce_quiet(mul_terms(elem_n3, e_word)),
                             reduce_quiet(mul_terms(elem_p3, e_word))),
        "A3_brunnian4_core": (baryon(b4, ["u", "d", "d"]),
                              baryon(b4, ["u", "u", "d"])),
    }
    # published full-ladder c2 shifts (exact, from the Route-A audit)
    published_dc2 = {"A1_brane_hopf_strand": sp.Integer(12),
                     "A2_lepton_strand": sp.Rational(13, 6),
                     "A3_brunnian4_core": sp.Integer(-40)}

    nine = {}
    for name, (en, ep) in {**framings,
                           **{k: v for k, v in cands.items()}}.items():
        dnet4 = sp.simplify(net(en) - net(ep))
        if sp.simplify(dnet4 - dnet3) == 0:
            nine[name] = {"verdict": "TRIVIAL (== Delta(net)_3)"}
            print(f"    {name:22s}: TRIVIAL")
            continue
        phis_sym = log_f_coeffs_sympy(dnet3, dnet4)
        phis_num = log_f_coeffs_numeric(dnet3, dnet4)
        max_dev = max(abs(mp.mpf(str(sp.N(phis_sym[i], 50))) - phis_num[i])
                      for i in range(7))
        engines_agree = max_dev < mp.mpf("1e-18")
        entry = {
            "phi": {f"s^{i+1}": str(phis_sym[i]) for i in range(7)},
            "phi_numeric_max_dev": mp.nstr(max_dev, 5),
            "engines_agree_1e-18": bool(engines_agree),
            "odd_leakage_s5": str(phis_sym[4]),
            "odd_leakage_s7": str(phis_sym[6]),
        }
        line = (f"    {name:22s}: phi_4={sp.nsimplify(phis_sym[3])}  "
                f"phi_6={sp.nsimplify(phis_sym[5])}  "
                f"engines_agree={engines_agree} (dev {mp.nstr(max_dev, 3)})")
        if name in published_dc2:
            pred = sp.simplify(phis_sym[3] * sp.Rational(4, 3))
            ok = sp.simplify(pred - published_dc2[name]) == 0
            entry["dc2_pred_from_phi4"] = str(pred)
            entry["dc2_published"] = str(published_dc2[name])
            entry["cross_probe_match"] = bool(ok)
            line += f"  Dc2 pred={pred} vs published={published_dc2[name]} [{ok}]"
        print(line)
        nine[name] = entry

    # ── witness ──
    xchecks = [v for v in nine.values() if "cross_probe_match" in v]
    agree = [v for v in nine.values() if "engines_agree_1e-18" in v]
    witness = {
        "computation": "qbeta-h4-screen-calibration-verify",
        "description": (
            "Critical-eye verification of the O(u^4) screen machinery (bean "
            "8we6 follow-up, qou-tti3): (1) symbolic derivation of the "
            "screen-to-ladder calibration identity Dc2=(4/3)phi_4, "
            "Dc3=(phi_6-Dc2*U2[6])/U3[6] from the ladder's own u(q); (2) three "
            "synthetic test vectors run through the real ladder solver "
            "(machinery test, not physics; nothing tuned); (3) two-engine "
            "recomputation of phi_4/phi_6 for all nine published candidates "
            "(sympy series vs independent mpmath Vandermonde fit) + cross-probe "
            "check of the Route-A exact c2 shifts against the identity. Also "
            "reports the screen's odd-coefficient blind spot [s^5],[s^7]. "
            "auditOnly; no fit; scope-(a)."
        ),
        "audit_only": True,
        "parameters": {"series_order": NS, "numeric_dps": 60,
                       "numeric_fit_h": "1e-3"},
        "calibration": {
            "U2_s4": str(U2[4]), "U2_s6": str(U2[6]), "U3_s6": str(U3[6]),
            "identity": "Dc2=(4/3)*phi_4; Dc3=(phi_6-Dc2*U2[6])/U3[6]",
        },
        "synthetic_vectors": vec_results,
        "nine_candidates": nine,
        "assertions": [
            {"label": "U2[4] == 3/4 and U3[6] == 3*sqrt(3)/8",
             "passed": bool(ok_u24 and ok_u36)},
            {"label": "all synthetic vectors: ladder shifts match identity",
             "passed": all(v["dc2_match"] and v["dc3_match"]
                           for v in vec_results.values())},
            {"label": "odd seed V3 does not shift c2 (odd-blindness confirmed)",
             "passed": vec_results["V3_t3_seed"]["dc2_measured"] == "0"},
            {"label": "both engines agree on phi to 1e-18 (all candidates)",
             "passed": all(v["engines_agree_1e-18"] for v in agree)},
            {"label": "Route-A published exact c2 shifts match (4/3)*phi_4",
             "passed": all(v["cross_probe_match"] for v in xchecks)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-h4-screen-calibration-verify.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  allPassed: {witness['allPassed']}")
    print(f"  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
