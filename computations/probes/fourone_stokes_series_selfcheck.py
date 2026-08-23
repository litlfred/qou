#!/usr/bin/env python3
"""Self-check of the figure-eight knot 4_1 Stokes q-series of Fantini-Wheeler.

Reference
---------
V. Fantini and C. Wheeler, "Summability for state integrals of hyperbolic
knots", arXiv:2410.20973v1 [math.GT] (28 Oct 2024).  Section 4.1 works the
figure-eight knot 4_1 in full at maximal saddle data (A, B) = (1, 2), giving
the 2x2 Stokes matrix S_{pi-eps, 0+eps} of the Borel-Laplace resummations of
its state integrals.  The building blocks are the q-series of eq (72), (73),
(74):

    g_m(q) = sum_{k>=0} (-1)^k q^{k(k+1)/2 + m k} / (q;q)_k^2                (72a)

    G_m(q) = sum_{k>=0} (-1)^k q^{k(k+1)/2 + m k} / (q;q)_k^2
                        * ( m - 2 E_1(q) + sum_{l=1}^{k} (1+q^l)/(1-q^l) )   (72b)

    E_1(q) = -1/4 + sum_{k>=1} q^k/(1-q^k)
           = -1/4 + q + 2q^2 + 2q^3 + 3q^4 + 2q^5 + 4q^6 + 2q^7
                        + 4q^8 + 3q^9 + ...                                  (73)

    g_0(q) = 1 - q - 2q^2 - 2q^3 - 2q^4 + q^6 + 5q^7 + 7q^8
                   + 11q^9 + 13q^10 + 16q^11 + ...                          (74a)

    2 G_0(q) = 1 - 7q - 14q^2 - 8q^3 - 2q^4 + 30q^5 + 43q^6 + 95q^7
                     + 109q^8 + 137q^9 + ...                                (74b)

What this probe establishes
---------------------------
1. eq (73) is *derived from scratch*, not merely transcribed.  The Lambert
   series sum_{k>=1} q^k/(1-q^k) equals sum_{n>=1} d(n) q^n, where d(n) is the
   number-of-divisors function sigma_0(n).  So E_1(q) = -1/4 + sum_n d(n) q^n,
   and the printed integer coefficients (1,2,2,3,2,4,2,4,3,...) are exactly
   d(1),...,d(9).  The probe computes d(n) independently (by counting divisors)
   and confirms both the closed-form Lambert expansion and the printed values.

2. The *full* eq (72) -> (74) machinery is exercised: g_0 and G_0 are assembled
   from E_1 via the (q;q)_k^2 Pochhammer series and the inner
   sum_{l=1}^k (1+q^l)/(1-q^l), then matched coefficient-by-coefficient against
   the printed eq (74).  This checks E_1 *in situ*, not just as an isolated
   sequence.

All arithmetic is exact (fractions.Fraction over Q[[q]] truncated at order N),
so there is no floating-point tolerance and nothing is fitted.  The muon anchor
of the QOU framework is the figure-eight knot 4_1 (via Vol(4_1) = 2*Cl_2(pi/3) = 6*Lambda(pi/3)
~ 2.0299, the *hyperbolic volume* -- a distinct object from these E_1 integer
q-series), so reproducing a published integer sequence for 4_1 is a
production-adjacent literature self-check.  Nothing here is wired to any QOU
observable.
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import subprocess
from fractions import Fraction
from pathlib import Path

# Truncation order for the power-series ring Q[[q]] / (q^{N+1}).
N = 16


# --------------------------------------------------------------------------
# Minimal exact power-series arithmetic over Q, truncated at order N.
# A series is a list of N+1 Fraction coefficients [a_0, a_1, ..., a_N].
# --------------------------------------------------------------------------
def zero() -> list[Fraction]:
    return [Fraction(0)] * (N + 1)


def smul(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return [c * x for x in a]


def sadd(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [a[i] + b[i] for i in range(N + 1)]


def ssub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return [a[i] - b[i] for i in range(N + 1)]


def smulseries(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    c = zero()
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if i + j > N:
                break
            if bj:
                c[i + j] += ai * bj
    return c


def sinv(a: list[Fraction]) -> list[Fraction]:
    """Inverse of a series with nonzero constant term."""
    assert a[0] != 0, "series not invertible (zero constant term)"
    b = zero()
    b[0] = Fraction(1) / a[0]
    for n in range(1, N + 1):
        s = Fraction(0)
        for i in range(1, n + 1):
            s += a[i] * b[n - i]
        b[n] = -s / a[0]
    return b


# --------------------------------------------------------------------------
# Number-theoretic ingredients.
# --------------------------------------------------------------------------
def divisor_count(n: int) -> int:
    """sigma_0(n): number of positive divisors of n."""
    return sum(1 for d in range(1, n + 1) if n % d == 0)


def lambert_divisor_series() -> list[Fraction]:
    """sum_{k>=1} q^k/(1-q^k), expanded as a power series.

    q^k/(1-q^k) = sum_{j>=1} q^{k j}, so coeff of q^n is the number of
    (k, j) with k*j = n, i.e. the number of divisors d(n).
    """
    coeff = zero()
    for k in range(1, N + 1):
        j = 1
        while k * j <= N:
            coeff[k * j] += 1
            j += 1
    return coeff


def E1_series() -> list[Fraction]:
    """E_1(q) = -1/4 + sum_{k>=1} q^k/(1-q^k)  [FW eq (73)]."""
    e = lambert_divisor_series()
    e[0] += Fraction(-1, 4)
    return e


def qpochhammer(k: int) -> list[Fraction]:
    """(q;q)_k = prod_{i=1}^{k} (1 - q^i), as a power series."""
    p = zero()
    p[0] = Fraction(1)
    for i in range(1, k + 1):
        factor = zero()
        factor[0] = Fraction(1)
        if i <= N:
            factor[i] = Fraction(-1)
        p = smulseries(p, factor)
    return p


def inner_reciprocal_sum(k: int) -> list[Fraction]:
    """sum_{l=1}^{k} (1+q^l)/(1-q^l), as a power series.

    (1+x)/(1-x) = 1 + 2 sum_{j>=1} x^j, with x = q^l.
    """
    s = zero()
    for l in range(1, k + 1):
        s[0] += Fraction(1)
        j = 1
        while l * j <= N:
            s[l * j] += Fraction(2)
            j += 1
    return s


def gm_Gm(m: int, E1: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """g_m(q) and G_m(q) from FW eq (72)."""
    g = zero()
    G = zero()
    for k in range(0, N + 1):
        expo = k * (k + 1) // 2 + m * k
        if expo > N:
            break
        poch2_inv = sinv(smulseries(qpochhammer(k), qpochhammer(k)))
        qexpo = zero()
        qexpo[expo] = Fraction(1)
        base = smulseries(qexpo, poch2_inv)  # q^expo / (q;q)_k^2
        base = smul(base, Fraction((-1) ** k))
        g = sadd(g, base)
        bracket = zero()
        bracket[0] += Fraction(m)
        bracket = ssub(bracket, smul(E1, Fraction(2)))
        bracket = sadd(bracket, inner_reciprocal_sum(k))
        G = sadd(G, smulseries(base, bracket))
    return g, G


# --------------------------------------------------------------------------
# Probe body.
# --------------------------------------------------------------------------
def main() -> int:
    E1 = E1_series()

    # -- Check 1: eq (73) integer coefficients == divisor function d(n). -----
    printed_E1 = [1, 2, 2, 3, 2, 4, 2, 4, 3]  # coeffs of q^1..q^9 (FW eq 73)
    derived_E1 = [int(E1[n]) for n in range(1, 10)]
    divisor_fn = [divisor_count(n) for n in range(1, 10)]
    e1_const_ok = E1[0] == Fraction(-1, 4)
    e1_vs_printed = derived_E1 == printed_E1
    e1_vs_divisor = derived_E1 == divisor_fn

    # -- Check 2: full eq (72)->(74) machinery for g_0 and 2 G_0. ------------
    g0, G0 = gm_Gm(0, E1)
    printed_g0 = [1, -1, -2, -2, -2, 0, 1, 5, 7, 11, 13, 16]  # q^0..q^11
    printed_2G0 = [1, -7, -14, -8, -2, 30, 43, 95, 109, 137]  # q^0..q^9
    derived_g0 = [int(g0[n]) for n in range(0, 12)]
    derived_2G0 = [int(2 * G0[n]) for n in range(0, 10)]
    g0_ok = derived_g0 == printed_g0
    G0_ok = derived_2G0 == printed_2G0

    assertions = [
        {
            "name": "E1_constant_term_is_minus_one_quarter",
            "computed": str(E1[0]),
            "expected": "-1/4",
            "passed": e1_const_ok,
        },
        {
            "name": "E1_integer_coeffs_match_printed_eq73",
            "computed": derived_E1,
            "expected": printed_E1,
            "passed": e1_vs_printed,
        },
        {
            "name": "E1_integer_coeffs_equal_divisor_function_sigma0",
            "computed": derived_E1,
            "expected": divisor_fn,
            "passed": e1_vs_divisor,
        },
        {
            "name": "g0_series_matches_printed_eq74a",
            "computed": derived_g0,
            "expected": printed_g0,
            "passed": g0_ok,
        },
        {
            "name": "two_G0_series_matches_printed_eq74b",
            "computed": derived_2G0,
            "expected": printed_2G0,
            "passed": G0_ok,
        },
    ]
    all_passed = all(a["passed"] for a in assertions)

    # -- Full derived E_1 tail (for the witness record). --------------------
    e1_full = {str(n): (str(E1[0]) if n == 0 else int(E1[n])) for n in range(0, N + 1)}

    def _git(args: list[str]) -> str:
        try:
            return subprocess.check_output(
                ["git", *args], cwd=Path(__file__).resolve().parent, text=True
            ).strip()
        except Exception:
            return ""

    script_path = Path(__file__).resolve()
    script_bytes = script_path.read_bytes()
    witness = {
        "computation": "fourone-stokes-series-selfcheck",
        "scriptFile": script_path.name,
        "scriptHash": hashlib.sha256(script_bytes).hexdigest()[:12],
        "commitSha": _git(["rev-parse", "HEAD"]),
        "scriptCommitSha": _git(["log", "-1", "--format=%H", "--", script_path.name]),
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": "python-fractions (exact Q[[q]] arithmetic)",
        "reference": "Fantini-Wheeler, arXiv:2410.20973v1, Section 4.1, eq (72)-(74)",
        "knot": "4_1 (figure-eight)",
        "saddle_data_AB": [1, 2],
        "max_saddle": 2,
        "truncation_order_N": N,
        "closed_form": {
            "E1": "E_1(q) = -1/4 + sum_{k>=1} q^k/(1-q^k) = -1/4 + sum_{n>=1} d(n) q^n",
            "d(n)": "sigma_0(n), the number-of-divisors function",
        },
        "derived": {
            "E1_constant": str(E1[0]),
            "E1_coeffs_q1_to_qN": e1_full,
            "g0_coeffs_q0_to_q11": derived_g0,
            "two_G0_coeffs_q0_to_q9": derived_2G0,
        },
        "assertions": assertions,
        "allPassed": all_passed,
        "verdict": (
            "MATCH -- E_1 (eq 73) derived from the divisor-function Lambert "
            "series reproduces the published integer sequence exactly; the full "
            "eq (72)->(74) machinery (g_0, G_0) also matches FW eq (74)."
            if all_passed
            else "MISMATCH -- see failing assertions."
        ),
        "discipline": (
            "self-check vs published integer sequence (Fantini-Wheeler eq 73); "
            "no fit; nothing wired"
        ),
    }

    out_path = script_path.with_name("fourone-stokes-series-selfcheck.witness.json")
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` — and a witness without one cannot be
    # compared against its producer, so it drops OUT of the self-staleness
    # audit and reads as "not stale" forever. Regenerating it then looks
    # like progress while removing it from the count: a false drain.
    # Full rationale and the detector: computations/witness_drain_audit.py.
    #
    # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
    # fields in place and leaves the on-disk shape untouched, so consumers
    # of legacy `assertions` records (which key on `label`, not `name`) do
    # not have to change. `engine` is passed back from the payload because
    # the helper overwrites it, and a descriptive engine string is worth
    # keeping.
    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:  # cluster subdir without the _path_bridge bootstrap
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(next(
            _a / "substrate" for _a in _Path(__file__).resolve().parents
            if (_a / "substrate" / "witness_base.py").is_file())))
        from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", 'python'))
    out_path.write_text(json.dumps(witness, indent=2) + "\n")

    # -- Console summary. ---------------------------------------------------
    print("Fantini-Wheeler 4_1 Stokes-series self-check (arXiv:2410.20973v1, Sec 4.1)")
    print(f"  (A, B) = (1, 2), max saddle = 2")
    print(f"  E_1(q) = -1/4 + sum_n d(n) q^n   [eq (73)]")
    print(f"    constant term       : {E1[0]}   (expected -1/4)  -> {e1_const_ok}")
    print(f"    coeffs q^1..q^9     : {derived_E1}")
    print(f"    printed eq (73)     : {printed_E1}   -> {e1_vs_printed}")
    print(f"    divisor fn d(1..9)  : {divisor_fn}   -> {e1_vs_divisor}")
    print(f"  g_0(q) q^0..q^11      : {derived_g0}")
    print(f"    printed eq (74a)    : {printed_g0}   -> {g0_ok}")
    print(f"  2 G_0(q) q^0..q^9     : {derived_2G0}")
    print(f"    printed eq (74b)    : {printed_2G0}   -> {G0_ok}")
    print(f"  allPassed = {all_passed}")
    print(f"  witness -> {out_path.name}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
