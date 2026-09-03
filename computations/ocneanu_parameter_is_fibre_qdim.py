#!/usr/bin/env python3
"""Why is the mass channel the N = 2 one?  Because N is the fibre's quantum
dimension, not a free choice.  (beans qou-w5fw / T3f successor, qou-8p1x)

The question
------------
`ocneanu_N_lockin_probe.py` closed one half of T3f: the `N = 2` and `N = 3`
Ocneanu traces are not proportional, so the mass pipeline cannot be re-tuned to
`N = 3`.  That left the successor question open:

    **why is the mass channel the N = 2 one?**

T3f's §1 table records the Ocneanu parameter's constraint as literally
"**Unknown**", on the grounds that "the Ocneanu trace is defined on `H_n(q)`
**abstractly** -- it does not require a specific `V` to exist."

That is true of the *abstract* trace.  It is not true of the trace the mass
pipeline actually uses.

The resolution
--------------
`feynman-eigenbasis.md` states what the mass *is*:

    "This replaces the continuum path integral with a finite algebraic
     operation: **the categorical trace** ... the sum runs over the finitely
     many irreducible summands of **V^{tensor n}**."

and quotes the skein relation

    q m(L_+) - q^{-1} m(L_-) = (q^{1/2} - q^{-1/2}) m(L_0),

which is HOMFLY `a P(L_+) - a^{-1} P(L_-) = z P(L_0)` at **`a = q`** -- i.e.
`a = q^{N-1}` with `N = 2`, already baked in.

So the mass channel does not use an abstract Markov trace with a chosen
parameter.  It uses the **categorical trace on an actual object**, and for that
trace the parameter is not free: it is read off from the object.

The identity that makes this exact
-----------------------------------
The total weight of the Markov trace at parameter `N` is

    sum over lambda |- n  of  f^lambda * s_lambda(1, q, ..., q^{N-1})

with `f^lambda` the number of standard Young tableaux (the dimension of the
`H_n(q)` irreducible) and `s_lambda(1,q,...,q^{N-1})` the principal
specialisation (the Ocneanu weight, per `schur_principal_mpmath`).  By the dual
Cauchy identity `p_1^n = sum_lambda f^lambda s_lambda`, evaluating at
`(1, q, ..., q^{N-1})` where `p_1 = 1 + q + ... + q^{N-1} = [N]_q` gives

    sum over lambda |- n  of  f^lambda * s_lambda(1,q,...,q^{N-1})  =  [N]_q^n.

The right-hand side is exactly the categorical trace of the identity on
`V^{tensor n}` when `dim_q V = [N]_q`.  So:

    **the Ocneanu parameter N is the quantum dimension of the fibre.**

It is not a knob.  Choosing `N` *is* choosing which `V` you are tracing over,
and the mass pipeline has already chosen: the Descartes condition fixes
`dim V = 2`, hence `[N]_q = [2]_q`, hence `N = 2`, hence `a = q^{N-1} = q` --
precisely the skein relation the mass block quotes.

What this script verifies (exact arithmetic)
--------------------------------------------
  C1  `sum_lambda f^lambda s_lambda(1,q,...,q^{N-1}) = [N]_q^n` for
      `n = 1..5` and `N = 2..4` at several exact rational `q`.  This is the
      identity that ties the trace parameter to the fibre.
  C2  `f^lambda` from the hook-length formula sums to `n!` (a sanity check on
      the SYT counts feeding C1).
  C3  the `q -> 1` shadow: the same identity becomes the classical Schur-Weyl
      dimension count `sum_lambda f^lambda dim V_lambda = N^n`.

Consequence
-----------
T3f's "Unknown" is resolved **for the mass channel**: the parameter is slaved to
the fibre's quantum dimension.  The freedom T3f identified is real, but it is
freedom to compute *other link invariants on the abstract algebra*, not freedom
in what the categorical trace of a given object is.

This also sharpens what an `N = 3` flavour channel would have to be.  It cannot
be "the same trace re-tuned" (excluded by the lock-in probe).  By this identity
it must be **the categorical trace on a genuinely 3-dimensional object** --
which is exactly the missing 3-dimensional fibre that `qou-8p1x` identifies as
the real gap.  So the Ocneanu route does not *avoid* needing a 3-dim fibre; it
restates the need for one.

Scope
-----
This is a **derivation of the constraint**, not a numerical result: the identity
is classical (dual Cauchy), and what is new here is only its application --
reading `N` as `dim_q V` rather than as a free parameter, and checking the
identity exactly against the framework's own conventions.

NOT claimed:
  * that the Descartes condition is itself derived.  It is an input here.
  * that no other trace could serve the mass pipeline.  The claim is narrower:
    *given* that the mass is the categorical trace on `V^{tensor n}` (which the
    corpus states), `N = dim_q V` follows.
  * anything about colour `SU(3)`.

Exact `Fraction` arithmetic; no floating point.
"""
from __future__ import annotations

import json
from fractions import Fraction
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
_OUT = HERE / "ocneanu-parameter-is-fibre-qdim.witness.json"


def partitions(n: int, maxpart: int | None = None):
    """All partitions of n as weakly decreasing tuples."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def cells(lam):
    return [(i, j) for i, row in enumerate(lam) for j in range(row)]


def hook_length(lam, i, j):
    arm = lam[i] - j - 1
    leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
    return arm + leg + 1


def n_of(lam):
    return sum(i * part for i, part in enumerate(lam))


def f_lambda(lam) -> int:
    """Number of standard Young tableaux, by the hook-length formula."""
    n = sum(lam)
    prod = 1
    for (i, j) in cells(lam):
        prod *= hook_length(lam, i, j)
    return factorial(n) // prod


def q_int(m: int, q: Fraction) -> Fraction:
    if m <= 0:
        return Fraction(0)
    return sum((q ** k for k in range(m)), Fraction(0))


def principal_spec(lam, N: int, q: Fraction) -> Fraction:
    """s_lambda(1, q, ..., q^{N-1}) by the q-hook-content formula."""
    num, den = Fraction(1), Fraction(1)
    for (i, j) in cells(lam):
        num *= q_int(N + (j - i), q)
        den *= q_int(hook_length(lam, i, j), q)
    return (q ** n_of(lam)) * num / den


def main() -> int:
    print("=" * 74)
    print("T3f successor : is the Ocneanu parameter the fibre's quantum dimension?")
    print("=" * 74)

    checks: dict[str, bool] = {}
    QS = [Fraction(2), Fraction(3), Fraction(5, 2), Fraction(11, 10), Fraction(7, 5)]

    # -- C2 : SYT counts sane -------------------------------------------
    c2 = True
    for n in range(1, 7):
        tot = sum(f_lambda(lam) for lam in partitions(n))
        # sum of (f^lambda)^2 = n!; sum of f^lambda = number of involutions.
        tot_sq = sum(f_lambda(lam) ** 2 for lam in partitions(n))
        c2 &= (tot_sq == factorial(n))
    checks["C2_sum_f_squared_eq_n_factorial"] = c2
    print(f"\nC2  sum_lambda (f^lambda)^2 = n! for n = 1..6 : {c2}")

    # -- C1 : the identity ----------------------------------------------
    print("\nC1  sum_lambda f^lambda * s_lambda(1,q,...,q^{N-1})  ==  [N]_q^n")
    print("    %-4s %-4s %-10s %s" % ("n", "N", "q", "holds"))
    c1 = True
    samples = []
    for n in range(1, 6):
        for N in (2, 3, 4):
            for q in QS:
                lhs = sum((Fraction(f_lambda(lam)) * principal_spec(lam, N, q)
                           for lam in partitions(n)), Fraction(0))
                rhs = q_int(N, q) ** n
                ok = lhs == rhs
                c1 &= ok
                if q == QS[0] and n <= 3:
                    print("    %-4d %-4d %-10s %s" % (n, N, q, ok))
                    samples.append({"n": n, "N": N, "q": str(q),
                                    "lhs": str(lhs), "rhs": str(rhs), "ok": ok})
    checks["C1_total_weight_eq_qdim_power"] = c1
    print(f"    all n = 1..5, N = 2..4, {len(QS)} values of q : {c1}")

    # -- C3 : q -> 1 shadow is classical Schur-Weyl ----------------------
    one = Fraction(1)
    c3 = True
    for n in range(1, 6):
        for N in (2, 3, 4):
            lhs = sum((Fraction(f_lambda(lam)) * principal_spec(lam, N, one)
                       for lam in partitions(n)), Fraction(0))
            c3 &= (lhs == Fraction(N ** n))
    checks["C3_q1_is_classical_schur_weyl"] = c3
    print(f"\nC3  q -> 1 gives the classical count sum f^lambda dim V_lambda = N^n : {c3}")

    # -- the reading -----------------------------------------------------
    print("\n    [N]_q is the quantum dimension of an N-dimensional fibre, so the")
    print("    total Ocneanu weight at parameter N equals the categorical trace")
    print("    of the identity on V^(tensor n) when dim_q V = [N]_q.")
    print("    => N is READ OFF the fibre; it is not a free knob.")
    print(f"\n    Descartes fixes dim V = 2  =>  [N]_q = [2]_q  =>  N = 2")
    print(f"                               =>  a = q^(N-1) = q")
    print("    which is exactly the skein relation feynman-eigenbasis.md quotes.")

    all_ok = all(checks.values())
    print("\n" + "=" * 74)
    print(f"ALL CHECKS PASS : {all_ok}")
    print("=" * 74)
    print("""
VERDICT (T3f successor)
-----------------------
THE MASS CHANNEL IS N = 2 BECAUSE N IS THE FIBRE'S QUANTUM DIMENSION.

T3f recorded the Ocneanu parameter's constraint as "Unknown", correctly, for
the ABSTRACT Markov trace on H_n(q) -- which indeed needs no V to exist. But
the mass pipeline does not use that trace. feynman-eigenbasis.md defines the
mass as the CATEGORICAL trace, summed "over the finitely many irreducible
summands of V^(tensor n)", and quotes the skein relation at a = q. For a
categorical trace the parameter is not a knob: the identity verified here,

    sum_lambda f^lambda s_lambda(1,q,...,q^{N-1}) = [N]_q^n,

says the total weight at parameter N is the categorical trace of the identity
on V^(tensor n) with dim_q V = [N]_q. So choosing N IS choosing V. Descartes
fixes dim V = 2, hence N = 2, hence a = q.

AND IT SHARPENS THE FLAVOUR QUESTION. An N = 3 flavour channel cannot be the
same trace re-tuned (excluded by the lock-in probe). By this identity it must
be the categorical trace on a genuinely 3-DIMENSIONAL OBJECT -- which is
exactly the missing 3-dimensional fibre qou-8p1x identifies as the real gap.
So the Ocneanu route does not AVOID needing a 3-dim fibre; it RESTATES the
need for one. The two open threads are one thread.

NOT CLAIMED: that the Descartes condition is derived (it is an input here);
that no other trace could serve the mass pipeline (the claim is conditional on
the corpus's own definition of mass as a categorical trace); anything about
colour SU(3).
""")

    payload = {
        "schema": "witness/v1",
        "description": (
            "The Ocneanu parameter N is the quantum dimension of the fibre, not "
            "a free knob: sum_lambda f^lambda s_lambda(1,q,..,q^{N-1}) = [N]_q^n, "
            "the categorical trace of the identity on V^(tensor n). Resolves "
            "T3f's 'Unknown' for the mass channel. Beans qou-w5fw, qou-8p1x."
        ),
        "computation": {
            "script": "computations/ocneanu_parameter_is_fibre_qdim.py",
            "arithmetic": "exact Fraction; hook-length + q-hook-content; no floats",
        },
        "data": {
            "identity": "sum_{lambda |- n} f^lambda * s_lambda(1,q,...,q^{N-1}) = [N]_q^n",
            "provenance": "dual Cauchy identity p_1^n = sum_lambda f^lambda s_lambda, evaluated at the principal specialisation where p_1 = [N]_q",
            "verified_for": {"n": "1..5", "N": "2..4", "q": [str(x) for x in QS]},
            "samples": samples,
            "reading": (
                "[N]_q is the quantum dimension of an N-dimensional fibre, so the "
                "total Ocneanu weight at parameter N is the categorical trace of "
                "the identity on V^(tensor n) with dim_q V = [N]_q; choosing N is "
                "choosing V"
            ),
            "corpus_basis": (
                "feynman-eigenbasis.md defines the mass as the categorical trace "
                "summed over irreducible summands of V^(tensor n), and quotes the "
                "skein relation at a = q (i.e. a = q^{N-1} with N = 2)"
            ),
            "verdict": (
                "the mass channel is N = 2 because the Descartes condition fixes "
                "dim V = 2 and the categorical trace's parameter is slaved to the "
                "fibre's quantum dimension; T3f's 'Unknown' is resolved for the "
                "mass channel"
            ),
            "sharpens_flavour": (
                "an N = 3 flavour channel cannot be the same trace re-tuned "
                "(lock-in probe) and by this identity must be the categorical "
                "trace on a genuinely 3-dimensional object -- the same missing "
                "3-dim fibre qou-8p1x identifies. The Ocneanu route restates the "
                "need for a 3-dim fibre rather than avoiding it"
            ),
            "not_claimed": [
                "that the Descartes condition is itself derived -- it is an input",
                "that no other trace could serve the mass pipeline; the claim is "
                "conditional on the corpus's own definition of mass as a "
                "categorical trace on V^(tensor n)",
                "anything about colour SU(3)",
            ],
            "all_checks_pass": all_ok,
            "checks": checks,
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=False)
    _OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {_OUT.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
