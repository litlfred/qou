#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase7_transfer_bound.py — Phase 7 of the covariance-kernel proof epic
(qou-x631), effective-Stein program, STEP 2: the transfer-error BOUND (Gaussian main term dominates).

Write g(θ) := E_{β=2+θ}[ω₃] = Σ_λ f^{2+θ}ω₃ / Σ_λ f^{2+θ}  (ω₃ = Σc² − C(n,2)).  Then:
  • g(0) = E_2[ω₃] = 0                       (Plancherel content mean, exact);
  • g(1) = E_3[ω₃] = cov(n)/cubeSum(n)       (the KERNEL, up to a positive factor);
  • g'(0) = Cov_Planch(ln f, ω₃)             (the Gaussian / linear "main" term).
Since `f^θ = e^{θ ln f}`, `g` is the exponentially-tilted (dimension-tilted) mean of ω₃, and its
Taylor coefficients `g^{(m)}(0)` are the mixed Plancherel cumulants `κ_{m+1}(ln f;…;ln f;ω₃)`.  Taylor
at θ=1:
    kernel-sign  g(1) = g'(0) + R,   R := Σ_{m≥2} g^{(m)}(0)/m!   (the non-Gaussian remainder).
Hence
    **kernel `cov(n) ≤ 0`  ⇐  [ g'(0) = Cov_Planch(ln f, ω₃) ≤ 0 ]  AND  [ |R| < |g'(0)| ]**
(the linear/Gaussian term dominates the non-Gaussian remainder, so the sum keeps `g'(0)`'s sign).

RESULT — the bound HOLDS with margin (verified 40 dps, n ≤ 14): `g'(0) < 0` for all n, and the
transfer ratio `r := g(1)/g'(0) ∈ (0.54, 0.87)`, so `|R|/|g'(0)| = |r−1| ∈ (0.13, 0.46) < 1` — the
non-Gaussian correction is at most ≈46 % of the linear term, never enough to flip the sign.  This is
the concrete quantitative content the joint effective Berry–Esseen must certify.

ROUTE (negative quadrant dependence, NQD) — ELIMINATED.  A clean sufficient condition would be that
`(ln f, ω₃)` are NQD (Hoeffding kernel `H(s,t) = P(ln f>s, ω₃>t) − P(ln f>s)P(ω₃>t) ≤ 0 ∀ s,t`), which
by Hoeffding's identity would give `Cov(g(ln f), ω₃) ≤ 0` for every increasing `g` — the kernel, the
interval, and the whole β≥2 family at once.  It FAILS: `H(s,t) > 0` at some thresholds, and the bad
count grows with n (n=4..14: 1,1,5,5,10,20,46,50,91,142,171; worst `H ≈ +0.13`).  So there is no
pointwise NQD certificate — the sign is (again) a weighted-integral cancellation.

NET: the kernel is bounded — `cov(n) ≤ 0` reduces to two concrete analytic targets, `Cov(ln f,ω₃) ≤ 0`
and the remainder bound `|R| < |g'(0)|`, both verified numerically; the rigorous versions need
Plancherel-cumulant control of `g^{(m)}(0)` (Kerov CLT), the open core.  scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged (2/7).  In-sandbox (mpmath 40 dps).

# Ref: [fulman2004stein] https://doi.org/10.1090/S0002-9947-04-03499-3
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from mpmath import mp, mpf, power, fsum, log as mlog  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
NMAX = 14


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hooks(l):
    l = list(l)
    if not l:
        return []
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(l) for j in range(row)]


def dim(l):
    d = 1
    for h in hooks(l):
        d *= h
    return math.factorial(sum(l)) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def g_and_derivs(n):
    """g(θ)=E_{2+θ}[ω₃]; return g(0), g(1), g'(0), g''(0), g'''(0) at 40 dps."""
    Ck2 = n * (n - 1) // 2
    S = [(mpf(dim(l)), mpf(C2(l) - Ck2)) for l in partitions_of(n)]

    def g(theta):
        b = mpf(2) + theta
        num = fsum(power(f, b) * w for f, w in S)
        den = fsum(power(f, b) for f, w in S)
        return num / den

    h = mpf('1e-6')
    g0, g1 = g(mpf(0)), g(mpf(1))
    d1 = (g(h) - g(-h)) / (2 * h)
    d2 = (g(h) - 2 * g0 + g(-h)) / (h * h)
    d3 = (g(2 * h) - 2 * g(h) + 2 * g(-h) - g(-2 * h)) / (2 * h ** 3)
    return g0, g1, d1, d2, d3


def nqd_bad_count(n):
    """#thresholds (s,t) with Hoeffding kernel H(s,t)>0 (NQD violation)."""
    Ck2 = n * (n - 1) // 2
    fact = math.factorial(n)
    data = [(mlog(mpf(dim(l))), mpf(C2(l) - Ck2), mpf(dim(l) ** 2) / fact)
            for l in partitions_of(n)]
    Xs = sorted(set(d[0] for d in data))
    Ys = sorted(set(d[1] for d in data))
    bad = 0
    worst = mpf(0)
    for s in Xs:
        PX = fsum(w for x, _y, w in data if x > s + mpf('1e-15'))
        for t in Ys:
            PY = fsum(w for _x, y, w in data if y > t + mpf('1e-12'))
            PJ = fsum(w for x, y, w in data if x > s + mpf('1e-15') and y > t + mpf('1e-12'))
            H = PJ - PX * PY
            if H > mpf('1e-15'):
                bad += 1
                worst = max(worst, H)
    return bad, float(worst)


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — Phase 7 (effective Stein) STEP 2: transfer bound ===\n")
    print(" n | g(1)=kernel | g'(0)=main | r=g(1)/g'(0) | |R|/|main|=|r-1| | bound<1 | NQD bad")
    rows = []
    all_bound = True
    all_main_neg = True
    for n in range(3, NMAX + 1):
        g0, g1, d1, d2, d3 = g_and_derivs(n)
        r = g1 / d1
        rem = abs(r - 1)
        bd = rem < 1
        badc, worst = nqd_bad_count(n)
        all_bound &= bd
        all_main_neg &= (d1 < 0)
        rows.append((n, float(g1), float(d1), float(r), float(rem), bd, badc, worst))
        print(f"{n:2d} | {float(g1):+.5f}   | {float(d1):+.5f}  | {float(r):.5f}     | "
              f"{float(rem):.5f}         | {bd}    | {badc}")

    nqd_fails = any(badc > 0 for (_n, _g1, _d1, _r, _rem, _bd, badc, _w) in rows)
    max_rem = max(rem for (_n, _g1, _d1, _r, rem, _bd, _bc, _w) in rows)
    ok = all_bound and all_main_neg and nqd_fails
    print(f"\nmain term g'(0)=Cov_Planch(ln f,ω₃) < 0 all n≤{NMAX}: {all_main_neg}")
    print(f"transfer-error bound |R| < |main| all n (max |r−1| = {max_rem:.3f} < 1): {all_bound}")
    print(f"NQD (Hoeffding kernel ≤0 pointwise): ELIMINATED (bad points grow with n): {nqd_fails}")
    print(f"\nkernel cov(n)≤0 ⇐ [Cov_Planch(ln f,ω₃)≤0] AND [|Taylor remainder|<|linear term|] — both")
    print(f"verified numerically; rigorous bound needs Plancherel-cumulant control of g^(m)(0) (Kerov CLT).")
    print(f"\nRESULT: transfer-error bound holds + NQD eliminated: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase7-transfer-bound", engine="python-mpmath")
        w.set_description(
            "Phase 7 (effective-Stein) STEP 2 of the covariance-kernel epic (qou-x631): the "
            "transfer-error BOUND. With g(θ)=E_{2+θ}[ω₃] (dimension-tilted mean; g^{(m)}(0)=mixed "
            "Plancherel cumulants κ_{m+1}(ln f;…;ω₃)), g(0)=0, g(1)=kernel (∝cov(n)), g'(0)="
            "Cov_Planch(ln f,ω₃)=Gaussian main term. Taylor: g(1)=g'(0)+R, R=Σ_{m≥2}g^{(m)}(0)/m!. So "
            "kernel≤0 ⇐ [g'(0)≤0] AND [|R|<|g'(0)|]. BOUND HOLDS (40dps, n≤14): g'(0)<0 all n; transfer "
            "ratio r=g(1)/g'(0)∈(0.54,0.87) ⇒ |R|/|g'(0)|=|r−1|∈(0.13,0.46)<1 — the non-Gaussian "
            "correction is ≤~46% of the linear term, never flips the sign. NQD route ELIMINATED: the "
            "Hoeffding kernel H(s,t)=P(ln f>s,ω₃>t)−P(ln f>s)P(ω₃>t) is >0 at some thresholds (bad count "
            "grows with n; worst H≈+0.13), so there is no pointwise negative-quadrant-dependence "
            "certificate. NET: kernel reduces to two concrete analytic targets [Cov(ln f,ω₃)≤0] and "
            "[|remainder|<|linear|], both verified numerically; rigorous bound needs Plancherel-cumulant "
            "control of g^{(m)}(0) (Kerov CLT) — the open core. scope-(a); no fit; nothing wired; no c_k; "
            "L2 2/7.")
        w.add_data("g_tilted_mean", "g(theta)=E_{2+theta}[omega3]; g(0)=0, g(1)=kernel, g'(0)=Cov(lnf,omega3)")
        w.add_data("main_term_negative_all_n", bool(all_main_neg))
        w.add_data("transfer_ratio_range", "r=g(1)/g'(0) in (0.54, 0.87)")
        w.add_data("remainder_over_main_max", round(max_rem, 4))
        w.add_data("transfer_bound_holds", bool(all_bound))
        w.add_data("nqd_eliminated", bool(nqd_fails))
        w.add_data("nqd_bad_counts", [badc for (_n, _g1, _d1, _r, _rem, _bd, badc, _w) in rows])
        w.add_data("reduction", "kernel<=0 <= [Cov(lnf,omega3)<=0] AND [|remainder|<|linear term|]")
        w.add_assertion(
            "covariance_epic_phase7_transfer_bound",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Transfer-error bound: g'(0)=Cov_Planch(ln f,ω₃)<0 and |Taylor remainder|/|linear| "
                    "=|r−1|<1 (max 0.46), all n≤14 at 40dps ⇒ non-Gaussian correction cannot flip the "
                    "sign. NQD eliminated (Hoeffding kernel >0 pointwise). Rigorous bound needs "
                    "Plancherel-cumulant control of g^(m)(0). No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
