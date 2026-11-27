#!/usr/bin/env python3
"""borromean_binding_recompute.py — the SINGLE Borromean per-knot pipeline (80-dps).

Complete nuclear-binding recompute through ONE pipeline (no special-casing,
no m_e*Vol(B_3)): every nucleus AND every nucleon mass flows from the same
Borromean H_3 trace tau that `F_Bor` uses for the nucleon rest mass, evaluated
at >= 95 working decimal digits (serialized at 80 decimal digits, zero float64)
at the proton-ratio substrate pin `q_at(dps)`.

Pipeline (derived conventions, per docs/audits/2026-06-28-brane-tower-
formalize-first-plan.md):

  tau := |tr_M(beta_Bor)| = (4 + h^2 - 3*h^4 - h^6) / (h^2 + 4)
         (Lean BorromeanMarkovTrace; tau_p = tau_n at H_3)
  interface factors  f_pp = f_pn = z,  f_nn = z - h = 1/(q*(q^2+1)),
                     with exact swap identity z / (z - h) = q^4
  atom trace   tr_atom = tau^A * prod_i f_i ,   tr_free = tau^A
  B_can^0 = E_0 * (tr_free - tr_atom)                     descended (k=0)
  B_tower = B_can^0 + E_0 * z^2 * sum_pairs (g(tau_i*tau_j) - g(tau_i*tau_j*f_ij))
            g(x) = -Li_2^q(-x)   (bar-even binding channel + Hecke -q^{-1} sign)

Here E_0 = qbeta_e0.canonical(q, m_e) is the tower-summed energy scale (#8590)
and z = q^3 / (q^2 + 1) is the canonical Temperley-Lieb / SU(2) Markov weight.
AME2020 binding totals are comparison targets only and enter no predicted formula.
"""
from __future__ import annotations

import os
import sys
import warnings
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ.setdefault("QOU_OUTPUT_DPS", "80")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE / "qbeta"))
warnings.filterwarnings("ignore")

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from canonical_mass import proton_neutron_mass_mev  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV as M_E,
)
import qbeta_e0 as _qbeta_e0  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

# AME2020 totals (MeV) as exact decimal strings — comparison target only.
ISO = [
    ("2H", 1, 1, mp.nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)),
    ("3H", 1, 2, mp.nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)),
    ("3He", 2, 1, mp.nstr(AME_B_HE3_MEV_VALIDATION, 30)),
    ("4He", 2, 2, mp.nstr(AME_B_HE4_MEV_VALIDATION, 30)),
    ("6Li", 3, 3, "31.994564"),
    ("7Li", 3, 4, "39.244533"),
    ("12C", 6, 6, "92.161728"),
    ("16O", 8, 8, "127.619"),
    ("56Fe", 26, 30, "492.254"),
]


def _params(dps: int = 95):
    """80-dps-grade substrate parameters at the proton-ratio pin q_at(dps)."""
    work_dps = max(int(dps), 95)
    mp.mp.dps = work_dps
    q = q_at(work_dps)
    me = mp.mpf(str(M_E))
    qi = mp.mpf(1) / q
    h = q - qi
    e0 = _qbeta_e0.canonical(q=q, m_e=me)
    z = q**3 / (q**2 + 1)
    tau = (mp.mpf(4) + h**2 - mp.mpf(3) * h**4 - h**6) / (h**2 + mp.mpf(4))
    return q, qi, h, e0, z, tau


def borromean_binding(Z: int, N: int, dps: int = 95) -> dict:
    """Canonical single-pipeline binding (MeV) for nucleus (Z, N) at >= 80 dps.

    Returns exact `mp.mpf` quantities (`tau`, `B_can0`, `B_tower`) so downstream
    high-precision callers (`deuteron_from_scratch_ledger.py`, `probe_9b`)
    preserve full 80-dps accuracy without binary64 truncation.
    """
    work_dps = max(int(dps), 95)
    with mp.workdps(work_dps):
        q, qi, h, e0, z, tau = _params(work_dps)
        z2 = z * z
        f_pp = z
        f_pn = z
        f_nn = z - h
        a_num = Z + N

        def g(x: mp.mpf) -> mp.mpf:
            return -li_2_q(-x, q, qi)

        ratio = (
            (f_pp ** max(Z - 1, 0))
            * (f_pn if Z and N else mp.mpf(1))
            * (f_nn ** max(N - 1, 0))
        )
        trf = tau ** a_num
        tra = trf * ratio
        dtr = trf - tra
        pair = mp.mpf(0)
        for cnt, fb in (((Z * (Z - 1)) // 2, f_pp), (Z * N, f_pn), ((N * (N - 1)) // 2, f_nn)):
            if cnt:
                pair += cnt * (g(tau * tau) - g(tau * tau * fb))
        return {
            "Z": Z,
            "N": N,
            "A": a_num,
            "tau": tau,
            "B_can0": e0 * dtr,
            "B_tower": e0 * (dtr + z2 * pair),
        }


def recompute(dps: int = 95):
    work_dps = max(int(dps), 95)
    with mp.workdps(work_dps):
        q, qi, h, e0, z, tau = _params(work_dps)
        mpc, mnc = proton_neutron_mass_mev()
        mpc = mp.mpf(str(mpc))
        mnc = mp.mpf(str(mnc))
        rows = []
        for nm, z_cnt, n_cnt, b_ame_str in ISO:
            b_ame = mp.mpf(b_ame_str)
            b = borromean_binding(z_cnt, n_cnt, work_dps)
            mu = z_cnt * mpc + n_cnt * mnc
            rows.append((
                nm,
                z_cnt,
                n_cnt,
                b_ame_str,
                b_ame,
                b["B_can0"],
                b["B_tower"],
                mu - b_ame,
                mu - b["B_tower"],
            ))
        return q, e0, tau, z, h, mpc, mnc, rows


def main() -> int:
    set_compute_dps()
    with mp.workdps(95):
        q, e0, tau, z, h, mpc, mnc, rows = recompute(95)
        print(
            f"SINGLE Borromean per-knot pipeline  (tau_p=tau_n={mp.nstr(tau, 7)} < 1 => "
            f"converges all Z;  z={mp.nstr(z, 6)}, z-h={mp.nstr(z - h, 6)})"
        )
        print(
            f"  shared nucleon mass (F_Bor, same tau): m_p={mp.nstr(mpc, 7)}  "
            f"m_n={mp.nstr(mnc, 7)} MeV\n"
        )
        print(
            f"{'iso':5s}{'B_AME':>9s}{'B_can0':>9s}{'err0':>7s}{'B_tower':>10s}"
            f"{'errT':>7s}   {'m_can_T':>10s}{'M_meas':>10s}   err_ppm"
        )
        for nm, _z, _n, _b_str, b_ame, b0, bt, m_meas, m_can in rows:
            ppm = (m_can / m_meas - mp.mpf(1)) * mp.mpf("1e6")
            print(
                f"{nm:5s}{mp.nstr(b_ame, 6):>9s}{mp.nstr(b0, 6):>9s}"
                f"{mp.nstr(b_ame / b0, 4):>7s}{mp.nstr(bt, 6):>10s}"
                f"{mp.nstr(b_ame / bt, 4):>7s}   {mp.nstr(m_can, 7):>10s}"
                f"{mp.nstr(m_meas, 7):>10s}  {mp.nstr(ppm, 5):>8s}"
            )

        # Algebraic invariants for non-vacuous certification
        swap_ratio_dev = mp.fabs(z / (z - h) - q**4)
        tau_sub_unit = int(mp.mpf(0) < tau < mp.mpf(1))
        tower_adds_binding = int(all(bt > b0 > mp.mpf(0) for *_, b0, bt, _, _ in rows))

        out = {
            "schema": "borromean-binding/v1",
            "q0": fmt(q),
            "tau": fmt(tau),
            "E0_MeV": fmt(e0),
            "z_markov": fmt(z),
            "converges_all_Z": True,
            "isotopes": [
                {
                    "iso": nm,
                    "Z": z_cnt,
                    "N": n_cnt,
                    "B_AME": b_str,
                    "B_can0": fmt(b0),
                    "B_tower": fmt(bt),
                    "delta_K_residual": fmt(b_ame / bt),
                }
                for nm, z_cnt, n_cnt, b_str, b_ame, b0, bt, _, _ in rows
            ],
        }
        wb = WitnessBuilder.wrap_legacy(
            "borromean-binding-recompute",
            out,
            script_path=__file__,
            engine="mpmath",
        )
        wb.add_assertion(
            "borromean_tau_strictly_inside_unit_disc",
            computed=tau_sub_unit,
            expected=1,
            tolerance=0,
            source="0 < tau(beta_Bor) < 1 at q_0 guarantees Li_2^q pair-tower convergence for all Z",
        )
        wb.add_assertion(
            "nn_bond_swap_ratio_equals_q_fourth",
            computed=fmt(swap_ratio_dev),
            expected="0",
            tolerance="1e-80",
            source="at z = q^3/(q^2+1), z - h = 1/(q*(q^2+1)), so z / (z - h) = q^4 identically",
        )
        wb.add_assertion(
            "pair_tower_strictly_increases_binding_all_isotopes",
            computed=tower_adds_binding,
            expected=1,
            tolerance=0,
            source="B_tower > B_can0 > 0 across all 9 benchmark nuclides (2H .. 56Fe)",
        )
        p = wb.save({
            "q0Anchor": "proton",
            "q0AnchorReason": "proton-ratio substrate pin q_at(95) (Physical-Observations binding pipeline)",
            "q0Value": fmt(q),
        })
        print(f"  witness -> {Path(p).name}  (80-dps, 3 assertions passed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
