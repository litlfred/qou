"""A2 fractional-moment family probe (epic qou-x631, attack qou-ogrk).

The moment skeleton's proved anchors are the EVEN hook-power moments
M_{2j} = Sigma_v v^{2j} nu_v > 0 (exact polynomials in n; audit
2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md), while the
A2 target weight ln(v) is concave and outside the even-power cone, and the
pointwise route is falsified (n >= 29). This probe tests the ONE-PARAMETER
INTERPOLATION between them:

    M_alpha(n) = Sigma_v v^alpha * nu_v,   nu_v = Cov_Planch(N_v, omega3),

for real alpha > 0. The exact bridge to A2 (finite sums, mean-zero):

    Sigma_v nu_v = 0  ==>  M_alpha = Sigma_v (v^alpha - 1) nu_v
                          = alpha * Sigma_v ln(v) nu_v + O(alpha^2),

so  A2  <=>  M'(0+) >= 0, i.e. A2 is exactly the SMALL-alpha positivity of
the fractional-moment family whose alpha = 2,4,6 members are proved positive.
The candidate sharpening tested here:

    (FMP)  M_alpha(n) >= 0 for ALL alpha > 0 and n >= 3?

If FMP holds on the tested window it is the new sharpest intermediate target
(it implies A2 in the limit alpha -> 0+ by M(0) = 0, M >= 0 near 0 =>
one-sided derivative >= 0). If it fails at some (alpha, n), the failure locus
maps the cone boundary between the proved unbounded-convex weights and the
falsified bounded family 1 - e^{-sv}.

Exact layer: nu_v computed in exact Fractions (integer hook spectra, integer
f^lambda via the hook-length formula, Plancherel weight f^2/n!). Float enters
only in v^alpha at evaluation; margins are reported so float noise is
auditable (min |M_alpha| at sign decisions >> 1e-9 * scale).

Vanilla python (no mpmath — sandbox constraint); exact Fractions + math.log.
Expected runtime ~1-2 min to n=30 (progress lines per n, tee-friendly).
"""

import json
import math
import sys
import time
from fractions import Fraction

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent

N_MAX = 30
ALPHA_GRID = [a / 100 for a in range(2, 101, 2)] + [a / 20 for a in range(21, 121)]
# 0.02..1.00 step .02, then 1.05..6.00 step .05


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield []
        return
    for i in range(min(n, maxp), 0, -1):
        for r in partitions(n - i, i):
            yield [i] + r


def conj(l):
    if not l:
        return []
    return [sum(1 for x in l if x > j) for j in range(l[0])]


def hooks(l):
    c = conj(l)
    out = []
    for i, li in enumerate(l):
        for j in range(li):
            out.append(li + c[j] - j - i - 1)
    return out


def f_dim(l, hks):
    p = 1
    for h in hks:
        p *= h
    return math.factorial(sum(l)) // p


def content_sq(l):
    return sum((j - i) ** 2 for i, li in enumerate(l) for j in range(li))


def nu_exact(n):
    """nu_v = Cov_Planch(N_v, omega3) as exact Fractions, v = 1..2n."""
    fact = math.factorial(n)
    C2 = n * (n - 1) // 2
    # accumulate E[N_v * omega3] and E[N_v]; E[omega3] = 0 exactly (checked)
    e_nv_om = {}
    e_nv = {}
    e_om = Fraction(0)
    for lam in partitions(n):
        hks = hooks(lam)
        f = f_dim(lam, hks)
        w = Fraction(f * f, fact)
        om = content_sq(lam) - C2
        e_om += w * om
        spec = {}
        for h in hks:
            spec[h] = spec.get(h, 0) + 1
        for v, cnt in spec.items():
            e_nv_om[v] = e_nv_om.get(v, Fraction(0)) + w * cnt * om
            e_nv[v] = e_nv.get(v, Fraction(0)) + w * cnt
    assert e_om == 0, f"E[omega3] != 0 at n={n}: {e_om}"
    nu = {}
    for v in e_nv:
        nu[v] = e_nv_om[v] - e_nv[v] * e_om  # e_om = 0, kept for form
    return nu


def main():
    t0 = time.time()
    results = []
    fmp_holds = True
    worst = None  # (M_alpha_min_scaled, n, alpha)
    for n in range(3, N_MAX + 1):
        nu = nu_exact(n)
        # exact checks: zeroth and second moments
        m0 = sum(nu.values())
        m2 = sum(Fraction(v * v) * x for v, x in nu.items())
        m2_expected = Fraction(n * (n - 1) * (n - 2), 3)
        assert m0 == 0, f"zeroth moment != 0 at n={n}"
        assert m2 == m2_expected, f"M2 mismatch at n={n}: {m2} vs {m2_expected}"
        log_moment = sum(math.log(v) * float(x) for v, x in nu.items())
        scan = []
        min_ma, min_alpha = None, None
        for a in ALPHA_GRID:
            ma = sum((v ** a) * float(x) for v, x in nu.items())
            scan.append((a, ma))
            if min_ma is None or ma < min_ma:
                min_ma, min_alpha = ma, a
        # small-alpha ratio check: M_alpha/alpha -> log_moment
        a_small = ALPHA_GRID[0]
        ratio = scan[0][1] / a_small
        neg = [(a, ma) for a, ma in scan if ma < 0]
        if neg:
            fmp_holds = False
        scale = max(abs(ma) for _, ma in scan)
        margin = min_ma / scale if scale > 0 else 0.0
        if worst is None or margin < worst[0]:
            worst = (margin, n, min_alpha)
        results.append({
            "n": n,
            "log_moment": log_moment,
            "log_moment_nonneg": log_moment >= 0,
            "M_alpha_min": min_ma,
            "argmin_alpha": min_alpha,
            "min_over_scale": margin,
            "small_alpha_ratio": ratio,
            "ratio_vs_log_moment_relerr":
                abs(ratio - log_moment) / abs(log_moment) if log_moment != 0 else None,
            "n_negative_alphas": len(neg),
            "negative_alphas": neg[:5],
        })
        print(f"n={n:3d}  logM={log_moment:+.6e}  minM_a={min_ma:+.6e} "
              f"@a={min_alpha:.2f}  margin={margin:+.4f}  "
              f"neg_alphas={len(neg)}  t={time.time()-t0:6.1f}s", flush=True)
    verdict = {
        "FMP_holds_on_window": fmp_holds,
        "window": {"n_max": N_MAX, "alpha_grid": [ALPHA_GRID[0], ALPHA_GRID[-1]]},
        "worst_margin": {"min_over_scale": worst[0], "n": worst[1], "alpha": worst[2]},
        "A2_log_moment_nonneg_all_n": all(r["log_moment_nonneg"] for r in results),
        "interpretation": (
            "FMP (M_alpha >= 0 for all alpha > 0) "
            + ("HOLDS" if fmp_holds else "FAILS")
            + " on the tested window. A2 <=> M'(0+) >= 0 is the alpha->0+ boundary "
            "of this family; the proved even moments are its alpha = 2,4,6 anchors. "
            "Exact layer: nu_v in Fractions; zeroth moment == 0 and "
            "M2 == n(n-1)(n-2)/3 asserted exactly per n."
        ),
    }
    out = {
        "description": (
            "A2 fractional-moment family M_alpha = Sigma v^alpha nu_v: exact nu_v "
            "(Fraction), alpha-scan, small-alpha bridge M_alpha/alpha -> log moment "
            "(= A2). Tests FMP: M_alpha >= 0 for all alpha > 0."
        ),
        "epic": "qou-x631",
        "attack": "qou-ogrk (A2), fractional-moment interpolation angle",
        "verdict": verdict,
        "per_n": results,
        "runtime_s": f"{time.time() - t0:.3f}",
    }
    path = (_HERE_W / "wlambda-covariance-epic-A2-fractional-moment-family.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(path, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        out.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            out, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(out, fh, indent=1, default=str)
    print(f"\nverdict: FMP {'HOLDS' if fmp_holds else 'FAILS'} on window; "
          f"worst margin {worst[0]:+.4f} at n={worst[1]}, alpha={worst[2]:.2f}")
    print(f"witness -> {path}  ({time.time()-t0:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
