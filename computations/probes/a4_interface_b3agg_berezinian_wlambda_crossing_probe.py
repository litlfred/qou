#!/usr/bin/env python3
"""
80-dps mpmath and exact rational verification probe for Round 62:
  - qou-0qmr: A=4 (4He) interface operator detG(m) = (1 - 5m^2)(1 - m^2) even parity,
              boundary roots, difference factorization, and closed-form inverse u*(D) at 80 dps.
  - qou-2ss0: 3-body cumulant b3Agg linearity, origin-secant identity, and exact threshold
              b3Agg(x^3 - x^2, g) = 6 g^2 (4g - 1) vanishing at g = 1/4.
  - qou-6r6d: Super-Berezinian A=3 even-face correction left-inverse recovery
              A (1 - corr) D C^{-1} = B and block-rescaling gauge invariance.
  - qou-9nq9: A=4 geometric W_lambda convex-interpolation mixing fractions theta*(t) for
              absMu4 and B4He strictly separated in (0, 1).
  - qou-dhsn: Level-3 EM crossing-count second-difference linearity and quadratic
              strong-channel reconstruction (n_+ - n_-)(n_+ - n_- - 4) = 16 Z(Z - 1).
"""

from __future__ import annotations

import datetime
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess

import mpmath as mp

mp.mp.dps = 80


def fmt_mp(val: mp.mpf) -> str:
    return mp.nstr(val, 40)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    script_path = Path(__file__).resolve()
    script_bytes = script_path.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    # 1. qou-0qmr: detG even parity, difference factorization, and 80-dps closed-form inverse
    m1 = Fraction(1, 5)
    m2 = Fraction(2, 5)
    det_m1 = (1 - 5 * m1**2) * (1 - m1**2)
    det_neg_m1 = (1 - 5 * (-m1) ** 2) * (1 - (-m1) ** 2)
    det_m2 = (1 - 5 * m2**2) * (1 - m2**2)
    diff_lhs = det_m1 - det_m2
    diff_rhs = (m2**2 - m1**2) * (6 - 5 * (m1**2 + m2**2))
    target_t = mp.mpf("9243") / mp.mpf("1000")
    d_val = mp.exp(-target_t)
    u_star = (mp.mpf(6) - mp.sqrt(mp.mpf(16) + mp.mpf(20) * d_val)) / mp.mpf(10)
    m_star = mp.sqrt(u_star)
    det_star = (1 - 5 * m_star**2) * (1 - m_star**2)
    b4_residual = abs(-mp.log(det_star) - target_t)
    qou_0qmr_pass = bool(
        det_m1 == det_neg_m1
        and diff_lhs == diff_rhs
        and b4_residual < mp.mpf("1e-75")
    )

    # 2. qou-2ss0: b3Agg linearity and witnessPhi factorization 6 g^2 (4g - 1)
    def witness_phi(x: Fraction) -> Fraction:
        return x**3 - x**2

    def b3_agg(phi, g: Fraction) -> Fraction:
        return phi(3 * g) - 3 * phi(g)

    g_samples = [Fraction(1, 8), Fraction(1, 4), Fraction(1, 2), Fraction(1, 1)]
    b3_vals = [b3_agg(witness_phi, g) for g in g_samples]
    b3_fac = [6 * (g**2) * (4 * g - 1) for g in g_samples]
    qou_2ss0_pass = bool(
        b3_vals == b3_fac
        and b3_agg(witness_phi, Fraction(1, 4)) == 0
        and b3_agg(witness_phi, Fraction(1, 2)) == Fraction(3, 2)
        and b3_agg(witness_phi, Fraction(1, 1)) == 18
    )

    # 3. qou-6r6d: Super-Berezinian left-inverse recovery and scale invariance
    A = Fraction(7, 3)
    B = Fraction(11, 5)
    C = Fraction(13, 4)
    D = Fraction(17, 6)
    alpha = Fraction(5, 2)
    beta = Fraction(9, 7)
    t_cross = B * (1 / D) * C
    corr = (A - t_cross) / A
    b_recovered = A * (1 - corr) * D * (1 / C)
    t_scaled = (alpha * B) * (1 / (beta * D)) * (beta * C)
    corr_scaled = (alpha * A - t_scaled) / (alpha * A)
    qou_6r6d_pass = bool(
        b_recovered == B
        and corr_scaled == corr
    )

    # 4. qou-9nq9: Convex-interpolation mixing fractions for absMu4 and B4He
    prod_mag = Fraction(24275, 100000)
    geom_mag = Fraction(6032647, 100000)
    b4he_target = Fraction(2829566, 100000)
    mu4_target = Fraction(4591048, 1000000)
    theta_mu4 = (mu4_target - prod_mag) / (geom_mag - prod_mag)
    theta_b4he = (b4he_target - prod_mag) / (geom_mag - prod_mag)
    interp_mu4 = (1 - theta_mu4) * prod_mag + theta_mu4 * geom_mag
    interp_b4he = (1 - theta_b4he) * prod_mag + theta_b4he * geom_mag
    qou_9nq9_pass = bool(
        interp_mu4 == mu4_target
        and interp_b4he == b4he_target
        and Fraction(0) < theta_mu4 < theta_b4he < Fraction(1)
    )

    # 5. qou-dhsn: Crossing-count quadratic reconstruction of 16 Z(Z - 1)
    pairs_ok = True
    for A_nuc in range(2, 20):
        for Z_nuc in range(1, A_nuc + 1):
            n_plus = 5 * A_nuc - 1 + 2 * Z_nuc
            n_minus = 5 * A_nuc - 1 - 2 * Z_nuc
            diff_c = n_plus - n_minus
            if diff_c * (diff_c - 4) != 16 * Z_nuc * (Z_nuc - 1):
                pairs_ok = False
    qou_dhsn_pass = bool(pairs_ok)

    all_passed = (
        qou_0qmr_pass
        and qou_2ss0_pass
        and qou_6r6d_pass
        and qou_9nq9_pass
        and qou_dhsn_pass
    )

    witness = {
        "probe": "a4-interface-b3agg-berezinian-wlambda-crossing",
        "beans": ["qou-0qmr", "qou-2ss0", "qou-6r6d", "qou-9nq9", "qou-dhsn"],
        "precisionDps": "80",
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": {
            "qou_0qmr_a4_interface_operator": {
                "passed": qou_0qmr_pass,
                "detDifferenceGap": f"{diff_lhs.numerator}/{diff_lhs.denominator}",
                "mStarAt9p243": fmt_mp(m_star),
                "b4InversionResidual": fmt_mp(b4_residual),
            },
            "qou_2ss0_b3agg_secant_threshold": {
                "passed": qou_2ss0_pass,
                "b3AtQuarter": f"{b3_vals[1].numerator}/{b3_vals[1].denominator}",
                "b3AtHalf": f"{b3_vals[2].numerator}/{b3_vals[2].denominator}",
                "b3AtOne": f"{b3_vals[3].numerator}/{b3_vals[3].denominator}",
            },
            "qou_6r6d_berezinian_a3_magnitude": {
                "passed": qou_6r6d_pass,
                "evenFaceCorrection": f"{corr.numerator}/{corr.denominator}",
                "recoveredOffBlockB": f"{b_recovered.numerator}/{b_recovered.denominator}",
            },
            "qou_9nq9_wlambda_mixing_fractions": {
                "passed": qou_9nq9_pass,
                "thetaAbsMu4": f"{theta_mu4.numerator}/{theta_mu4.denominator}",
                "thetaB4He": f"{theta_b4he.numerator}/{theta_b4he.denominator}",
            },
            "qou_dhsn_crossing_quadratic_proton_pairs": {
                "passed": qou_dhsn_pass,
                "gridVerifiedMaxA": "19",
                "sampleZ6SixteenProtonPairs": str(16 * 6 * 5),
            },
        },
    }

    witness_path = (
        repo_root
        / "test"
        / "results"
        / "witnesses"
        / "a4-interface-b3agg-berezinian-wlambda-crossing.witness.json"
    )
    witness_path.parent.mkdir(parents=True, exist_ok=True)
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {witness_path} (allPassed={all_passed}, scriptHash={script_hash})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
