#!/usr/bin/env python3
"""alpha_em_polarized_determinant_removes_blowup_probe.py

T3 (α_EM pivot). Follow-up to the genus-4 Epstein det′Δ result (#3934): the UNPOLARIZED
real Laplacian determinant on Jac(Bring)=E_5τ₀³×E_τ₀ does NOT factorize (spectrum
{λ+μ}) and its near-degenerate E_τ₀ block (Im τ₀=0.187) collapses det′Δ, blowing the
boson measure up to ~1.47e12. The #3941/#3949 coordination hint says the α_EM per-loop
`1/(8π)` needs a fibre-level / compact-real-form (`U_q(su(2))` `*`-structure) POLARIZED
projection.

This probe tests the polarized object. On the diagonal isogeny period
diag(5τ₀,5τ₀,5τ₀,τ₀), the POLARIZED (holomorphic) determinant FACTORIZES cleanly into
per-factor pieces (unlike the real det′Δ) — it is exactly the product
m1(5τ₀)³·m1(τ₀) that the genus-4 work had "retracted" for the WRONG (unpolarized) reason.

FINDINGS:
  1. POLARIZATION REMOVES THE BLOW-UP. The polarized measure = m1(5τ₀)³·m1(τ₀) = 8.2263
     — O(1), vs the unpolarized 1.47e12. So polarization is essential AND identifies the
     polarized object as the factorized holomorphic measure (confirms #3941).
  2. BUT 8.2263 IS NOT A CLEAN α_EM COEFFICIENT. Nearest simple candidate is b₁=8
     (measure/8 = 1.028, 2.8% off); it is NOT 8π (0.327×), 4π, 2π, or π². So polarization
     fixes the SCALE but a residual normalization (the compact-`*` projection factor /
     #3941's "½·a₀") is still unaccounted.

DISCIPLINE: scope-(a). Identifies the polarized determinant + shows it removes the
blow-up; reports the residual normalization gap honestly. Does NOT manufacture 8π. No
fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
T0 = mp.mpc("-0.5", "0.186676")


def eta(t):
    q = mp.e ** (2j * mp.pi * t)
    return q ** (mp.mpf(1) / 24) * mp.qp(q)


def m1(t):
    return 1 / (mp.sqrt(mp.im(t)) * abs(eta(t)) ** 2)


def dethol(t):
    return mp.im(t) * abs(eta(t)) ** 4


def main() -> int:
    pi = mp.pi
    meas_pol = m1(5 * T0) ** 3 * m1(T0)
    det_pol = dethol(5 * T0) ** 3 * dethol(T0)
    print(f"  polarized (holomorphic, factorized) measure = {mp.nstr(meas_pol, 12)}", flush=True)
    print(f"  polarized det = {mp.nstr(det_pol, 12)}  (unpolarized real det measure was ~1.47e12)", flush=True)

    cands = {"8pi": 8 * pi, "8": mp.mpf(8), "4pi": 4 * pi, "2pi": 2 * pi, "pi^2": pi ** 2}
    ratios = {k: meas_pol / v for k, v in cands.items()}
    for k in cands:
        print(f"    measure/{k} = {mp.nstr(ratios[k], 7)}", flush=True)
    blowup_removed = meas_pol < mp.mpf(100)                     # O(1), not 1e12
    nearest = min(cands, key=lambda k: abs(ratios[k] - round(float(ratios[k]))) if k != "8pi" else 1e9)
    no_clean_8pi = abs(ratios["8pi"] - 1) > mp.mpf("0.1")       # not 8pi
    b1_close_not_exact = abs(ratios["8"] - 1) < mp.mpf("0.05") and abs(ratios["8"] - 1) > mp.mpf("0.005")

    assertions = [
        ("polarization_removes_blowup", bool(blowup_removed)),
        ("polarized_measure_not_8pi", bool(no_clean_8pi)),
        ("nearest_candidate_is_b1_2p8pct_off", bool(b1_close_not_exact)),
    ]

    verdict = (
        f"POLARIZATION REMOVES THE BLOW-UP BUT DOES NOT LAND ON 8π (scope-(a), α_EM T3). The "
        f"polarized (holomorphic, factorized) determinant measure on Jac(Bring)=E_5τ₀³×E_τ₀ = "
        f"{mp.nstr(meas_pol,10)} — O(1), vs the unpolarized real det′Δ's ~1.47e12. So polarization "
        f"IS essential (confirms #3941) and the polarized object is the factorized holomorphic "
        f"measure that the genus-4 work retracted for the WRONG (unpolarized) reason. BUT "
        f"{mp.nstr(meas_pol,6)} is NOT a clean α_EM coefficient: nearest simple candidate is b₁=8 "
        f"(measure/8={mp.nstr(ratios['8'],6)}, 2.8% off); it is NOT 8π (measure/8π="
        f"{mp.nstr(ratios['8pi'],5)}), 4π, 2π, or π². Polarization fixes the SCALE; a residual "
        f"normalization (the compact-`*` projection / #3941's ½·a₀) is unaccounted. No 8π "
        f"manufactured. No fit; no c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("alpha-em-polarized-determinant-removes-blowup", engine="mpmath")
    wb.set_description(
        "α_EM T3: the polarized (holomorphic, factorized) determinant measure on Jac(Bring) = "
        "8.226 — O(1), removes the unpolarized 1.47e12 blow-up (polarization essential, #3941). "
        "But 8.226 is not a clean α_EM coefficient (nearest b₁=8, 2.8% off; not 8π) — a residual "
        "normalization (compact-* projection / ½·a₀) remains.")
    wb.set_audit_only("docs/audits/2026-07-19-alpha-em-polarized-determinant-removes-blowup.md")
    for name, passed in assertions:
        wb.add_assertion(name, str(passed), "True")
    wb.add_data("polarized_measure", mp.nstr(meas_pol, 15))
    wb.add_data("polarized_det", mp.nstr(det_pol, 15))
    wb.add_data("unpolarized_measure_reference", "~1.47e12")
    wb.add_data("measure_over_8pi", mp.nstr(ratios["8pi"], 10))
    wb.add_data("measure_over_8_b1", mp.nstr(ratios["8"], 10))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all(p for _, p in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
