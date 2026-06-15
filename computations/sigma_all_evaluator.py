"""
Σ_all closed-form evaluator (pure mpmath).

Direct, allocation-free evaluator for the unfiltered β-decay character
sum Σ_all(A), based on the symbolic factorisation verified for A=1..6
in `sigma_all_symbolic_decay.py` and documented in the audit
`docs/audits/2026-05-02-nv-frob-filter-conjectures.md` lines 683–769.

Closed form (verified A=1..6, conjecturally extends to all A ≥ 1):

    Σ_all(A) = (-1)^{A-1} · (3^{⌊A/2⌋} / 2^{a(A)})
             · (q-1)^A · (q+1)^A · (q²+1)^{2⌊A/2⌋}
             · (3 q⁴ + 4 q² + 3) / q^{d(A)}

with the "+2 then +1" period-2 exponent progression

    a(A) = (3A + 1)/2  if A odd,   (3A + 2)/2  if A even.
    d(A) = 2A + 1      if A odd,   2A + 2      if A even.

The two-step ratio identity (exact in ℤ[q^{±1}]):

    Σ_all(A+2) / Σ_all(A) = 3 (q⁴ - 1)² / (8 q⁴),

i.e. the per-A geometric-mean decay rate is

    γ(q) = ½ log(8 q⁴ / (3 (q⁴ - 1)²)).

Why this module exists
======================

Computing Σ_all(A) by enumerating all 4^A per-nucleon channel
configurations and summing Δme suffers from catastrophic cancellation.
The required precision scales linearly with A (≈ 0.589 decimal digits
per unit A), so f64 is only safe up to A ≤ 27, 50 dps to A ≤ 84,
and across the full β-decay table (A ≤ 240) one needs 130+ dps.

Evaluating the closed form **above** instead has *zero* cancellation:
the (q-1)^A and (q+1)^A factors are already extracted symbolically,
so the product is computed at the working precision in O(log A)
multiplications. Constant compute time per digit at any A.

This evaluator is the canonical replacement for raw config-sum routes
in the β-decay / binding-energy compute pipeline. Sympy is *not*
imported — symbolic compute happens in `sigma_all_symbolic_decay.py`
once, off-line; runtime evaluation here is pure mpmath.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
from typing import Optional

import mpmath as mp

__all__ = [
    "DEFAULT_DPS",
    "sigma_all_closed",
    "sigma_all_ratio",
    "sigma_all_decay_rate",
    "frob_filter_required",
    "precision_digits_required",
    "a_exponent",
    "d_exponent",
]

# Default mpmath precision when the caller does not specify their own.
DEFAULT_DPS = 50

# Per-A asymptotic decay slope (decimal digits): log10(per-A decay) ≈ -0.589.
# Used by `precision_digits_required` / `frob_filter_required`.
_LOG10_PER_A_DECAY = 0.5893


def a_exponent(A: int) -> int:
    """Exponent of 2 in the denominator of the closed form: a(A).

    a(A) = (3A + 1)/2 if A odd, (3A + 2)/2 if A even.
    Verified A=1..6: {2, 4, 5, 7, 8, 10}.
    """
    if A < 1:
        raise ValueError(f"A must be ≥ 1, got {A}")
    return (3 * A + 1) // 2 if A % 2 == 1 else (3 * A + 2) // 2


def d_exponent(A: int) -> int:
    """Exponent of q in the denominator of the closed form: d(A).

    d(A) = 2A + 1 if A odd, 2A + 2 if A even.
    Verified A=1..6: {3, 6, 7, 10, 11, 14}.
    """
    if A < 1:
        raise ValueError(f"A must be ≥ 1, got {A}")
    return 2 * A + 1 if A % 2 == 1 else 2 * A + 2


def sigma_all_closed(
    A: int,
    q: mp.mpf,
    dps: Optional[int] = None,
) -> mp.mpf:
    """Evaluate Σ_all(A) in closed form at the given q.

    Parameters
    ----------
    A : int
        Atomic mass (number of nucleons in the chain), A ≥ 1.
    q : mpmath.mpf
        Substrate parameter, evaluated at the caller's working
        precision.
    dps : int, optional
        Override mpmath working precision for this call. If None,
        uses the current ``mp.mp.dps`` (or ``DEFAULT_DPS`` if that is
        smaller). The previous precision is restored on exit.

    Returns
    -------
    mpmath.mpf
        Σ_all(A) evaluated at q, with full working-precision
        accuracy. No catastrophic cancellation — the factors that
        cancel in the raw sum have already been extracted
        symbolically.
    """
    if A < 1:
        raise ValueError(f"A must be ≥ 1, got {A}")

    # Working precision: caller override > current dps > default.
    work_dps = dps if dps is not None else max(mp.mp.dps, DEFAULT_DPS)
    with mp.workdps(work_dps):
        q_mp = mp.mpf(q)
        a = a_exponent(A)
        d = d_exponent(A)
        half_A = A // 2  # ⌊A/2⌋

        sign = mp.mpf(1) if (A % 2 == 1) else mp.mpf(-1)

        # numerator factors
        three_pow = mp.mpf(3) ** half_A
        qm1_pow = (q_mp - 1) ** A
        qp1_pow = (q_mp + 1) ** A
        q2p1_pow = (q_mp * q_mp + 1) ** (2 * half_A)
        rational_factor = 3 * q_mp ** 4 + 4 * q_mp ** 2 + 3

        # denominator factors
        two_pow = mp.mpf(2) ** a
        q_pow = q_mp ** d

        result = sign * three_pow * qm1_pow * qp1_pow * q2p1_pow * rational_factor
        result = result / (two_pow * q_pow)
        return +result  # round to current working precision


def sigma_all_ratio(
    A1: int,
    A2: int,
    q: mp.mpf,
    dps: Optional[int] = None,
) -> mp.mpf:
    """Compute Σ_all(A2) / Σ_all(A1).

    If A2 - A1 is even, uses the exact two-step identity
    Σ_all(A+2)/Σ_all(A) = 3(q⁴-1)² / (8 q⁴) raised to (A2-A1)/2,
    which avoids any per-A evaluation.

    Otherwise falls back to the ratio of two ``sigma_all_closed``
    calls.
    """
    if A1 < 1 or A2 < 1:
        raise ValueError(f"A1, A2 must be ≥ 1, got {A1}, {A2}")

    work_dps = dps if dps is not None else max(mp.mp.dps, DEFAULT_DPS)
    with mp.workdps(work_dps):
        q_mp = mp.mpf(q)
        delta = A2 - A1
        if delta % 2 == 0:
            # Exact two-step identity, raised to |delta|/2 with sign
            # for the direction. The two-step ratio is positive (it is
            # a ratio of |·|² over q⁴), so the parity of (delta/2)
            # alone does NOT flip the sign — but the sign factor in
            # Σ_all is (-1)^{A-1}, which for ΔA = 2k contributes
            # (-1)^{2k} = 1. So the ratio is signed positive.
            two_step = 3 * (q_mp ** 4 - 1) ** 2 / (8 * q_mp ** 4)
            steps = delta // 2  # may be negative if A2 < A1
            return +(two_step ** steps)
        # Odd Δ: fall back to ratio of two evaluations.
        num = sigma_all_closed(A2, q_mp, dps=work_dps)
        den = sigma_all_closed(A1, q_mp, dps=work_dps)
        return +(num / den)


def sigma_all_decay_rate(
    q: mp.mpf,
    dps: Optional[int] = None,
) -> mp.mpf:
    """Per-A geometric-mean decay rate γ(q) of |Σ_all|.

    γ(q) = ½ log(8 q⁴ / (3 (q⁴ - 1)²)).

    At q_0 ≈ 1.10998, γ ≈ 1.357 (≈ 0.589 in base-10 / log 10).
    """
    work_dps = dps if dps is not None else max(mp.mp.dps, DEFAULT_DPS)
    with mp.workdps(work_dps):
        q_mp = mp.mpf(q)
        ratio = 8 * q_mp ** 4 / (3 * (q_mp ** 4 - 1) ** 2)
        return +(mp.log(ratio) / 2)


def precision_digits_required(A: int, q: Optional[mp.mpf] = None) -> int:
    """Decimal digits of precision required for the *raw* Σ_all
    config-sum at this A, before catastrophic cancellation eats the
    answer.

    Uses the asymptotic schedule documented in
    `docs/audits/2026-05-02-nv-frob-filter-conjectures.md` lines 746–
    761 and verified numerically: digits ≈ A · 0.589.

    Returns ``ceil(A · 0.589)``, which exactly matches the audit's
    "max A safe" boundary at every documented working precision:

    | working dps | floor   | max A safe | required digits at max A |
    |-------------|---------|------------|--------------------------|
    | f64 (16)    | 10⁻¹⁶   | 27         | ceil(15.903) = 16        |
    | 25          | 10⁻²⁵   | 42         | ceil(24.738) = 25        |
    | 50          | 10⁻⁵⁰   | 84         | ceil(49.476) = 50        |
    | 100         | 10⁻¹⁰⁰  | 169        | ceil(99.541) = 100       |
    | 200         | 10⁻²⁰⁰  | 338        | ceil(199.082) = 200      |

    The result is independent of q to leading order; q is accepted so
    a more refined estimate can be computed on demand if ever needed.
    """
    if A < 1:
        raise ValueError(f"A must be ≥ 1, got {A}")
    return int(math.ceil(A * _LOG10_PER_A_DECAY))


def frob_filter_required(
    A: int,
    q: mp.mpf,
    target_relative_precision: float,
) -> bool:
    """True iff evaluating Σ_all(A) by raw config sum at the working
    precision corresponding to ``target_relative_precision`` would
    suffer catastrophic cancellation worse than the target — i.e. the
    closed-form (FROB-FILTER) evaluator is required to reach that
    precision.

    The criterion: the cancellation factor (q-1)^A · (q+1)^A · ... at
    this A drops below ``target_relative_precision``, so evaluating
    the raw sum at f64 / working precision loses more than the
    requested digits.

    Convention: ``target_relative_precision`` is a *positive* number
    (e.g. 1e-16 for f64, 1e-50 for 50 dps). True means the closed form
    is needed.

    Examples
    --------
    >>> from q_parameter import Q_MP
    >>> frob_filter_required(27, Q_MP, 1e-16)  # max safe at f64 — closed form NOT required
    False
    >>> frob_filter_required(28, Q_MP, 1e-16)  # past f64 floor
    True
    >>> frob_filter_required(84, Q_MP, 1e-50)  # max safe at 50 dps — closed form NOT required
    False
    >>> frob_filter_required(85, Q_MP, 1e-50)  # past 50 dps floor
    True
    """
    if target_relative_precision <= 0:
        raise ValueError(
            f"target_relative_precision must be > 0, got {target_relative_precision}"
        )
    log10_target = -math.log10(target_relative_precision)
    digits_needed = precision_digits_required(A, q)
    # Strict ``>``: at A = audit's "max safe" (e.g. A=27 for f64), the
    # required digits exactly match the working precision floor — this
    # is the boundary where the raw config sum still fits.  Closed-form
    # is required only past the floor.
    return digits_needed > log10_target


# ── Self-verification: when run as a script, compare against the
# symbolic table (A=1..6) at q_0 ─────────────────────────────────
if __name__ == "__main__":
    from q_parameter import Q_MP, q_at  # late import; not needed at use-site

    expected = {
        1:  0.5295037320168715,
        2: -0.3357233125749398,
        3:  0.035093211913212914,
        4: -0.022250285767622852,
        5:  0.002325825953473032,
        6: -0.001474652483748414,
    }

    print(f"Σ_all closed-form evaluator self-test at q_0 = {Q_MP}")
    print(f"{'A':>3} {'closed-form':>22} {'symbolic-table':>22} {'rel err':>12}")
    print("-" * 64)
    max_rel = 0.0
    q_hi = q_at(50)
    for A, exp in expected.items():
        got = sigma_all_closed(A, q_hi)
        got_f = float(got)
        rel = abs(got_f - exp) / abs(exp)
        max_rel = max(max_rel, rel)
        print(f"{A:>3} {got_f:>22.16e} {exp:>22.16e} {rel:>12.2e}")
    # Tolerance: the symbolic-table values were stored as f64 truncations
    # of full-precision symbolic evaluations, so the agreement floor is
    # dominated by f64 rounding (~1e-15) once the mpmath result is cast
    # back to float.
    assert max_rel < 1e-14, f"closed form mismatch (max rel err {max_rel:.2e})"
    print(f"\nMax relative error vs symbolic table: {max_rel:.2e}  (passes 1e-14)")

    # Two-step ratio identity
    print(f"\nTwo-step ratio identity 3(q⁴-1)²/(8 q⁴) at q_0:")
    expected_ratio = 3 * (q_hi ** 4 - 1) ** 2 / (8 * q_hi ** 4)
    print(f"  symbolic prediction: {mp.nstr(expected_ratio, 20)}")
    for A in (1, 2, 3, 4):
        got = sigma_all_closed(A + 2, q_hi) / sigma_all_closed(A, q_hi)
        rel = abs(got - expected_ratio) / abs(expected_ratio)
        print(f"  A={A} → A={A+2}: ratio = {mp.nstr(got, 20)}  rel err = {float(rel):.2e}")

    gamma = sigma_all_decay_rate(q_hi)
    print(f"\nDecay rate γ(q_0) = {float(gamma):.6f} (audit predicts ≈ 1.357)")

    print(f"\nfrob_filter_required at q_0:")
    for A, tgt in [(10, 1e-16), (27, 1e-16), (84, 1e-50), (84, 1e-15), (240, 1e-100)]:
        req = frob_filter_required(A, q_hi, tgt)
        print(f"  A={A:>3}, target={tgt:.0e} → {req}")
