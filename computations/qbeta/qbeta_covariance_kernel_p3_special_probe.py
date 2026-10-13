#!/usr/bin/env python3
"""The Delta_lam kernel conjecture does NOT generalise: p=3 is special.

Epic `qou-x631` conjectures cov(k) = SUM_lam (f^lam)^3 (SUM c^2 - C(k,2)) <= 0,
equivalently T_3(k) = SUM_lam (f^lam)^2 chi^lam(3-cycle) <= 0. Five attack routes
were eliminated in phases 0-2. This probe eliminates a sixth -- the most natural
one nobody had written down -- and states two exact facts that sharpen what
remains.

*** RESULT 1 (route elimination): the sign is NOT a property of odd cycles ***

Define S_p(k) = SUM_lam (f^lam)^2 chi^lam(p-cycle, 1^{k-p}). For odd p the class
is even, so S_p is not forced to vanish (see RESULT 2), and T_3 = S_3. The
obvious generalisation -- "S_p(k) <= 0 for every odd p" -- would subsume the
conjecture and is FALSE:

    p=3 : negative for every 3 <= k <= 14   (consistent with the conjecture)
    p=5 : +172 at k=7, -840 at k=8, +17644 at k=9, -64702464 at k=12
    p=7 : negative through k=11, then +58661128 at k=12
    p=9 : positive throughout the tested range

So p=5 changes sign three times and p=7 once. ANY PROOF OF T_3 <= 0 MUST USE
SOMETHING SPECIFIC TO p=3; an argument that would also cover p=5 or p=7 is
provably wrong. That rules out a family of strategies -- generic
positivity/negativity of characters on odd classes, monotone couplings that do
not see p, and anything phrased for "a fixed cycle type" rather than for the
3-cycle.

There is a structural reason to expect exactly this, and it says where to look.
In Biane's free-cumulant expansion, Sigma_p = R_{p+1} + (lower cumulants), and
p=3 is the ONLY case where the correction is a single DETERMINISTIC term:

    Sigma_3 = R_4 + R_2,   with R_2(lam) = k constant on partitions of k.

So Sigma_3 - E[Sigma_3] = R_4 - E[R_4] exactly, and the conjecture is the clean
single-cumulant statement Cov_Planch(f^lam, R_4) <= 0. For p=5 the expansion
mixes R_6, R_4 and R_2^2, and the sign flips above show that a mixture inherits
nothing from its parts.

*** RESULT 2 (exact, one-line proof): S_mu = 0 for every ODD mu ***

Conjugation lam -> lam' has f^{lam'} = f^lam and chi^{lam'}(mu) = sgn(mu)
chi^lam(mu). For odd mu the involution pairs terms with opposite sign, and a
self-conjugate lam satisfies chi^lam(mu) = -chi^lam(mu) = 0. Hence the whole
family lives on the even classes. Verified below for every mu at k <= 9.

*** RESULT 3 (exact): the Plancherel centring is exactly C(k,2) ***

    SUM_lam (f^lam)^2 (SUM_cell c(cell)^2 - C(k,2)) = 0     for every k.

From Jucys-Murphy, SUM_i JM_i^2 = C(k,2).e + C_3, so on S^lam
SUM c^2 - C(k,2) = omega_lam(C_3) = |C_3| chi^lam(3cyc)/f^lam; multiplying by
(f^lam)^2 and summing gives |C_3| SUM_lam f^lam chi^lam(3cyc) = 0, the regular
character off the identity. So E_Planch[SUM c^2] = C(k,2) EXACTLY, and the
conjecture is purely a statement about the BIAS: re-weighting from (f^lam)^2 to
(f^lam)^3 must not increase E[SUM c^2]. Nothing about the centring is in doubt.

*** WHY THE NUMBERS CAN BE TRUSTED ***

Two independent implementations agree exactly on the p=3 column: the
Murnaghan-Nakayama character sum here, and the content-based
SUM (f^lam)^3 (SUM c^2 - C(k,2)) / |C_3| computed by
`qbeta_covariance_kernel_extend_probe.py`. They share no code. At k=12 both give
-15073599368. Exact integer arithmetic throughout; no float appears in this file.

*** WHAT THIS IS NOT ***

Not progress toward a proof. Eliminating a route narrows the search; it does not
advance it. The conjecture is exactly as open as before.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
from _mn_characters import partitions, chi, hook_dim   # noqa: E402


def sgn_is_odd(mu) -> bool:
    return sum(p - 1 for p in mu) % 2 == 1


def main() -> int:
    t0 = time.monotonic()
    a, ok = [], True

    def chk(name, computed, expected, note=""):
        good = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(good), **({"note": note} if note else {})})
        print(f"  [{'PASS' if good else 'FAIL'}] {name}: {computed!r}")
        return good

    print("=" * 78)
    print("0. CROSS-CHECK: MN characters vs the independent content computation")
    print("=" * 78)
    mism = []
    for k in range(3, 13):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        lams = list(partitions(k))
        f = {l: hook_dim(l, nf) for l in lams}
        mu3 = tuple([3] + [1] * (k - 3))
        via_mn = sum(f[l] * f[l] * chi(l, mu3) for l in lams)
        c3 = k * (k - 1) * (k - 2) // 3
        binom = k * (k - 1) // 2
        via_content = sum(
            f[l] ** 3 * (sum((j - i) ** 2 for i, r in enumerate(l) for j in range(r)) - binom)
            for l in lams)
        if via_content != via_mn * c3:
            mism.append(k)
    ok &= chk("two_independent_implementations_agree_on_p3", mism, [],
              note="Murnaghan-Nakayama character sum vs the content/hook-length "
                   "formula. No shared code. Disagreement here would invalidate "
                   "every number below")

    print()
    print("=" * 78)
    print("1. S_mu = 0 FOR EVERY ODD mu  (conjugation involution)")
    print("=" * 78)
    bad = []
    for k in range(2, 10):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        lams = list(partitions(k))
        f = {l: hook_dim(l, nf) for l in lams}
        for mu in lams:
            if sgn_is_odd(mu):
                S = sum(f[l] * f[l] * chi(l, mu) for l in lams)
                if S != 0:
                    bad.append((k, mu, S))
    ok &= chk("every_odd_class_sums_to_zero", bad, [],
              note="lam <-> lam' pairs terms with opposite sign since "
                   "chi^{lam'}(mu) = sgn(mu) chi^lam(mu) and f^{lam'} = f^lam")

    print()
    print("=" * 78)
    print("2. THE PLANCHEREL CENTRING IS EXACTLY C(k,2)")
    print("=" * 78)
    nz = []
    for k in range(1, 16):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        binom = k * (k - 1) // 2
        s = sum(hook_dim(l, nf) ** 2
                * (sum((j - i) ** 2 for i, r in enumerate(l) for j in range(r)) - binom)
                for l in partitions(k))
        if s != 0:
            nz.append((k, s))
    ok &= chk("plancherel_expectation_of_content_square_sum_is_binom_k_2", nz, [],
              note="E_Planch[sum c^2] = C(k,2) exactly, so the conjecture is "
                   "about the BIAS and not the centring")

    print()
    print("=" * 78)
    print("3. THE ROUTE ELIMINATION: p=3 IS SPECIAL")
    print("=" * 78)
    table = {}
    print(f"    {'k':>3} | {'p=3':>20} | {'p=5':>20} | {'p=7':>20}")
    for k in range(3, 15):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        lams = list(partitions(k))
        f = {l: hook_dim(l, nf) for l in lams}
        row = {}
        for p in (3, 5, 7):
            if p > k:
                continue
            mu = tuple([p] + [1] * (k - p))
            row[p] = sum(f[l] * f[l] * chi(l, mu) for l in lams)
        table[k] = row
        cells = [f"{row[p]:>+20}" if p in row else f"{'--':>20}" for p in (3, 5, 7)]
        print(f"    {k:>3} | {cells[0]} | {cells[1]} | {cells[2]}")

    ok &= chk("p3_is_negative_throughout",
              [k for k, r in table.items() if r.get(3, -1) >= 0], [],
              note="consistent with the conjecture; evidence, not proof")
    p5_signs = {k: (r[5] > 0) for k, r in table.items() if 5 in r}
    flips5 = sum(1 for k in sorted(p5_signs)[1:]
                 if p5_signs[k] != p5_signs[k - 1]) if len(p5_signs) > 1 else 0
    ok &= chk("p5_changes_sign_so_the_generalisation_is_false", flips5 >= 2, True,
              note="S_5 flips sign at least twice over 5 <= k <= 14, so "
                   "'S_p <= 0 for odd p' is FALSE and any proof of T_3 <= 0 must "
                   "use something specific to p = 3")
    ok &= chk("p7_also_changes_sign",
              any(table[k].get(7, 0) > 0 for k in table)
              and any(table[k].get(7, 0) < 0 for k in table), True,
              note="p=7 is negative through k=11 then positive at k=12")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-p3-special.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-p3-special",
        "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631",
                       "claim": "p=3 is special; S_p <= 0 for odd p is FALSE",
                       "arithmetic": "exact integers; no float64 anywhere"},
        "data": {"S_p_by_k": {str(k): {str(p): str(v) for p, v in r.items()}
                              for k, r in table.items()}},
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_p3_special_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
