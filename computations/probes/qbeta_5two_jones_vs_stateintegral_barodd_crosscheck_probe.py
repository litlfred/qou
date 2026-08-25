#!/usr/bin/env python3
"""qbeta_5two_jones_vs_stateintegral_barodd_crosscheck_probe.py

Cross-check the two 5₂ bar-odd faces — the ALGEBRAIC (Jones) datum built in
PR #4099 vs the ANALYTIC (state-integral) datum — with pre-stated kill-criteria.
Scout step #2 of the G3 attack map.

The two faces (same knot, same substrate q₀):

  (algebraic)  bar-odd(J_{5₂})(q₀)  — the 0-framing knot-invariant Jones bar-odd
     `(q−1)³(q+1)(q²+1)(q²−q+1)(q²+q+1)²/(2q⁶)`, framing-INVARIANT by construction
     (PR #4099, `qbeta_5two_categorical_markov_volume_probe.py`). Prefactor-free.

  (analytic)   Im(𝔏_odd)  — the imaginary part of the Theorem-22 state-integral
     log-split `𝔏_odd = (log Z_{5₂}(q) − log Z_{5₂}(q⁻¹))/2`
     (`qbeta_g3_5two_barodd_substrate.py`), AFTER the classical exponential
     (volume, `Re 𝔏_odd`) is stripped — the intrinsic bar-odd PHASE.

QUESTION (the scout's step #2): is the framing-invariant Jones bar-odd the
intrinsic bar-odd datum the state-integral route could not cleanly extract, up to
a fixed DERIVED normalization?

KILL-CRITERIA (stated BEFORE the run):
  (a) MATCH — if `Im(𝔏_odd) / bar-odd(J)(q₀)` equals a recognizable derived
      normalization from the pre-stated basis {1, 2π, π², [3]_q, Vol(5₂),
      [3]_q!, 2π·[3]_q, …} to ≤ 1% (the state-integral drift floor), the Jones
      datum IS that intrinsic bar-odd — a real advance on the barodd_substrate
      open step.
  (b) DISTINCT — if the ratio matches no pre-stated candidate beyond the floor,
      the two faces carry genuinely different normalizations; only the §4e
      quantum-modularity identification (algebraic ζ_N + analytic q₀ ⇒ forced
      Stokes A_ω) bridges them. Record and stop; nothing wired.

Anti-laundering: nothing inverted from S; both faces are computed from their own
first principles (Jones polynomial + Theorem-22 Z₅₂). No fit; no c_k wired; no
tier change. This is a fibre-vs-fibre structural comparison — it does NOT itself
cross the G3 argument→S wall.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# --- the algebraic face: bar-odd(J_{5₂})(q) --------------------------------
# J_{5₂}(q) = q⁻¹ − q⁻² + 2q⁻³ − q⁻⁴ + q⁻⁵ − q⁻⁶ ; bar-odd = ½(J(q) − J(q⁻¹)).
JONES_5_2 = {-1: 1, -2: -1, -3: 2, -4: -1, -5: 1, -6: -1}


def jones_5_2(q):
    return sum(c * q ** p for p, c in JONES_5_2.items())


def barodd_jones(q):
    return (jones_5_2(q) - jones_5_2(1 / q)) / 2


# --- the analytic face: Im(𝔏_odd) from the Theorem-22 state integral -------
_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_exact_blocks", _HERE / "qbeta_g3_5two_exact_blocks.py")
_b52 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_b52)


def Z52(u, tau):
    ta = tau + 1 / tau
    cA = mp.e ** (mp.mpc(0, 3) * mp.pi / 4 + mp.mpc(0, 5) * mp.pi / 12 * ta)
    cBC = mp.e ** (mp.mpc(0, -1) * mp.pi / 4 + mp.mpc(0, 1) * mp.pi / 12 * ta)
    PA, PB, PC = _b52.products(u, tau)
    return cA * PA + cBC * (PB + PC)


def Z52_avg(u0, tau, K=12, r=mp.mpf("1e-4")):
    acc = mp.mpc(0)
    for j in range(K):
        acc += Z52(u0 + r * mp.e ** (2 * mp.pi * mp.mpc(0, 1) * j / K), tau)
    return acc / K


def main() -> int:
    print("=" * 78)
    print(" 5₂ bar-odd cross-check: algebraic (Jones) vs analytic (state integral)")
    print("=" * 78)

    q0 = q_at(45)
    t = mp.log(q0)
    tau = mp.mpc(0, 1) * t / (2 * mp.pi)

    # algebraic face
    bj = barodd_jones(q0)
    print(f"\n[alg]  bar-odd(J_{{5₂}})(q₀) = {mp.nstr(bj, 15)}  (real; framing-invariant)")

    # analytic face
    u_sub = 2 * t
    Zq = Z52_avg(u_sub, tau)
    Zqi = Z52_avg(u_sub, -tau)
    L_odd = (mp.log(Zq) - mp.log(Zqi)) / 2
    im_L = mp.im(L_odd)
    print(f"[ana]  𝔏_odd = {mp.nstr(L_odd, 12)}")
    print(f"       Re 𝔏_odd = {mp.nstr(mp.re(L_odd), 10)}  (classical volume asymmetry — stripped)")
    print(f"       Im 𝔏_odd = {mp.nstr(im_L, 12)}  (intrinsic bar-odd phase)")

    # the ratio and the pre-stated normalization basis
    ratio = im_L / bj
    print(f"\n[cmp]  Im 𝔏_odd / bar-odd(J) = {mp.nstr(ratio, 12)}")
    q3 = 1 + q0 + q0 ** 2                       # [3]_q
    vol52 = mp.mpf("2.82812208833")             # Vol(5₂)
    q3fac = q3 * (1 + q0)                        # [3]_q! = [3][2][1]
    candidates = {
        "1": mp.mpf(1), "2pi": 2 * mp.pi, "pi^2": mp.pi ** 2,
        "[3]_q": q3, "Vol(5_2)": vol52, "[3]_q!": q3fac,
        "2pi*[3]_q": 2 * mp.pi * q3, "pi^2*[3]_q": mp.pi ** 2 * q3,
        "2pi^2": 2 * mp.pi ** 2, "4pi": 4 * mp.pi,
    }
    floor = mp.mpf("0.01")  # 1% state-integral drift floor
    best_name, best_rel = None, mp.mpf("inf")
    print("       nearest derived-normalization candidates (|ratio/cand − 1|):")
    for name, val in sorted(candidates.items(), key=lambda kv: abs(ratio / kv[1] - 1)):
        rel = abs(ratio / val - 1)
        if rel < best_rel:
            best_rel, best_name = rel, name
        print(f"         {name:14s} = {mp.nstr(val, 8):>12s}   rel = {mp.nstr(rel, 6)}")
    matched = best_rel < floor
    verdict = "a_MATCH" if matched else "b_DISTINCT"
    print(f"\n[verdict]  best candidate '{best_name}' rel = {mp.nstr(best_rel, 6)}  "
          f"⇒ kill-criterion ({'a' if matched else 'b'})")
    if matched:
        print(f"           (a) Jones bar-odd IS the intrinsic state-integral datum × {best_name}")
    else:
        print("           (b) DISTINCT normalizations — the two 5₂ faces are not related by a")
        print("               pre-stated derived factor; the bridge is the OPEN §4e quantum-")
        print("               modularity identification (algebraic ζ_N + analytic q₀ ⇒ A_ω).")

    wb = WitnessBuilder("qbeta-5two-jones-vs-stateintegral-barodd-crosscheck", engine="mpmath")
    wb.set_description(
        "Cross-check the two 5₂ bar-odd faces (scout G3 step #2): algebraic Jones "
        "bar-odd(J_5₂)(q₀) (framing-invariant, PR #4099) vs analytic Im(𝔏_odd), the "
        "prefactor-stripped phase of the Theorem-22 state-integral log-split "
        "(qbeta_g3_5two_barodd_substrate.py). Pre-stated kill-criteria: (a) MATCH if "
        "Im(𝔏_odd)/bar-odd(J) equals a derived normalization from a fixed basis to "
        "≤1% (state-integral drift floor); (b) DISTINCT otherwise ⇒ bridge is the open "
        "§4e quantum-modularity identification. Numbers: bar-odd(J)(q₀)≈0.021 (real), "
        "Im(𝔏_odd)≈2.27; ratio≈108 matches no pre-stated candidate ⇒ (b). The two faces "
        "carry genuinely different normalizations — the Jones datum is NOT the "
        "state-integral intrinsic bar-odd up to a trivial factor. Anti-laundering: "
        "nothing inverted from S; both faces from first principles; no fit; no c_k "
        "wired; fibre-vs-fibre only (does NOT cross the G3 argument→S wall)."
    )
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("faces", {
        "barodd_jones_q0": mp.nstr(bj, 15),
        "L_odd": mp.nstr(L_odd, 12),
        "Re_L_odd_classical": mp.nstr(mp.re(L_odd), 10),
        "Im_L_odd_intrinsic": mp.nstr(im_L, 12),
        "ratio_Im_L_over_jones": mp.nstr(ratio, 12)})
    wb.add_data("normalization_search", {
        "best_candidate": best_name, "best_rel": mp.nstr(best_rel, 8),
        "floor": "0.01",
        "candidates": {k: mp.nstr(v, 8) for k, v in candidates.items()}})
    wb.add_data("scope", {
        "verdict": verdict,
        "interpretation": ("distinct normalizations — the two 5₂ faces are not related by a "
                           "pre-stated derived factor; bridge is the open §4e quantum-modularity"),
        "crosses_g3_wall": False, "c_k_wired": False, "fit": False})
    wb.add_assertion("both_faces_bar_odd_nonzero",
                     computed=1.0 if (abs(bj) > 1e-6 and abs(im_L) > 1e-6) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="both the Jones bar-odd and the state-integral Im(L_odd) are nonzero "
                            "(chiral 5₂ carries a bar-odd datum on both faces)")
    wb.add_assertion("crosscheck_verdict_distinct_normalizations",
                     computed=1.0 if best_rel > mp.mpf("0.01") else 0.0,
                     expected=1.0, tolerance=0.5,
                     source=f"kill-criterion (b) PINNED as regression guard: best derived "
                            f"normalization '{best_name}' rel={float(best_rel):.4g} exceeds the "
                            f"1% floor — DISTINCT normalizations, bridge is the open §4e "
                            f"quantum-modularity. A rerun finding a sub-floor match flips this "
                            f"assertion so a human re-adjudicates the verdict.")
    wb.save()
    print(f"\n  RESULT: 5₂ bar-odd faces cross-checked ⇒ kill-criterion "
          f"({'a' if matched else 'b'}); {'match' if matched else 'distinct normalizations'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
