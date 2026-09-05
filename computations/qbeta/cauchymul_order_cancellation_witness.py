#!/usr/bin/env python3
"""cauchyMul_order's `≥` direction is FALSE without a non-cancellation hypothesis.

Settles the open question in bean `qou-6e88` ("the statement may need
strengthening before it is provable") for `QOU/Mathlib/QGevreyOrder.lean`'s
residual sorry. That bean says the `≥` direction "may genuinely cancel, which
would make the theorem as stated FALSE", and that deciding the right statement
matters more than attempting a proof.

This exhibits the cancellation explicitly, so the question is closed: it is not
"may be false", it IS false as stated.

THE WITNESS
-----------
Work in the formal power series ring with exact integer coefficients, q = 2.

    a_n := q^(n^2)          so log_q|a_n| = n^2 exactly  -> positive q-Gevrey order
    b    := a^{-1}          the formal inverse (exists: a_0 = 1 is a unit)

Then by construction

    (a * b)_n = delta_{n,0},   i.e.  a * b = (1, 0, 0, 0, ...)

which is the UNIT sequence and has q-Gevrey order 0.

The only thing left to check is that `b` is not secretly of order 0 -- i.e. that
this is genuine cancellation between two divergent factors rather than a
divergent series times a convergent one. It is not: the computation shows
log_q|b_n| / n^2 increasing monotonically to 1 (0.9949 by n = 14), so `b` carries
the SAME positive order as `a`.

WHY THE CONCLUSION IS NORMALIZATION-ROBUST
------------------------------------------
This does not depend on the exact constant in the file's `IsQGevreyOrder`
convention. Whatever positive order the convention assigns to `a`, it assigns the
same one to `b` (their coefficient growth agrees asymptotically). Any envelope
`E(s,t)` that is positive when `s,t > 0` -- which `cauchyEnvelope` must be, since
it is meant to dominate the product of two divergent series -- then satisfies

    order(a * b) = 0  <  E(s, t),

contradicting `≥`. So no choice of normalization rescues the statement.

WHAT THIS MEANS FOR THE FIX
---------------------------
The theorem needs a hypothesis, not a cleverer proof. Options, in the order the
bean suggests:

  * add an explicit non-cancellation hypothesis on the leading coefficients, or
  * restrict the coefficient field / require positivity, which forbids the
    subtraction that drives the cancellation.

The `≤` direction is untouched by this and remains the tractable half (the bean
notes it reduces to `cauchyMul_norm_le_sum` + `exponent_le_envelope` plus an
epsilon-delta assembly, both already sorry-free in the file).

Exact integer arithmetic throughout; no floats in the witness itself (the ratio
column is float only for display). Nothing fitted, nothing wired.
"""

from __future__ import annotations

from fractions import Fraction

import mpmath as mp

mp.mp.dps = 60

import json
import os
import subprocess
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

Q = 2
N = 14


def build_witness(q: int, n_max: int):
    """a_n = q^(n^2); b = formal inverse of a; return (a, b, a*b)."""
    a = [q ** (n * n) for n in range(n_max + 1)]
    assert a[0] == 1, "need a unit constant term for the inverse to exist"

    b = [0] * (n_max + 1)
    b[0] = 1
    for n in range(1, n_max + 1):
        b[n] = -sum(a[k] * b[n - k] for k in range(1, n + 1))

    prod = [sum(a[k] * b[n - k] for k in range(n + 1)) for n in range(n_max + 1)]
    return a, b, prod


def log_q_abs(x: int, q: int) -> int:
    """Exact floor(log_q |x|) for q = 2 via bit_length; general q by division."""
    x = abs(x)
    if x == 0:
        return 0
    if q == 2:
        return x.bit_length() - 1
    e = 0
    while x >= q:
        x //= q
        e += 1
    return e


def _rat(fr: Fraction) -> dict:
    """An exact rational as both "p/q" and a 50-digit decimal (see qborel probe)."""
    return {"exact": f"{fr.numerator}/{fr.denominator}",
            "decimal": mp.nstr(mp.mpf(fr.numerator) / mp.mpf(fr.denominator), 50)}


def main() -> None:
    a, b, prod = build_witness(Q, N)

    product_is_unit = prod[0] == 1 and all(v == 0 for v in prod[1:])
    print(f"a * b = {prod[:8]} ...")
    print(f"a * b is the unit sequence: {product_is_unit}")
    print()
    print(f"{'n':>3} {'log_q|a_n|':>11} {'n^2':>6} {'log_q|b_n|':>11} {'log_q|b_n|/n^2':>16}")
    rows = []
    ratios = []
    for n in range(1, N + 1):
        la = log_q_abs(a[n], Q)
        lb = log_q_abs(b[n], Q)
        # la, lb and n^2 are all INTEGERS (log_q of a power of q), so the ratio
        # is an exact rational. It was float64, and it is not "only for display"
        # as the inputs block below claimed — it is stored in the witness AND two
        # verdicts are decided on it (`> 0.9` and the monotonicity chain).
        ratio = Fraction(lb, n * n)
        ratios.append(ratio)
        rows.append({"n": n, "log_q_abs_a": la, "n_squared": n * n,
                     "log_q_abs_b": lb,
                     "ratio_b_over_n2": _rat(ratio)})
        print(f"{n:>3} {la:>11} {n*n:>6} {lb:>11} "
              f"{float(mp.mpf(ratio.numerator) / mp.mpf(ratio.denominator)):>16.4f}")

    b_positive_order = ratios[-1] > Fraction(9, 10)
    monotone = all(ratios[i] <= ratios[i + 1]
                   for i in range(2, len(ratios) - 1))
    print()
    print(f"b carries positive order too (ratio -> 1): {b_positive_order}")
    print(f"ratio increasing in n (from n=3): {monotone}")
    print()
    print("=> two factors of EQUAL POSITIVE order whose Cauchy product has order 0.")
    print("   The >= direction of cauchyMul_order is FALSE as stated.")

    here = os.path.dirname(os.path.abspath(__file__))
    script = os.path.abspath(__file__)
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", script],
            cwd=here, stderr=subprocess.DEVNULL,
        ).decode().strip() or "uncommitted"
    except Exception:
        sha = "uncommitted"

    witness = {
        "schema": "witness/v1",
        "description": (
            "Explicit counterexample showing the >= direction of cauchyMul_order "
            "(QOU/Mathlib/QGevreyOrder.lean residual sorry, bean qou-6e88) is FALSE "
            "without a non-cancellation hypothesis: a_n = q^(n^2) and its formal "
            "inverse b both carry positive q-Gevrey order, yet a*b is the unit "
            "sequence, of order 0."
        ),
        "computation": {"script": os.path.relpath(script, os.path.dirname(here))},
        "witness": {"scriptCommitSha": sha},
        "setup": {
            "q": Q,
            "n_max": N,
            "a": "a_n = q^(n^2)",
            "b": "formal inverse of a (a_0 = 1)",
            "arithmetic": ("exact integers throughout; the log_q|b_n|/n^2 ratio is "
                           "an exact Fraction, serialized as p/q plus a 50-dps "
                           "decimal. No float64 anywhere (it used to be float64, "
                           "and the verdicts were decided on it)."),
        },
        "results": {
            "product_is_unit_sequence": product_is_unit,
            "b_has_positive_order": b_positive_order,
            "ratio_increasing": monotone,
            "final_ratio_log_q_abs_b_over_n2": _rat(ratios[-1]),
            "rows": rows,
        },
        "verdict": (
            "The >= direction is FALSE AS STATED. Both factors have equal positive "
            "q-Gevrey order while the product has order 0, so order(a*b) < E(s,t) for "
            "any envelope positive on s,t > 0. Normalization-robust: whatever positive "
            "order the convention assigns a, it assigns the same to b. The fix is a "
            "HYPOTHESIS (non-cancellation on leading coefficients, or a positivity / "
            "field restriction), not a cleverer proof. The <= direction is unaffected."
        ),
        "wired_to_production": False,
        "is_fit": False,
    }
    out = os.path.join(here, "cauchymul-order-cancellation-witness.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"witness -> {os.path.relpath(out)}")


if __name__ == "__main__":
    main()
