"""
mpmath-precision q-arithmetic helpers — shared across witness scripts.

Use this module instead of redefining qint/qfac/qpoch in each script.
The float-precision canonical substrate parameter lives in
q_parameter.py; this module wraps the same arithmetic at arbitrary
mpmath precision.

Usage:
    import mpmath as mp
    mp.mp.dps = 30
    from q_parameter import Q as Q0_FLOAT
    from q_mpmath import qint, qfac, qpoch, set_q

    set_q(Q0_FLOAT)        # sets module-level Q, QI from Q0_FLOAT
    a = qint(3)            # [3]_q at high precision
    f = qfac(4)            # [4]_q!
    p = qpoch(3)           # (q;q)_3 = ∏_{k=1}^3 (1 - q^k)
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import mpmath as mp

# Module-level state.  Call set_q(Q0) before using qint/qfac/qpoch.
Q: mp.mpf | None = None
QI: mp.mpf | None = None


def set_q(q0_float: float | str) -> None:
    """Configure the module's q value (call once per script)."""
    global Q, QI
    Q = mp.mpf(str(q0_float))
    QI = mp.mpf(1) / Q


def qint(n: int) -> mp.mpf:
    """q-integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if Q is None:
        raise RuntimeError("call set_q(Q0) before using qint()")
    return (Q**n - QI**n) / (Q - QI)


def qfac(n: int) -> mp.mpf:
    """q-factorial [n]_q! = ∏_{k=1}^n [k]_q."""
    out = mp.mpf(1)
    for k in range(2, n + 1):
        out *= qint(k)
    return out


def qpoch(n: int) -> mp.mpf:
    """q-Pochhammer (q;q)_n = ∏_{k=1}^n (1 - q^k)."""
    if Q is None:
        raise RuntimeError("call set_q(Q0) before using qpoch()")
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= (1 - Q**k)
    return out


def qbinom(n: int, k: int) -> mp.mpf:
    """q-binomial [n choose k]_q = [n]_q! / ([k]_q! · [n-k]_q!)."""
    if k < 0 or k > n:
        return mp.mpf(0)
    return qfac(n) / (qfac(k) * qfac(n - k))
