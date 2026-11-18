#!/usr/bin/env python3
"""
80-dps mpmath numerical falsification & verification probe for:
- qou-lyq2: Rigid monoidal structural gap invariance under dual rescaling
- qou-pbjv: Three-strand braided representation and quadratic-braid relations
- qou-e6db: Braid closure degree window width invariance and smoothing parity
- qou-su6h: Cumulative transposition elements, commutativity, and central symmetric sum
- qou-svnb: Bilinear trace-form cyclicity from off-diagonal pairing symmetry

No raw float64 arithmetic is used; all real calculations are performed via mpmath at 80 decimal digits.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 80


def _git_commit_sha(repo_root: Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(repo_root), text=True
        ).strip()
        return out
    except Exception:
        return "0" * 40


def _script_sha256(script_path: Path) -> str:
    return hashlib.sha256(script_path.read_bytes()).hexdigest()


def _mul2(
    a: tuple[mpf, mpf, mpf, mpf], b: tuple[mpf, mpf, mpf, mpf]
) -> tuple[mpf, mpf, mpf, mpf]:
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def _add2(
    a: tuple[mpf, mpf, mpf, mpf], b: tuple[mpf, mpf, mpf, mpf]
) -> tuple[mpf, mpf, mpf, mpf]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def _smul2(c: mpf, a: tuple[mpf, mpf, mpf, mpf]) -> tuple[mpf, mpf, mpf, mpf]:
    return (c * a[0], c * a[1], c * a[2], c * a[3])


def _max_diff2(
    a: tuple[mpf, mpf, mpf, mpf], b: tuple[mpf, mpf, mpf, mpf]
) -> mpf:
    return max(abs(a[i] - b[i]) for i in range(4))


def run_probe() -> dict:
    mp.dps = 80
    tol = mpf("1e-70")
    results = []

    q_val = mpf("1.1099785827513808")

    # 1. qou-lyq2: Rigid monoidal structural gap invariance under dual rescaling
    w1 = mpf("5") / mpf("7")
    w2 = mpf("11") / mpf("13")
    lam1 = mpf("17") / mpf("19")
    lam2 = mpf("3") / mpf("19")
    s_scale = mpf("23") / mpf("17")

    gap_orig = (w1 * lam1) * w2 - (w2 * lam2) * w1
    gap_factored = w1 * w2 * (lam1 - lam2)
    gap_rescaled = ((s_scale * w1) * lam1) * (s_scale * w2) - ((s_scale * w2) * lam2) * (s_scale * w1)
    gap_degen = (w1 * lam1) * w2 - (w2 * lam1) * w1
    err_lyq2 = max(
        abs(gap_orig - gap_factored),
        abs(gap_rescaled - (s_scale * s_scale) * gap_orig),
        abs(gap_degen),
    )
    qou_lyq2_ok = err_lyq2 <= tol

    results.append(
        {
            "beanId": "qou-lyq2",
            "claim": "Rigid structural gap cross-residual factors as w1 w2 (lam1 - lam2), scales by s^2 under dual rescaling, and vanishes at lam1 = lam2",
            "maxResidual": mp.nstr(err_lyq2, 25),
            "passed": bool(qou_lyq2_ok),
        }
    )

    # 2. qou-pbjv: Three-strand braided representation and quadratic-braid relations
    id2 = (mpf("1"), mpf("0"), mpf("0"), mpf("1"))
    t1 = (q_val, mpf("1"), mpf("0"), -mpf("1"))
    t2 = (-mpf("1"), mpf("0"), q_val, q_val)

    t1_sq = _mul2(t1, t1)
    t1_rhs = _add2(_smul2(q_val - mpf("1"), t1), _smul2(q_val, id2))
    t2_sq = _mul2(t2, t2)
    t2_rhs = _add2(_smul2(q_val - mpf("1"), t2), _smul2(q_val, id2))
    t121 = _mul2(_mul2(t1, t2), t1)
    t212 = _mul2(_mul2(t2, t1), t2)
    expected_121 = (mpf("0"), -q_val, -(q_val * q_val), mpf("0"))
    err_pbjv = max(
        _max_diff2(t1_sq, t1_rhs),
        _max_diff2(t2_sq, t2_rhs),
        _max_diff2(t121, t212),
        _max_diff2(t121, expected_121),
    )
    qou_pbjv_ok = err_pbjv <= tol

    results.append(
        {
            "beanId": "qou-pbjv",
            "claim": "2D 3-strand representation satisfies quadratic relations T_i^2 = (q-1)T_i + q I_2 and braid relation T1 T2 T1 = T2 T1 T2",
            "maxResidual": mp.nstr(err_pbjv, 25),
            "passed": bool(qou_pbjv_ok),
        }
    )

    # 3. qou-e6db: Braid closure degree window width invariance and smoothing parity
    n_strands = mpf("4")
    e_writhe = mpf("5")
    c_comp = mpf("2")
    low_orig = e_writhe - (n_strands - c_comp)
    high_orig = e_writhe + (n_strands - c_comp)
    low_sw = (e_writhe - mpf("2")) - (n_strands - c_comp)
    high_sw = (e_writhe - mpf("2")) + (n_strands - c_comp)
    low_sm_plus = (e_writhe - mpf("1")) - (n_strands - (c_comp + mpf("1")))
    low_sm_minus = (e_writhe - mpf("1")) - (n_strands - (c_comp - mpf("1")))
    err_e6db = max(
        abs(low_sw - (low_orig - mpf("2"))),
        abs((high_sw - low_sw) - (high_orig - low_orig)),
        abs(low_sm_plus - low_orig),
        abs(low_sm_minus - (low_orig - mpf("2"))),
    )
    qou_e6db_ok = err_e6db <= tol

    results.append(
        {
            "beanId": "qou-e6db",
            "claim": "Crossing switch shifts degree window by -2 with invariant width 2(n-c), and smoothing shifts e-(n-c) by 0 or -2 (preserving parity)",
            "maxResidual": mp.nstr(err_e6db, 25),
            "passed": bool(qou_e6db_ok),
        }
    )

    # 4. qou-su6h: Cumulative transposition elements, commutativity, and central symmetric sum
    l2 = _smul2(q_val, t1)
    l3 = _add2(_smul2(q_val, t2), t121)
    l_sum = _add2(l2, l3)
    l_prod23 = _mul2(l2, l3)
    l_prod32 = _mul2(l3, l2)
    err_su6h = max(
        _max_diff2(l_sum, _smul2(q_val * q_val - q_val, id2)),
        _max_diff2(l_prod23, _smul2(-(q_val**3), id2)),
        _max_diff2(l_prod23, l_prod32),
    )
    qou_su6h_ok = err_su6h <= tol

    results.append(
        {
            "beanId": "qou-su6h",
            "claim": "Cumulative transposition elements L2 and L3 commute and have central scalar symmetric sum (q^2-q)I_2 and product -q^3 I_2",
            "maxResidual": mp.nstr(err_su6h, 25),
            "passed": bool(qou_su6h_ok),
        }
    )

    # 5. qou-svnb: Bilinear trace-form cyclicity from off-diagonal pairing symmetry
    g11, g12, g21, g22 = mpf("3") / mpf("5"), mpf("7") / mpf("11"), mpf("9") / mpf("13"), mpf("-4") / mpf("7")
    u1, u2 = mpf("5") / mpf("9"), mpf("-2") / mpf("7")
    v1, v2 = mpf("11") / mpf("15"), mpf("4") / mpf("11")
    b_uv = u1 * v1 * g11 + u1 * v2 * g12 + u2 * v1 * g21 + u2 * v2 * g22
    b_vu = v1 * u1 * g11 + v1 * u2 * g12 + v2 * u1 * g21 + v2 * u2 * g22
    comm_expected = (u1 * v2 - u2 * v1) * (g12 - g21)
    b_sym_uv = u1 * v1 * g11 + u1 * v2 * g12 + u2 * v1 * g12 + u2 * v2 * g22
    b_sym_vu = v1 * u1 * g11 + v1 * u2 * g12 + v2 * u1 * g12 + v2 * u2 * g22
    err_svnb = max(
        abs((b_uv - b_vu) - comm_expected),
        abs(b_sym_uv - b_sym_vu),
    )
    qou_svnb_ok = err_svnb <= tol

    results.append(
        {
            "beanId": "qou-svnb",
            "claim": "Bilinear trace form satisfies B(u,v)-B(v,u) = (u1 v2 - u2 v1)(g12 - g21) and is cyclic when g12 = g21",
            "maxResidual": mp.nstr(err_svnb, 25),
            "passed": bool(qou_svnb_ok),
        }
    )

    all_passed = all(r["passed"] for r in results)
    repo_root = Path(__file__).resolve().parents[2]
    script_path = Path(__file__).resolve()
    full_sha256 = _script_sha256(script_path)

    witness = {
        "probe": "rigid_gap_braided_three_strand_closure_window_cumulative_commutant_bilinear_cyclicity_probe",
        "beans": ["qou-lyq2", "qou-pbjv", "qou-e6db", "qou-su6h", "qou-svnb"],
        "parents": ["qou-o9ge", "qou-0cyu", "qou-1oif", "qou-59vq", "qou-rtxm"],
        "leanModule": "QOU.Foundations.RigidGapBraidedThreeStrandClosureWindowCumulativeCommutantBilinearCyclicity",
        "precisionDps": 80,
        "scriptPath": "computations/probes/rigid_gap_braided_three_strand_closure_window_cumulative_commutant_bilinear_cyclicity_probe.py",
        "scriptHash": full_sha256,
        "scriptSha256": full_sha256,
        "scriptCommitSha": _git_commit_sha(repo_root),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": bool(all_passed),
        "results": results,
    }
    return witness


def main() -> None:
    witness = run_probe()
    out_path = Path(__file__).with_name(
        "rigid-gap-braided-three-strand-closure-window-cumulative-commutant-bilinear-cyclicity.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={witness['allPassed']}, scriptHash={witness['scriptHash']})")
    if not witness["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
