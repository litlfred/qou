"""GAP-A-4 probe helper — q=1-safe q-integer / dim_q utilities.

Centralised helper for the T4-T12 GAP-A-4 probe series.  Resolves the
duplication called out by Gemini (and T4's own review) in PRs touching
the probe family: every probe in this series needs

  - the substrate parameter ``Q_0_50DPS`` (50-dps mpf string),
  - a q-integer ``q_number(n, q)`` that handles the classical limit
    q → 1 (where the ratio form ``(q^n − q^{-n})/(q − q^{-1})`` is 0/0),
  - the matching ``q_factorial`` and ``dim_q_partition``,
  - and the classical (q=1) integer dim of an S_n irrep via the
    hook-length formula.

Why this module instead of ``murnaghan_nakayama.dim_q_lambda``:

  The canonical helper ``murnaghan_nakayama.dim_q_lambda`` evaluates
  ``[n]_q = (q^n − q^{-n}) / (q − q^{-1})`` directly, which is 0/0
  at the classical limit q = 1.  The GAP-A-4 probes (especially T4 and
  T6) exercise the classical limit explicitly for the linking-weight
  identity check and the Clifford-excess test, so the canonical
  helper crashes on those code paths.  This module routes through a
  q=1-safe branch (``[n]_q → n`` as q → 1) without changing the
  q ≠ 1 numerics — at q_0 ≈ 1.10998 the two implementations agree
  to 50 dps.

Importing convention (probes do):

    from _gap_a4_qsafe import Q_0_50DPS, q_number, q_factorial, \\
                             dim_q_partition, classical_dim_partition
"""
from __future__ import annotations

import mpmath as mp

from partition_utils import hook_lengths

# Substrate parameter, 50 dps, RESOLVED THROUGH q_parameter.
#
# This was a literal, commented "proton-mass-anchored q_0" while holding the
# MUON value 1.10997859555733471989… . The comment and the value disagreed,
# and 22 modules import this name, so every one of them computed at muon while
# its manifest entry said proton -- which is how the T5-T12 probes came to be
# tagged `physical_proton` with muon-valued witnesses.
#
# Resolving through q_parameter makes the value follow the anchor each importer
# is actually assigned, so the label cannot drift from the number again. Do not
# replace this with a literal.
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q_0_50DPS: str = Q_50_DIGIT_STR


def q_number(n: int, q: mp.mpf) -> mp.mpf:
    """Symmetric q-integer [n]_q = (q^n − q^{-n}) / (q − q^{-1}).

    Q=1-SAFE: at q = 1 the ratio form is 0/0; this implementation
    returns the limiting value [n]_{q=1} = n explicitly.  At q ≠ 1
    the standard ratio form is used at full mpmath precision.
    """
    if n == 0:
        return mp.mpf(0)
    if abs(q - 1) < mp.mpf("1e-30"):
        return mp.mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    """[n]_q! = Π_{k=1}^{n} [k]_q via q=1-safe ``q_number``."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_number(k, q)
    return out


def dim_q_partition(lam: tuple, q: mp.mpf) -> mp.mpf:
    """dim_q(V_λ) = [n]_q! / Π_{x∈λ} [h(x)]_q (q-hook formula).

    Q=1-safe wrapper around the canonical ``dim_q_lambda`` in
    ``computations/murnaghan_nakayama.py`` — same
    formula, same hook-length input (``partition_utils.hook_lengths``),
    but routes through this module's q=1-safe ``q_number`` so probes
    exercising the classical limit don't trip 0/0.
    """
    n = sum(lam)
    num = q_factorial(n, q)
    den = mp.mpf(1)
    for h in hook_lengths(list(lam)):
        den *= q_number(h, q)
    return num / den


def classical_dim_partition(lam: tuple) -> int:
    """Integer dimension of S^λ as an S_n-irrep at q = 1.

    Hook-length formula: dim(S^λ) = n! / Π_{x∈λ} h(x).  Used by T7's
    Wenzl-weight check and T10's 2I character lift; centralised here
    to remove the local copies Gemini flagged.
    """
    from math import factorial
    n = sum(lam)
    d = factorial(n)
    for h in hook_lengths(list(lam)):
        d //= h
    return d
