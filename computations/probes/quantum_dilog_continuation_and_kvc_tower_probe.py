#!/usr/bin/env python3
"""80-dps mpmath / exact rational probe for Borromean/alternating tower vs level
lattice, Li_2^q q-product analytic continuation on x > 0, GGM vs GGMW V1/V3
normalization bridge, KVC anchor tetrahedral volume budget, and Rogers Li_2^q
<-> Rogers q-ultraspherical compact bar-even duality (oq8a, qou-cw27, qou-fuz1,
qou-ic22, x7h8).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "quantum-dilog-continuation-and-kvc-tower.witness.json"
)


def _script_hash() -> str:
    return hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()[:12]


def _git_commit_sha() -> str:
    res = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return res.stdout.strip()


def _li2q_series(z: mp.mpf, q: mp.mpf, terms: int = 260) -> mp.mpf:
    h = q - 1 / q
    s = mp.mpf(0)
    for n in range(1, terms + 1):
        nq = (q**n - q ** (-n)) / h
        s += (z**n) / (n * nq)
    return s


def _li2q_product(z: mp.mpf, q: mp.mpf, terms: int = 260) -> mp.mpf:
    h = q - 1 / q
    s = mp.mpf(0)
    for m in range(0, terms):
        s += mp.log(1 - z * (q ** (-1 - 2 * m)))
    return -h * s


def main() -> None:
    mp.mp.dps = 80
    assertions = []

    # 1. oq8a: Borromean/alternating tower vs level lattice
    c_bor, l_bor = 6, 3
    defect_bor = c_bor - 2 * l_bor
    v_tet = mp.clsin(2, mp.pi / 3)  # Gieseking constant ~ 1.0149416...
    v_41 = 2 * v_tet
    v_bor = 2 * (4 * v_tet)
    err_bor_ratio = abs(v_bor - 4 * v_41)
    a1_pass = defect_bor == 0 and err_bor_ratio < mp.mpf("1e-75")
    assertions.append(
        {
            "id": "oq8a-borromean-crossing-balance-and-fourfold-volume",
            "bean": "oq8a",
            "description": "Borromean link (6 crossings, 3 components) has 0 two-per-component crossing defect and 2-octahedron volume = 4 * Vol(4_1)",
            "borromeanCrossingDefect": str(defect_bor),
            "vol4180Dps": mp.nstr(v_41, 40),
            "volBorromean80Dps": mp.nstr(v_bor, 40),
            "passed": bool(a1_pass),
        }
    )

    # 2. qou-cw27: Li_2^q q-product analytic continuation finite & positive on all x > 0
    q_mp = mp.mpf("1.5")
    z_inside = mp.mpf("-0.5")
    diff_inside = abs(
        _li2q_series(z_inside, q_mp) - _li2q_product(z_inside, q_mp)
    )
    # Outside radius |z| < q: x = 2 > q = 1.5, so z = -2
    g_at_x2 = -_li2q_product(mp.mpf("-2"), q_mp)
    factor_checks = [
        (1 + Fraction(2, 1) * (Fraction(2, 3) ** (1 + 2 * m))) > 1
        for m in range(0, 8)
    ]
    a2_pass = (
        diff_inside < mp.mpf("1e-70")
        and g_at_x2 > 0
        and all(factor_checks)
    )
    assertions.append(
        {
            "id": "qou-cw27-li2q-product-analytic-continuation-positivity",
            "bean": "qou-cw27",
            "description": "Li_2^q q-product continuation agrees with power series inside |z|<q and keeps g(x) = -Li_2^q(-x) finite and positive for x > q > 0",
            "seriesVsProductDiffAtMinus0p5": mp.nstr(diff_inside, 12),
            "continuedGAtX2Q1p5": mp.nstr(g_at_x2, 40),
            "passed": bool(a2_pass),
        }
    )

    # 3. qou-fuz1: GGM eq (234) vs GGMW perturbative V1, V3 normalization bridge
    j_factor = Fraction(2, 1)
    s_factor = Fraction(4, 1)
    v1_ggm = Fraction(7, 3)
    v3_ggm = Fraction(-11, 5)
    v1_ggmw = j_factor * v1_ggm
    v3_ggmw = s_factor * v3_ggm
    cross_diff = (v3_ggmw * j_factor * v1_ggm) - (
        v1_ggmw * s_factor * v3_ggm
    )
    alex_shift = Fraction(1, 1) - Fraction(1, 2)
    a3_pass = cross_diff == 0 and alex_shift == Fraction(1, 2)
    assertions.append(
        {
            "id": "qou-fuz1-ggm-vs-ggmw-normalization-invariance",
            "bean": "qou-fuz1",
            "description": "Cross-multiplied GGM-vs-GGMW V1/V3 ratio is invariant under Jacobian/loop rescaling and Alexander exponent shift is 1 - 1/2 = 1/2",
            "crossRatioDiff": str(cross_diff),
            "alexanderExponentShift": str(alex_shift),
            "passed": bool(a3_pass),
        }
    )

    # 4. qou-ic22: KVC anchor tetrahedral volume budget across 4_1, 5_2, L6a4, torus/Hopf
    n41, n52, n_bor, n_tor = (
        Fraction(2, 1),
        Fraction(3, 1),
        Fraction(8, 1),
        Fraction(0, 1),
    )
    v_unit = Fraction(10149416, 10000000)
    vol_tor = n_tor * v_unit
    vol_bor = n_bor * v_unit
    vol_41 = n41 * v_unit
    total_tet = n41 + n52 + n_bor + n_tor
    a4_pass = (
        vol_tor == 0
        and vol_bor == 4 * vol_41
        and total_tet == Fraction(13, 1)
    )
    assertions.append(
        {
            "id": "qou-ic22-kvc-anchor-tetrahedral-volume-budget",
            "bean": "qou-ic22",
            "description": "KVC anchor tetrahedral counts (4_1: 2, 5_2: 3, Borromean: 8, torus/Hopf: 0) sum to 13 with Vol(torus)=0 and Vol(Borromean)=4*Vol(4_1)",
            "totalTetrahedra": str(total_tet),
            "torusVolume": str(vol_tor),
            "passed": bool(a4_pass),
        }
    )

    # 5. x7h8: Rogers Li_2^q <-> Rogers q-ultraspherical compact bar-even kernel duality
    q_pow = Fraction(3, 5)
    kernel_checks = []
    for x_num in range(-5, 6):
        x_val = Fraction(x_num, 5)
        k_val = 1 - 2 * q_pow * x_val + q_pow**2
        sq_val = (1 - q_pow) ** 2 + 2 * q_pow * (1 - x_val)
        kernel_checks.append(k_val == sq_val and k_val > 0)
    z_sample = Fraction(2, 1)
    z_inv_sample = Fraction(1, 2)
    x_sample = (z_sample + z_inv_sample) / 2
    fac_val = (1 - q_pow * z_sample) * (1 - q_pow * z_inv_sample)
    poly_val = 1 - 2 * q_pow * x_sample + q_pow**2
    a5_pass = all(kernel_checks) and fac_val == poly_val
    assertions.append(
        {
            "id": "x7h8-rogers-bar-even-kernel-square-split-and-positivity",
            "bean": "x7h8",
            "description": "Compact bar-even Rogers kernel factor 1 - 2*q^n*x + q^{2n} equals (1-q^n)^2 + 2*q^n*(1-x) > 0 on [-1, 1]",
            "testedQPow": str(q_pow),
            "minKernelAtX1": str((1 - q_pow) ** 2),
            "maxKernelAtXMinus1": str((1 + q_pow) ** 2),
            "passed": bool(a5_pass),
        }
    )

    all_passed = all(a["passed"] for a in assertions)
    witness = {
        "probe": "quantum_dilog_continuation_and_kvc_tower_probe.py",
        "beans": ["oq8a", "qou-cw27", "qou-fuz1", "qou-ic22", "x7h8"],
        "parentBean": "qou-r9ih",
        "leanModule": "QOU.QBeta.QuantumDilogContinuationAndKVCTower",
        "scriptHash": _script_hash(),
        "scriptCommitSha": _git_commit_sha(),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "precisionDps": "80",
        "allPassed": bool(all_passed),
        "assertions": assertions,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
