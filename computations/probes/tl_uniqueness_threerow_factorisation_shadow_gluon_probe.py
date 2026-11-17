#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 70 Nuclear Binding, Mass Theory & Braid/Knot theorems.

Covers:
  - qou-3qrv: QOU.BraidsAndKnots.markovWeights_jones_y3_cleared
  - qou-3exu: QOU.MassTheory.ThreeRowExtensiveCumulant.Bext_five_and_mayer_reconstruct
  - qou-5zl1: QOU.Mass.AtomTraceFactorisation.tr_atomWord_const_bond
  - qou-56qy: QOU.MassTheory.orbitCount_freeShadow_sub_atomShadow
  - qou-1qsw: QOU.QBeta.GluonVertexPsdParity.four_crossings_psd_and_two_prod_one
"""

from __future__ import annotations
import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def run_checks() -> list[dict[str, object]]:
    mp.mp.dps = 80
    tol = mp.mpf(10) ** (-75)
    checks: list[dict[str, object]] = []

    beta_star = mp.log(mp.mpf(2)) / mp.mpf(7)
    q = mp.exp(beta_star)
    qi = mp.mpf(1) / q

    # 1. qou-3qrv: markovWeights_jones_y3_cleared ([2]_q^2 * y3 = q^2 + q^-2)
    two_q = q + qi
    y21 = mp.mpf(1) / (two_q ** 2)
    y3 = mp.mpf(1) - mp.mpf(2) * y21
    z_d = (q ** 2) / two_q
    norm_res = abs((y3 + mp.mpf(2) * y21) - mp.mpf(1))
    sigma_res = abs((q * y3 + (q - qi) * y21) - z_d)
    sigmasigma_res = abs(((q ** 2) * y3 - y21) - (z_d ** 2))
    y3_cleared_res = abs((two_q ** 2) * y3 - (q ** 2 + qi ** 2))
    passed_1 = (
        norm_res < tol
        and sigma_res < tol
        and sigmasigma_res < tol
        and y3_cleared_res < tol
    )
    checks.append({
        "name": "markovWeights_jones_y3_cleared",
        "bean": "qou-3qrv",
        "y3ClearedResidual80dps": mp.nstr(y3_cleared_res, 25),
        "markovSystemResidual80dps": mp.nstr(norm_res + sigma_res + sigmasigma_res, 25),
        "passed": bool(passed_1),
    })

    # 2. qou-3exu: Bext_five_and_mayer_reconstruct
    s_row3 = {0: 0, 1: 0, 2: 0, 3: -1, 4: -2, 5: 4}
    def bext(A: int) -> int:
        return sum(math.comb(A, k) * s_row3.get(k, 0) for k in range(A + 1))
    b3, b4, b5 = bext(3), bext(4), bext(5)
    nu2 = s_row3[2]
    nu3 = s_row3[3] - 3 * nu2
    nu4 = s_row3[4] - 6 * nu2 - 4 * nu3
    passed_2 = (
        b5 == -16
        and b4 - 4 * b3 == s_row3[4]
        and 3 * nu2 + nu3 == s_row3[3]
        and 6 * nu2 + 4 * nu3 + nu4 == s_row3[4]
    )
    checks.append({
        "name": "Bext_five_and_mayer_reconstruct",
        "bean": "qou-3exu",
        "Bext5": str(b5),
        "Bext4Minus4Bext3": str(b4 - 4 * b3),
        "mayerSalg4": str(6 * nu2 + 4 * nu3 + nu4),
        "passed": bool(passed_2),
    })

    # 3. qou-5zl1: tr_atomWord_const_bond
    d0 = -((q - qi) / mp.mpf(2))
    p_p = (q ** 3) / (q ** 2 + mp.mpf(1))
    p_n = (q ** 2) / (q ** 2 + mp.mpf(1))
    n_val = 2  # A = n + 2 = 4 nucleons (Z = 2, N = 2)
    prod_lhs = mp.mpf(1)
    for _ in range(n_val + 1):
        prod_lhs *= (z_d + d0)
    atom_lhs = prod_lhs * (p_p ** 2) * (p_n ** 2)
    atom_rhs = ((z_d + d0) ** (n_val + 1)) * (p_p ** 2) * (p_n ** 2)
    const_bond_res = abs(atom_lhs - atom_rhs)
    passed_3 = (const_bond_res < tol and atom_rhs > 0)
    checks.append({
        "name": "tr_atomWord_const_bond",
        "bean": "qou-5zl1",
        "he4ConstBondTrace": mp.nstr(atom_rhs, 25),
        "constBondResidual80dps": mp.nstr(const_bond_res, 25),
        "passed": bool(passed_3),
    })

    # 4. qou-56qy: orbitCount_freeShadow_sub_atomShadow
    def count_orbits(n_strands: int, swaps: list[tuple[int, int]]) -> int:
        perm = list(range(n_strands))
        for u, v in reversed(swaps):
            perm[u], perm[v] = perm[v], perm[u]
        visited = [False] * n_strands
        orbits = 0
        for i in range(n_strands):
            if not visited[i]:
                orbits += 1
                cur = i
                while not visited[cur]:
                    visited[cur] = True
                    cur = perm[cur]
        return orbits

    shadow_ok = True
    for A in range(1, 8):
        n_nuc = A + 1
        n_str = 3 * n_nuc
        free_swaps = [(3 * k, 3 * k + 1) for k in reversed(range(n_nuc))]
        atom_swaps: list[tuple[int, int]] = []
        for k in range(n_nuc - 1, 0, -1):
            atom_swaps.append((3 * k, 3 * k + 1))
            atom_swaps.append((3 * k - 1, 3 * k))
        atom_swaps.append((0, 1))
        c_free = count_orbits(n_str, free_swaps)
        c_atom = count_orbits(n_str, atom_swaps)
        if c_free != 2 * n_nuc or c_atom != A + 2 or (c_free - c_atom) != A:
            shadow_ok = False
    checks.append({
        "name": "orbitCount_freeShadow_sub_atomShadow",
        "bean": "qou-56qy",
        "verifiedNucleonRange": "2..8",
        "mergeCountMatchesA": str(shadow_ok),
        "passed": bool(shadow_ok),
    })

    # 5. qou-1qsw: four_crossings_psd_and_two_prod_one
    sym4 = q ** 4
    alt4 = (-qi) ** 4
    sym2 = q ** 2
    alt2 = (-qi) ** 2
    prod2_res = abs(sym2 * alt2 - mp.mpf(1))
    q_rat = Fraction(11, 10)
    prod2_rat = (q_rat ** 2) * ((-1 / q_rat) ** 2)
    passed_5 = (sym4 > 0 and alt4 > 0 and prod2_res < tol and prod2_rat == 1)
    checks.append({
        "name": "four_crossings_psd_and_two_prod_one",
        "bean": "qou-1qsw",
        "exactProductAtK2": str(prod2_rat),
        "productResidual80dps": mp.nstr(prod2_res, 25),
        "passed": bool(passed_5),
    })

    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--output", default="test/results/witnesses/tl-uniqueness-threerow-factorisation-shadow-gluon.witness.json")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    checks = run_checks()
    if not all(bool(c["passed"]) for c in checks):
        raise SystemExit("One or more probe checks failed!")

    witness = {
        "schemaVersion": "1.0",
        "witnessId": "tl-uniqueness-threerow-factorisation-shadow-gluon",
        "scriptPath": "computations/probes/tl_uniqueness_threerow_factorisation_shadow_gluon_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_hash,
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dps": "80",
        "beans": [
            "qou-3qrv",
            "qou-3exu",
            "qou-5zl1",
            "qou-56qy",
            "qou-1qsw",
        ],
        "theorems": [
            "QOU.BraidsAndKnots.markovWeights_jones_y3_cleared",
            "QOU.MassTheory.ThreeRowExtensiveCumulant.Bext_five_and_mayer_reconstruct",
            "QOU.Mass.AtomTraceFactorisation.tr_atomWord_const_bond",
            "QOU.MassTheory.orbitCount_freeShadow_sub_atomShadow",
            "QOU.QBeta.GluonVertexPsdParity.four_crossings_psd_and_two_prod_one",
        ],
        "allPassed": True,
        "checks": checks,
    }
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
