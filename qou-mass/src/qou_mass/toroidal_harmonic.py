from __future__ import annotations

from pathlib import Path

import mpmath as mp


def _canonical_q0() -> mp.mpf:
    try:
        from ._internal.q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    except ImportError:
        import sys  # noqa: PLC0415
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
        from qou_mass._internal.q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    with mp.workdps(max(80, mp.mp.dps)):
        return mp.mpf(Q_50_DIGIT_STR)


def toroidal_harmonic_P(m, n, cosh_eta) -> mp.mpf:
    """Computes the toroidal harmonic P_{n - 1/2}^m(cosh(eta)) at >= 80 dps."""
    with mp.workdps(max(80, mp.mp.dps)):
        degree = mp.mpf(n) - mp.mpf(1) / mp.mpf(2)
        x = cosh_eta if isinstance(cosh_eta, mp.mpf) else mp.mpf(str(cosh_eta))
        val = mp.legenp(degree, m, x, type=3)
        return val.real if isinstance(val, mp.mpc) else val


def toroidal_harmonic_Q(m, n, cosh_eta) -> mp.mpf:
    """Computes the toroidal harmonic Q_{n - 1/2}^m(cosh(eta)) at >= 80 dps."""
    with mp.workdps(max(80, mp.mp.dps)):
        degree = mp.mpf(n) - mp.mpf(1) / mp.mpf(2)
        x = cosh_eta if isinstance(cosh_eta, mp.mpf) else mp.mpf(str(cosh_eta))
        val = mp.legenq(degree, m, x, type=3)
        return val.real if isinstance(val, mp.mpc) else val


if __name__ == "__main__":
    mp.mp.dps = 80
    q0 = _canonical_q0()
    cosh_eta = (q0 + mp.mpf(1) / q0) / mp.mpf(2)
    print("Testing Toroidal Harmonic P_{n-1/2}^m at cosh(eta) =", mp.nstr(cosh_eta, 12))
    for n in range(1, 4):
        for m in range(0, 2):
            val = toroidal_harmonic_P(m, n, cosh_eta)
            print(f"  n={n}, m={m}: P_{n-1/2}^{m} = {mp.nstr(val, 12)}")
