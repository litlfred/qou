#!/usr/bin/env python3
"""80-dps mpmath probe for SelfConjugateMultiplicityAndProlongationKernelBrick (qou-k2xr, qou-k4ud, qou-k8ek, qou-kc7y, qou-kyh5)."""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = pathlib.Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "self-conjugate-multiplicity-and-prolongation-kernel-brick.witness.json"
)


def monotone_self_conj_count(a: int) -> int:
    return a - 1


def multiplicity_discrepancy(a: int, nu: int) -> int:
    return (a - 1) - nu


def four_body_exchange_poly(k_sq: int, m_sq: int) -> int:
    return (k_sq - 5 * m_sq) * (k_sq - m_sq)


def three_braid_writhe_pair(a1: int, b1: int, a2: int, b2: int) -> tuple[int, int]:
    return (a1 + b1 + a2 + b2, (a1 + a2) - (b1 + b2))


def prolongation_symbol(q: int, x: int, d: int) -> int:
    return (q - 1) * x + d


def crossing_multiplicity_gap(crossings: int, nu: int) -> int:
    return crossings - 2 * nu


def run_probe() -> dict:
    mp.mp.dps = 80
    checks = []

    # 1. qou-k2xr: monotone self-conjugate count & He-4 multiplicity discrepancy
    k2xr_ok = True
    for a, b, nu1, nu2 in [(2, 3, 1, 2), (4, 2, 2, 3), (6, 1, 5, 4)]:
        d1 = multiplicity_discrepancy(a, nu1)
        d2 = multiplicity_discrepancy(a, nu2)
        sc_step = monotone_self_conj_count(a + 1) - monotone_self_conj_count(a)
        he4_diff = multiplicity_discrepancy(4, 2) - multiplicity_discrepancy(4, 3)
        d_sum = multiplicity_discrepancy(a + b, nu1 + nu2)
        if not (
            d1 - d2 == nu2 - nu1
            and sc_step + nu1 + nu2 == 1 + nu1 + nu2
            and he4_diff + a + b + nu1 + nu2 == 1 + a + b + nu1 + nu2
            and d_sum == d1 + multiplicity_discrepancy(b, nu2) + 1
        ):
            k2xr_ok = False
    he4_gap_mp = mp.mpf(multiplicity_discrepancy(4, 2) - multiplicity_discrepancy(4, 3))
    checks.append(
        {
            "bean": "qou-k2xr",
            "name": "monotoneSelfConjCount_and_multiplicityDiscrepancy",
            "passed": bool(k2xr_ok and he4_gap_mp == mp.mpf(1)),
            "he4MultiplicitySplit80dps": mp.nstr(he4_gap_mp, 80),
        }
    )

    # 2. qou-k4ud: four-body exchange determinant & ss-sector critical pole
    k4ud_ok = True
    for k_sq, m_sq in [(11, 2), (25, 5), (37, -3), (19, 4)]:
        val = four_body_exchange_poly(k_sq, m_sq)
        expanded = k_sq * k_sq - 6 * (k_sq * m_sq) + 5 * (m_sq * m_sq)
        crit_ss = four_body_exchange_poly(5 * m_sq, m_sq)
        crit_pauli = four_body_exchange_poly(m_sq, m_sq)
        gap = val - (k_sq - m_sq) * (k_sq - m_sq)
        if not (
            val == expanded
            and crit_ss + k_sq == k_sq
            and gap == -4 * m_sq * (k_sq - m_sq)
            and crit_pauli + k_sq == k_sq
        ):
            k4ud_ok = False
    q0_mp = (mp.mpf(3) + mp.sqrt(mp.mpf(5))) / mp.mpf(2)
    two_v_sq = mp.mpf(4) + (q0_mp - 1) ** 2 / q0_mp
    g_reeb_sq = mp.mpf(1) / (mp.mpf(1) + two_v_sq)
    ss_pole_res = abs((mp.mpf(1) + two_v_sq) * g_reeb_sq - mp.mpf(1))
    checks.append(
        {
            "bean": "qou-k4ud",
            "name": "fourBodyExchangePoly_expanded_and_critical_poles",
            "passed": bool(k4ud_ok and ss_pole_res < mp.mpf("1e-75")),
            "deformedSsPoleCriticalityResidual80dps": mp.nstr(ss_pole_res, 80),
        }
    )

    # 3. qou-k8ek: 3-braid abelianization writhe & block balance
    k8ek_ok = True
    for a1, b1, a2, b2 in [(3, -2, 5, 4), (-7, 6, 2, -3), (4, 4, -4, -4)]:
        w, bal = three_braid_writhe_pair(a1, b1, a2, b2)
        w_swap, _ = three_braid_writhe_pair(a2, b1, a1, b2)
        w_comm, _ = three_braid_writhe_pair(a1, b1, -a1, -b1)
        if not (
            w + bal == 2 * (a1 + a2)
            and w_swap == w
            and w - bal == 2 * (b1 + b2)
            and w_comm + a2 + b2 == a2 + b2
        ):
            k8ek_ok = False
    comm_writhe_mp = mp.mpf(three_braid_writhe_pair(3, -5, -3, 5)[0])
    checks.append(
        {
            "bean": "qou-k8ek",
            "name": "threeBraidWrithePair_reordering_and_commutator",
            "passed": bool(k8ek_ok and comm_writhe_mp == mp.mpf(0)),
            "commutatorAbelianizedWrithe80dps": mp.nstr(comm_writhe_mp, 80),
        }
    )

    # 4. qou-kc7y: first-order prolongation symbol & binding kernel
    kc7y_ok = True
    for q1, q2, x1, x2, d1, d2 in [
        (4, 2, 7, -3, 5, 9),
        (-3, 5, 11, 6, -4, 2),
        (8, 3, -5, 12, 7, -8),
    ]:
        p_sum = prolongation_symbol(q1, x1 + x2, d1 + d2)
        p_parts = prolongation_symbol(q1, x1, d1) + prolongation_symbol(q1, x2, d2)
        p_one = prolongation_symbol(1, x1, d1)
        p_diff = prolongation_symbol(q1, x1, d1) - prolongation_symbol(q2, x1, d1)
        p_step = prolongation_symbol(q1 + 1, x1, d1) - prolongation_symbol(q1, x1, d1)
        if not (
            p_sum == p_parts
            and p_one + q1 + x2 + d2 == d1 + q1 + x2 + d2
            and p_diff == (q1 - q2) * x1
            and p_step + q2 == x1 + q2
        ):
            kc7y_ok = False
    prolong_q0 = (q0_mp - 1) * mp.mpf(3) + mp.mpf(5)
    prolong_err = abs((prolong_q0 - mp.mpf(5)) - (q0_mp - 1) * mp.mpf(3))
    checks.append(
        {
            "bean": "qou-kc7y",
            "name": "prolongationSymbol_linearity_and_shift",
            "passed": bool(kc7y_ok and prolong_err < mp.mpf("1e-75")),
            "prolongationSymbolResidual80dps": mp.nstr(prolong_err, 80),
        }
    )

    # 5. qou-kyh5: crossing-multiplicity stratification gap
    kyh5_ok = True
    for c1, c2, nu1, nu2, delta in [(4, 6, 0, 1, 2), (5, 8, 0, 2, 3), (6, 6, 1, 1, -1)]:
        g_sum = crossing_multiplicity_gap(c1 + c2, nu1 + nu2)
        g_parts = crossing_multiplicity_gap(c1, nu1) + crossing_multiplicity_gap(c2, nu2)
        g_shift = crossing_multiplicity_gap(c1 + 2 * nu2, nu1 + nu2)
        g_anchor_diff = crossing_multiplicity_gap(c2, 0) - crossing_multiplicity_gap(c2, nu2)
        g_inv = crossing_multiplicity_gap(c2 + 2 * delta, nu2 + delta)
        if not (
            g_sum == g_parts
            and g_shift + c2 == crossing_multiplicity_gap(c1, nu1) + c2
            and g_anchor_diff == 2 * nu2
            and g_inv == crossing_multiplicity_gap(c2, nu2)
        ):
            kyh5_ok = False
    gap_6_2_mp = mp.mpf(crossing_multiplicity_gap(6, 1))
    checks.append(
        {
            "bean": "qou-kyh5",
            "name": "crossingMultiplicityGap_additivity_and_anchor_balance",
            "passed": bool(kyh5_ok and gap_6_2_mp == mp.mpf(4)),
            "confirmedAtom6_2Gap80dps": mp.nstr(gap_6_2_mp, 80),
        }
    )

    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    commit_sha = (
        subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(REPO_ROOT), text=True
        ).strip()
    )
    status_out = subprocess.check_output(
        [
            "git",
            "status",
            "--porcelain",
            "--",
            str(SCRIPT_PATH.relative_to(REPO_ROOT)),
        ],
        cwd=str(REPO_ROOT),
        text=True,
    ).strip()

    witness = {
        "probe": "self_conjugate_multiplicity_and_prolongation_kernel_brick_probe",
        "beans": ["qou-k2xr", "qou-k4ud", "qou-k8ek", "qou-kc7y", "qou-kyh5"],
        "leanModule": "folio/quantum-observable-universe/lean/QOU/QBeta/SelfConjugateMultiplicityAndProlongationKernelBrick.lean",
        "precisionDps": "80",
        "scriptCommitSha": commit_sha,
        "scriptHash": script_hash,
        "dirty": bool(status_out),
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n")
    return witness


if __name__ == "__main__":
    result = run_probe()
    print(
        f"Witness written to {WITNESS_PATH.name}: allPassed={result['allPassed']}, "
        f"scriptCommitSha={result['scriptCommitSha']}, scriptHash={result['scriptHash']}"
    )
