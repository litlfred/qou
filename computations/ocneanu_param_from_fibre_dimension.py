#!/usr/bin/env python3
"""Which fibre does the mass channel trace over?  `z = q^N / [N]_q`.

Companion probe to
`QOU/BraidsAndKnots/FibreDimensionForcesTL.lean` (bean `qou-n1dj`).

The Lean file proves, division-free over a generic commutative domain, that the
categorical (quantum) trace on `V^{otimes n}` for a fibre of quantum dimension
`dim_q V = [N]_q` has Ocneanu parameter

    z * [N]_q = q^N ,

so at `N = 2` it satisfies `z * [2]_q = q^2` -- verbatim the convention-D
condition that `MarkovTraceTLUniqueness.lean` derives from the Temperley-Lieb
quotient.  This script is the numerical companion: it checks the identity, then
uses it to answer the question the bean actually asks -- *which* trace the mass
channel uses -- by asking which fibre dimension each circulating convention
corresponds to.

Checks (all must pass):

  C1  shift identity   `q*[N+1] - q^-1*[N-1] = q^N*[2]`, exact rationals,
                       N = 1..8, several rational q.
  C2  `z_N := q^N/[N]_q` solves the Markov system with the H_3(q) q-character
      table, and the resulting weight vector has `y_(1^3) = 0` iff N = 2.
  C3  at N = 2 the weight vector is `([4]_q/[2]_q^3, 1/[2]_q^2, 0)` --
      convention D.
  C4  convention C's quoted parameter `z_C = 1/(q^(1/2)+q^(-1/2))` reproduces
      the corpus's C weight vector.
  C5  `N_eff(z_C)`, the fibre dimension C would need, is NOT an integer.
  C6  the corpus's OWN closed-form mass weights reproduce convention D:
      `feynman-markov-identification.md` defines tr_M as the sum over
      `lambda |- n` with `l(lambda) <= 2` of `w_lambda * tr_{S_lambda}`, with
      `w_lambda = dim_q(V_lambda) * dim(S_lambda) / dim_q(V^(tensor n))`.  At
      N = 2, `dim_q V_lambda = [2j+1]_q` for spin `j = (l1-l2)/2` and
      `dim_q V^(tensor n) = [2]_q^n`, giving exactly D.

Nothing here reads a CODATA or AME value, and nothing is compared against one:
the question "which convention" is settled by which fibre, not by which number
lands on experiment.  The substrate `q_0` enters only to print numbers at the
anchor; every structural conclusion (C1, C2, C5's non-integrality as an
identity) is q-independent.

q_0 pin: EXPERIMENTAL / proton (`m_p/m_e`), per the AGENTS 2026-08-07 owner
directive that all new compute defaults to the experimental anchor.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from mpmath import mp, mpf, log, sqrt

mp.dps = 50

# --- q_0: experimental (proton) pin, per AGENTS 2026-08-07 owner directive ---
Q0_PROTON_STR = "1.1099785827513808"
Q0_PIN = "experimental/proton (m_p/m_e)"


def q_int(m: int, q):
    """Balanced quantum integer `[m]_q = (q^m - q^-m)/(q - q^-1)`."""
    if m == 0:
        return q * 0
    return (q**m - q ** (-m)) / (q - q ** (-1))


# ---------------------------------------------------------------- C1


def check_shift_identity() -> dict:
    """`q*[N+1] - q^-1*[N-1] = q^N*[2]`, exact, over the rationals."""
    fails = []
    for qnum, qden in [(2, 1), (3, 1), (5, 2), (11, 10), (7, 5), (13, 4)]:
        q = Fraction(qnum, qden)
        for N in range(1, 9):
            lhs = q * q_int(N + 1, q) - q ** (-1) * q_int(N - 1, q)
            rhs = q**N * q_int(2, q)
            if lhs != rhs:
                fails.append({"q": f"{qnum}/{qden}", "N": N,
                              "lhs": str(lhs), "rhs": str(rhs)})
    return {"check": "C1 shift identity q[N+1]-q^-1[N-1]=q^N[2]",
            "n_cases": 6 * 8, "failures": fails, "pass": not fails}


# ---------------------------------------------------------------- Markov solve

def markov_weights(q, z):
    """Solve `tr = sum_lambda y_lambda chi^lambda` on H_3(q) for a given z.

    The three normalised-Markov-trace equations against the H_3(q)
    q-character table on the class representatives `1`, `sigma_0`,
    `sigma_0 sigma_1` (the table quoted in MarkovTraceTLUniqueness.lean):

        y_(3)   + 2 y_(2,1)          + y_(1^3)          = 1
        q y_(3) + (q - q^-1) y_(2,1) - q^-1 y_(1^3)     = z
        q^2 y_3 -           y_(2,1)  + q^-2 y_(1^3)     = z^2

    Returns `(y_(3), y_(2,1), y_(1^3))`.  Solved by hand elimination so the
    routine works for both `Fraction` and `mpf` inputs.
    """
    qi = q ** (-1)
    d = q + qi
    # (A): d*(y21 + y13) = q - z      [from eq1, eq2]
    s = (q - z) / d
    # (B): (2q^2+1) y21 + (q^2 - qi^2) y13 = q^2 - z^2   [from eq1, eq3]
    # with y21 = s - y13:
    #   (2q^2+1)(s - y13) + (q^2 - qi^2) y13 = q^2 - z^2
    #   y13 * [(q^2 - qi^2) - (2q^2+1)] = q^2 - z^2 - (2q^2+1) s
    coef = (q**2 - qi**2) - (2 * q**2 + 1)
    y13 = (q**2 - z**2 - (2 * q**2 + 1) * s) / coef
    y21 = s - y13
    y3 = 1 - 2 * y21 - y13
    return y3, y21, y13


def residual(q, z, y):
    """Max abs residual of the three Markov equations (sanity)."""
    qi = q ** (-1)
    y3, y21, y13 = y
    r = [y3 + 2 * y21 + y13 - 1,
         q * y3 + (q - qi) * y21 - qi * y13 - z,
         q**2 * y3 - y21 + qi**2 * y13 - z**2]
    return max(abs(x) for x in r)


# ---------------------------------------------------------------- C2, C3


def check_fibre_traces(q) -> dict:
    """`z_N = q^N/[N]_q`: y_(1^3) vanishes exactly at N = 2."""
    rows = []
    for N in (2, 3, 4, 5):
        z = q**N / q_int(N, q)
        y = markov_weights(q, z)
        rows.append({
            "N": N,
            "z": str(z),
            "y_3": str(y[0]), "y_21": str(y[1]), "y_13": str(y[2]),
            "markov_residual": str(residual(q, z, y)),
            "three_row_vanishes": abs(y[2]) < mpf(10) ** (-40),
        })
    vanishes = [r["N"] for r in rows if r["three_row_vanishes"]]
    return {"check": "C2 y_(1^3) = 0 iff N = 2", "rows": rows,
            "N_with_vanishing_three_row": vanishes, "pass": vanishes == [2]}


def check_jones_vector(q) -> dict:
    """At N = 2 the weights are `([4]/[2]^3, 1/[2]^2, 0)` -- convention D."""
    z = q**2 / q_int(2, q)
    y = markov_weights(q, z)
    pred = (q_int(4, q) / q_int(2, q) ** 3, 1 / q_int(2, q) ** 2, mpf(0))
    err = max(abs(a - b) for a, b in zip(y, pred))
    return {"check": "C3 N=2 weights = ([4]/[2]^3, 1/[2]^2, 0) = convention D",
            "z_D": str(z), "z_D_times_bracket2": str(z * q_int(2, q)),
            "q_squared": str(q**2),
            "y_solved": [str(v) for v in y],
            "y_closed_form": [str(v) for v in pred],
            "max_abs_err": str(err), "pass": err < mpf(10) ** (-40)}


# ---------------------------------------------------------------- C4, C5


def check_convention_c(q) -> dict:
    """`z_C = 1/(q^(1/2)+q^(-1/2))` reproduces the corpus's C weights.

    Convention C is EXCISED (owner ruling 2026-08-09, re-affirmed 2026-08-15).
    This check is an audit *of* C, not a use of it: it confirms that the C
    weights the corpus once quoted are the ones z_C actually produces, which is
    what makes the C-era numbers identifiable wherever they survive. Deleting it
    would remove the ability to recognise them.
    """
    z_c = 1 / (sqrt(q) + 1 / sqrt(q))   # EXCISED — audited here, not used
    y = markov_weights(q, z_c)
    # The C vector as quoted in bean qou-n1dj / h3-markov-wenzl-weights-context.
    quoted = (mpf("0.415396"), mpf("0.280930"), mpf("0.022745"))
    err = max(abs(a - b) for a, b in zip(y, quoted))
    return {"check": "C4 z_C reproduces the quoted convention-C weights",
            "z_C": str(z_c),
            "y_solved": [str(v) for v in y],
            "y_quoted_in_corpus": [str(v) for v in quoted],
            "max_abs_err_vs_quoted": str(err),
            "pass": err < mpf("1e-6")}


def check_effective_N(q) -> dict:
    """Invert `z = q^N/[N]_q` for N.  For z_C the answer is not an integer.

    `z(N) = q^N/[N]_q = (q - q^-1)/(1 - q^(-2N))` is strictly decreasing in N
    for `q > 1`, hence injective, so N is recoverable:

        N = -ln(1 - (q - q^-1)/z) / (2 ln q).
    """
    def N_of(z):
        return -log(1 - (q - q ** (-1)) / z) / (2 * log(q))

    z_c = 1 / (sqrt(q) + 1 / sqrt(q))
    n_eff = N_of(z_c)
    nearest = int(mp.nint(n_eff))
    dist = abs(n_eff - nearest)
    return {"check": "C5 N_eff(z_C) is not an integer",
            "z_2": str(q**2 / q_int(2, q)),
            "z_3": str(q**3 / q_int(3, q)),
            "z_C": str(z_c),
            "N_eff_of_z_C": str(n_eff),
            "nearest_integer": nearest,
            "distance_to_nearest_integer": str(dist),
            "roundtrip_N_of_z_2": str(N_of(q**2 / q_int(2, q))),
            "roundtrip_N_of_z_3": str(N_of(q**3 / q_int(3, q))),
            "pass": dist > mpf("0.01")}


# ---------------------------------------------------------------- C6


def check_corpus_closed_form_weights(q) -> dict:
    """The corpus's own mass-trace weights, evaluated, are convention D.

    `feynman-markov-identification.md` states

        tr_M = sum_{lambda |- n, l(lambda) <= 2} w_lambda tr_{S_lambda}(rho(beta)),
        w_lambda = dim_q(V_lambda) * dim(S_lambda) / dim_q(V^(tensor n)),

    and calls the result the *Jones*-Markov trace.  At N = 2, `V_lambda` has
    spin `j = (lambda_1 - lambda_2)/2`, so `dim_q V_lambda = [2j+1]_q`, and
    `dim_q V^(tensor n) = [2]_q^n`.  For n = 3 the surviving partitions are
    `(3)` (j = 3/2, `[4]_q`, `dim S = 1`) and `(2,1)` (j = 1/2, `[2]_q`,
    `dim S = 2`); `(1^3)` has `l = 3 > 2` and does not appear at all.

    Two things are checked:

      * Schur-Weyl normalisation `sum_lambda dim_q(V_lambda) dim(S_lambda)
        = [2]_q^n`, i.e. the corpus's `sum_lambda y_lambda d_lambda = 1`;
      * the per-block weight `y_lambda = dim_q(V_lambda)/[2]_q^n` equals the
        convention-D vector `([4]/[2]^3, 1/[2]^2, 0)`.
    """
    n = 3
    denom = q_int(2, q) ** n
    # (partition, 2j+1, dim S_lambda) for lambda |- 3 with l(lambda) <= 2
    blocks = [("(3)", 4, 1), ("(2,1)", 2, 2)]
    norm = sum(q_int(twojp1, q) * dimS for _, twojp1, dimS in blocks) / denom
    y = {name: q_int(twojp1, q) / denom for name, twojp1, dimS in blocks}
    y["(1^3)"] = mpf(0)  # absent from the index set entirely
    d_vec = (q_int(4, q) / q_int(2, q) ** 3, 1 / q_int(2, q) ** 2, mpf(0))
    err = max(abs(a - b) for a, b in
              zip((y["(3)"], y["(2,1)"], y["(1^3)"]), d_vec))
    # and it must satisfy the Markov equations at z_D
    z = q**2 / q_int(2, q)
    res = residual(q, z, (y["(3)"], y["(2,1)"], y["(1^3)"]))
    return {"check": ("C6 corpus's own closed-form mass weights "
                      "(feynman-markov-identification) = convention D"),
            "schur_weyl_normalisation_sum": str(norm),
            "y_from_corpus_formula": {k: str(v) for k, v in y.items()},
            "y_convention_D": [str(v) for v in d_vec],
            "max_abs_err": str(err),
            "markov_residual_at_z_D": str(res),
            "pass": (abs(norm - 1) < mpf(10) ** (-40)
                     and err < mpf(10) ** (-40)
                     and res < mpf(10) ** (-40))}


# ---------------------------------------------------------------- main


def main() -> int:
    q = mpf(Q0_PROTON_STR)
    checks = [
        check_shift_identity(),
        check_fibre_traces(q),
        check_jones_vector(q),
        check_convention_c(q),
        check_effective_N(q),
        check_corpus_closed_form_weights(q),
    ]
    all_pass = all(c["pass"] for c in checks)

    out = {
        "schema": "witness/v1",
        "name": "ocneanu-param-from-fibre-dimension",
        "description": (
            "The Ocneanu parameter of the categorical trace on V^(tensor n) is "
            "z = q^N/[N]_q, so the fibre dimension determines the trace. At "
            "N = 2 this is z*[2]_q = q^2, i.e. convention D; the parameter "
            "quoted for convention C corresponds to no integer N."
        ),
        "computation": {
            "script": "computations/ocneanu_param_from_fibre_dimension.py",
            "lean": ("content/quantum-observable-universe/lean/QOU/"
                     "BraidsAndKnots/FibreDimensionForcesTL.lean"),
            "bean": "qou-n1dj",
        },
        "q0": {"value": Q0_PROTON_STR, "pin": Q0_PIN, "dps": mp.dps},
        "uses_experimental_target_values": False,
        "checks": checks,
        "all_pass": all_pass,
        "verdict": (
            "convention D" if all_pass else "INCONCLUSIVE - see failing checks"
        ),
    }

    # Anchored to THIS FILE, not to the caller's cwd. The literal
    # `Path("computations/…")` only resolves when the producer happens to be
    # invoked from the repo root; the regeneration harness runs every producer
    # from its own directory, so this became
    # `computations/computations/ocneanu-…` and died with FileNotFoundError.
    # That reads in the journal as a producer failure and the witness is never
    # migrated — the same cwd-assumption class as the `parents[2]` bug fixed in
    # 12 scripts on this branch.
    path = Path(__file__).resolve().parent / "ocneanu-param-from-fibre-dimension.witness.json"
    path.write_text(json.dumps(out, indent=2) + "\n")

    for c in checks:
        print(f"[{'PASS' if c['pass'] else 'FAIL'}] {c['check']}")
    print()
    print(f"q_0 = {Q0_PROTON_STR}  ({Q0_PIN})")
    c5 = checks[4]
    print(f"  z(N=2)  = {c5['z_2'][:24]}   -> N = {c5['roundtrip_N_of_z_2'][:12]}")
    print(f"  z(N=3)  = {c5['z_3'][:24]}   -> N = {c5['roundtrip_N_of_z_3'][:12]}")
    print(f"  z_C     = {c5['z_C'][:24]}   -> N = {c5['N_eff_of_z_C'][:12]}"
          f"  (not an integer)")
    print()
    print(f"wrote {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
