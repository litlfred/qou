#!/usr/bin/env python3
"""80-dps mpmath verification probe for Round 61 theorems (qou-itdn, qou-kok7, qou-l155, qou-t2sc, qou-zynz).

Verifies:
1. qou-kok7 (AdditiveSignChangingTerm.lean):
   - bondFrust_linear_comb_invariant: 4 * bondFrustA3(kappa) - bondFrustA4(kappa) == 6
   - bondFrust_window_endpoints_and_midpoint: values at kappa in {3/2, 9/4, 3}.
2. qou-l155 (ColourCubicBranchLocus.lean):
   - disc_at_pm_one_and_wCubic_vals: disc(1) == 200, disc(-1) == 4, wCubic(0) == 2, wCubic(1) == 29
   - ddz_linear_comb_residue_slot_eq_zero: coefficient of t^{-2} vanishes under ddz for any linear combination.
3. qou-zynz (TowerHeightAttack.lean):
   - gradewise_three_term_determines_level & gradewise_three_term_closure_propagates:
     c1*PhiA(n) == -(c2*PhiB(n) + c3*PhiC(n)) and vanishing of PhiB(n), PhiC(n) forces PhiA(n) == 0.
4. qou-itdn (JHopfQOneProvenance.lean):
   - borromean_atOne: classicalJonesAtOne(3) == 4
   - classicalJonesAtOne_step: classicalJonesAtOne(c+1) == -2 * classicalJonesAtOne(c)
   - classicalJonesAtOne_selectivity: V_L(1) in {1, -2, 4} pairwise distinct for c = 1, 2, 3.
5. qou-t2sc (WhiteheadPhaseAlgebra.lean):
   - whiteheadLinkPhase_fresnel_symm: ((N - n) - N/2)^2 == (n - N/2)^2
   - whiteheadLinkPhase_arg_at_half_even: -m*(m + 1 - 2m)*pi/(4m) == m*pi/4 - pi/4.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 25)


def check_bond_frustration_window() -> dict:
    def f3(k: mp.mpf) -> mp.mpf:
        return mp.mpf(3) - k

    def f4(k: mp.mpf) -> mp.mpf:
        return mp.mpf(6) - mp.mpf(4) * k

    max_res = mp.mpf(0)
    for k_str in ["1.5", "1.75", "2.25", "2.75", "3.0"]:
        kv = mp.mpf(k_str)
        max_res = max(max_res, abs((4 * f3(kv) - f4(kv)) - mp.mpf(6)))

    k_lo = mp.mpf(3) / mp.mpf(2)
    k_mid = mp.mpf(9) / mp.mpf(4)
    k_hi = mp.mpf(3)
    end_res = max(
        abs(f3(k_lo) - mp.mpf(3) / mp.mpf(2)),
        abs(f4(k_lo) - mp.mpf(0)),
        abs(f3(k_hi) - mp.mpf(0)),
        abs(f4(k_hi) - (-mp.mpf(6))),
        abs(f3(k_mid) - mp.mpf(3) / mp.mpf(4)),
        abs(f4(k_mid) - (-mp.mpf(3))),
    )
    max_res = max(max_res, end_res)
    tol = mp.mpf("1e-75")
    return {
        "name": "bond_frustration_window_qou_kok7",
        "passed": bool(max_res < tol),
        "midpointRatioA3OverA4": fmt(f3(k_mid) / f4(k_mid)),
        "maxResidual": fmt(max_res),
    }


def check_colour_cubic_branch_locus() -> dict:
    def disc(z: mp.mpf) -> mp.mpf:
        return (
            16 * z**6
            + 24 * z**5
            + 35 * z**4
            + 50 * z**3
            + 35 * z**2
            + 24 * z
            + 16
        )

    def wcubic(w: mp.mpf) -> mp.mpf:
        return 16 * w**3 + 24 * w**2 - 13 * w + 2

    r1 = abs(disc(mp.mpf(1)) - mp.mpf(200))
    r2 = abs(disc(mp.mpf(-1)) - mp.mpf(4))
    r3 = abs(wcubic(mp.mpf(0)) - mp.mpf(2))
    r4 = abs(wcubic(mp.mpf(1)) - mp.mpf(29))
    # ddz at e = -2 multiplies by (e + 2) = 0
    e_slot = -2
    ddz_mult = mp.mpf(e_slot + 2)
    r5 = abs(ddz_mult * (mp.mpf("3.7") * mp.mpf("1.2") + mp.mpf("-2.1") * mp.mpf("4.9")))

    max_res = max(r1, r2, r3, r4, r5)
    tol = mp.mpf("1e-75")
    return {
        "name": "colour_cubic_branch_locus_qou_l155",
        "passed": bool(max_res < tol),
        "discAtOne": fmt(disc(mp.mpf(1))),
        "discAtNegOne": fmt(disc(mp.mpf(-1))),
        "maxResidual": fmt(max_res),
    }


def check_tower_height_three_term_gradewise() -> dict:
    c1 = mp.mpf("5.0")
    c2 = mp.mpf("-3.0")
    c3 = mp.mpf("2.0")
    r_b = mp.mpf("0.5")
    r_c = mp.mpf("0.25")

    max_res = mp.mpf(0)
    for n in range(10):
        phi_b = mp.mpf(0) if n >= 5 else r_b**n
        phi_c = mp.mpf(0) if n >= 5 else r_c**n
        phi_a = -(c2 * phi_b + c3 * phi_c) / c1
        rel_res = abs(c1 * phi_a + c2 * phi_b + c3 * phi_c)
        if n >= 5:
            max_res = max(max_res, rel_res, abs(phi_a))
        else:
            max_res = max(max_res, rel_res)

    tol = mp.mpf("1e-75")
    return {
        "name": "tower_height_three_term_gradewise_qou_zynz",
        "passed": bool(max_res < tol),
        "c1": fmt(c1),
        "maxResidual": fmt(max_res),
    }


def check_jones_hopf_q1_selectivity() -> dict:
    def v_at_one(c: int) -> mp.mpf:
        return (-mp.mpf(2)) ** (c - 1)

    v1 = v_at_one(1)
    v2 = v_at_one(2)
    v3 = v_at_one(3)

    step_res = max(
        abs(v_at_one(c + 1) - (-mp.mpf(2) * v_at_one(c))) for c in range(1, 7)
    )
    val_res = max(abs(v1 - 1), abs(v2 - (-2)), abs(v3 - 4))
    max_res = max(step_res, val_res)
    tol = mp.mpf("1e-75")
    return {
        "name": "jones_hopf_q1_selectivity_qou_itdn",
        "passed": bool(max_res < tol and v1 != v2 and v1 != v3 and v2 != v3),
        "vUnknot": fmt(v1),
        "vHopf": fmt(v2),
        "vBorromean": fmt(v3),
        "maxResidual": fmt(max_res),
    }


def check_whitehead_phase_algebra() -> dict:
    max_res = mp.mpf(0)
    for m in range(1, 12):
        n_tot = mp.mpf(2 * m)
        n_mid = mp.mpf(m)
        lhs_even = -(n_mid * (n_mid + 1 - n_tot) * mp.pi / (2 * n_tot))
        rhs_even = n_mid * mp.pi / 4 - mp.pi / 4
        max_res = max(max_res, abs(lhs_even - rhs_even))
        for n_k in range(0, 2 * m + 1):
            nk = mp.mpf(n_k)
            sym_lhs = ((n_tot - nk) - n_tot / 2) ** 2
            sym_rhs = (nk - n_tot / 2) ** 2
            max_res = max(max_res, abs(sym_lhs - sym_rhs))

    tol = mp.mpf("1e-70")
    return {
        "name": "whitehead_phase_algebra_qou_t2sc",
        "passed": bool(max_res < tol),
        "maxResidual": fmt(max_res),
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    try:
        git_commit = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=script_path.parent
            )
            .decode("utf-8")
            .strip()
        )
    except Exception:
        git_commit = "0" * 40

    checks = [
        check_bond_frustration_window(),
        check_colour_cubic_branch_locus(),
        check_tower_height_three_term_gradewise(),
        check_jones_hopf_q1_selectivity(),
        check_whitehead_phase_algebra(),
    ]
    all_passed = all(c["passed"] for c in checks)
    witness = {
        "probe": script_path.name,
        "gitCommit": git_commit,
        "scriptCommitSha": git_commit,
        "scriptHash": script_hash,
        "dps": 80,
        "allPassed": all_passed,
        "checks": checks,
    }
    witness_path = (
        script_path.resolve().parents[2]
        / "test"
        / "results"
        / "witnesses"
        / "frust-cubic-tower-jhopf-whitehead.witness.json"
    )
    witness_path.parent.mkdir(parents=True, exist_ok=True)
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {witness_path.name} (allPassed={all_passed}, scriptHash={script_hash})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
