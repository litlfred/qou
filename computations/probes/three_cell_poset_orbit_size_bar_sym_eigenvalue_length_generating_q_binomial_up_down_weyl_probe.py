#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for QOU Round 64:
- qou-7xt3: 3-cell poset comparability-count to linear-extension orbit-size classification (1, 2, 3, 6)
- qou-ck0g: Bar-symmetric q-deformed Jucys-Murphy content eigenvalue sum identity sum (q^{2c} + q^{-2c}) = (q - q^{-1})^2 sum [c]_q^2 + 2n
- qou-em1j: S_3 inversion-length Poincare polynomial sum_{w in S_3} q^{ell(w)} = [3]_q! = (1 + q)(1 + q + q^2)
- qou-kbjc: q-binomial (Gaussian) coefficients [n, k]_q Pascal recurrences, reflection symmetry, and q-binomial product theorem
- qou-w0zn: Young lattice up-down commutator DU - UD = I (diagonal addable-minus-removable corner balance and off-diagonal cancellation)
"""

from __future__ import annotations

import hashlib
import itertools
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 80


def fmt(x: mpf) -> str:
    return mp.nstr(x, 30)


def check_7xt3_three_cell_poset_orbit_sizes() -> dict:
    """Enumerate linear extensions of the four 3-cell poset comparability classes:
    - chain (0 < 1 < 2, 3 comparable pairs): 1 linear extension
    - hook (0 < 1, 0 < 2, 2 comparable pairs): 2 linear extensions
    - single pair (0 < 1, 2 incomparable, 1 comparable pair): 3 linear extensions
    - antichain (0 comparable pairs): 6 linear extensions.
    """
    perms = list(itertools.permutations([0, 1, 2]))

    def count_lin_ext(relations: list[tuple[int, int]]) -> int:
        cnt = 0
        for p in perms:
            pos = {val: idx for idx, val in enumerate(p)}
            if all(pos[a] < pos[b] for a, b in relations):
                cnt += 1
        return cnt

    sz_chain = count_lin_ext([(0, 1), (1, 2), (0, 2)])
    sz_hook = count_lin_ext([(0, 1), (0, 2)])
    sz_single = count_lin_ext([(0, 1)])
    sz_anti = count_lin_ext([])

    div_err = (
        abs(sz_anti * 1 - 6)
        + abs(sz_single * 2 - 6)
        + abs(sz_hook * 3 - 6)
        + abs((sz_chain + sz_hook + sz_single) - sz_anti)
    )

    passed = bool(
        sz_chain == 1
        and sz_hook == 2
        and sz_single == 3
        and sz_anti == 6
        and div_err == 0
    )
    return {
        "beanId": "qou-7xt3",
        "orbitSizes_chain_hook_single_antichain": [
            str(sz_chain),
            str(sz_hook),
            str(sz_single),
            str(sz_anti),
        ],
        "divisorAndPartitionResidual": str(div_err),
        "passed": passed,
    }


def check_ck0g_bar_symmetric_jm_eigenvalues() -> dict:
    """Verify sum_{c in lambda} (q^{2c} + q^{-2c}) = (q - q^{-1})^2 * sum_{c in lambda} [c]_q^2 + 2*n
    at 80-dps precision for q = exp(0.37) across all partitions lambda of n = 4:
    (4), (3,1), (2,2), (2,1,1), (1,1,1,1).
    """
    q = mp.exp(mpf("0.37"))
    h = q - 1 / q

    def q_int(c: int) -> mpf:
        if c == 0:
            return mpf(0)
        return (q**c - q ** (-c)) / h

    partitions_4 = [
        [4],
        [3, 1],
        [2, 2],
        [2, 1, 1],
        [1, 1, 1, 1],
    ]

    max_err = mpf(0)
    bar_sums = []
    for part in partitions_4:
        contents = [j - i for i, row_len in enumerate(part) for j in range(row_len)]
        lhs = sum(q ** (2 * c) + q ** (-2 * c) for c in contents)
        rhs = (h**2) * sum(q_int(c) ** 2 for c in contents) + mpf(2 * len(contents))
        max_err = max(max_err, abs(lhs - rhs))
        bar_sums.append(fmt(lhs))

    passed = bool(max_err < mpf("1e-70"))
    return {
        "beanId": "qou-ck0g",
        "partitionBarSymmetricEigenvalueSumsN4": bar_sums,
        "maxBracketIdentityResidual": fmt(max_err),
        "passed": passed,
    }


def check_em1j_s3_poincare_length_polynomial() -> dict:
    """Verify sum_{w in S_3} q^{ell(w)} = 1 + 2q + 2q^2 + q^3 = (1 + q)(1 + q + q^2) = [3]_q!
    by explicit inversion counting over S_3 at q = pi / 5.
    """
    q = mp.pi / mpf("5")
    perms = list(itertools.permutations([0, 1, 2]))

    def inv_len(p: tuple[int, ...]) -> int:
        return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])

    poincare_sum = sum(q ** inv_len(p) for p in perms)
    q_fact_3 = (1 + q) * (1 + q + q**2)
    err = abs(poincare_sum - q_fact_3)

    # Parity check P(q) + P(-q) = 2*(1 + 2*q^2)
    poincare_neg = sum((-q) ** inv_len(p) for p in perms)
    parity_err = abs((poincare_sum + poincare_neg) - 2 * (1 + 2 * q**2))

    passed = bool(err < mpf("1e-75") and parity_err < mpf("1e-75"))
    return {
        "beanId": "qou-em1j",
        "poincareSumValue": fmt(poincare_sum),
        "qFactorial3Value": fmt(q_fact_3),
        "factorizationResidual": fmt(err),
        "paritySymmetrizationResidual": fmt(parity_err),
        "passed": passed,
    }


def check_kbjc_q_binomial_identities() -> dict:
    """Verify q-binomial coefficients [n, k]_q Pascal recurrences, reflection symmetry,
    and Cauchy q-binomial product theorem prod_{j=0}^{n-1} (1 + q^j z) = sum_{k=0}^n q^{k(k-1)/2} [n, k]_q z^k
    for n = 5 at q = 3/7, z = 5/11.
    """
    q = mpf("3") / mpf("7")
    z = mpf("5") / mpf("11")

    def q_num(m: int) -> mpf:
        return (1 - q**m) / (1 - q)

    def q_fact(m: int) -> mpf:
        res = mpf(1)
        for i in range(1, m + 1):
            res *= q_num(i)
        return res

    def q_binom(n: int, k: int) -> mpf:
        if k < 0 or k > n:
            return mpf(0)
        return q_fact(n) / (q_fact(k) * q_fact(n - k))

    n = 5
    max_pascal_err = mpf(0)
    max_sym_err = mpf(0)
    for k in range(1, n):
        lhs = q_binom(n, k)
        rhs1 = q_binom(n - 1, k - 1) + (q**k) * q_binom(n - 1, k)
        rhs2 = (q ** (n - k)) * q_binom(n - 1, k - 1) + q_binom(n - 1, k)
        max_pascal_err = max(max_pascal_err, abs(lhs - rhs1), abs(lhs - rhs2))
        max_sym_err = max(max_sym_err, abs(q_binom(n, k) - q_binom(n, n - k)))

    prod_lhs = mpf(1)
    for j in range(n):
        prod_lhs *= 1 + (q**j) * z
    prod_rhs = sum(
        (q ** (k * (k - 1) // 2)) * q_binom(n, k) * (z**k) for k in range(n + 1)
    )
    prod_err = abs(prod_lhs - prod_rhs)

    passed = bool(
        max_pascal_err < mpf("1e-75")
        and max_sym_err < mpf("1e-75")
        and prod_err < mpf("1e-75")
    )
    return {
        "beanId": "qou-kbjc",
        "maxPascalRecurrenceResidual": fmt(max_pascal_err),
        "maxReflectionSymmetryResidual": fmt(max_sym_err),
        "cauchyQBinomialProductValue": fmt(prod_lhs),
        "cauchyQBinomialProductResidual": fmt(prod_err),
        "passed": passed,
    }


def check_w0zn_young_lattice_du_minus_ud() -> dict:
    """Verify the full matrix identity D U - U D = I on the level n = 4 of the Young
    lattice (5 partitions of 4: (4), (3,1), (2,2), (2,1,1), (1,1,1,1), with 7 partitions of 5
    above and 3 partitions of 3 below).
    """
    parts_3 = [(3,), (2, 1), (1, 1, 1)]
    parts_4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    parts_5 = [
        (5,),
        (4, 1),
        (3, 2),
        (3, 1, 1),
        (2, 2, 1),
        (2, 1, 1, 1),
        (1, 1, 1, 1, 1),
    ]

    def covers(lam: tuple[int, ...], mu: tuple[int, ...]) -> bool:
        if sum(lam) != sum(mu) + 1:
            return False
        if len(lam) < len(mu) or len(lam) > len(mu) + 1:
            return False
        mu_pad = list(mu) + [0] * (len(lam) - len(mu))
        diffs = [lam[i] - mu_pad[i] for i in range(len(lam))]
        return diffs.count(1) == 1 and diffs.count(0) == len(lam) - 1

    # U: 7x5 matrix (parts_4 -> parts_5), D from level 5: U^T (5x7)
    # D to level 3: 3x5 matrix (parts_4 -> parts_3), U from level 3: D^T (5x3)
    max_diag_err = mpf(0)
    max_offdiag_err = mpf(0)
    diag_entries = []
    for i, mu in enumerate(parts_4):
        for j, nu in enumerate(parts_4):
            common_up = sum(1 for lam in parts_5 if covers(lam, mu) and covers(lam, nu))
            common_down = sum(1 for rho in parts_3 if covers(mu, rho) and covers(nu, rho))
            entry = mpf(common_up - common_down)
            if i == j:
                diag_entries.append(fmt(entry))
                max_diag_err = max(max_diag_err, abs(entry - mpf(1)))
            else:
                max_offdiag_err = max(max_offdiag_err, abs(entry))

    passed = bool(max_diag_err == mpf(0) and max_offdiag_err == mpf(0))
    return {
        "beanId": "qou-w0zn",
        "level4DiagonalEntries": diag_entries,
        "maxDiagonalResidual": fmt(max_diag_err),
        "maxOffDiagonalResidual": fmt(max_offdiag_err),
        "passed": passed,
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    script_bytes = script_path.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]

    try:
        commit_sha = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=script_path.parent
            )
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    checks = [
        check_7xt3_three_cell_poset_orbit_sizes(),
        check_ck0g_bar_symmetric_jm_eigenvalues(),
        check_em1j_s3_poincare_length_polynomial(),
        check_kbjc_q_binomial_identities(),
        check_w0zn_young_lattice_du_minus_ud(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probe": "three-cell-poset-orbit-size-bar-sym-eigenvalue-length-generating-q-binomial-up-down-weyl",
        "beans": ["qou-7xt3", "qou-ck0g", "qou-em1j", "qou-kbjc", "qou-w0zn"],
        "precisionDps": "80",
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    out_path = script_path.with_name(
        "three-cell-poset-orbit-size-bar-sym-eigenvalue-length-generating-q-binomial-up-down-weyl.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.name}: allPassed={all_passed}, scriptHash={script_hash}")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
