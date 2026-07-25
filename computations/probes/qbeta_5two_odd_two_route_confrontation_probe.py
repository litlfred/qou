#!/usr/bin/env python3
"""A6.2: the two odd-channel routes confronted — the saddle-side σ-pair
projection vs the W9-parallel resummed bar-side datum D_odd.

CONTEXT. Two independent lanes now hold 5₂ odd-channel data at the
substrate:
  * the MAIN-LINE Masbaum-face lane (probe qbeta_g3_5two_qborel_theta_
    laplace, merged): D_odd = (s(F̄) − F_conv)/2 ≈ −0.00758 ± 2e-10-band —
    a FUNCTION-VALUE odd datum from θ-Laplace resummation of the exact
    integer-Laurent Habiro tail;
  * this branch's A6 lane: the exact bar-odd σ-pair K-tower
    P_k(ξ₁) − P_k(ξ̄₁) of the state-integral saddle series (all 24 orders
    exact in the trace field).
Bridging the two at function level needs the state-integral factorization
normalization (Stokes sector population on the real-q ray) — named OPEN by
the W9-parallel verdict itself. This probe does the two things that need
NO scheme constant:

  A — the σ-pair odd projection EVALUATED at the substrate:
      O_φ := Im φ_σ1(x_sub), x_sub = −ln q₀ (the A4.3 substrate ray; the
      conjugate saddle gives the conjugate value, so the σ-pair difference
      is 2i·O_φ). Computed by 24-order truncation AND Borel–Padé
      directional Laplace (both converged at |x_sub| ≈ 0.104 — consistency
      gate). A derived, calibration-free odd number; recorded scope-(a)
      against D_odd and the anchor rows — NO identification.

  B — a normalization-free STRUCTURAL cross-check: the W9 exact q-Borel
      sequence T̂_n = C_n(q̄)(q̄;q̄)_n²a₀^{5n²+7n} has |ratio| → 1 (soft
      singularity at w = −1). The φ-side Gauss prefactor (ħ^{1/2} per
      saddle) predicts the soft exponent θ = 3/2 in
      (−1)^n T̂_n ~ A·rⁿ·n^{−θ}: extract θ from the exact integers by a
      3-parameter linear model in (1, n, ln n) — an exponent MEASUREMENT
      (linear algebra on exact data; no parameter enters any physical
      claim) — and compare. Agreement ties the two routes' analytic
      structure with zero scheme freedom; disagreement is recorded as the
      measured exponent.

auditOnly; no c_k wired; no fit (the θ extraction is a structural
measurement, labeled as such). Comparison to observed only; no
ontological claims.

Run: python3 -u computations/probes/qbeta_5two_odd_two_route_confrontation_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_odd_confrontation.log
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

mp.mp.dps = 60

# committed reference values (scope-(a) comparison rows)
D_ODD = mp.mpf("-0.00758")          # qbeta-g3-5two-qborel-theta-laplace (band 2e-10... 4e-4 kernel)
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
IM_VB = mp.mpf("0.0585499951473")
N_COEF = 44
T0 = time.monotonic()


def load_phi_basis():
    w = json.loads((_HERE / "qbeta-5two-phi-series-engine.witness.json")
                   .read_text())
    P = {0: mp.mpc(1)}
    for k, v in w["data"]["P_coefficients"].items():
        m = re.match(r"\(?\s*([-\d.e]+)\s*([+-])\s*([\d.e]+)j\)?", v)
        r_, s_, i_ = m.groups()
        P[int(k)] = mp.mpc(mp.mpf(r_), mp.mpf(i_) * (1 if s_ == "+" else -1))
    return P


def main() -> int:
    print("=" * 78)
    print(" A6.2 — odd-channel two-route confrontation (σ-pair vs D_odd)")
    print("=" * 78)

    t = mp.log(q_at(50))
    x_sub = -t                     # the A4.3 substrate ray x = −ln q₀

    # ---- A: σ-pair odd projection at the substrate ----
    P = load_phi_basis()
    OMAX = max(P)

    def phi_trunc(x):
        return sum(P[k] * x ** k for k in range(OMAX + 1))

    b = [P[k] / mp.factorial(k) for k in range(OMAX + 1)]
    p_num, p_den = mp.pade(b, 11, 12)

    def B_pade(zeta):
        num = sum(p_num[i] * zeta ** i for i in range(len(p_num)))
        den = sum(p_den[i] * zeta ** i for i in range(len(p_den)))
        return num / den

    def phi_res(x):
        ray = x / abs(x)
        f = lambda u: B_pade(u * ray) * mp.e ** (-(u * ray) / x) * ray
        return mp.quad(f, [0, 5, 20, 80]) / x

    pt = phi_trunc(x_sub)
    pr = phi_res(x_sub)
    O_t = mp.im(pt)
    O_r = mp.im(pr)
    consA = abs(O_t - O_r) / abs(O_t)
    gA = consA < mp.mpf("1e-6")
    log = lambda m_: print(f"  [{time.monotonic()-T0:5.0f}s] {m_}", flush=True)
    log(f"[A] x_sub = {mp.nstr(x_sub, 10)}")
    log(f"    Im φ_σ1: truncation {mp.nstr(O_t, 15)}  resummed "
        f"{mp.nstr(O_r, 15)}  consistency {mp.nstr(consA, 3)}")
    print(f"    σ-pair odd projection O_φ = {mp.nstr(O_t, 12)}  "
          f"{'PASS' if gA else 'FAIL'} (truncation/resummation gate)")
    rows = {"O_phi_sigma_pair": O_t, "D_odd_masbaum_face": D_ODD,
            "ratio_O_phi_over_D_odd": O_t / D_ODD,
            "S_muon": S_MUON, "S_proton": S_PROTON,
            "u_cubed": (2 * t) ** 3, "Im_Vb": IM_VB}
    print("\n    scope-(a) rows (NOT identifications; the function-level "
          "bridge needs the")
    print("    Stokes-population normalization — open per the W9-parallel "
          "verdict):")
    for k, v in rows.items():
        print(f"      {k:>24} = {mp.nstr(v, 10)}")

    # ---- B: soft-singularity exponent of the exact W9 sequence ----
    a0 = mp.e ** (-t / 2)
    ainv = 1 / a0
    qbar = ainv ** 2
    Th = []
    poch = mp.mpf(1)
    for n in range(N_COEF):
        if n > 0:
            poch *= (1 - qbar ** n)
        Th.append(_mb.leval(_mb.C52(n), ainv) * poch ** 2
                  * a0 ** (5 * n * n + 7 * n))
    # exponent measurement: ln|T_n| = c0 + c1·n − θ·ln n on the tail
    ns = list(range(20, N_COEF))
    A_ = mp.matrix([[1, n, -mp.log(n)] for n in ns])
    y = mp.matrix([mp.log(abs(Th[n])) for n in ns])
    AtA = A_.T * A_
    coef = mp.lu_solve(AtA, A_.T * y)
    theta = coef[2]
    # stability: repeat on a shifted window
    ns2 = list(range(28, N_COEF))
    A2 = mp.matrix([[1, n, -mp.log(n)] for n in ns2])
    y2 = mp.matrix([mp.log(abs(Th[n])) for n in ns2])
    theta2 = mp.lu_solve(A2.T * A2, A2.T * y2)[2]
    dtheta = abs(theta - theta2)
    log(f"[B] soft-singularity exponent of (−1)^n·T̂_n (exact integers):")
    log(f"    θ(window 20..43) = {mp.nstr(theta, 8)}   θ(28..43) = "
        f"{mp.nstr(theta2, 8)}   window drift {mp.nstr(dtheta, 3)}")
    theta_pred = mp.mpf(3) / 2
    dev_pred = abs(theta - theta_pred)
    gB_stable = dtheta < mp.mpf("0.2")
    match_32 = dev_pred < mp.mpf("0.25")
    print(f"    φ-side Gauss-prefactor prediction θ = 3/2: measured "
          f"{mp.nstr(theta, 6)} (|Δ| = {mp.nstr(dev_pred, 3)}) — "
          f"{'CONSISTENT' if match_32 else 'DIFFERS (measured exponent recorded)'}")

    wb = WitnessBuilder("qbeta-5two-odd-two-route-confrontation",
                        engine="mpmath", _script_path=__file__)
    wb.set_description(
        "A6.2: the two independent 5₂ odd-channel routes confronted at the "
        "substrate with NO scheme constant. A: the saddle-side σ-pair odd "
        "projection O_φ = Im φ_σ1(−ln q₀) (24-order basis; truncation vs "
        "Borel–Padé directional Laplace consistency-gated) — a derived, "
        "calibration-free odd number recorded scope-(a) against the "
        "Masbaum-face resummed D_odd and the anchor rows, with the "
        "function-level bridge (Stokes sector population on the real-q "
        "ray) explicitly named OPEN. B: a normalization-free structural "
        "tie — the soft-singularity exponent θ of the exact W9 q-Borel "
        "integer sequence, measured by a 3-parameter linear model "
        "(structural measurement, not a physics fit), vs the φ-side "
        "Gauss-prefactor prediction θ = 3/2. auditOnly; no c_k wired; "
        "no fit; no identification.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("sigma_pair_projection_consistent",
                     computed=float(consA), expected=0.0, tolerance=1e-6,
                     source="Im φ_σ1(x_sub): truncation = directional "
                            "resummation (both converged at |x| ≈ 0.104)")
    wb.add_assertion("exponent_extraction_stable",
                     computed=1.0 if gB_stable else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="θ window-drift < 0.2 across tail windows "
                            "(20..43 vs 28..43) on the exact T̂_n")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("sigma_pair", {"x_sub": mp.nstr(x_sub, 15),
                               "O_phi_trunc": mp.nstr(O_t, 25),
                               "O_phi_resummed": mp.nstr(O_r, 25)})
    wb.add_data("confrontation_rows", {k: mp.nstr(v, 12)
                                       for k, v in rows.items()})
    wb.add_data("soft_exponent", {"theta_20_43": mp.nstr(theta, 12),
                                  "theta_28_43": mp.nstr(theta2, 12),
                                  "prediction_phi_side": "3/2",
                                  "consistent_with_3_2": bool(match_32)})
    wb.add_data("open_bridge",
                "the function-level identification O_φ ↔ D_odd requires the "
                "Stokes sector population of the state-integral transseries "
                "on the real-q ray (the factorization normalization) — open; "
                "named by the W9-parallel verdict as the scheme-fixing step. "
                "Neither route's number is wired anywhere.")
    wb.add_data("verdict",
                (f"TWO-ROUTE CONFRONTATION RECORDED: O_φ = {mp.nstr(O_t, 8)} "
                 f"(σ-pair, calibration-free) vs D_odd = {mp.nstr(D_ODD, 6)} "
                 f"(Masbaum-face resummation) — ratio {mp.nstr(O_t/D_ODD, 6)}, "
                 f"scope-(a), bridge OPEN. Soft exponent θ = "
                 f"{mp.nstr(theta, 6)} vs the φ-side 3/2 prediction: "
                 f"{'consistent' if match_32 else 'differs'} "
                 f"(window drift {mp.nstr(dtheta, 3)}). auditOnly."
                 if ok else "A gate failed — inspect before use."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-odd-two-route-confrontation.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
