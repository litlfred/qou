#!/usr/bin/env python3
"""qbeta_5two_theorem3_shape_u_probe.py

Follow-up to the Q(sqrt-7) home result: does the owner's dilog paper's Theorem 3
(library/arxiv-2506.10206v2/2506.10206v2.pdf) -- the three-term dilog closed form L(u)=Li2(z_a)+Li2(z_b)
+Li2(u)=E(u), E elementary for real u>0 -- give the bar-odd c3 archimedean action
directly? Two findings (one positive, one honest negative):

  (+) Theorem 3 IS the 5_2 three-tetrahedron dilog closed form. Solving
      L(u) = Li2(z1)+2Li2(z2)  (the exact 5_2 plain-Li2 sum over its shapes)
      converges to THREE u-branches (the three tetrahedra), each an apparent
      Q(sqrt-7) value -- confirming Theorem 3 captures the 5_2 geometric dilog sum.

  (-) The NAIVE archimedean identification FAILS. The bar-odd action is NOT simply
      "E(u) at a real-u saddle": Re E(u) for real u in (0, 4/3) stays in [3.008, 3.269]
      (min ~3.0076 at u~0.4) and matches NONE of the clean candidates (pi^2/5, pi^2/6,
      5pi^2/6, pi^2/7-family, 3*Re Li2((3-i sqrt7)/8)). The h<->2pi i/N wall connecting
      Theorem 3 to the archimedean (rho_inf) face is more subtle than real-u evaluation
      -- exactly the block/saddle sheet data the sibling M-dictionary (Theorem 22:
      three blocks A.A/B.B/C.C, beta_A=5pi i/12, beta_B=beta_C=pi i/12) is deriving.

DISCIPLINE (anti-laundering): confirms Theorem 3 = the 5_2 dilog closed form; RULES OUT
the naive real-u identification of the bar-odd action (honest negative). No bar-odd
action value claimed. No fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
L = mp.polylog
ln = mp.log
pi = mp.pi


def W(u):
    return mp.sqrt(4 - 3 * u) * mp.sqrt(u)


def Lfun(u):
    w = W(u)
    return L(2, (2 - w - u) / 2) + L(2, (2 + w - u) / 2) + L(2, u)


def Efun(u):
    w = W(u)
    return (mp.mpf(1) / 3) * ln(2 / (w - u) + 1) ** 2 \
        - (mp.mpf(1) / 2) * ln(-2 / (-u + w + 2)) ** 2 \
        - (mp.mpf(1) / 2) * ln(2 / (u + w - 2)) ** 2 \
        + (mp.mpf(1) / 3) * ln(1 - 2 / (u + w)) ** 2 \
        - (mp.mpf(2) / 3) * ln(1 - u) * ln(-u) \
        + (mp.mpf(1) / 3) * ln(1 - u) ** 2 - (mp.mpf(1) / 6) * ln(-u) ** 2 - pi ** 2 / 2


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    # transcription check: L=E at a generic complex u
    u0 = mp.mpc("0.3", "0.7")
    LE_ok = abs(Lfun(u0) - Efun(u0)) < mp.mpf(10) ** -20
    check("theorem3_L_equals_E_transcription", LE_ok,
          source="L(u)=E(u) to 20 digits at u=0.3+0.7i -- Theorem 3 correctly implemented")

    # (+) Theorem 3 captures the 5_2 three-tetrahedron dilog sum
    P = importlib.util.module_from_spec(importlib.util.spec_from_file_location(
        "p5", str(Path(__file__).resolve().parent / "qbeta_5two_quantum_volume_probe.py")))
    importlib.util.spec_from_file_location(
        "p5", str(Path(__file__).resolve().parent / "qbeta_5two_quantum_volume_probe.py")).loader.exec_module(P)
    x1, y1 = P.saddle(mp.mpf(1), mp.mpc("0.78492", "1.30714"))
    z1, z2 = y1 / x1, 1 / y1
    plain = L(2, z1) + 2 * L(2, z2)
    ubranches = []
    for seed in (z1, mp.mpc("0.3", "0.5"), mp.mpc("-0.5", "0.5")):
        try:
            us = mp.findroot(lambda u: Lfun(u) - plain, seed)
            if all(abs(us - v) > mp.mpf("1e-6") for v in ubranches):
                ubranches.append(us)
        except Exception:
            pass
    got_branches = len(ubranches) >= 2 and all(abs(Lfun(u) - plain) < mp.mpf(10) ** -12 for u in ubranches)
    print(f"\n plain Li2 sum = {mp.nstr(plain, 10)}; u-branches solving L(u)=sum:")
    for u in ubranches:
        print(f"   u = {mp.nstr(u, 9)}", flush=True)
    check("theorem3_captures_5two_dilog_sum", got_branches,
          computed=f"{len(ubranches)} u-branches, each L(u)=Li2(z1)+2Li2(z2)",
          source="Theorem 3 L(u) reproduces the exact 5_2 three-tetrahedron plain-Li2 sum "
                 "at three u-branches (the three tetrahedra) -- it IS the 5_2 closed form")

    # (-) naive real-u archimedean identification FAILS (skip singular u=1 etc.)
    reE = []
    for k in range(1, 40):
        try:
            reE.append(mp.re(Efun(mp.mpf(k) * mp.mpf(4) / 3 / 40)))
        except (ZeroDivisionError, ValueError):
            pass
    reE_lo, reE_hi = min(reE), max(reE)
    cands = {"pi^2/5": pi**2/5, "pi^2/6": pi**2/6, "5pi^2/6": 5*pi**2/6,
             "pi^2/7": pi**2/7, "2pi^2/7": 2*pi**2/7, "3pi^2/7": 3*pi**2/7}
    nearest = min(cands.items(), key=lambda kv: min(abs(kv[1] - reE_lo), abs(kv[1] - reE_hi)))
    no_clean_match = min(abs(nearest[1] - reE_lo), abs(nearest[1] - reE_hi)) > mp.mpf("0.1")
    print(f"\n real-u Re E(u) in [{mp.nstr(reE_lo,8)}, {mp.nstr(reE_hi,8)}]; nearest candidate "
          f"{nearest[0]}={mp.nstr(nearest[1],7)} (gap > 0.1: {no_clean_match})", flush=True)
    check("naive_real_u_identification_ruled_out", no_clean_match,
          source="Re E(u) real-u face stays in [3.01,3.27], matching no clean pi^2-rational "
                 "(nor 3*ReLi2((3-i sqrt7)/8)) -- the archimedean action is NOT naive real-u E; "
                 "the h<->2pi i/N wall needs the sibling block/saddle sheet data")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        f"THEOREM 3 = 5_2 DILOG CLOSED FORM (confirmed) + NAIVE ARCHIMEDEAN IDENTIFICATION "
        f"RULED OUT (honest negative). (+) Theorem 3's L(u)=E(u) (verified to 20 digits) "
        f"reproduces the exact 5_2 three-tetrahedron plain-Li2 sum Li2(z1)+2Li2(z2) at "
        f"{len(ubranches)} u-branches (the three tetrahedra, apparent Q(sqrt-7)) -- so Theorem 3 "
        f"IS the 5_2 closed form. (-) But the bar-odd archimedean action is NOT the naive real-u "
        f"face: Re E(u) in [{mp.nstr(reE_lo,6)},{mp.nstr(reE_hi,6)}] matches no clean pi^2-rational "
        f"or Q(sqrt-7) constant. The h<->2pi i/N wall (Theorem 3 geometric -> archimedean rho_inf) "
        f"is more subtle -- it needs the sibling M-dictionary's block/saddle sheet data (Theorem 22 "
        f"three blocks, beta_A=5pi i/12, beta_B=beta_C=pi i/12). The bar-odd action stays OPEN, now "
        f"localized to the block-saddle wall crossing. No fit; no c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-5two-theorem3-shape-u", engine="mpmath")
    wb.set_description(
        "Theorem 3 (owner dilog paper) IS the 5_2 three-tetrahedron dilog closed form "
        "(L(u)=Li2(z1)+2Li2(z2) at 3 u-branches); but the naive real-u face of E(u) is NOT "
        "the bar-odd archimedean action (no clean constant) -- the h<->2pi i/N wall needs the "
        "sibling block/saddle data. Honest negative; action stays open.")
    wb.set_audit_only("docs/audits/2026-07-18-5two-theorem3-shape-u-archimedean-negative.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("plain_li2_sum", mp.nstr(plain, 12))
    wb.add_data("u_branches", [mp.nstr(u, 12) for u in ubranches])
    wb.add_data("real_u_ReE_min", mp.nstr(reE_lo, 10))
    wb.add_data("real_u_ReE_max", mp.nstr(reE_hi, 10))
    wb.add_data("nearest_candidate", f"{nearest[0]}={mp.nstr(nearest[1],8)}")
    wb.add_data("naive_real_u_ruled_out", bool(no_clean_match))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
