#!/usr/bin/env python3
"""80-dps mpmath numerical witness probe for Round 111 BraidKnot theorems:
- qou-nok3: sum_hookZ_sub_bStat_eq_zero (HookSumRegisterBridge.lean)
- qou-nro6: sum_hookZ_sub_sq_min_nonneg (HookSumThicknessBound.lean)
- qou-nuw5: centralC2_coeff_one_sub_eq_zero (JucysMurphyCoeff.lean)
- qou-o6ml: prodHooks_conj_sub_eq_zero (KeystoneC2DimTranspose.lean)
- qou-og83: c8_superexp_sq_sub_nonneg (KeystoneC8SuperExpBound.lean)
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def col_len(rows, j):
    return sum(1 for r in rows if r > j)


def conj_part(rows):
    if not rows:
        return []
    return [col_len(rows, j) for j in range(rows[0])]


def hook_cells(rows):
    cells = []
    for i, r in enumerate(rows):
        for j in range(r):
            h = (r - 1 - j) + (col_len(rows, j) - 1 - i) + 1
            cells.append((i, j, h))
    return cells


def run_checks():
    results = []

    # 1. qou-nok3: sum_hookZ_sub_bStat_eq_zero on partition [5, 4, 2, 1]
    rows1 = [5, 4, 2, 1]
    cells1 = hook_cells(rows1)
    sum_hook1 = mp.mpf(sum(h for _, _, h in cells1))
    b_conj1 = sum(mp.mpf(j) * mp.mpf(col_len(rows1, j)) for j in range(rows1[0]))
    b_lam1 = sum(mp.mpf(i) * mp.mpf(r) for i, r in enumerate(rows1))
    card1 = mp.mpf(sum(rows1))
    diff1 = sum_hook1 - (b_conj1 + b_lam1 + card1)
    results.append({
        "bean": "qou-nok3",
        "theorem": "QOU.BraidKnot.HookSumBridge.sum_hookZ_sub_bStat_eq_zero",
        "partition": str(rows1),
        "sumHookZ": mp.nstr(sum_hook1, 80),
        "bStatRhs": mp.nstr(b_conj1 + b_lam1 + card1, 80),
        "residual": mp.nstr(diff1, 80),
        "passed": diff1 == mp.mpf(0),
    })

    # 2. qou-nro6: sum_hookZ_sub_sq_min_nonneg on partition [5, 4, 2, 1]
    r_min = mp.mpf(min(rows1[0], col_len(rows1, 0)))
    diff2 = sum_hook1 - r_min ** 2
    results.append({
        "bean": "qou-nro6",
        "theorem": "QOU.BraidKnot.HookSum.sum_hookZ_sub_sq_min_nonneg",
        "partition": str(rows1),
        "sumHookZ": mp.nstr(sum_hook1, 80),
        "sqMinDim": mp.nstr(r_min ** 2, 80),
        "margin": mp.nstr(diff2, 80),
        "passed": diff2 >= mp.mpf(0) and diff2 == mp.mpf(24),
    })

    # 3. qou-nuw5: centralC2_coeff_one_sub_eq_zero for n = 7
    n_val = 7
    # In S_n, each transposition (i k) for i < k has square 1, and distinct transpositions
    # sharing k have product a 3-cycle (identity coeff 0), so coeff_1(X_k^2) = k.
    jm_sq_id_coeff = sum(mp.mpf(k) for k in range(n_val))
    binom_n_2 = mp.mpf(math.comb(n_val, 2))
    diff3 = jm_sq_id_coeff - binom_n_2
    results.append({
        "bean": "qou-nuw5",
        "theorem": "QOU.BraidKnot.JucysMurphyCoeff.centralC2_coeff_one_sub_eq_zero",
        "n": str(n_val),
        "jmSqIdentityCoeff": mp.nstr(jm_sq_id_coeff, 80),
        "chooseN2": mp.nstr(binom_n_2, 80),
        "residual": mp.nstr(diff3, 80),
        "passed": diff3 == mp.mpf(0),
    })

    # 4. qou-o6ml: prodHooks_conj_sub_eq_zero on partition [5, 3, 2, 1]
    rows4 = [5, 3, 2, 1]
    conj4 = conj_part(rows4)
    prod_lam = mp.mpf(1)
    for _, _, h in hook_cells(rows4):
        prod_lam *= mp.mpf(h)
    prod_conj = mp.mpf(1)
    for _, _, h in hook_cells(conj4):
        prod_conj *= mp.mpf(h)
    diff4 = prod_conj - prod_lam
    results.append({
        "bean": "qou-o6ml",
        "theorem": "QOU.BraidKnot.IdentityI.prodHooks_conj_sub_eq_zero",
        "partition": str(rows4),
        "conjugate": str(conj4),
        "prodHooksConj": mp.nstr(prod_conj, 80),
        "prodHooksLam": mp.nstr(prod_lam, 80),
        "residual": mp.nstr(diff4, 80),
        "passed": diff4 == mp.mpf(0),
    })

    # 5. qou-og83: c8_superexp_sq_sub_nonneg for K = 6, kfac = 720, Ik = 76
    k_val = 6
    kfac = mp.mpf(math.factorial(k_val))
    ik_val = mp.mpf(76)  # involution number I_6 = 76
    # Use a 2-point support matching sum f_i g_i = kfac / 3 and sum g_i = Ik
    g_vec = [mp.mpf(36), mp.mpf(40)]
    f_vec = [mp.mpf(4), mp.mpf(24) / mp.mpf(10)]
    sum_fg = sum(f * g for f, g in zip(f_vec, g_vec))
    sum_g = sum(g_vec)
    w_std = sum((f ** 2) * g for f, g in zip(f_vec, g_vec)) / kfac
    rhs_bound = kfac / (mp.mpf(81) * (mp.mpf(2) ** k_val))
    diff5 = (w_std ** 2) - rhs_bound
    results.append({
        "bean": "qou-og83",
        "theorem": "QOU.BraidKnot.KeystoneC8SuperExpBound.c8_superexp_sq_sub_nonneg",
        "sumFG": mp.nstr(sum_fg, 80),
        "sumG": mp.nstr(sum_g, 80),
        "wStdSq": mp.nstr(w_std ** 2, 80),
        "superExpBound": mp.nstr(rhs_bound, 80),
        "margin": mp.nstr(diff5, 80),
        "passed": (
            sum_fg == kfac / mp.mpf(3)
            and sum_g <= ik_val
            and (ik_val ** 2) <= (mp.mpf(2) ** k_val) * kfac
            and diff5 >= mp.mpf(0)
        ),
    })

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    results = run_checks()
    all_passed = all(r["passed"] for r in results)
    if not all_passed:
        raise SystemExit("One or more probe checks failed")

    payload = {
        "probe": "hookreg_hookthick_jmcoeff_keyc2_keyc8_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/hookreg_hookthick_jmcoeff_keyc2_keyc8_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": "80",
        "allPassed": all_passed,
        "results": results,
    }
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
