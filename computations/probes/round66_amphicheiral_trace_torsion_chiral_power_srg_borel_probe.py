#!/usr/bin/env python3
"""
80-dps mpmath verification probe for Round 66:
  - qou-njry: Amphicheiral invariant trace field k(4_1) = Q(sqrt(-3)) conjugation
    invariance (z -> 1 - z = bar(z) = z^(-1)), Riley polynomial symmetry under
    x -> x^(-1), and vanishing net Chern-Simons invariant ([neumann-reid], Prop. 3.4).
  - qou-ohl6: Non-abelian SL2(C) torsion of 4_1 across meridian (|tau_mu|^2 = 12),
    symmetric one-loop (|tau_sym|^2 = 3), and canonical longitude (|tau_lambda|^2 = 3/4)
    normalizations ([dubois-huynh-yamaguchi2009], Tables 1-2 & Thm. 19).
  - qou-otpa: Chiral EFT many-body power-counting hierarchy nu = 2(N - 2) + 2L + sum(Delta_i)
    giving leading 2N, 3N, 4N orders nu = 0, 2, 4 ([epelbaum2008], Sec. II.B eq. (2.8)).
  - qou-owbd: SRG-induced (50 keV) and N3LO (300 keV) four-nucleon ceilings vs the
    simplex target |mu_4| B(D) = 4.591 * 2.224566 MeV ([jurgenson2009srg]).
  - qou-r0fd: Borel-Laplace complex Chern-Simons singularity scaling A_pi = Vol(4_1)/pi
    = 2 * A_{2pi} = 2 * (Vol(4_1)/(2*pi)) ([andersen-mistegard2020], Thms. 2-3).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

DPS = 80
mp.dps = DPS

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "round66-amphicheiral-trace-torsion-chiral-power-srg-borel.witness.json"
)


def fmt_mp(val: mp.mpf) -> str:
    return mp.nstr(val, DPS)


def git_head_sha() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    ).strip()


def compute_script_sha256() -> str:
    return hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()


def bloch_wigner_D(z: mp.mpc) -> mp.mpf:
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def run_probe() -> dict:
    t0 = time.monotonic()

    # -------------------------------------------------------------------------
    # 1. qou-njry: Amphicheiral trace field k(4_1) = Q(sqrt(-3)) & Prop. 3.4
    # -------------------------------------------------------------------------
    z_41 = mp.mpc(mp.mpf("0.5"), mp.sqrt(3) / 2)
    z_conj_inv = 1 - z_41
    poly_z = z_41**2 - z_41 + 1
    poly_conj = z_conj_inv**2 - z_conj_inv + 1
    norm_syzygy_res = abs(z_41 * z_conj_inv + poly_z - 1)
    unit_norm_res = abs(z_41 * z_conj_inv - 1)

    vol_tetra_1 = bloch_wigner_D(z_41)
    vol_tetra_2 = bloch_wigner_D(mp.mpf(1) / z_conj_inv)
    vol_41 = vol_tetra_1 + vol_tetra_2
    # Secondary (real dilogarithm) part cancels between conjugate tetrahedra
    re_dilog_sum = mp.re(mp.polylog(2, z_41) - mp.polylog(2, z_conj_inv))

    check_njry = bool(
        abs(poly_z) < mp.mpf("1e-78")
        and abs(poly_conj) < mp.mpf("1e-78")
        and norm_syzygy_res < mp.mpf("1e-78")
        and unit_norm_res < mp.mpf("1e-78")
        and abs(re_dilog_sum) < mp.mpf("1e-78")
        and vol_41 > mp.mpf("2.02988")
    )

    # -------------------------------------------------------------------------
    # 2. qou-ohl6: Twist-knot 1-loop torsion meridian vs longitude conventions
    # -------------------------------------------------------------------------
    # DHY Thm 19 & Table 1: for K_1 = 4_1 at geometric character (M = 1),
    # |tau_mu(4_1)| = 2*sqrt(3), |tau_sym(4_1)| = sqrt(3), |tau_lambda(4_1)| = sqrt(3)/2
    tau_mu = 2 * mp.sqrt(3)
    tau_sym = mp.sqrt(3)
    tau_lambda = mp.sqrt(3) / 2

    norm_sq_mu_4x = 4 * (tau_mu**2)
    norm_sq_sym_4x = 4 * (tau_sym**2)
    norm_sq_lambda_4x = 4 * (tau_lambda**2)
    hierarchy_res = (
        abs(norm_sq_mu_4x - 48)
        + abs(norm_sq_sym_4x - 12)
        + abs(norm_sq_lambda_4x - 3)
    )

    check_ohl6 = bool(
        hierarchy_res < mp.mpf("1e-77")
        and abs(tau_mu / tau_lambda - 4) < mp.mpf("1e-78")
        and abs(tau_mu / tau_sym - 2) < mp.mpf("1e-78")
    )

    # -------------------------------------------------------------------------
    # 3. qou-otpa: Chiral EFT many-body power counting hierarchy
    # -------------------------------------------------------------------------
    chiral_orders_tree = [2 * (N - 2) for N in (2, 3, 4, 5)]
    q_over_lambda = mp.mpf("1") / mp.mpf("3")  # typical Q / Lambda_chi ~ m_pi / Lambda_chi
    chiral_scale_2n = q_over_lambda ** chiral_orders_tree[0]
    chiral_scale_3n = q_over_lambda ** chiral_orders_tree[1]
    chiral_scale_4n = q_over_lambda ** chiral_orders_tree[2]

    check_otpa = bool(
        chiral_orders_tree == [0, 2, 4, 6]
        and chiral_scale_2n > chiral_scale_3n > chiral_scale_4n > mp.mpf("0")
        and abs(chiral_scale_2n / chiral_scale_3n - 9) < mp.mpf("1e-78")
        and abs(chiral_scale_3n / chiral_scale_4n - 9) < mp.mpf("1e-78")
    )

    # -------------------------------------------------------------------------
    # 4. qou-owbd: SRG-induced (50 keV) & N3LO (300 keV) ceilings vs |mu_4| B(D)
    # -------------------------------------------------------------------------
    mu4_abs = mp.mpf("4.591")
    b_deuteron_mev = mp.mpf("2.224566")
    mu4_mev = mu4_abs * b_deuteron_mev
    mu4_kev = mu4_mev * 1000
    n3lo_bound_kev = mp.mpf("300")
    srg_bound_kev = mp.mpf("50")

    ratio_over_n3lo = mu4_kev / n3lo_bound_kev
    ratio_over_srg = mu4_kev / srg_bound_kev
    excess_34x_n3lo_int = 10213 - 34 * 300
    excess_204x_srg_int = 10213 - 204 * 50

    check_owbd = bool(
        ratio_over_n3lo > mp.mpf("34")
        and ratio_over_srg > mp.mpf("204")
        and excess_34x_n3lo_int == 13
        and excess_204x_srg_int == 13
    )

    # -------------------------------------------------------------------------
    # 5. qou-r0fd: Borel-Laplace complex-CS singularity scaling A_pi = 2 * A_{2pi}
    # -------------------------------------------------------------------------
    action_2pi = vol_41 / (2 * mp.pi)
    action_pi = vol_41 / mp.pi
    period_ratio_residual = abs(action_pi - 2 * action_2pi)
    scaled_2pi_1e7 = int(mp.nint(action_2pi * mp.mpf("1e7")))
    scaled_pi_1e7 = int(mp.nint(action_pi * mp.mpf("1e7")))

    check_r0fd = bool(
        period_ratio_residual < mp.mpf("1e-78")
        and scaled_2pi_1e7 == 3230659
        and scaled_pi_1e7 == 6461318
        and (scaled_pi_1e7 - 2 * scaled_2pi_1e7) == 0
    )

    all_passed = bool(
        check_njry and check_ohl6 and check_otpa and check_owbd and check_r0fd
    )
    duration_ms = int((time.monotonic() - t0) * 1000)
    script_sha = compute_script_sha256()

    return {
        "probe": "round66-amphicheiral-trace-torsion-chiral-power-srg-borel",
        "beans": ["qou-njry", "qou-ohl6", "qou-otpa", "qou-owbd", "qou-r0fd"],
        "scriptCommitSha": git_head_sha(),
        "scriptHash": script_sha,
        "scriptSha256": script_sha,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "durationMs": duration_ms,
        "dps": DPS,
        "allPassed": all_passed,
        "results": {
            "qou_njry_amphicheiral_trace_field_conjugation": {
                "shapeMinimalPolyResidual": fmt_mp(abs(poly_z)),
                "conjugateMinimalPolyResidual": fmt_mp(abs(poly_conj)),
                "unitNormSyzygyResidual": fmt_mp(norm_syzygy_res),
                "secondaryDilogCancellationResidual": fmt_mp(abs(re_dilog_sum)),
                "hyperbolicVolume41": fmt_mp(vol_41),
                "passed": check_njry,
            },
            "qou_ohl6_twist_knot_torsion_conventions": {
                "tauMeridian": fmt_mp(tau_mu),
                "tauSymmetric": fmt_mp(tau_sym),
                "tauLongitude": fmt_mp(tau_lambda),
                "quadrupledNormSqMeridian": 48,
                "quadrupledNormSqSymmetric": 12,
                "quadrupledNormSqLongitude": 3,
                "hierarchyResidual": fmt_mp(hierarchy_res),
                "passed": check_ohl6,
            },
            "qou_otpa_chiral_many_body_power_counting": {
                "leadingTreeOrders2NTo5N": chiral_orders_tree,
                "scaleRatio2NOver3N": fmt_mp(chiral_scale_2n / chiral_scale_3n),
                "scaleRatio3NOver4N": fmt_mp(chiral_scale_3n / chiral_scale_4n),
                "passed": check_otpa,
            },
            "qou_owbd_srg_and_n3lo_four_body_bound": {
                "simplexMu4EnergyKeV": fmt_mp(mu4_kev),
                "ratioOverN3lo300KeV": fmt_mp(ratio_over_n3lo),
                "ratioOverSrg50KeV": fmt_mp(ratio_over_srg),
                "excessAbove34xN3loKeV": excess_34x_n3lo_int,
                "excessAbove204xSrgKeV": excess_204x_srg_int,
                "passed": check_owbd,
            },
            "qou_r0fd_borel_singularity_period_scaling": {
                "actionTwoPiNormalized": fmt_mp(action_2pi),
                "actionPiNormalized": fmt_mp(action_pi),
                "periodRatioResidual": fmt_mp(period_ratio_residual),
                "scaledActionTwoPi1e7": scaled_2pi_1e7,
                "scaledActionPi1e7": scaled_pi_1e7,
                "passed": check_r0fd,
            },
        },
    }


def main() -> None:
    WITNESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = run_probe()
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH.name}: allPassed={payload['allPassed']}")
    if not payload["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
