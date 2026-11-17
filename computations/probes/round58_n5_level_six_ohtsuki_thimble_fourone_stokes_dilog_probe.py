#!/usr/bin/env python3
"""
Round 58 80-dps mpmath probe for beans:
  - bwsc: n=5 level-6 WRT/modular-data fibre interpolation threshold (d((3,1,1)) = t^4 - 3t^2 + 2 of degree 4 vs [6]_q of degree 5; Vandermonde determinant & Lagrange recovery across 5 interior fold points 2*cos(k*pi/6), k=1..5)
  - thmb: Ohtsuki 2016 (DOI 10.4171/QT/83) 5_2 critical system (1-x)y = 1, x(y-1)^2 = 1 -> x^3 = (1-x)^2 <=> (1-y)^3 = y^2; complex saddle potential Im V_hat = Vol(5_2) = 2.828122088330783... vs real root control 1.7668... and trefoil Vol(3_1) = 0
  - qou-07m1: Cross-check [arxiv-2302.08363v2] eq (4.5) M_1(q), M_2(q) against fantini-wheeler2024 eq (74) g_0(q) * 2G_0(q) = M_1(q) through q^4 and quotient series M_2/g_0, M_2/M_1
  - qou-z9hf: Cross-check [hakimoglu-brown2025] Li_2(phi^{-2}) = pi^2/15 - ln^2(phi), Li_2(phi^{-1}) = pi^2/10 - (1/2)ln^2(phi), and 4_1 Habiro tail action A_0 = pi^2/5 at 80 dps
  - qou-zkkv: Habiro 2000 [habiro2000] Prop. 7.1 closed colored-Jones formula for the Borromean rings in the cyclotomic Kauffman-bracket basis, permutation symmetry in (j_1, j_2, j_3), and specialization to color 2
"""

from __future__ import annotations
import hashlib
import json
import os
import subprocess
from mpmath import mp

mp.dps = 80


def fmt(val: mp.mpf | mp.mpc) -> str:
    if isinstance(val, mp.mpc):
        return f"{mp.nstr(val.real, 40)} + {mp.nstr(val.imag, 40)}i"
    return mp.nstr(val, 40)


def check_bwsc_level_six_interpolation() -> dict:
    # Five interior fold points at level N = 6: t_k = 2 * cos(k * pi / 6), k = 1..5
    fold_points = [2 * mp.cos(mp.mpf(k) * mp.pi / 6) for k in range(1, 6)]

    # Mark-6 block polynomial d((3,1,1))(t) = t^4 - 3*t^2 + 2 (degree 4)
    def d_311(t: mp.mpf) -> mp.mpf:
        return t**4 - 3 * t**2 + 2

    # Quantum integer [6]_q(t) = t^5 - 4*t^3 + 3*t (degree 5)
    def q_int_6(t: mp.mpf) -> mp.mpf:
        return t**5 - 4 * t**3 + 3 * t

    # Lagrange interpolation of d_311 from the 5 level-6 fold points evaluated at t_test = 2
    t_test = mp.mpf(2)
    lagrange_d311_at_2 = mp.mpf(0)
    lagrange_q6_at_2 = mp.mpf(0)
    for i in range(5):
        li = mp.mpf(1)
        for j in range(5):
            if i != j:
                li *= (t_test - fold_points[j]) / (fold_points[i] - fold_points[j])
        lagrange_d311_at_2 += d_311(fold_points[i]) * li
        lagrange_q6_at_2 += q_int_6(fold_points[i]) * li

    res_d311 = abs(lagrange_d311_at_2 - d_311(t_test))
    # Because [6]_q has degree 5 and prod_{k=1}^5 (t - t_k) = t * (t^2 - 1) * (t^2 - 3) = [6]_q(t),
    # [6]_q vanishes on ALL 5 interior fold points of level 6!
    max_q6_on_level6 = max(abs(q_int_6(tp)) for tp in fold_points)
    gap_q6_at_2 = abs(lagrange_q6_at_2 - q_int_6(t_test))

    passed = bool(
        res_d311 < mp.mpf("1e-70")
        and max_q6_on_level6 < mp.mpf("1e-70")
        and abs(gap_q6_at_2 - 6) < mp.mpf("1e-70")
    )
    return {
        "bean": "bwsc",
        "description": "Level N=6 (5 interior fold points) Lagrange recovery of degree-4 block d((3,1,1)) vs vanishing of degree-5 [6]_q on level-6 fold points",
        "d311AtTwo": fmt(d_311(t_test)),
        "lagrangeD311AtTwoResidual": fmt(res_d311),
        "maxAbsQInt6OnLevel6FoldPoints": fmt(max_q6_on_level6),
        "degree5LagrangeGapAtTwo": fmt(gap_q6_at_2),
        "passed": passed,
    }


def check_thmb_ohtsuki_critical_point() -> dict:
    # Solve saddle cubic (1 - y)^3 - y^2 = 0 <=> y^3 - 2*y^2 + 3*y - 1 = 0
    # Complex root in upper half-plane: y1 ≈ 0.78492 + 1.30714i, x1 = 1 - y1
    # Use Newton iteration at 80 dps
    y = mp.mpc("0.7849201457", "1.3071412787")
    for _ in range(40):
        f = (1 - y) ** 3 - y**2
        df = -3 * (1 - y) ** 2 - 2 * y
        y = y - f / df

    x = 1 - y
    # Ohtsuki system: (1 - x) * y = 1 => y = 1 / (1 - x), and x * (y - 1)^2 = 1
    # Note in Ohtsuki's variables: x_oht satisfies x_oht^3 = (1 - x_oht)^2, so x_oht = 1 - y_corp
    # and y_oht = 1 / (1 - x_oht) = 1 / y_corp.
    x_oht = 1 - y
    y_oht = 1 / (1 - x_oht)
    sys_res_1 = abs((1 - x_oht) * y_oht - 1)
    sys_res_2 = abs(x_oht * (y_oht - 1) ** 2 - 1)
    cubic_res = abs(x_oht**3 - (1 - x_oht) ** 2)

    # Bloch-Wigner dilogarithm D(z) = Im(Li_2(z)) + arg(1 - z) * ln|z|
    def bloch_wigner(z: mp.mpc) -> mp.mpf:
        return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))

    vol_5_2 = 3 * bloch_wigner(y)
    vol_5_2_ref = mp.mpf(
        "2.8281220883307831627638988092766349427709813173006494770435203272588025483"
    )
    vol_diff = abs(vol_5_2 - vol_5_2_ref)

    # Real root control: y_real in (0, 1) has Bloch-Wigner volume 0
    y_real = mp.mpf("0.4301597090")
    for _ in range(40):
        f = (1 - y_real) ** 3 - y_real**2
        df = -3 * (1 - y_real) ** 2 - 2 * y_real
        y_real = y_real - f / df
    real_cubic_res = abs((1 - y_real) ** 3 - y_real**2)

    passed = bool(
        sys_res_1 < mp.mpf("1e-75")
        and sys_res_2 < mp.mpf("1e-75")
        and cubic_res < mp.mpf("1e-75")
        and vol_diff < mp.mpf("1e-70")
        and real_cubic_res < mp.mpf("1e-75")
    )
    return {
        "bean": "thmb",
        "description": "Ohtsuki 2016 5_2 critical system elimination x^3 = (1-x)^2, complex saddle volume 3*D(y_1) = Vol(5_2), and real root control",
        "saddleRootY1": fmt(y),
        "ohtsukiSystemResidual1": fmt(sys_res_1),
        "ohtsukiSystemResidual2": fmt(sys_res_2),
        "ohtsukiCubicResidual": fmt(cubic_res),
        "volume52Computed": fmt(vol_5_2),
        "volume52ReferenceDiff": fmt(vol_diff),
        "realRootControlY0": fmt(y_real),
        "realRootCubicResidual": fmt(real_cubic_res),
        "passed": passed,
    }


def check_qou_07m1_fourone_stokes_series() -> dict:
    g0 = [1, -1, -2, -2, -2]
    two_g0 = [1, -7, -14, -8, -2]
    m1_pub = [1, -8, -9, 18, 46]
    m2_pub = [0, -9, -3, 39, 69]

    def cauchy_trunc(a: list[int], b: list[int], deg: int = 4) -> list[int]:
        return [
            sum(a[k] * b[n - k] for k in range(n + 1))
            for n in range(deg + 1)
        ]

    prod_g0_2g0 = cauchy_trunc(g0, two_g0, 4)
    m2_over_g0 = [0, -9, -12, 9, 36]
    m2_over_m1 = [0, -9, -75, -642, -5580]

    rec_m2_from_g0 = cauchy_trunc(g0, m2_over_g0, 4)
    rec_m2_from_m1 = cauchy_trunc(m1_pub, m2_over_m1, 4)

    # Evaluate at q = 1/100 in 80-dps mpmath
    q_val = mp.mpf(1) / mp.mpf(100)
    g0_val = sum(mp.mpf(c) * (q_val**k) for k, c in enumerate(g0))
    two_g0_val = sum(mp.mpf(c) * (q_val**k) for k, c in enumerate(two_g0))
    m1_val = sum(mp.mpf(c) * (q_val**k) for k, c in enumerate(m1_pub))
    trunc_err = abs(g0_val * two_g0_val - m1_val)

    passed = bool(
        prod_g0_2g0 == m1_pub
        and rec_m2_from_g0 == m2_pub
        and rec_m2_from_m1 == m2_pub
        and trunc_err < mp.mpf("1e-8")
    )
    return {
        "bean": "qou-07m1",
        "description": "Cross-check 2302.08363v2 eq (4.5) M_1 = g_0 * 2G_0 through q^4 and M_2 quotient series against fantini-wheeler2024 eq (74)",
        "productG0Times2G0": [str(c) for c in prod_g0_2g0],
        "publishedM1": [str(c) for c in m1_pub],
        "quotientM2OverG0": [str(c) for c in m2_over_g0],
        "quotientM2OverM1": [str(c) for c in m2_over_m1],
        "qOneHundredthTruncationResidual": fmt(trunc_err),
        "passed": passed,
    }


def check_qou_z9hf_hakimoglu_brown_dilog() -> dict:
    phi = (1 + mp.sqrt(5)) / 2
    phi_inv = 1 / phi
    phi_inv_sq = 1 / (phi**2)

    li2_phi_inv_sq = mp.polylog(2, phi_inv_sq)
    rhs_phi_inv_sq = (mp.pi**2) / 15 - (mp.log(phi) ** 2)
    res_phi_inv_sq = abs(li2_phi_inv_sq - rhs_phi_inv_sq)

    li2_phi_inv = mp.polylog(2, phi_inv)
    rhs_phi_inv = (mp.pi**2) / 10 - (mp.log(phi) ** 2)
    res_phi_inv = abs(li2_phi_inv - rhs_phi_inv)

    # Resulting 4_1 tail action A_0 = pi^2 / 5 = 3 * (Li_2(phi^{-2}) + ln^2(phi)) = 2 * (Li_2(phi^{-1}) + ln^2(phi))
    a0_exact = (mp.pi**2) / 5
    a0_from_phi_inv_sq = 3 * (li2_phi_inv_sq + mp.log(phi) ** 2)
    a0_from_phi_inv = 2 * (li2_phi_inv + mp.log(phi) ** 2)
    res_a0_1 = abs(a0_exact - a0_from_phi_inv_sq)
    res_a0_2 = abs(a0_exact - a0_from_phi_inv)

    passed = bool(
        res_phi_inv_sq < mp.mpf("1e-75")
        and res_phi_inv < mp.mpf("1e-75")
        and res_a0_1 < mp.mpf("1e-75")
        and res_a0_2 < mp.mpf("1e-75")
    )
    return {
        "bean": "qou-z9hf",
        "description": "Cross-check [hakimoglu-brown2025] Li_2(phi^{-2}) = pi^2/15 - ln^2(phi) and resulting 4_1 tail action A_0 = pi^2/5 at 80 dps",
        "li2PhiInvSq": fmt(li2_phi_inv_sq),
        "li2PhiInvSqResidual": fmt(res_phi_inv_sq),
        "li2PhiInvResidual": fmt(res_phi_inv),
        "tailActionA0": fmt(a0_exact),
        "tailActionA0FromPhiInvSqResidual": fmt(res_a0_1),
        "tailActionA0FromPhiInvResidual": fmt(res_a0_2),
        "passed": passed,
    }


def check_qou_zkkv_habiro_borromean_prop71() -> dict:
    # Habiro [habiro2000] Prop. 7.1 closed formula for the colored Jones polynomial of the Borromean rings:
    # J_{j1, j2, j3}(B; q) = sum_{k=0}^{min(j1, j2, j3) - 1} (-1)^k * (q^{1/2} - q^{-1/2})^{2k}
    #   * prod_{i=1}^3 ([j_i + k]_q ... [j_i - k]_q / [j_i]_q)
    def q_int(n: int, q: mp.mpf) -> mp.mpf:
        if n == 0:
            return mp.mpf(0)
        s = mp.sqrt(q)
        return (s**n - s ** (-n)) / (s - 1 / s)

    def habiro_factor(j: int, k: int, q: mp.mpf) -> mp.mpf:
        prod_val = mp.mpf(1)
        for m in range(1, k + 1):
            prod_val *= q_int(j + m, q) * q_int(j - m, q)
        return prod_val

    def borromean_colored_jones(j1: int, j2: int, j3: int, q: mp.mpf) -> mp.mpf:
        cutoff = min(j1, j2, j3)
        s = mp.sqrt(q)
        z = (s - 1 / s) ** 2
        total = mp.mpf(0)
        for k in range(cutoff):
            term = ((-1) ** k) * (z**k)
            term *= (
                habiro_factor(j1, k, q)
                * habiro_factor(j2, k, q)
                * habiro_factor(j3, k, q)
            )
            total += term
        return total

    q_test = mp.exp(mp.mpf("0.17"))
    # Verify total S_3 permutation symmetry for distinct colors (2, 3, 4)
    val_234 = borromean_colored_jones(2, 3, 4, q_test)
    val_324 = borromean_colored_jones(3, 2, 4, q_test)
    val_432 = borromean_colored_jones(4, 3, 2, q_test)
    sym_res = max(abs(val_234 - val_324), abs(val_234 - val_432))

    # Unknot/trivial color j=1 forces J_{1, j2, j3} = 1 identically
    val_134 = borromean_colored_jones(1, 3, 4, q_test)
    trivial_res = abs(val_134 - 1)

    # Fundamental color (2, 2, 2): k=0 gives 1, k=1 gives -(q^{1/2} - q^{-1/2})^2 * ([3]_q [1]_q)^3 = -(q - 2 + q^{-1}) * (q + 1 + q^{-1})^3
    val_222 = borromean_colored_jones(2, 2, 2, q_test)
    direct_222 = 1 - (q_test - 2 + 1 / q_test) * ((q_test + 1 + 1 / q_test) ** 3)
    res_222 = abs(val_222 - direct_222)

    passed = bool(
        sym_res < mp.mpf("1e-75")
        and trivial_res < mp.mpf("1e-75")
        and res_222 < mp.mpf("1e-70")
    )
    return {
        "bean": "qou-zkkv",
        "description": "Habiro [habiro2000] Prop. 7.1 Borromean colored-Jones closed formula: S_3 colour symmetry, trivial-colour normalization, and (2,2,2) cyclotomic identity",
        "valueJ234AtExp017": fmt(val_234),
        "permutationSymmetryResidual": fmt(sym_res),
        "trivialColorOneResidual": fmt(trivial_res),
        "color222FormulaResidual": fmt(res_222),
        "passed": passed,
    }


def main() -> None:
    script_rel = "computations/probes/round58_n5_level_six_ohtsuki_thimble_fourone_stokes_dilog_probe.py"
    witness_rel = "computations/probes/round58-n5-level-six-ohtsuki-thimble-fourone-stokes-dilog.witness.json"

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    script_abs = os.path.join(repo_root, script_rel)
    witness_abs = os.path.join(repo_root, witness_rel)

    with open(script_abs, "rb") as f:
        script_sha256 = hashlib.sha256(f.read()).hexdigest()

    commit_sha = (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
        .decode("utf-8")
        .strip()
    )

    checks = [
        check_bwsc_level_six_interpolation(),
        check_thmb_ohtsuki_critical_point(),
        check_qou_07m1_fourone_stokes_series(),
        check_qou_z9hf_hakimoglu_brown_dilog(),
        check_qou_zkkv_habiro_borromean_prop71(),
    ]

    all_passed = all(c["passed"] for c in checks)
    if not all_passed:
        raise RuntimeError("One or more Round 58 probe checks failed!")

    payload = {
        "probe": "round58-n5-level-six-ohtsuki-thimble-fourone-stokes-dilog",
        "scriptPath": script_rel,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "scriptCommitSha": commit_sha,
        "precisionDps": "80",
        "beans": ["bwsc", "thmb", "qou-07m1", "qou-z9hf", "qou-zkkv"],
        "leanModules": [
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/N5LevelSixRootThresholdAndThreeLinkTriad.lean",
            "folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSaddleHessianAndFourOneStokesCrossCheck.lean",
        ],
        "allPassed": all_passed,
        "checks": checks,
    }

    with open(witness_abs, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")

    print(f"Wrote {witness_rel} (allPassed={all_passed}, scriptCommitSha={commit_sha})")


if __name__ == "__main__":
    main()
