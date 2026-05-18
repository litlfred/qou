"""
Shared utility: symmetric q-dilogarithm Li_2^q at MPFR precision.

Per `prop:mass-endomorphism-tower` ([mass-endomorphism-tower.md]),
the canonical mass-formula brane-tower contribution uses the
**symmetric q-dilogarithm**

    Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q),

with the symmetric q-integer

    [n]_q = (q^n − q^{-n}) / (q − q^{-1}).

This replaces the earlier Faddeev Φ_q form (asymmetric (q^n − 1)
q-integer), per the 2026-05-03 paper revision note.  The Faddeev
form is empirically incompatible with isospin symmetry at q_0
(`brane-tower-isospin-diagnosis.witness.json`).

The canonical brane-tower terms are

    T2 = − Σ_i Li_2^q(−|V̂_i^full|)
    T3 = − z² · Σ_{i<j} Li_2^q(−|V̂_i V̂_j|)

— note the **minus signs** outside and the **negative argument**
inside.  At the substrate value q_0 with |V̂| ∈ [0, 1) these
evaluate to small positive corrections (the alternating series
converges far from any pole, unlike Faddeev Φ_q which blows up
near |z| = q).

Convergence: Li_2^q(z) converges absolutely for |z| < 1; the
factor z^n / (n · [n]_q) decays super-exponentially because
[n]_q ~ q^{n-1}/(q − q^{-1}) grows exponentially.  We truncate
when the next-term magnitude falls below `eps`.
"""
from __future__ import annotations

import json as _json
from pathlib import Path

from mpmath import mp, mpf


def _q_int(n: int, q: mpf, q_inv: mpf) -> mpf:
    """Symmetric q-integer [n]_q = (q^n − q^{-n})/(q − q^{-1}).

    [0]_q := 0 by convention; [1]_q = 1; [n]_q approaches the
    classical integer as q → 1.
    """
    if n == 0:
        return mpf(0)
    if n == 1:
        return mpf(1)
    return (q**n - q_inv**n) / (q - q_inv)


def li_2_q(
    z_val: mpf,
    q: mpf,
    q_inv: mpf | None = None,
    max_k: int = 2000,
    eps: mpf | None = None,
) -> mpf:
    """Symmetric q-dilogarithm Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q).

    Convergence: the radius of convergence is |z| < q (not |z| < 1):
    by ratio test, |a_{n+1}/a_n| → |z|/q since [n+1]_q/[n]_q → q
    as n → ∞.  At |z| = q the series fails the necessary condition
    (terms ~ 1/n at the boundary).  We return ``mp.mpf('inf')`` only
    when |z| ≥ q.  In particular Li_2^q(-1) IS FINITE at q_0 ≈ 1.11
    (alternating series with super-exponentially-decaying terms).
    Truncation cuts at the first term whose magnitude < eps.
    """
    if q_inv is None:
        q_inv = mpf(1) / q
    if eps is None:
        eps = mpf(10) ** (5 - mp.dps)
    if mp.fabs(z_val) >= q:
        return mpf("inf")
    total = mpf(0)
    z_pow = mpf(1)
    for n in range(1, max_k + 1):
        z_pow = z_pow * z_val  # z^n
        qn = _q_int(n, q, q_inv)
        if qn == 0:
            return mpf("inf")
        term = z_pow / (mpf(n) * qn)
        total = total + term
        if mp.fabs(term) < eps:
            break
    return total


# ── Shared helpers (centralized per gemini #687 review) ─────────

_Q_WITNESS_DEFAULT = Path(__file__).parent / "q-pinning-50-digit.witness.json"


def load_q_50dps(path: Path | None = None) -> tuple[mpf, mpf, mpf]:
    """Load q_0, q_0^{-1}, and z = 1/(q^{1/2}+q^{-1/2}) at full
    ``mp.dps`` precision from the canonical pinning witness.

    Returns ``(q, q_inv, z)``.  Shared by every script that ingests
    per-generator Wedderburn volumes — centralized per gemini #687.
    """
    if path is None:
        path = _Q_WITNESS_DEFAULT
    with path.open() as fh:
        d = _json.load(fh)
    q = mpf(d["derived_50_digit"]["q"])
    qi = mpf(1) / q
    z = mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))
    return q, qi, z


def compute_t2_t3_from_vols(
    vols: list[mpf], q: mpf, q_inv: mpf, z: mpf,
) -> tuple[mpf, mpf]:
    """Compute T2 = Σ_i Li_2^q(|V̂_i|) and T3 = z²·Σ_{i<j} Li_2^q(|V̂_i·V̂_j|).

    Canonical Li_2^q brane-tower contributions per
    ``prop:mass-endomorphism-tower``, applied locally to a list of
    per-generator Wedderburn full-volume scalars.

    Used by ``derive_m_{p,n}_hecke_full_tower_50dps`` when the
    upstream producer no longer emits pre-summed
    ``term2_single_50dps`` / ``term3_pair_50dps`` fields.
    """
    t2 = mpf(0)
    for v in vols:
        t2 = t2 + li_2_q(mp.fabs(v), q, q_inv)
    t3 = mpf(0)
    for i, vi in enumerate(vols):
        for vj in vols[i + 1:]:
            t3 = t3 + li_2_q(mp.fabs(vi * vj), q, q_inv)
    t3 = t3 * z ** 2
    return t2, t3
