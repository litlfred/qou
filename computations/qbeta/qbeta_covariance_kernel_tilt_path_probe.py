"""The tilt path: the conjecture as an integral of covariances, and why first order is not enough.

Epic `qou-x631`. After `qou-ml0m` the conjecture is rho(k) = E_Q[Sigma_3]/sd_P(Sigma_3) <= 0
with rho ~ -0.164, where Q ~ (f^lam)^3 and P ~ (f^lam)^2.

Embed both in one family: Q_t ~ (f^lam)^{2+t}, so t=0 is Plancherel and t=1 is Q.
Write g(t) = E_{Q_t}[Sigma_3] / sd_P(Sigma_3), so g(0) = 0 EXACTLY (qou-cze8) and
g(1) is the conjecture's quantity.

*** RESULT 1: g is monotone decreasing and markedly SUBLINEAR ***

Measured 16 <= k <= 40:

    g'(0) = -0.245 +/- 0.008       (linear response, stable)
    g(1)  = -0.164 +/- 0.015       (the conjecture's quantity)

A first-order expansion in the tilt predicts g(1) = g'(0) = -0.245 and the truth
is -0.164, so LINEAR RESPONSE OVERSHOOTS BY ~50% AND ABOUT A THIRD OF THE ANSWER
IS NONLINEAR. It gets worse further out: at k=40, linear predicts g(3) = -0.74
against an actual -0.374.

This settles a question route `qou-t5m1` has to answer before starting: a
first-order Sniady genus expansion in the tilt CANNOT produce -0.164. It would
produce about -0.245.

*** RESULT 2: a reformulation that restores first order ***

Since d/dt E_{Q_t}[X] = Cov_{Q_t}(log f^lam, X),

    E_Q[Sigma_3]  =  INTEGRAL_0^1  Cov_{Q_t}(log f^lam, Sigma_3)  dt .

So the conjecture FOLLOWS FROM the pointwise condition

    Cov_{Q_t}(log f^lam, Sigma_3)  <=  0     for all t in [0,1] ,

which is verified here for every k and t tested (values run from -0.245 at t=0 to
about -0.12 at t=1, monotone in magnitude).

This is the useful shape. Each instance is a COVARIANCE -- first order -- so a
genus expansion applies at each t, and the nonlinearity that defeated the direct
expansion is absorbed into the t-integration instead of having to be expanded.
Sufficient, not equivalent: the integral can be negative without the integrand
being so everywhere, and the pointwise claim is checked numerically only.

*** CONSISTENCY WITH THE EARLIER MEASUREMENT ***

`qou-ml0m` measured Cov_P(log f, Sigma_3) / E_Q[Sigma_3] = 1.44 +/- 0.19 and
called the linearisation quantitatively wrong. That ratio is exactly g'(0)/g(1),
and 0.245/0.164 = 1.49 -- the same number seen from the other side, now with an
explanation (the integrand decays over the path) rather than as a bare
discrepancy.

Floats are used for the tilted sums; every weight is formed as exp((2+t) log f - max)
so no overflow occurs, and the quantities compared carry three or more significant
figures against tolerances of 0.02.
"""
from __future__ import annotations

import json
import math  # float64-ok: remaining uses are display and the exact-integer falling factorial; the tilted sums themselves are mpmath (see g_and_deriv)
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()
sys.setrecursionlimit(10000)


def partitions(n: int, cap: int | None = None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hook_dim(lam, nfact: int) -> int:
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return nfact // prod


def falling(k: int, p: int) -> int:
    r = 1
    for i in range(p):
        r *= k - i
    return r


def rows_for(k: int):
    nf = 1
    for i in range(2, k + 1):
        nf *= i
    b = k * (k - 1) // 2
    out = []
    for lam in partitions(k):
        f = hook_dim(lam, nf)
        s3 = 3 * (sum((j - i) ** 2 for i, r in enumerate(lam) for j in range(r)) - b)
        # `mp.log` of the exact integer, not `math.log`. The tilted sums below
        # ACCUMULATE these over every partition of k -- 37,338 of them at
        # k = 40 -- which is an aggregate over a large sample, the case
        # AGENTS.md names specifically. Measured before changing it: the old
        # float64 accumulation was accurate to ~1.5e-14 relative, so this moves
        # nothing the probe asserts (its tolerances are 0.02); what it changes
        # is that the RECORD now carries digits that were actually computed
        # rather than a 53-bit value rendered to 60 places.
        out.append((mp.log(mp.mpf(f)), s3))
    return out


def g_and_deriv(rows, t, sd):
    e = 2 + t
    m = max(e * lf for lf, _ in rows)
    den = sL = sS = sLS = mp.mpf(0)
    for lf, s3 in rows:
        w = mp.exp(e * lf - m)
        den += w
        sL += w * lf
        sS += w * s3
        sLS += w * lf * s3
    mean = sS / den
    cov = sLS / den - (sL / den) * mean
    return mean / sd, cov / sd


def main() -> int:
    t0 = time.monotonic()
    a, ok = [], True

    def chk(name, computed, expected, note=""):
        good = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(good), **({"note": note} if note else {})})
        print(f"  [{'PASS' if good else 'FAIL'}] {name}: {computed!r}")
        return good

    ks = (16, 20, 24, 28, 32, 36, 40)
    # mpf from the literals, not floats: these are DECLARED path points that
    # get written to the witness, and `e = 2 + t` feeds them into the tilted
    # sums. Carrying them as mpf keeps the whole path in one arithmetic.
    ts = tuple(mp.mpf(x) for x in ("0", "0.25", "0.5", "0.75", "1"))
    gvals, dvals = {}, {}
    print("=" * 78)
    print("g(t) = E_{Q_t}[Sigma_3]/sd_P(Sigma_3)   and   g'(t) = Cov_{Q_t}(log f, Sigma_3)/sd")
    print("=" * 78)
    print(f"    {'k':>3} |" + "".join(f"{('g('+str(t)+')'):>10}" for t in ts)
          + " |" + "".join(f"{chr(39)+'('+str(t)+')':>10}" for t in ts))
    pos_g, pos_d, nonmono = [], [], []
    for k in ks:
        rows = rows_for(k)
        sd = math.sqrt(3 * falling(k, 3))
        gs, ds = [], []
        for t in ts:
            g, d = g_and_deriv(rows, t, sd)
            gs.append(g)
            ds.append(d)
        gvals[k], dvals[k] = gs, ds
        if any(g > 1e-12 for g in gs):
            pos_g.append(k)
        if any(d > 0 for d in ds):
            pos_d.append(k)
        if any(gs[i + 1] > gs[i] + 1e-12 for i in range(len(gs) - 1)):
            nonmono.append(k)
        print(f"    {k:>3} |" + "".join(f"{v:>+10.4f}" for v in gs)
              + " |" + "".join(f"{v:>+10.4f}" for v in ds))

    ok &= chk("g_is_nonpositive_on_the_whole_path", pos_g, [],
              note="not just at t=1; the conjecture appears to hold for the whole "
                   "tilt family")
    ok &= chk("derivative_is_nonpositive_on_[0,1]", pos_d, [],
              note="Cov_{Q_t}(log f, Sigma_3) <= 0, which by "
                   "E_Q[Sigma_3] = int_0^1 Cov_{Q_t} dt SUFFICES for the "
                   "conjecture. Sufficient, not equivalent, and checked "
                   "numerically only")
    ok &= chk("g_is_monotone_decreasing", nonmono, [])

    lin = [dvals[k][0] for k in ks]
    act = [gvals[k][-1] for k in ks]
    ratios = [lin[i] / act[i] for i in range(len(ks))]
    lo, hi = min(ratios), max(ratios)
    ok &= chk("linear_response_overshoots_by_about_half",
              bool(1.3 < lo and hi < 1.8), True,
              note=f"g'(0)/g(1) in [{lo:.3f}, {hi:.3f}]. A first-order expansion "
                   "in the tilt predicts about -0.245 where the truth is -0.164, "
                   "so a first-order genus expansion cannot produce the constant")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-tilt-path.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-tilt-path",
        "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631",
                       "claim": "g is sublinear; the conjecture follows from "
                                "Cov_{Q_t}(log f, Sigma_3) <= 0 on [0,1]"},
        "data": {"g_by_k": {str(k): [fmt(v) for v in gvals[k]] for k in ks},
                 "gprime_by_k": {str(k): [fmt(v) for v in dvals[k]] for k in ks},
                 "t_values": [fmt(t) for t in ts]},
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_tilt_path_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
