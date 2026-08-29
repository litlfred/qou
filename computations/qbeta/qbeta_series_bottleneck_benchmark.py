#!/usr/bin/env python3
"""WHY the exact-s-series probes time out, profiled — and a measured 3x fix.

Six producers in the Q0_FLIP drain tranche (#5927) hit the 180 s budget. This
identifies the bottleneck in the `qbeta_c*even_exact_sseries_probe` family and
measures one fix end to end. Writes no witness.

PROFILE (cProfile, alarm-dumped at 90 s on qbeta_c3even_exact_sseries_probe):

    182,024,925 function calls in 90.0 s

      cumtime  calls  frame
       89.4       1   probe main()
       82.0       1     sympy.series.series          <- 91 % OF RUNTIME, ONE CALL
       82.0       1       log/exp._eval_nseries
       81.7     267         expr.expand
       81.6      45           polytools.cancel       <- 45 calls
       81.2      31             polys.rings.sring    <- 31 full ring builds
       48.2    1782         core.mul.<listcomp>

So essentially all of it is ONE `sp.series` call, and inside it `cancel()`
rebuilding a polynomial ring 31 times.

WHY `cancel` IS EXPENSIVE HERE, specifically. The expression is

    log( R(1+s) / R(1) ),   R = Qb / (QA * cos_alpha)

where `Qb` carries `sqrt(q**4 + q**2 + 1)`. So `cancel` is not working over
`QQ(q)` -- it is working over the ALGEBRAIC EXTENSION `QQ(q)[sqrt(q^4+q^2+1)]`,
and every one of those 31 `sring` builds carries the extension.

THE FIX, and it is the probe's own technique applied one layer deeper. The
probe already pre-expands `cos(alpha_eff)` to a finite Taylor polynomial rather
than letting a live trig node reach `sp.series` -- its comment records that
keeping the live node costs >= 93x, because `trigsimp`/`futrig` hands the
surd-carrying expression to `polys.factor`, i.e. factoring over the extension.
The surd in `Qb` is the SAME class of problem and survives that fix.

Pre-expanding the surd as a rational power series in `s` BEFORE the outer
series removes the extension from `cancel`'s domain entirely.

MEASURED, on the representative shape at the probe's own order NS+1 = 9:

    sp.series, surd live          169.7 s   (156.1 s on a second run)
    surd pre-expanded              57.6 s
    -----------------------------------------
    speedup                          ~3x
    coefficients s^0..s^8         ALL EXACTLY EQUAL

WHAT THIS DOES NOT DO -- 3x is not an order of magnitude. It is not enough to
rescue the worst producer in the tranche: `cross_check_trM_cw_seminormal_leg`
still exceeds a 900 s budget, so it needs a different attack, not this one.

ALSO MEASURED AND REJECTED: `sympy.polys.ring_series.rs_series`, which is the
tool designed for exactly this and never leaves the series ring. It raises
`NotImplementedError` on this expression -- the series ring does not accept the
algebraic extension either. Recorded so the next agent does not spend the
attempt: the fix has to remove the surd BEFORE the ring is built, which is what
pre-expansion does.
"""
from __future__ import annotations

import time

import sympy as sp

q, s = sp.symbols("q s")
NS = 8


def build():
    b, hbar = sp.Rational(3, 7), (q - 1) / q
    u = b * hbar**2
    z, h = q**3 / (q**2 + 1), q - 1 / q
    alpha = (z - 1) * h / 2 - u / 2
    QA = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    surd = sp.sqrt(q**4 + q**2 + 1)
    Qb = surd * (q**2 - 2 * q - 1) / (q * (q**2 + 1))
    cosa = sum((-1) ** k * alpha ** (2 * k) / sp.factorial(2 * k)
               for k in range(NS // 2 + 1))
    return surd, Qb, QA, cosa


def main() -> int:
    surd, Qb, QA, cosa = build()
    Rq = Qb / (QA * cosa)
    R1 = sp.simplify(Rq.subs(q, 1))

    t = time.time()
    slow = sp.series(sp.log(Rq.subs(q, 1 + s) / R1), s, 0, NS + 1).removeO()
    t_slow = time.time() - t
    print(f"  surd live (current route) : {t_slow:8.1f}s")

    t = time.time()
    surd_s = sp.series(surd.subs(q, 1 + s), s, 0, NS + 1).removeO()
    Rq_s = sp.cancel(surd_s * ((q**2 - 2 * q - 1) / (q * (q**2 + 1))).subs(q, 1 + s)
                     / (QA.subs(q, 1 + s) * cosa.subs(q, 1 + s)))
    fast = sp.series(sp.log(Rq_s / sp.simplify(Rq_s.subs(s, 0))), s, 0, NS + 1).removeO()
    t_fast = time.time() - t
    print(f"  surd pre-expanded         : {t_fast:8.1f}s   -> {t_slow/t_fast:.1f}x")

    bad = [k for k in range(NS + 1)
           if sp.simplify(slow.coeff(s, k) - fast.coeff(s, k)) != 0]
    print(f"  coefficients s^0..s^{NS} agree : {not bad}"
          + (f"  DIFFER AT {bad}" if bad else ""))

    try:
        from sympy.polys.ring_series import rs_series
        rs_series(sp.log(Rq.subs(q, 1 + s) / R1), s, NS + 1)
        print("  rs_series                 : succeeded (unexpected — re-read the docstring)")
    except NotImplementedError:
        print("  rs_series                 : NotImplementedError (the series ring "
              "rejects the algebraic extension too — expected)")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
