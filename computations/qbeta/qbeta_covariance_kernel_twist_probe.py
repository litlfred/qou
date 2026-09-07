#!/usr/bin/env python3
"""Self-duality and the Frobenius pairing: what the quadratic twist does and does not give.

Epic `qou-x631`, T_3(k) = SUM_lam (f^lam)^2 chi^lam(3-cyc) <= 0.

There IS a quadratic twist here, and it is the only one S_k has: twisting by the
sign character sends S^lam to S^{lam'}, so "self-dual" means self-conjugate and
the twist involution is transposition of the Young diagram. This probe settles
what that structure buys.

*** WHAT IT GIVES (1): a one-line proof that S_mu = 0 on odd classes ***

Let P_k := SUM_lam (f^lam)^2 s_lam, so S_mu = <p_mu, P_k> in the Hall (Frobenius)
pairing. The involution omega has omega(s_lam) = s_{lam'} and
omega(p_mu) = eps_mu p_mu with eps_mu = sgn. Since f^{lam'} = f^lam, P_k is
omega-INVARIANT; and omega is an ISOMETRY of the pairing. Hence

    S_mu = <omega p_mu, omega P_k> = eps_mu S_mu ,

so S_mu = 0 whenever eps_mu = -1. The whole family lives on even classes, and
this derivation is cleaner than the term-pairing argument in
`qbeta_covariance_kernel_p3_special_probe.py` -- it is orthogonality of the two
omega-eigenspaces, nothing more.

*** WHAT IT GIVES (2): two-sided bounds, from positivity ***

A := SUM_lam f^lam e_lam acts on the lam-block by f^lam > 0, so A is a POSITIVE
element of C[S_k] and sigma -> A(sigma) = T_{type(sigma)}/k! is a
positive-definite function. Restricting a positive-definite function to a
subgroup keeps it positive-definite, so SUM_{h in H} A(h) >= 0 for every H:

    H = <3-cycle> = Z/3 :   M(k) + 2 T_3(k)                 >= 0
    H = A_4             :   M(k) + 3 T_{(2,2,1^{k-4})} + 8 T_3(k) >= 0

with M(k) = SUM_lam (f^lam)^3. Both verified below. Cauchy-Schwarz on the same
positivity gives |S_mu| <= M(k).

*** WHAT IT DOES NOT GIVE -- AND THIS IS THE POINT ***

Every constraint positivity yields is a LOWER bound on T_3. The conjecture is an
UPPER bound (T_3 <= 0). The quadratic structure is SIGN-BLIND in the direction
needed, and the bounds are not close: at k = 13, T_3 is about -5.1e11 against a
Z/3 bound of -4.4e13, two orders of magnitude of slack.

*** ROUTE ELIMINATED: splitting by the twist orbit ***

The natural refinement suggested by self-duality is to split the sum into
self-dual shapes and 2-element twist orbits, T_3 = SC + PR, and prove each piece
negative. BOTH PIECES CHANGE SIGN:

    SC > 0 at k = 7 (+800) and k = 9 (+38416)
    PR > 0 at k = 3, 4, 6 (+252) and k = 10 (+3015552)

so no argument that treats self-dual and paired shapes separately can work; the
negativity of T_3 is a genuine cancellation between the two. This is a different
elimination from the epic's earlier "sub-family sign-definiteness" (two-row
flips, hooks), which concerned shape families rather than the twist orbit.

Exact integer arithmetic throughout; no float decides any assertion.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
from _mn_characters import partitions, chi, hook_dim   # noqa: E402


def conjugate(lam):
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0])) if lam else ()


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
    print("1. THE TWIST ORBIT SPLIT DOES NOT REFINE THE CONJECTURE")
    print("=" * 78)
    print(f"    {'k':>3} | {'T_3':>16} | {'SC (self-dual)':>17} | {'PR (pairs)':>17}")
    sc_pos, pr_pos, data = [], [], {}
    for k in range(3, 15):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        lams = list(partitions(k))
        f = {l: hook_dim(l, nf) for l in lams}
        mu = tuple([3] + [1] * (k - 3))
        SC = sum(f[l] ** 2 * chi(l, mu) for l in lams if conjugate(l) == l)
        PR = sum(f[l] ** 2 * chi(l, mu) for l in lams if conjugate(l) != l)
        data[k] = (SC + PR, SC, PR)
        if SC > 0:
            sc_pos.append(k)
        if PR > 0:
            pr_pos.append(k)
        print(f"    {k:>3} | {SC+PR:>16} | {SC:>17} | {PR:>17}")

    ok &= chk("self_dual_part_changes_sign", sc_pos, [7, 9],
              note="SC > 0 at k=7 (+800) and k=9 (+38416), so the self-dual part "
                   "is not negative on its own")
    ok &= chk("paired_part_changes_sign", pr_pos, [3, 4, 6, 10],
              note="PR > 0 at four values, so the paired part is not negative on "
                   "its own either. T_3 <= 0 is a genuine cancellation between "
                   "the two twist orbits")

    print()
    print("=" * 78)
    print("2. POSITIVITY GIVES LOWER BOUNDS ONLY -- IT CANNOT REACH T_3 <= 0")
    print("=" * 78)
    print(f"    {'k':>3} | {'T_3':>16} | {'Z/3 bound -M/2':>18} | {'A_4 bound':>18}")
    viol = []
    for k in range(4, 14):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        lams = list(partitions(k))
        f = {l: hook_dim(l, nf) for l in lams}
        M = sum(f[l] ** 3 for l in lams)
        T3 = sum(f[l] ** 2 * chi(l, tuple([3] + [1] * (k - 3))) for l in lams)
        T22 = sum(f[l] ** 2 * chi(l, tuple([2, 2] + [1] * (k - 4))) for l in lams)
        z3, a4 = Fraction(-M, 2), Fraction(-(M + 3 * T22), 8)
        if not (T3 >= z3 and T3 >= a4):
            viol.append(k)
        print(f"    {k:>3} | {T3:>16} | {float(z3):>18.1f} | {float(a4):>18.1f}")  # float64-ok: display of the two bounds only; the comparison that decides the assertion is T3 >= z3 and T3 >= a4 on exact Fractions, above
    ok &= chk("positive_definiteness_bounds_hold", viol, [],
              note="sum_{h in H} A(h) >= 0 for H = Z/3 and H = A_4, where "
                   "A = sum_lam f^lam e_lam is positive. BOTH ARE LOWER BOUNDS; "
                   "the conjecture is an upper bound, so this structure is "
                   "sign-blind in the needed direction")

    print()
    print("=" * 78)
    print("3. THE omega-ISOMETRY PROOF OF THE ODD-CLASS VANISHING")
    print("=" * 78)
    bad = []
    for k in range(2, 10):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        lams = list(partitions(k))
        f = {l: hook_dim(l, nf) for l in lams}
        for mu in lams:
            if sum(p - 1 for p in mu) % 2 == 1:
                if sum(f[l] ** 2 * chi(l, mu) for l in lams) != 0:
                    bad.append((k, mu))
    ok &= chk("odd_classes_vanish_by_omega_orthogonality", bad, [],
              note="P_k = sum (f^lam)^2 s_lam is omega-invariant, p_mu is "
                   "omega-anti-invariant for odd mu, and omega is an isometry of "
                   "the Frobenius pairing -- so the two are orthogonal")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-twist.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-twist",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631",
                       "claim": "the quadratic twist is conjugation; it proves the "
                                "odd-class vanishing and gives lower bounds only",
                       "arithmetic": "exact integers and Fractions"},
        "data": {"T3_SC_PR_by_k": {str(k): [str(x) for x in v] for k, v in data.items()}},
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_twist_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
