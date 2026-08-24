#!/usr/bin/env python3
"""qbeta_even_channel_magnitude_probe.py — the EVEN (cosh/Vol) channel on the
winding lattice: derive the second integer form, then test the pre-registered
derived magnitude candidates against |S_p/S_m|. No tuning; misses recorded.

Continuation of qbeta_cusp_lattice_geodesic_probe.py (sign = odd channel) and
qbeta_disc5_parity_probe.py (parity). The owner question: "can use q-bar norm
to get magnitude?" — the bar-norm on the lattice is the SIGN datum (norm form
G); the magnitude candidate is the OTHER bar-parity channel of the same 𝔙:

    V₄₁(u) = Vol + (i√3/4)u²   (FigureEightComplexVolume, κ=+√3/4 — confirmed
                                against the A-polynomial in the #4405 audit)
    u_{m,ℓ} = ln q₀ · (m + ℓω),  ω = e^{iπ/3}

DERIVED (checked exactly, [M1]): the even channel is the second integer form —
the CROSS form C(m,ℓ) = (2m+ℓ)·ℓ:

    Re 𝔙₄₁(u_{m,ℓ}) = Vol₄₁ − (3/8)(ln q₀)² · (2m+ℓ)ℓ
    Im 𝔙₄₁(u_{m,ℓ}) =        (√3/16)(ln q₀)² · [(2m+ℓ)² − 3ℓ²]

So on the lattice the full complex volume is two integer forms: magnitude
channel = cross form C (bar-even), sign channel = norm form G (bar-odd).

CHECKED, PRE-REGISTERED magnitude candidates ([M2]) — all fixed before
evaluation, none tuned, ALL results reported:

  (a) exponential bridge, per-anchor knot reading (μ↔4₁, p↔Borromean):
      |S_p/S_m| =? e^{−(Vol_Bor − Vol_41)/ℏ}, ℏ ∈ {ℏ_q, ℏ_q², 1}
  (b) same-knot winding scaling wⁿ ⇒ u ↦ n·u ⇒ deviations scale n²:
      |S_p/S_m| =? (3/2)² = 2.25  (n=3 vs n=2)
  (c) plain even-channel volume ratio: |S_p/S_m| =? Vol_Bor/Vol_41

Observed target: |S_p/S_m| ≈ 4.075.

EXPECTED AND CONFIRMED OUTCOME (honest): every candidate misses (>1%); the
closest is the volume ratio at ~11%. Assertion [M2] asserts the MISSES — this
probe rules the tested derived maps OUT (scope-(a): these candidates, alone,
as-is), it does not identify a magnitude map. Magnitude stays OPEN. Nothing
adopted, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
    # Vol(Borromean) = 8·Catalan (corpus: fundamental-knots-operator-basis)
    VOLBOR = 8 * mp.catalan
KAPPA = mp.sqrt(3) / 4
OMEGA = mp.exp(mp.mpc(0, 1) * mp.pi / 3)


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def V41(u: mp.mpc) -> mp.mpc:
    return VOL41 + mp.mpc(0, 1) * KAPPA * u * u


def u_geodesic(q, m: int, ell: int) -> mp.mpc:
    return mp.log(q) * (m + ell * OMEGA)


def cross(m: int, ell: int) -> int:
    """The even-channel integer form C(m,ℓ) = (2m+ℓ)·ℓ."""
    return (2 * m + ell) * ell


def main() -> int:
    print("=" * 78)
    print(" EVEN channel on the winding lattice: cross form + magnitude candidates")
    print("=" * 78)
    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_mu, S_pr = S(q_mu), S(q_pr)
    target = abs(S_pr / S_mu)
    hq = 1 - 1 / q_mu                       # ℏ_q = 1 − q₀⁻¹ (corpus)
    print(f"\n target |S_p/S_m| = {mp.nstr(target,8)}   ℏ_q = {mp.nstr(hq,8)}")

    # ---- [M1] the even channel is the cross form, exactly ---------------------
    print("\n [M1] Re 𝔙₄₁(u_{m,ℓ}) = Vol₄₁ − (3/8)(ln q₀)²·(2m+ℓ)ℓ   (cross form)")
    coef = mp.mpf(3) / 8 * mp.log(q_mu) ** 2
    m1_err = mp.mpf(0)
    print("      (m, ℓ)    C    Re 𝔙₄₁ − Vol₄₁")
    for (m, ell) in [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (2, 0), (0, 2), (3, 0), (0, 3)]:
        lhs = mp.re(V41(u_geodesic(q_mu, m, ell))) - VOL41
        rhs = -coef * cross(m, ell)
        m1_err = max(m1_err, abs(lhs - rhs))
        print(f"      ({m:2d},{ell:2d})  {cross(m,ell):4d}   {mp.nstr(lhs,8)}")
    m1 = m1_err < mp.mpf("1e-40")
    print(f"      max err {mp.nstr(m1_err,3)}  ⇒ exact: {bool(m1)}")
    print("      ⇒ BOTH channels are integer forms on the lattice:")
    print("        magnitude (bar-even/cosh) = cross form (2m+ℓ)ℓ;")
    print("        sign (bar-odd/sinh)       = norm form (2m+ℓ)²−3ℓ².")

    # ---- [M2] pre-registered candidates, all reported -------------------------
    print(f"\n [M2] pre-registered derived magnitude candidates vs {mp.nstr(target,6)}:")
    cands = {
        "exp bridge, ΔVol/ℏ_q  (μ↔4₁, p↔Bor)": mp.e ** (-(VOLBOR - VOL41) / hq),
        "exp bridge, ΔVol/ℏ_q²": mp.e ** (-(VOLBOR - VOL41) / hq ** 2),
        "exp bridge, ΔVol/1": mp.e ** (-(VOLBOR - VOL41)),
        "winding scaling n²: (3/2)²": mp.mpf(9) / 4,
        "volume ratio Vol_Bor/Vol_41": VOLBOR / VOL41,
    }
    all_miss, best, best_miss = True, None, None
    for k, v in cands.items():
        miss = abs(v - target) / target * 100
        if best_miss is None or miss < best_miss:
            best, best_miss = k, miss
        flag = "MISS" if miss > 1 else "match?!"
        all_miss &= miss > 1
        print(f"      {k:42s} = {mp.nstr(v,6):>12}   miss {mp.nstr(miss,4)}%  {flag}")
    m2 = all_miss
    print(f"      closest: {best} at {mp.nstr(best_miss,4)}% — all candidates miss >1%: {bool(m2)}")
    print("\n ⇒ scope-(a): the tested derived even-channel maps, alone and as-is, do not")
    print("   reproduce the magnitude ratio. The magnitude remains OPEN. Nothing adopted.")

    wb = WitnessBuilder("qbeta-even-channel-magnitude", engine="mpmath")
    wb.set_description(
        "Even (cosh/Vol) channel of the winding lattice (#4401/#4405): derived exactly, "
        "Re 𝔙₄₁(u_{m,ℓ}) = Vol₄₁ − (3/8)(ln q₀)²·(2m+ℓ)ℓ — the CROSS form, the second "
        "integer form alongside the sign channel's norm form (2m+ℓ)²−3ℓ². Pre-registered "
        "derived magnitude candidates ALL MISS the observed |S_p/S_m| ≈ 4.075: exponential "
        "bridge e^{−ΔVol/ℏ} at ℏ ∈ {ℏ_q, ℏ_q², 1} (astronomically small — the per-anchor "
        "knot reading with ΔVol = Vol_Bor − Vol_41 ≈ 5.30 is dead on arrival for the ratio), "
        "winding scaling n² = 2.25 (45% miss), volume ratio Vol_Bor/Vol_41 ≈ 3.610 (closest, "
        "11.4% miss). Scope-(a): these candidates alone as-is are excluded; magnitude OPEN; "
        "nothing adopted, nothing wired, no tuning (all candidates fixed before evaluation).")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("even_channel_readout", {
        "cross_form": "Re 𝔙₄₁ − Vol₄₁ = −(3/8)(ln q₀)²·(2m+ℓ)ℓ (exact, [M1])",
        "two_channel_split": ("magnitude=bar-even cross form (2m+ℓ)ℓ; "
                              "sign=bar-odd norm form (2m+ℓ)²−3ℓ²"),
        "target_ratio": mp.nstr(target, 10),
        "candidates": {k: mp.nstr(v, 10) for k, v in cands.items()},
        "closest": f"{best} at {mp.nstr(best_miss,4)}%",
        "verdict": ("all pre-registered derived magnitude maps miss >1% (closest: volume "
                    "ratio, 11.4%) — scope-(a) exclusion of these candidates as-is; "
                    "magnitude OPEN")})
    wb.add_assertion("even_channel_is_cross_form_exact", str(bool(m1)), "True")
    wb.add_assertion("all_preregistered_magnitude_candidates_miss", str(bool(m2)), "True")
    wb.save()
    print("\nwitness → qbeta-even-channel-magnitude.witness.json")
    ok = m1 and m2
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
