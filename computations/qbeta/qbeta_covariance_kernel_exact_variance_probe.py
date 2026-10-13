"""Exact Plancherel second moments: Var(Sigma_3) = 3(k)_3, and the conjecture as a correlation.

Epic `qou-x631`, T_3(k) = SUM_lam (f^lam)^2 chi^lam(3-cyc) <= 0.

`qou-ujil` located the margin at the scale k^{3/2} and cited Kerov's CLT for the
Plancherel standard deviation sqrt(3) k^{3/2}. That constant is not merely
asymptotic. It is EXACT for every k, and the derivation is elementary.

*** RESULT 1: Var_P(Sigma_p) = (k)_p^2 / |C_p|, so Var_P(Sigma_3) = 3 (k)_3 ***

Sigma_p(lam) = (k)_p chi^lam(p-cyc)/f^lam, so (f^lam)^2 Sigma_p Sigma_q collapses
to (k)_p (k)_q chi^lam(p) chi^lam(q) -- the f^lam cancel completely. Summing over
lam is then CHARACTER COLUMN ORTHOGONALITY:

    SUM_lam chi^lam(sigma) chi^lam(tau) = |C_G(sigma)| if sigma ~ tau, else 0.

Hence for p != q the mixed moment vanishes EXACTLY, and

    Var_P(Sigma_3) = (k)_3^2 / |C_3| = (k)_3^2 * 3/(k)_3 = 3 k(k-1)(k-2).

Verified against a direct computation for 4 <= k <= 12. Asymptotically
sqrt(3) k^{3/2}, matching the CLT, but here it is an identity at every k.

*** RESULT 2: the Sigma_p are EXACTLY uncorrelated under Plancherel ***

Not just asymptotically independent, which is what the CLT provides. E_P[Sigma_p
Sigma_q] = 0 for every p != q and every k, by the same orthogonality.

*** RESULT 3: the conjecture is a correlation coefficient near -0.16 ***

With an exact denominator,

    rho(k) := E_Q[Sigma_3] / sd_P(Sigma_3)  =  -0.164 +/- 0.015   for 10 <= k <= 42

and the conjecture is exactly rho(k) <= 0. So the target for route `qou-t5m1` is a
single dimensionless number, and a derivation can be checked against -0.164
rather than against a sign.

*** A SELF-CORRECTION WORTH RECORDING ***

I first attributed the vanishing of E_P[Sigma_p Sigma_q] to the quadratic twist:
Sigma_p(lam') = (-1)^{p-1} Sigma_p(lam), so the product is omega-odd when exactly
one of p,q is even, forcing it to vanish. That reasoning is correct but SUBSUMED
-- orthogonality kills the mixed moment for ALL p != q, including the pairs the
parity argument leaves free (measured: (3,5) and (2,4) also vanish). The twist is
genuinely needed only for S_mu = 0 on odd classes, which is a TRIPLE product
SUM_lam chi(e) chi(e) chi(mu) and is not an orthogonality relation.

*** AND ONE THING THAT DOES NOT WORK ***

Q ~ (f^lam)^3 is P ~ (f^lam)^2 tilted by f^lam = exp(log f^lam), so one hopes
E_Q[Sigma_3] ~= Cov_P(log f^lam, Sigma_3). Measured, the ratio is 1.44 +/- 0.19
over 6 <= k <= 30 with no trend: the linearisation gets the SIGN and the SCALE
right and the CONSTANT wrong, so it cannot be used to transfer the inequality.
The exact statement remains E_Q[Sigma_3] = Cov_P(f^lam, Sigma_3)/E_P[f^lam].
"""
from __future__ import annotations

import json
import math  # float64-ok: sqrt for the exact-integer variance denominator, and display; every assertion is decided on exact Fractions or integers
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as _mpm  # NOT `mp`: this module already binds `mp` to a partition

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()
from _mn_characters import partitions, chi, hook_dim   # noqa: E402


def falling(k: int, p: int) -> int:
    r = 1
    for i in range(p):
        r *= k - i
    return r


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
    print("1. Var_P(Sigma_3) = 3 (k)_3, EXACTLY")
    print("=" * 78)
    bad_var, bad_mixed = [], []
    for k in range(4, 13):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        lams = list(partitions(k))
        mu3 = tuple([3] + [1] * (k - 3))
        var = Fraction(falling(k, 3) ** 2 * sum(chi(l, mu3) ** 2 for l in lams), nf)
        if var != 3 * falling(k, 3):
            bad_var.append(k)
        for (p, q) in [(2, 3), (3, 5), (2, 4), (3, 4)]:
            if p > k or q > k:
                continue
            mp = tuple([p] + [1] * (k - p))
            mq = tuple([q] + [1] * (k - q))
            m = Fraction(falling(k, p) * falling(k, q)
                         * sum(chi(l, mp) * chi(l, mq) for l in lams), nf)
            if m != 0:
                bad_mixed.append((k, p, q))
        print(f"    k={k:>3}  Var = {var}   3(k)_3 = {3*falling(k,3)}")

    ok &= chk("variance_matches_closed_form", bad_var, [],
              note="(f^lam)^2 Sigma_p Sigma_q = (k)_p (k)_q chi(p) chi(q): the "
                   "f^lam cancel, and column orthogonality gives "
                   "Var = (k)_3^2/|C_3| = 3(k)_3")
    ok &= chk("mixed_moments_vanish_for_all_distinct_p_q", bad_mixed, [],
              note="EXACT uncorrelatedness, stronger than the CLT's asymptotic "
                   "independence. Includes (3,5) and (2,4), which the omega-parity "
                   "argument leaves free -- so orthogonality, not the twist, is "
                   "what kills these")

    print()
    print("=" * 78)
    print("2. THE CONJECTURE AS A CORRELATION COEFFICIENT")
    print("=" * 78)
    rho = {}
    rho_mp: dict[int, object] = {}
    exact_eq: dict[int, str] = {}
    for k in range(10, 43, 2):
        nf = 1
        for i in range(2, k + 1):
            nf *= i
        b = k * (k - 1) // 2
        M = cov = 0
        for lam in partitions(k):
            fl = hook_dim(lam, nf)
            c2 = sum((j - i) ** 2 for i, r in enumerate(lam) for j in range(r))
            f3 = fl ** 3
            M += f3
            cov += f3 * (c2 - b)
        r = float(Fraction(3 * cov, M)) / math.sqrt(3 * falling(k, 3))  # float64-ok: numerator is an exact Fraction, denominator an exact integer under one sqrt; the assertion tests rho against bounds with 0.03 of slack, far outside double precision
        rho[k] = r
        # THE RECORD, separately from the test. The float above is untouched
        # and its justification stands -- it decides an assertion with 0.03 of
        # slack. But the witness is not a test: a probe's numbers are read
        # later by things that never re-derive them, so the serialized rho is
        # carried in mpf from the exact Fraction over the exact integer, and
        # E_Q[Sigma_3] = 3cov/M is recorded EXACTLY as num/den. Same treatment
        # as the sibling `qbeta_covariance_kernel_scale_probe`.
        exact_eq[k] = f"{3 * cov}/{M}"
        rho_mp[k] = (_mpm.mpf(3 * cov) / _mpm.mpf(M)
                     / _mpm.sqrt(_mpm.mpf(3 * falling(k, 3))))
        print(f"    k={k:>3}  rho = {r:>+9.5f}")

    lo, hi = min(rho.values()), max(rho.values())
    ok &= chk("rho_is_negative_and_order_one", bool(-0.20 < lo and hi < -0.13), True,
              note=f"observed [{lo:.5f}, {hi:.5f}] over k=10..42. The conjecture is "
                   "rho(k) <= 0, so route qou-t5m1 has a single dimensionless "
                   "target near -0.164 to check a derivation against, not a sign")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-exact-variance.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-exact-variance",
        "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631",
                       "claim": "Var_P(Sigma_3) = 3(k)_3 exactly; the conjecture is "
                                "rho(k) <= 0 with rho ~ -0.164"},
        "data": {
            "rho_by_k": {str(k): fmt(rho_mp[k]) for k in sorted(rho_mp)},
            "eq_sigma3_exact": exact_eq,
        },
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_exact_variance_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
