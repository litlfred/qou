"""Iterated-limit closure of the dilog Part-B W-P1 residual — numerical sanity check.

Context: `conj:dilogarithm-archimedean-limit`, Part B, piece W-P1.
Coordination ledger: docs/coordination/dilog-part-b-cusp-attack.md.

The *joint* limit `(q-1)*log(1-x q^n) -> 0` is non-uniform (proved false along a
resonant subsequence; see dilog_partb_wp1_residual_uniformity_probe.py). This probe
verifies the *iterated-limit* reading that SIDESTEPS the wall entirely and needs NO
Diophantine hypothesis — the path flagged in the ledger and PR #4299 as the honest
closeable route to W-P1.

Building block already proved sorry-free in Lean (DilogPartBBranchPointSum.lean,
`wp1_riemann_bound`, PR #4262): for `1 < q`, `x q^n < 1`,

    0 <= (Li2(x q^n) - Li2(x)) - (1-q) * sum_{k<n} log(1 - x q^k)
      <= (q-1)*(-log(1 - x q^n)) - (q-1)*q^n*(-log(1-x)).           (WP1BOUND)

Iterated limit:
  * INNER (bulk, q -> 1+, rho fixed in (x,1)): choose n = n(q) = max{n : x q^n <= rho}
    (endpoint bounded away from the branch point u=1/x). Then x q^{n(q)} -> rho^- as
    q -> 1+, so Li2(x q^{n(q)}) -> Li2(rho); and the RHS majorant -> 0 because
    -log(1 - x q^n) <= -log(1 - rho) is BOUNDED (this is where the Diophantine
    subtlety is avoided). Hence

        WP1_rho(q) := -(1-q) * sum_{k<n(q)} log(1 - x q^k)  ->  Li2(x) - Li2(rho).

  * OUTER (rho -> 1-): Li2(x) - Li2(rho) -> Li2(x) - pi^2/6  (Abel / left-continuity
    of Li2 at 1; Lean brick `tendsto_LiTwo_nhdsWithin_lt_one`, sorry-free).

  Combined iterated limit = Li2(x) - pi^2/6 = the W-P1 target. No Diophantine input.

This script confirms both stages numerically at 50 dps and checks the residual
against (WP1BOUND). It computes nothing wired to production; it is a route-soundness
check ahead of the Lean assembly.
"""

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def li2(z):
    return mp.polylog(2, z)


def n_of_q(x, q, rho):
    """max{n >= 0 : x q^n <= rho}. For q>1, x q^n increases in n, so this is the
    largest n keeping the endpoint at/below the bulk cutoff rho."""
    # x q^n <= rho  <=>  n <= log(rho/x)/log(q)
    import math
    val = mp.log(rho / x) / mp.log(q)
    n = int(mp.floor(val))
    if n < 0:
        n = 0
    return n


def wp1_rho(x, q, n):
    """-(1-q) * sum_{k<n} log(1 - x q^k) = (q-1) * sum_{k<n} log(1 - x q^k) * (-1)...
    careful: -(1-q) = (q-1). We compute (q-1) * sum_{k<n} [ -log? ] — no:
    W-P1 as defined in the ledger is  -(1-q) * sum log(1 - x q^k).
    Each factor 1 - x q^k > 0 for k < n(q) (endpoint <= rho < 1), so log(1-x q^k) < 0,
    the sum is negative, and -(1-q)=+(q-1)>0 times a negative sum is negative... but
    Li2(x)-Li2(rho) < 0 too (rho>x => Li2(rho)>Li2(x)). Consistent."""
    s = mp.mpf(0)
    for k in range(n):
        s += mp.log(1 - x * q ** k)
    return -(1 - q) * s


def wp1_bound_rhs(x, q, n):
    """RHS majorant of (WP1BOUND): (q-1)*(-log(1-x q^n)) - (q-1)*q^n*(-log(1-x))."""
    xqn = x * q ** n
    return (q - 1) * (-mp.log(1 - xqn)) - (q - 1) * q ** n * (-mp.log(1 - x))


def check_inner(x, rho, qs):
    """Bulk stage: WP1_rho(q) -> Li2(x) - Li2(rho) as q -> 1+, with the residual
    (Li2(x q^n) - Li2(x)) - (1-q) sum ... squeezed by (WP1BOUND)."""
    target = li2(x) - li2(rho)
    print(f"  INNER  x={float(x):.4f}  rho={float(rho):.6f}  "
          f"target Li2(x)-Li2(rho) = {mp.nstr(target, 12)}")
    print(f"    {'q':>12} {'n(q)':>6} {'x q^n':>12} {'WP1_rho(q)':>16} "
          f"{'|WP1-target|':>14} {'residual':>12} {'bound(WP1)':>12} {'ok':>4}")
    ok_all = True
    last_err = mp.mpf("nan")
    errs = []
    for q in qs:
        n = n_of_q(x, q, rho)
        if n > 60000:
            print(f"    {float(q):>12.8f} {n:>6d}  (skipped: n too large for explicit sum)")
            continue
        xqn = x * q ** n
        # compute the partial sum ONCE and derive both wp1 and the residual E
        s = mp.mpf(0)
        qk = mp.mpf(1)
        for _ in range(n):
            s += mp.log(1 - x * qk)
            qk *= q
        wp1 = -(1 - q) * s
        # residual of (WP1BOUND): E = (Li2(x q^n)-Li2(x)) - (1-q) sum log(1-x q^k)
        E = (li2(xqn) - li2(x)) - (1 - q) * s
        rhs = wp1_bound_rhs(x, q, n)
        tol = mp.mpf(10) ** (-20)
        bound_ok = (E >= -tol) and (E <= rhs + tol)
        ok_all = ok_all and bound_ok
        last_err = abs(wp1 - target)
        errs.append(last_err)
        print(f"    {float(q):>12.8f} {n:>6d} {float(xqn):>12.8f} "
              f"{mp.nstr(wp1, 10):>16} {mp.nstr(last_err, 4):>14} "
              f"{mp.nstr(E, 4):>12} {mp.nstr(rhs, 4):>12} {str(bound_ok):>4}")
    monotone = all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
    print(f"    => inner converges to Li2(x)-Li2(rho): final |err| = {mp.nstr(errs[-1], 6)}, "
          f"error strictly decreasing: {monotone}, bound-respected all rows: {ok_all}")
    return monotone and ok_all, ok_all


def check_outer(x, rhos):
    """Outer stage: Li2(x) - Li2(rho) -> Li2(x) - pi^2/6 as rho -> 1-."""
    wp1_target = li2(x) - mp.pi ** 2 / 6
    print(f"  OUTER  x={float(x):.4f}  W-P1 target Li2(x)-pi^2/6 = {mp.nstr(wp1_target, 12)}")
    errs = []
    for rho in rhos:
        val = li2(x) - li2(rho)
        e = abs(val - wp1_target)
        errs.append(e)
        print(f"    rho={float(rho):.8f}  Li2(x)-Li2(rho) = {mp.nstr(val, 12)}  "
              f"|.. - target| = {mp.nstr(e, 6)}")
    monotone = all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
    print(f"    => outer converges to Li2(x)-pi^2/6: final |err| = {mp.nstr(errs[-1], 6)}, "
          f"error strictly decreasing: {monotone}")
    return monotone


def main():
    print("=" * 78)
    print(f"Iterated-limit closure of dilog Part-B W-P1 residual ({mp.mp.dps} dps)")
    print("Route: bulk (q->1+, rho fixed) then rho->1- ; NO Diophantine input.")
    print("=" * 78)

    all_ok = True
    for x in [mp.mpf("0.3"), mp.mpf("0.7")]:
        print(f"\n### x = {float(x)}")
        # OUTER: rho -> 1-
        rhos = [mp.mpf("0.9"), mp.mpf("0.99"), mp.mpf("0.999"),
                mp.mpf("0.9999"), mp.mpf("0.99999")]
        outer_ok = check_outer(x, rhos)

        # INNER: for a representative bulk cutoff rho, q -> 1+
        for rho in [mp.mpf("0.9"), mp.mpf("0.99")]:
            qs = [mp.mpf("1") + mp.mpf(10) ** (-e) for e in range(2, 5)]  # 1.01, 1.001, 1.0001
            inner_ok, bound_ok = check_inner(x, rho, qs)
            all_ok = all_ok and inner_ok and bound_ok
        all_ok = all_ok and outer_ok

    print("\n" + "=" * 78)
    print(f"ROUTE SOUND (both stages converge + (WP1BOUND) respected everywhere): {all_ok}")
    print("Interpretation: the iterated limit closes W-P1 -> Li2(x) - pi^2/6 with no")
    print("Diophantine hypothesis. Combined with W-P2 (Dedekind-eta, #4191) this gives")
    print("reg_n -> Li2(x) - pi^2/3 under the iterated ordering. This is a WEAKER")
    print("statement than the joint limit (which is proved-false unconditionally); it")
    print("is the honest closeable target for a Lean V4 assembly.")
    print("=" * 78)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
