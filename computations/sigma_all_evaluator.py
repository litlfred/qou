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


# ── Witness emission ─────────────────────────────────────────────
#
# `sigma-all-evaluator.witness.json` named this module as its `scriptFile`
# for fifteen months while nothing here wrote it: the file was hand-authored
# alongside the 2026-05-03 wiring task and committed by hand. The provenance
# audit scored it NOT_A_PRODUCER — a witness whose named producer provably
# cannot produce it, so re-running regenerates nothing and the pipeline goes
# on treating a frozen file as current. That is what this section closes.
#
# The numeric sections below are DERIVED from this module's own API
# (`sigma_all_closed`, `sigma_all_decay_rate`, `precision_digits_required`,
# `a_exponent`, `d_exponent`), not transcribed. The documentary sections —
# which callers were rewired in 2026-05-03 and which were deliberately left
# alone — are a record of a one-time task and are carried verbatim.

_CLOSED_FORM_PRECISION_CLAIM = (
    "The closed-form evaluator has zero catastrophic cancellation (the "
    "(q-1)^A · (q+1)^A factors are extracted symbolically). Working precision "
    "= output precision, in O(log A) multiplications. Valid for any A ≥ 1 at "
    "any mpmath dps. Constant compute time per requested digit."
)

_PIPELINE_CALLERS_UPDATED = [
    {
        "file": "computations/full-derivation-verified.py",
        "case": "A=1 free neutron",
        "before": "char_sum_n = sum_p - sum_n",
        "after": "char_sum_n = float(sigma_all_closed(1, mp.mpf(q0)))",
        "approx_line": 263,
    },
    {
        "file": "computations/full-derivation-verified.py",
        "case": "A=3 tritium ³H→³He",
        "before": "for config in cartesian(ch_names, repeat=3): total_3h += me_d - me_p",
        "after": "total_3h = float(sigma_all_closed(3, mp.mpf(q0)))",
        "approx_line": 277,
    },
    {
        "file": "computations/full-derivation-verified.py",
        "case": "A=6 ⁶He→⁶Li (Σ_all only; Σ_FP still enumerates)",
        "before": "for config in cartesian(ch_names, repeat=6): total_6he_all += dme",
        "after": "total_6he_all = float(sigma_all_closed(6, mp.mpf(q0)))",
        "approx_line": 297,
    },
]

_PIPELINE_CALLERS_INTENTIONALLY_UNWIRED = [
    {
        "file": "computations/frob_filter_cancellation_test.py",
        "reason": "Test driver for the cancellation diagnostic itself — intentionally "
                  "exercises the raw config-sum path so the f64 precision-budget "
                  "crossover can be measured. Wiring this to the closed form would "
                  "defeat the test.",
    },
    {
        "file": "computations/sigma_all_symbolic_decay.py",
        "reason": "The symbolic-derivation reference. Per task: do NOT modify; this is "
                  "the source of truth for the closed form.",
    },
]

_PRECISION_SCHEDULE_FLOORS = [
    ("f64", -16),
    ("25 dps", -25),
    ("50 dps", -50),
    ("100 dps", -100),
    ("200 dps", -200),
]

_WITNESS_OUTPUT_DPS = 30


def build_witness(q: mp.mpf, dps: int = 60) -> dict:
    """Assemble the `sigma-all-evaluator` witness payload at `q`.

    Every number is serialized as a full-precision decimal string. The
    committed witness carried a `*_f64` twin beside each one; those are
    dropped here. A float64 copy of a value already present at 30 significant
    figures is float64 padding by the definition the precision gates use, and
    wiring this producer pulls the witness into the raw-float64 audit's scope
    for the first time — re-emitting ~40 raw floats would land as a fresh
    regression on a gate whose baseline is supposed to drain, never grow.
    """
    from q_parameter import MASS_RATIO_MU_E  # late import; not needed at use-site

    def s(x) -> str:
        return mp.nstr(x, _WITNESS_OUTPUT_DPS)

    with mp.workdps(dps):
        q = mp.mpf(q)
        gamma = sigma_all_decay_rate(q, dps=dps)
        log10_per_A = gamma / mp.log(10)
        # Vol(4_1) = 2·Cl₂(π/3) = 6Λ(π/3). NOT 2Λ(π/3) and NOT 3·Cl₂(π/3):
        # Λ(θ) = Cl₂(2θ)/2, so those two spellings are the classic
        # coefficient slip and give 0.6766 / 3.0448 instead of 2.0299.
        vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)

        sigma_1 = sigma_all_closed(1, q, dps=dps)
        table = []
        for A in range(1, 11):
            sigma_A = sigma_all_closed(A, q, dps=dps)
            table.append({
                "A": A,
                "a_exp": a_exponent(A),
                "d_exp": d_exponent(A),
                "sigma_all_at_q0": s(sigma_A),
                "ratio_to_A1": s(sigma_A / sigma_1),
                "log10_abs": s(mp.log10(abs(sigma_A))),
                "precision_digits_required_for_raw_sum": precision_digits_required(A, q),
            })

        schedule = [
            {
                "precision_label": label,
                "log10_floor": floor,
                "max_A_safe_for_raw_sum": int(mp.floor(abs(floor) / log10_per_A)),
            }
            for label, floor in _PRECISION_SCHEDULE_FLOORS
        ]

        return {
            "computation": "sigma-all-evaluator",
            "description": (
                "Reference table + precision schedule for the Σ_all closed-form "
                "evaluator (sigma_all_evaluator.py). Replaces raw 4^A configuration-sum "
                "routes in the β-decay / binding-energy pipeline with a constant-time, "
                "cancellation-free evaluator. Closed form verified for A=1..6 in "
                "sigma_all_symbolic_decay.py and documented in "
                "docs/audits/2026-05-02-nv-frob-filter-conjectures.md lines 683-769."
            ),
            "auditOnly": "docs/audits/2026-05-03-frob-filter-evaluator-wired.md",
            "q_parameter": {
                "q_at_q0": s(q),
                "vol_4_1": s(vol_4_1),
                "mu_over_e": str(MASS_RATIO_MU_E),
                "dps_used": dps,
            },
            "closed_form": {
                "formula": "Σ_all(A) = (-1)^{A-1} · 3^{floor(A/2)} / 2^{a(A)} · (q-1)^A "
                           "· (q+1)^A · (q^2+1)^{2 floor(A/2)} · (3 q^4 + 4 q^2 + 3) / q^{d(A)}",
                "a_exponent_rule": "a(A) = (3A+1)/2 if A odd, (3A+2)/2 if A even",
                "d_exponent_rule": "d(A) = 2A+1 if A odd, 2A+2 if A even",
                "two_step_ratio": "Σ_all(A+2) / Σ_all(A) = 3 (q^4-1)^2 / (8 q^4)",
                "two_step_ratio_at_q0": s(3 * (q ** 4 - 1) ** 2 / (8 * q ** 4)),
            },
            "decay_rate": {
                "gamma_q0_natural_log": s(gamma),
                "log10_per_A_decay": s(-log10_per_A),
                "per_A_geometric_decay_factor": s(mp.exp(-gamma)),
                "audit_reference_value": "1.357",
            },
            "reference_table_A_1_to_10": table,
            "precision_schedule_for_raw_config_sum": schedule,
            "closed_form_precision_claim": _CLOSED_FORM_PRECISION_CLAIM,
            "pipeline_callers_updated": _PIPELINE_CALLERS_UPDATED,
            "pipeline_callers_intentionally_unwired": _PIPELINE_CALLERS_INTENTIONALLY_UNWIRED,
            "tests": {
                "test_file": "computations/test_sigma_all_evaluator.py",
                "test_count": 11,
            },
            "evaluator_module": "computations/sigma_all_evaluator.py",
            "audit_doc_reference": "docs/audits/2026-05-02-nv-frob-filter-conjectures.md "
                                   "lines 683-769 (closed form + precision schedule)",
            "memo_doc_reference": "docs/audits/2026-05-03-frob-filter-evaluator-wired.md "
                                  "(this wiring task)",
        }


def _emit_witness(q: mp.mpf, start_time: float) -> str:
    """Write the witness beside this module."""
    from witness_base import WitnessBuilder  # late import; keeps the evaluator lean

    return (WitnessBuilder.wrap_legacy(
        "sigma-all-evaluator", build_witness(q),
        script_path=__file__,
        engine="python",
        start_time=start_time,
    ).save())


# ── Self-verification: when run as a script, compare against the
# symbolic table (A=1..6) at q_0 ─────────────────────────────────
if __name__ == "__main__":
    import time

    from q_parameter import Q_MP, q_at  # late import; not needed at use-site

    _t0 = time.monotonic()

    # Reference values from `sigma_all_symbolic_decay.py` (independent sympy
    # enumeration), evaluated at the q_0 that was live when they were stored.
    #
    # The comparison q is PINNED to that value and must not be swapped for the
    # current `q_at()`. What this cross-check tests is the algebraic identity
    # "closed form == symbolic enumeration", which is q-generic; evaluating the
    # two sides at two different q turns it into a q-drift measurement that
    # fails for a reason having nothing to do with the closed form.
    #
    # That is exactly what happened. After the 2026-05-28 proton re-pin,
    # `q_at()` moved 1.10997859555 -> 1.10997858275 while this table stayed at
    # the muon anchor, and the assert below started failing at 6.76e-07 against
    # a 1e-14 tolerance -- on `main`, for over a year. Nothing caught it because
    # nothing ran this file: the module produced no witness, so no pipeline
    # invoked it. Wiring the producer (below) is what surfaced it.
    #
    # Pinning both sides here makes the test survive every future re-pin. The
    # witness IS emitted at the live proton q_0, per the standing
    # experimental-anchor directive -- the two anchors are deliberate.
    # Kept as a STRING, not an mpf. `mp.mpf(<49-digit literal>)` here would be
    # built at the ambient dps (15 by default) and truncated at construction --
    # the value would already be wrong before it is used. `sigma_all_closed`
    # does its own `mp.mpf(q)` inside `mp.workdps(dps)`, so handing it the
    # string defers the conversion to full working precision.
    _SELFTEST_Q0 = "1.1099785955541805752815940796095093779932822799587"

    expected = {
        1:  0.5295037320168715,
        2: -0.3357233125749398,
        3:  0.035093211913212914,
        4: -0.022250285767622852,
        5:  0.002325825953473032,
        6: -0.001474652483748414,
    }

    print(f"Σ_all closed-form evaluator self-test at the table's q_0 = "
          f"{_SELFTEST_Q0}")
    print(f"{'A':>3} {'closed-form':>22} {'symbolic-table':>22} {'rel err':>12}")
    print("-" * 64)
    max_rel = 0.0
    q_hi = q_at(50)
    for A, exp in expected.items():
        got = sigma_all_closed(A, _SELFTEST_Q0, dps=50)
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
    print(f"Live q_0 (used for the witness below): {mp.nstr(q_hi, 20)}")

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

    # The self-test above is the gate; emit the witness only once it passes,
    # so a failing evaluator cannot overwrite a good reference table.
    print(f"\nWitness: {_emit_witness(q_hi, _t0)}")
