"""qbeta_e0 — the ONE place E_0, the Q_beta energy scale, is defined.

# Ref: AGENTS.md §"OWNER RULING (2026-09-03)" — the full-tower directive
# Ref: docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md

WHY THIS MODULE EXISTS.  E_0 had TWO live forms in `computations/qbeta/`,
differing by 1/(1 - hbar_q^2) = +0.9915 %:

    order-zero    E_0 = m_e / (q(q-1))                    <- most call sites
    tower-summed  E_0 = m_e / (q(q-1)) / (1 - hbar_q^2)   <- qbeta_bar_branch_refuted_probe:88,
                                                             marked "tower-summed, as ruled"

Nothing reconciled them, so two producers computing "the same" Q_beta differed
by 1 % with no signal at either call site.  Unified here on owner instruction,
2026-09-12.

WHICH FORM IS CANONICAL, and why: the TOWER-SUMMED one.  The owner ruled
2026-09-03 that "the QOU should be on the full tower in the derivations to the
standard model -- should make use of the full tower even though what is
observable is only order zero", and the one producer that already carried the
tower sum annotated it "as ruled".  `order_zero()` is kept, named for what it
is, so a historical figure stays reproducible.

🛑 WHAT IS *NOT* ESTABLISHED HERE.  That the tower sum IS the geometric series
Sum_{k>=0} hbar_q^{2k} = 1/(1 - hbar_q^2) is taken from the one live precedent,
NOT derived.  I did not find a derivation of that series in the corpus and did
not construct one -- inventing it would be exactly the laundering AGENTS.md
forbids.  So `tower_summed()` is canonical BY RULING and its series is an
OPEN derivation, tracked as bean qou-y3bm.  A later agent deriving a different
tower sum changes this function, not its call sites -- which is the point of
routing everything through one module.

SCALE, so nobody mistakes this for the Q_beta problem: E_0 moves Q_beta by
0.9915 %.  The convention-D functional moves it by 257x (base to base).  These
are not comparable and fixing E_0 does not address the gap.
"""
from __future__ import annotations

import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

from mpmath import mpf  # noqa: E402

__all__ = ["order_zero", "order_zero_scaled", "tower_summed", "canonical", "TOWER_FACTOR_DOC"]

TOWER_FACTOR_DOC = (
    "1/(1 - hbar_q^2), taken from qbeta_bar_branch_refuted_probe.py:88 "
    "('tower-summed, as ruled'); the series itself is an OPEN derivation "
    "(bean qou-y3bm), canonical by the 2026-09-03 full-tower ruling."
)


def _inputs(q=None, m_e=None):
    """mpf-only, no float64 path — AGENTS.md NO-FLOAT64."""
    import qou_substrate.constants as C
    q = mpf(C.Q_50_DIGIT_STR) if q is None else mpf(str(q))
    m_e = mpf(str(C.M_E_MEV)) if m_e is None else mpf(str(m_e))
    return q, m_e


def order_zero(q=None, m_e=None):
    """E_0 = m_e / (q(q-1)).  The N=0 / observable-order form.

    Kept so historical figures (the published 0.168 % cell among them) stay
    reproducible.  NOT canonical — see `canonical`.
    """
    q, m_e = _inputs(q, m_e)
    return m_e / (q * (q - 1))


def order_zero_scaled(x, q):
    """x / (q(q-1)): the order-zero E_0 with numerator x, type-preserving.

    For call sites that must keep their arithmetic exactly as it was (sympy
    symbols, floats, an mpf at the caller's dps, or E_0 in units of m_e with
    x = 1). Same operation order as the inline form it replaces, so the
    result is bit-identical. Owner ruling 2026-11-20 (#8590): historical
    reproductions and probes route their order-zero E_0 through this module,
    labelled, rather than open-coding it. NOT canonical — see `canonical`.
    """
    return x / (q * (q - 1))


def tower_summed(q=None, m_e=None):
    """E_0 = m_e / (q(q-1)) / (1 - hbar_q^2), hbar_q = 1 - 1/q.  CANONICAL.

    Canonical by the 2026-09-03 full-tower ruling; the series is open
    (`TOWER_FACTOR_DOC`, bean qou-y3bm).
    """
    q, m_e = _inputs(q, m_e)
    hbar = 1 - 1 / q
    return m_e / (q * (q - 1)) / (1 - hbar ** 2)


def canonical(q=None, m_e=None):
    """The form every new producer should call.  Currently `tower_summed`."""
    return tower_summed(q, m_e)


if __name__ == "__main__":  # pragma: no cover
    from mpmath import mp, nstr
    mp.dps = 50
    print(f"order_zero   = {nstr(order_zero(), 14)} MeV")
    print(f"tower_summed = {nstr(tower_summed(), 14)} MeV   <- canonical")
    print(f"ratio        = {nstr(tower_summed() / order_zero(), 12)}")
