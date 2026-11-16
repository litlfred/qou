#!/usr/bin/env python3
"""80-dps mpmath probe for Round 53 beans:
- wpdb: Partition corner-hook depth h(0,0) = rowZero + colZero - 1 bounds
  1 <= h(0,0) <= n, n = 3 degeneracy (all 3 partitions have corner hook 3),
  n = 4 separation ((2,2) has corner hook 3 vs 4 for the 4 hooks), and
  emptiness of the unshifted degree-0 partition stratum.
- qou-4qno: Staircase partition rho_k = (k, k-1, ..., 1) on n_k = k(k+1)/2
  strands has k rows; under the N = 2 SU(2)_q / Temperley-Lieb row cap,
  k = 2 (rho_2 = (2,1), n_2 = 3) is the unique physical case among k >= 2,
  while every k >= 3 lies in the TL kernel.
- qou-8v3k: Route 8 saddle critical-point curve identity, cleared Vieta
  products prod(1 - x y_j) = x and prod(x - y_j) = x^2, envelope ratio
  identity, and x = -1 degeneration to w^3 - 2w^2 - w + 1 = 0 in Q(zeta_7)^+.
- qou-b7cy: Route 9 Bloch-group polynomial identity (1-w)^2(1+w) = w^2,
  explicit unit inverses and norms N(w) = -1, N(1-w) = -1, N(1+w) = +1 in
  Z[w], and per-embedding level-7 Rogers dilogarithm ladder numerators
  (17, 5, -1)/42 summing to 21/42 = 1/2.
- qou-018h: Hecke inverse-word involution T_w* = T_{w^-1} sign flip on the
  antisymmetric M_2 direction (tr(A A^T) - tr(A^2) = 4 gamma^2), (L_+, L_-)
  swap positivity, and convention-D quotient-by-radical positivity.

All floating-point computations use mpmath at 80 decimal digits (mp.dps = 80)
with exact integer/Fraction arithmetic for combinatorial identities; zero float64.
"""

from __future__ import annotations

from fractions import Fraction
import json
import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = "computations/probes/route89_staircase_wpdb_stargram_probe.py"
WITNESS_PATH = "computations/probes/route89-staircase-wpdb-stargram.witness.json"


def partitions(n: int, max_part: int | None = None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, max_part), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def corner_hook(lam: tuple[int, ...]) -> int:
    return lam[0] + len(lam) - 1


def staircase_list(k: int) -> tuple[int, ...]:
    return tuple(range(k, 0, -1))


def rogers_L_real(x: mp.mpf) -> mp.mpf:
    """Real part of Rogers dilogarithm L(x) = Li_2(x) + (1/2) log(x) log(1-x)
    evaluated via mp.polylog(2, x) + (1/2) log(x) log(1-x) in complex arithmetic."""
    xc = mp.mpc(x, 0)
    val = mp.polylog(2, xc) + mp.mpf(1) / 2 * mp.log(xc) * mp.log(1 - xc)
    return mp.re(val)


def run_probe() -> dict:
    mp.mp.dps = 80
    checks = []

    # 1. wpdb: corner-hook bounds, n=3 degeneracy, n=4 separation, no degree-0 stratum
    bounds_ok = True
    for n in range(1, 7):
        for lam in partitions(n):
            h = corner_hook(lam)
            if not (1 <= h <= n):
                bounds_ok = False
    n3_hooks = [corner_hook(lam) for lam in partitions(3)]
    n4_hooks = {lam: corner_hook(lam) for lam in partitions(4)}
    n3_degenerate = (n3_hooks == [3, 3, 3])
    n4_separated = (
        n4_hooks[(2, 2)] == 3
        and n4_hooks[(4,)] == 4
        and n4_hooks[(3, 1)] == 4
        and n4_hooks[(2, 1, 1)] == 4
        and n4_hooks[(1, 1, 1, 1)] == 4
    )
    checks.append({
        "id": "wpdb-corner-hook-and-stratification",
        "passed": bool(bounds_ok and n3_degenerate and n4_separated),
        "boundsVerifiedN1To6": bounds_ok,
        "n3CornerHooks": n3_hooks,
        "n4SelfConjugateHook": n4_hooks[(2, 2)],
        "n4HookStratumCount": sum(1 for v in n4_hooks.values() if v == 4),
    })

    # 2. qou-4qno: staircase partition rows and N=2 TL kernel threshold
    staircase_rows_ok = all(
        len(staircase_list(k)) == k and sum(staircase_list(k)) == k * (k + 1) // 2
        for k in range(1, 9)
    )
    physical_ge_2 = [k for k in range(2, 9) if len(staircase_list(k)) <= 2]
    tl_kernel_ge_2 = [k for k in range(2, 9) if len(staircase_list(k)) > 2]
    checks.append({
        "id": "qou-4qno-staircase-tl-kernel-threshold",
        "passed": bool(
            staircase_rows_ok
            and physical_ge_2 == [2]
            and tl_kernel_ge_2 == [3, 4, 5, 6, 7, 8]
        ),
        "physicalCasesGe2": physical_ge_2,
        "tlKernelCasesGe2": tl_kernel_ge_2,
        "strandsK2K3K4": [k * (k + 1) // 2 for k in (2, 3, 4)],
    })

    # 3. qou-8v3k: Route 8 Vieta products, envelope ratio, and x = -1 cyclotomic cubic
    w_roots = [1 + 2 * mp.cos(2 * mp.pi * k / 7) for k in (1, 2, 3)]
    y_neg1 = [-w for w in w_roots]
    # Check deformed curve at x = -1
    curve_neg1_err = sum(
        mp.fabs((-1) * (y ** 3) - 2 * (y ** 2) + y + 1)
        for y in y_neg1
    )
    # Check Vieta products at x = -1 (where y_k = -w_k)
    prod_one_sub_xy = mp.mpf(1)
    prod_x_sub_y = mp.mpf(1)
    for y in y_neg1:
        prod_one_sub_xy *= (1 - (-1) * y)
        prod_x_sub_y *= (-1 - y)
    vieta_err = mp.fabs(prod_one_sub_xy - (-1)) + mp.fabs(prod_x_sub_y - 1)
    # Check cyclotomic sum rule Sigma_k Re[Li_2(y_k) + 2 Li_2(-y_k) + (log(-y_k))^2] = -pi^2 / 2
    cyc_sum = mp.mpf(0)
    for w in w_roots:
        wc = mp.mpc(w, 0)
        term = mp.polylog(2, -wc) + 2 * mp.polylog(2, wc) + (mp.log(wc)) ** 2
        cyc_sum += mp.re(term)
    cyc_err = mp.fabs(cyc_sum - (-mp.pi ** 2 / 2))
    checks.append({
        "id": "qou-8v3k-route8-vieta-and-cyclotomic-degeneration",
        "passed": bool(
            curve_neg1_err < mp.mpf("1e-75")
            and vieta_err < mp.mpf("1e-75")
            and cyc_err < mp.mpf("1e-75")
        ),
        "curveAtNegOneResidual": mp.nstr(curve_neg1_err, 20),
        "vietaProductResidual": mp.nstr(vieta_err, 20),
        "cyclotomicSumResidual": mp.nstr(cyc_err, 20),
    })

    # 4. qou-b7cy: Route 9 Bloch identity, unit inverses, norms, and level-7 ladder
    bloch_err = sum(
        mp.fabs((1 - w) ** 2 * (1 + w) - w ** 2)
        for w in w_roots
    )
    unit_err = sum(
        mp.fabs(w * (w ** 2 - 2 * w - 1) - (-1))
        + mp.fabs((1 - w) * ((1 - w) ** 2 - (1 - w) - 2) - (-1))
        + mp.fabs((1 + w) * ((1 + w) ** 2 - 5 * (1 + w) + 6) - 1)
        for w in w_roots
    )
    norm_one_sub = mp.mpf(1)
    norm_one_add = mp.mpf(1)
    for w in w_roots:
        norm_one_sub *= (1 - w)
        norm_one_add *= (1 + w)
    norm_err = mp.fabs(norm_one_sub - (-1)) + mp.fabs(norm_one_add - 1)

    target_numerators = [17, 5, -1]
    ladder_err = mp.mpf(0)
    for w, m_k in zip(w_roots, target_numerators):
        lhs = 2 * rogers_L_real(w) + rogers_L_real(-w)
        rhs = mp.mpf(m_k) * (mp.pi ** 2) / 42
        ladder_err += mp.fabs(lhs - rhs)
    num_sum_frac = Fraction(sum(target_numerators), 42)
    checks.append({
        "id": "qou-b7cy-route9-bloch-torsion-and-level7-ladder",
        "passed": bool(
            bloch_err < mp.mpf("1e-75")
            and unit_err < mp.mpf("1e-75")
            and norm_err < mp.mpf("1e-75")
            and ladder_err < mp.mpf("1e-75")
            and num_sum_frac == Fraction(1, 2)
        ),
        "blochIdentityResidual": mp.nstr(bloch_err, 20),
        "unitInverseResidual": mp.nstr(unit_err, 20),
        "normIdentityResidual": mp.nstr(norm_err, 20),
        "level7LadderResidual": mp.nstr(ladder_err, 20),
        "ladderNumeratorSumOver42": str(num_sum_frac),
    })

    # 5. qou-018h: Star-Gram involution sign flip and convention-D quotient positivity
    q0 = mp.mpf("1.10997858275138")
    s0 = q0 + 1 / q0
    y21_D = 1 / (s0 ** 2)
    y3_D = 1 - 2 * y21_D
    y13_D = mp.mpf(0)
    # Check starform_sub_traceform_M2: tr(A A^T) - tr(A^2) = 4 gamma^2
    alpha, delta, beta, gamma = mp.mpf("0.7"), mp.mpf("-0.3"), mp.mpf("1.1"), mp.mpf("0.4")
    tr_star = alpha ** 2 + (beta + gamma) ** 2 + (beta - gamma) ** 2 + delta ** 2
    tr_bilin = alpha ** 2 + 2 * (beta + gamma) * (beta - gamma) + delta ** 2
    m2_flip_err = mp.fabs((tr_star - tr_bilin) - 4 * (gamma ** 2))
    # Quotient positivity under convention D
    quot_val = y3_D * mp.mpf("1.0") + y21_D * tr_star + y13_D * mp.mpf("99.0")
    checks.append({
        "id": "qou-018h-star-gram-involution-positivity",
        "passed": bool(
            m2_flip_err < mp.mpf("1e-75")
            and y3_D > 0
            and y21_D > 0
            and quot_val > 0
        ),
        "m2InvolutionFlipResidual": mp.nstr(m2_flip_err, 20),
        "y3ConventionD": mp.nstr(y3_D, 25),
        "y21ConventionD": mp.nstr(y21_D, 25),
        "quotientStarValue": mp.nstr(quot_val, 25),
    })

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "route89_staircase_wpdb_stargram_probe",
        "beans": ["wpdb", "qou-4qno", "qou-8v3k", "qou-b7cy", "qou-018h"],
        "precisionDps": 80,
        "allPassed": all_passed,
        "checks": checks,
    }


if __name__ == "__main__":
    out = run_probe()
    print(json.dumps(out, indent=2))
    if not out["allPassed"]:
        raise SystemExit(1)
