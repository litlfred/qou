#!/usr/bin/env python3
"""M_1>0: the VKLS site-density bound needs only ONE MOMENT of kappa, because rho is CONCAVE.

Gap `qou-k5r5`, epic `qou-x631`.  Sequel to `..._M1_kappa_site_distribution.py`, whose
machinery this reuses unchanged (same corner enumeration, same weights, same kappa).

===============================================================================
WHERE THE ROUTE STANDS, in the corpus's own terms
===============================================================================

`..._M1_telescoping_route.py` reduces `M_1 > 0` to `N/P = S + Q < 1`, with `Q ~ 2.07/sqrt(n)
-> 0`, so `S = 2 E_omega[slope]` carries it.  By the telescoping lemmas a same-sign slope is
the density of drop sites `delta(t) = D(t) - D(t+1) in {0,1}` inside the edge's content
interval, and `..._M1_kappa_site_distribution.py` identifies the omega-average of that
density exactly:

    kappa(t) := sum_{e ni t} w_e / g_e,     sum_t kappa(t) = sum_e w_e
    E_omega[density] = sum_t kappa(t) delta(t) / sum_e w_e

(both formalised sorry-free in `QOU/BraidKnot/M1EdgeCalculus.lean` as `kappa_sum` and
`weighted_density_eq_kappa_dot`).  So, normalised, **kappa is a probability distribution on
SITES**, and the route needs

    E_omega[density] < 1/2.

That probe then made the correction that matters here: `infl -> pi/2` is the SAME statement
as `E_omega[density] -> 1/2`, and `1/2` is the pointwise maximum of the VKLS local drop
density

    rho(u) = (1 - (2/pi) arcsin(u/2)) / 2,      u = rescaled content |c|/sqrt(n),

attained ONLY at `u = 0`.  It measured the VKLS-predicted density `E_kappa[rho]` at ~0.35 and
recorded it as *"evidence, not proof"*, the open input being the whole distribution of kappa.

===============================================================================
THE OBSERVATION -- rho is CONCAVE, so the whole distribution is not needed
===============================================================================

    rho(u)   = 1/2 - (1/pi) arcsin(u/2)
    rho'(u)  = -(1/pi) / sqrt(4 - u^2)
    rho''(u) = -u / (pi (4 - u^2)^{3/2})        <  0   for u in (0, 2)

so **rho is strictly concave on (0,2)**, and Jensen gives, for any distribution supported in
[0,2],

    E_kappa[rho(U)]  <=  rho( E_kappa[U] ).                                   (JENSEN)

Since `rho(m) < 1/2` for EVERY `m > 0`, the required `E_omega[density] < 1/2` follows from a
LOWER BOUND ON THE KAPPA-MEAN ALONE.  The open input drops from *"pin the distribution of
kappa"* to *"show its first moment is bounded away from the origin"*, which is the same
strengthening-by-weakening move `..._M1_jensen_route.py` already made for the area functional
`A_sigma` -- a different object, and the reason this is a separate probe rather than an edit
to that one.

**The support caveat is load-bearing and is NOT hand-waved.**  The producer's `rho` CLAMPS,
`asin(min(u,2)/2)`, i.e. it uses `rho~(u) = rho(min(u,2))`, which is `0` for `u >= 2`.  That
clamped function is **not** concave on `[0, inf)`: `rho'(2^-) = -inf` and the extension is
flat, so the slope *increases* across `u = 2` and (JENSEN) does not apply to it as written.
Handled by conditioning instead, which is exact and needs no extra hypothesis:

    E_kappa[rho~(U)] = p * E_kappa[rho(U) | U <= 2]  <=  p * rho( E_kappa[U | U <= 2] )
                                                                                  (JENSEN-C)
    p := kappa({U <= 2}),   since rho~ vanishes off {U <= 2}.

Still a first-moment statement, now on the conditioned law, whose support IS inside [0,2].

===============================================================================
WHAT THIS PROBE DOES
===============================================================================

1. Verifies the concavity claim two independent ways: the symbolic second derivative via
   sympy, and a direct numerical secant/midpoint test of concavity on a grid in (0,2).
2. Reproduces `..._M1_kappa_site_distribution.py`'s `E_kappa[rho~]` exactly (CONTROL -- if
   this probe's kappa differed from that one's, nothing below would be comparable).
3. Computes the conditioned mean `E_kappa[U | U <= 2]`, the mass `p`, and the (JENSEN-C)
   bound `p * rho(E_kappa[U | U <= 2])`.
4. Checks (JENSEN-C) actually holds at every `n` (CONTROL -- a violation would mean the
   concavity claim or the accumulation is wrong, and is the only thing that could make the
   reduction above false).
5. Reports what `E_kappa[U | U <= 2]` would have to be to certify a given margin.

===============================================================================
WHAT THIS DOES NOT DO -- read before quoting anything below
===============================================================================

- **It bounds the VKLS-PREDICTED density, not the finite-n empirical one.**  The two are
  different objects and the sibling probe measured the gap: actual `E_omega[density]` is only
  ~0.5 of the VKLS prediction over `n <= 48`, and rising.  So at every `n` reached here the
  empirical density is well BELOW the bound, and (JENSEN-C) is not the binding constraint
  yet.  Closing the route still needs the VKLS limit as an input, exactly as before.
- **It does not lower-bound the kappa-mean.**  That is the reduced open problem, and it is
  not attempted here.  A reduction is not a proof.
- **It is same-sign edges only** (the producer's own restriction, `cx > 0 > cy` skipped).
  `S_opp` saturates near 0.118, ~36% of `S`, and is untouched by this.
- The range is small.  Nothing here is an asymptotic claim.

Exact `Fraction` for kappa and all first moments; mpmath (40 dps) for `rho`, the bound and
display.  No float64 anywhere.  scope-(a); no fit; nothing wired; `qou-k5r5` stays OPEN.
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wlambda_covariance_epic_M1_edge_ratio_monotonicity import (  # noqa: E402
    corners, dim, factorial, partitions,
)
from mpmath import mp, mpf, asin, pi, nstr, sqrt as mpsqrt  # noqa: E402

mp.dps = 40

NMIN, NMAX = 8, 30


def qf(x: F):
    """Fraction -> mpf without ever touching binary64."""
    return mpf(x.numerator) / mpf(x.denominator)


def rho(u):
    """VKLS local drop density at rescaled content u, UNCLAMPED (valid on [0,2])."""
    return (1 - (2 / pi) * asin(u / 2)) / 2


def rho_clamped(u):
    """The producer's clamped form: rho(min(u,2)), i.e. 0 for u >= 2."""
    return (1 - (2 / pi) * asin(min(u, mpf(2)) / 2)) / 2


def rho_second_derivative(u):
    """rho''(u) = -u / (pi (4-u^2)^{3/2})."""
    return -u / (pi * (4 - u * u) ** mpf("1.5"))


def analyse(n):
    """Reuses `..._M1_kappa_site_distribution.py::analyse` verbatim, plus the conditioned
    first moment and mass that (JENSEN-C) needs."""
    nfac = factorial(n)
    dimc = {lam: dim(lam, nfac) for lam in partitions(n)}
    prof: dict = {}
    W = 0
    Ksum = F(0)        # sum_t kappa        (unnormalised) -- must equal W
    kpos = F(0)        # sum_t kappa * t
    krho = mpf(0)      # sum_t kappa * rho~(t/sqrt n)   <- the sibling's "vkls_ceiling"
    Ksum_le = F(0)     # kappa mass on {t <= 2 sqrt n}
    kpos_le = F(0)     # sum_t kappa * t restricted to {t <= 2 sqrt n}
    sq = mpf(n) ** mpf("0.5")
    # exact integer cut: t <= 2 sqrt(n)  <=>  t^2 <= 4n   (no float comparison)
    for Lam in partitions(n + 1):
        cs = corners(Lam)
        k = len(cs)
        if k < 2:
            continue
        ds = [dimc[c[2]] for c in cs]
        for x in range(k):
            cx, Dx, chx = cs[x]
            for y in range(x + 1, k):
                cy, Dy, chy = cs[y]
                dABS = abs(cy) - abs(cx)
                if dABS == 0 or (cx > 0 > cy):
                    continue                        # same-sign edges only
                dO = cy * cy - cx * cx
                Pt = ds[x] * ds[y] * dABS * dO
                W += Pt
                g = abs(dABS)
                lam = chx if dABS > 0 else chy
                if lam not in prof:
                    D: dict = {}
                    for i, part in enumerate(lam):
                        for j in range(part):
                            D[j - i] = D.get(j - i, 0) + 1
                    prof[lam] = D
                u, v = min(abs(cx), abs(cy)), max(abs(cx), abs(cy))
                unit = F(Pt, g)
                ufl = qf(unit)
                for t in range(u, v):
                    Ksum += unit
                    kpos += unit * t
                    krho += ufl * rho_clamped(mpf(t) / sq)
                    if t * t <= 4 * n:              # exact: t <= 2 sqrt(n)
                        Ksum_le += unit
                        kpos_le += unit * t
    mean_all = F(kpos, Ksum)
    mean_le = F(kpos_le, Ksum_le) if Ksum_le else F(0)
    p = F(Ksum_le, Ksum)
    m_le_scaled = qf(mean_le) / sq
    return {
        "n": n,
        "kappa_sum_over_W": F(Ksum, W),            # exactly 1 iff the kappa identity holds
        "E_kappa_rho": krho / mpf(W),              # the sibling's VKLS-predicted density
        "kappa_mean_scaled": qf(mean_all) / sq,
        "p_mass_le_2sqrtn": p,
        "kappa_cond_mean_scaled": m_le_scaled,
        "jensen_bound": qf(p) * rho(m_le_scaled),  # (JENSEN-C) right-hand side
    }


def main() -> int:
    t0 = time.monotonic_ns()
    fails: list[str] = []
    passes = 0

    def check(name, ok, detail):
        nonlocal passes
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}", flush=True)
        if ok:
            passes += 1
        else:
            fails.append(name)

    print("=" * 78)
    print("M_1>0 (qou-k5r5): rho is CONCAVE, so the site-density bound needs one moment")
    print("=" * 78)

    # ---- 1. concavity, symbolically ------------------------------------------------
    try:
        import sympy as sp
        us = sp.Symbol("u", positive=True)
        rho_sym = sp.Rational(1, 2) - sp.asin(us / 2) / sp.pi
        d2 = sp.simplify(sp.diff(rho_sym, us, 2))
        target = sp.simplify(-us / (sp.pi * (4 - us**2) ** sp.Rational(3, 2)))
        ok_sym = sp.simplify(d2 - target) == 0
        check("rho''(u) = -u / (pi (4-u^2)^(3/2))  [sympy, symbolic]",
              ok_sym, f"sympy d2/du2 = {d2}")
    except ImportError:
        check("rho'' symbolic form", False, "sympy unavailable -- symbolic leg NOT run")

    # ---- 2. concavity, numerically (independent of sympy) --------------------------
    grid = [mpf(j) / 20 for j in range(1, 40)]          # u = 0.05 .. 1.95, inside (0,2)
    neg = all(rho_second_derivative(u) < 0 for u in grid)
    check("rho''(u) < 0 on a grid in (0,2)  [closed form, 40 dps]",
          neg,
          f"max rho'' over {len(grid)} points = "
          f"{nstr(max(rho_second_derivative(u) for u in grid), 6)} < 0")

    # midpoint concavity: rho((a+b)/2) >= (rho(a)+rho(b))/2, from rho ITSELF not rho''
    mid_ok, worst = True, mpf(0)
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            a, b = grid[i], grid[j]
            slack = rho((a + b) / 2) - (rho(a) + rho(b)) / 2
            if slack < 0:
                mid_ok = False
            worst = min(worst, slack) if (i or j) else slack
    check("midpoint concavity of rho holds on every pair in the grid  [no derivative used]",
          mid_ok,
          f"min over {len(grid)*(len(grid)-1)//2} pairs of "
          f"rho((a+b)/2) - (rho(a)+rho(b))/2 = {nstr(worst, 6)} >= 0")

    # the clamped form is NOT concave -- the caveat, measured rather than asserted
    a_, b_ = mpf("1.9"), mpf("2.5")
    clamp_slack = rho_clamped((a_ + b_) / 2) - (rho_clamped(a_) + rho_clamped(b_)) / 2
    check("the CLAMPED rho~ is NOT concave across u = 2 (why conditioning is required)",
          clamp_slack < 0,
          f"rho~(2.2) - (rho~(1.9)+rho~(2.5))/2 = {nstr(clamp_slack, 6)} < 0, so "
          f"(JENSEN) does not apply to rho~ and (JENSEN-C) is used instead")

    # ---- 3. the table --------------------------------------------------------------
    print()
    print(f"# {'n':>3} {'sum k/W':>9} {'E_k[rho~]':>11} {'k-mean':>9} "
          f"{'p(U<=2)':>9} {'cond mean':>10} {'JENSEN-C bd':>12} {'slack':>10}")
    rows = []
    for n in range(NMIN, NMAX + 1):
        r = analyse(n)
        r["slack"] = r["jensen_bound"] - r["E_kappa_rho"]
        rows.append(r)
        print(f"  {n:>3} {nstr(qf(r['kappa_sum_over_W']), 7):>9} "
              f"{nstr(r['E_kappa_rho'], 7):>11} "
              f"{nstr(r['kappa_mean_scaled'], 6):>9} "
              f"{nstr(qf(r['p_mass_le_2sqrtn']), 6):>9} "
              f"{nstr(r['kappa_cond_mean_scaled'], 6):>10} "
              f"{nstr(r['jensen_bound'], 7):>12} "
              f"{nstr(r['slack'], 6):>10}", flush=True)

    # ---- 4. controls ---------------------------------------------------------------
    print()
    ident = all(r["kappa_sum_over_W"] == 1 for r in rows)
    check("CONTROL: sum_t kappa(t) == sum_e w_e exactly at every n  [the kappa identity]",
          ident,
          f"sum_t kappa / W == 1 exactly (Fraction) for all n = {NMIN}..{NMAX}; this is the "
          f"Lean `kappa_sum`, and it is what makes this probe's kappa the sibling's kappa")

    jensen_ok = all(r["slack"] >= 0 for r in rows)
    worst_row = min(rows, key=lambda r: r["slack"])
    check("CONTROL: (JENSEN-C) holds at every n -- E_k[rho~] <= p * rho(E_k[U | U<=2])",
          jensen_ok,
          f"min slack = {nstr(worst_row['slack'], 6)} at n = {worst_row['n']}; a negative "
          f"slack would refute the concavity claim or the accumulation, and is the only "
          f"measurement that could make the reduction false")

    below_half = all(r["jensen_bound"] < mpf(1) / 2 for r in rows)
    worst_bd = max(rows, key=lambda r: r["jensen_bound"])
    check("the (JENSEN-C) bound is < 1/2 at every n reached",
          below_half,
          f"max bound = {nstr(worst_bd['jensen_bound'], 7)} at n = {worst_bd['n']}, "
          f"against the 1/2 the route needs")

    # ---- 5. what a margin would cost -----------------------------------------------
    print()
    print("  What the reduced open problem has to deliver.  rho is strictly decreasing, so")
    print("  `E_omega[density]_VKLS <= 1/2 - eps` follows from a lower bound on the")
    print("  conditioned kappa-mean alone (taking p <= 1, i.e. discarding the mass term):")
    print()
    print(f"    {'eps':>8} {'needs cond mean >=':>20}")
    for eps in ("0.05", "0.10", "0.15", "0.1838"):
        e = mpf(eps)
        # rho(m) = 1/2 - eps  =>  arcsin(m/2) = pi*eps  =>  m = 2 sin(pi eps)
        from mpmath import sin as mpsin
        m_need = 2 * mpsin(pi * e)
        print(f"    {eps:>8} {nstr(m_need, 6):>20}")
    print()
    print(f"  Measured conditioned mean at n = {NMAX}: "
          f"{nstr(rows[-1]['kappa_cond_mean_scaled'], 6)}, and it is RISING across the "
          f"range ({nstr(rows[0]['kappa_cond_mean_scaled'], 6)} at n = {NMIN}).")
    print("  Not an asymptotic claim: the range is small and the trend is not pinned.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    out = {
        "computation": "m1-site-density-jensen-reduction",
        "description": (
            "M_1>0 (qou-k5r5): the VKLS local drop density rho(u) = 1/2 - arcsin(u/2)/pi is "
            "strictly CONCAVE on (0,2) (rho'' = -u/(pi(4-u^2)^{3/2})), so by Jensen the "
            "omega-averaged site density E_kappa[rho] is bounded by rho evaluated at the "
            "kappa-MEAN. This reduces the open input for the telescoping route from the whole "
            "kappa distribution to a lower bound on its first moment. The producer's clamped "
            "rho~ is NOT concave across u=2, so the bound is taken on the conditioned law "
            "(JENSEN-C). Bounds the VKLS-predicted density, NOT the finite-n empirical one."
        ),
        "scope": "same-sign edges only; S_opp (~36% of S) untouched; not an asymptotic claim",
        "elapsed_sec": ms / 1000,
        "allPassed": not fails,
        "assertions_passed": passes,
        "assertions_failed": fails,
        "data": {
            "rho_second_derivative": "-u / (pi * (4 - u^2)^(3/2))",
            "rows": [
                {
                    "n": r["n"],
                    "E_kappa_rho": nstr(r["E_kappa_rho"], 30),
                    "kappa_mean_scaled": nstr(r["kappa_mean_scaled"], 30),
                    "p_mass_le_2sqrtn": str(r["p_mass_le_2sqrtn"]),
                    "kappa_cond_mean_scaled": nstr(r["kappa_cond_mean_scaled"], 30),
                    "jensen_bound": nstr(r["jensen_bound"], 30),
                    "slack": nstr(r["slack"], 30),
                }
                for r in rows
            ],
        },
    }
    Path(__file__).with_name("m1-site-density-jensen-reduction.witness.json").write_text(
        json.dumps(out, indent=2) + "\n")

    print()
    print("=" * 78)
    print(f"{passes} passed, {len(fails)} failed  ({ms} ms)")
    if fails:
        for f_ in fails:
            print(f"  FAILED: {f_}")
    print("RESULT: rho concave => the site-density input reduces to ONE MOMENT of kappa.")
    print("RESULT: gap qou-k5r5 stays OPEN -- a reduction is not a proof, and the "
          "kappa-mean lower bound is not attempted here.")
    print("=" * 78)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
