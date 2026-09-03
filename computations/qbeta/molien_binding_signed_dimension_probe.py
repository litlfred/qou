#!/usr/bin/env python3
"""molien_binding_signed_dimension_probe.py — the binding signed-dimensions
Delta_lambda are read off the SAME S_n Molien series as the Jones-Markov weights
(qou-3quc / qou-sf1t; the "Molien -> binding" hook).

## Context

The companion probes/Lean (molien_jones_markov_n3_identification_probe.py,
MolienJonesMarkovN3.lean) established that the H_n(q) Jones-Markov weights ARE
the Webster-Williamson S_n reflection-rep Molien series M_nu(u,t) at the forced
specialisation u=q^2, t=qz/(q^2-qz-1):

    y_lambda(q,z) = M_nu(u=q^2, t=qz/(q^2-qz-1)) * (1 + qz - q^2)^(n-1).

The binding formula is B = m_e * Sum_lambda y_lambda chi^lambda Delta_lambda with
the PROVED per-partition signed dimension (2026-08-02, sorry-free, general-n,
QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional):

    Delta_lambda = (-1)^{n(lambda)} * dim V_lambda

n(lambda) the jet-order valuation parity, dim V_lambda the Wedderburn dimension.

## This probe's claim (the hook)

Delta_lambda is encoded in the SAME Molien object, at the OTHER corner of the
bigrading (t=0, the Sym-only / fake-degree edge):

    fd_lambda(u) := numerator of M_nu(u, t=0)   (the fake-degree polynomial)
    n(lambda)    = u-valuation (lowest u-degree) of fd_lambda(u)
    dim V_lambda = fd_lambda(1)

so   Delta_lambda = (-1)^{u-val fd_lambda} * fd_lambda(1).

Both the weights y_lambda (from the (u=q^2, t=qz/W) corner) AND the binding
signed-dimensions Delta_lambda (from the (u, t=0) fake-degree edge) come from the
ONE bigraded Molien series M_nu(u,t). That is what Molien buys for binding: the
whole B = Sum y_lambda chi^lambda Delta_lambda is a single Molien object read at
two specialisations.

Verified EXACT (sympy, no float) at S_3 and S_4 against the independently-known
(n(lambda), dim V_lambda) table. Nothing wired; free_parameters = 0.

-- Ref: [webster-williamson-2014-markov] arXiv:0911.4494 (geometry of Markov traces)
-- Ref: computations/qbeta/molien_jones_markov_n3_identification_probe.py (weights corner)
-- Ref: QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional (Delta_lambda proved)
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

u = sp.Symbol("u")


def fake_degree(classes, chars, nm, order, degrees):
    """The fake-degree polynomial fd_lambda(u) of V_lambda.

    fd_lambda(u) = M_nu(u,0) * PROD_i (1 - u^{d_i}),  where {d_i} are the
    fundamental degrees of the reflection group (for S_n on the reflection rep,
    d_i = 2,3,...,n) and M_nu(u,0) = (1/|G|) Sum_g chi_nu(g)/det(1-u g) is the
    graded multiplicity of V_lambda in the symmetric algebra of h*. Multiplying
    by the FULL coinvariant denominator (not the reduced one) makes it a genuine
    polynomial with non-negative integer coefficients whose sum is dim V_lambda:

        u-valuation fd_lambda = n(lambda)   (jet-order / lowest occurrence degree)
        fd_lambda(1)          = dim V_lambda.
    """
    s = sum(sz * chars[nm][k] / det for k, (sz, det) in enumerate(classes))
    Mu0 = sp.together(s / order)
    coinv_den = sp.prod([1 - u ** d for d in degrees])
    fd = sp.expand(sp.cancel(Mu0 * coinv_den))
    return sp.Poly(fd, u)


def run_case(name, classes, chars, order, degrees, table):
    """table: nm -> (n_lambda, dim_V_lambda) known independently."""
    print(f"### {name}  (fundamental degrees {degrees})")
    ok = True
    rows = []
    for nm, (nlam, dim) in table.items():
        fd = fake_degree(classes, chars, nm, order, degrees)
        monoms = fd.monoms()
        uval = min(m[0] for m in monoms) if monoms else 0
        fd1 = int(fd.as_expr().subs(u, 1))
        # non-negative integer coefficients (genuine graded-multiplicity polynomial)
        coeffs = [int(c) for c in fd.all_coeffs()]
        nonneg = all(c >= 0 for c in coeffs)
        delta_want = (-1) ** nlam * dim
        delta_got = (-1) ** uval * fd1
        row_ok = (uval == nlam) and (fd1 == dim) and nonneg and (delta_got == delta_want)
        ok = ok and row_ok
        rows.append((nm, fd.as_expr(), uval, nlam, fd1, dim, delta_got, delta_want, row_ok))
        print(f"  {nm:>8}: fd(u)={fd.as_expr()}")
        print(f"           u-val={uval} (n={nlam})  fd(1)={fd1} (dim={dim})  "
              f"coeffs>=0={nonneg}  Delta=(-1)^{uval}*{fd1}={delta_got} (want {delta_want})  "
              f"[{'PASS' if row_ok else 'FAIL'}]")
    return ok, rows


def main() -> int:
    # S_3, reflection rep dim 2. classes: (size, det(1-u g)); char of reflection rep
    # per class is the standard-rep character; chars below are chi_nu per class.
    cls3 = [(1, (1 - u) ** 2), (3, (1 - u) * (1 + u)), (2, 1 + u + u ** 2)]
    ch3 = {"(3)": [1, 1, 1], "(2,1)": [2, 0, -1], "(1^3)": [1, -1, 1]}
    tbl3 = {"(3)": (0, 1), "(2,1)": (1, 2), "(1^3)": (3, 1)}
    ok3, rows3 = run_case("S_3", cls3, ch3, 6, [2, 3], tbl3)

    # S_4, reflection rep dim 3.
    cls4 = [(1, (1 - u) ** 3), (6, (1 - u) ** 2 * (1 + u)),
            (3, (1 - u) * (1 + u) ** 2), (8, (1 - u) * (1 + u + u ** 2)),
            (6, (1 + u) * (1 + u ** 2))]
    ch4 = {"(4)": [1, 1, 1, 1, 1], "(3,1)": [3, 1, -1, 0, -1],
           "(2,2)": [2, 0, 2, -1, 0], "(2,1,1)": [3, -1, -1, 0, 1],
           "(1^4)": [1, -1, 1, 1, -1]}
    tbl4 = {"(4)": (0, 1), "(3,1)": (1, 3), "(2,2)": (2, 2),
            "(2,1,1)": (3, 3), "(1^4)": (6, 1)}
    ok4, rows4 = run_case("S_4", cls4, ch4, 24, [2, 3, 4], tbl4)

    ok = ok3 and ok4
    print(f"\nVERDICT: Delta_lambda = (-1)^(u-val fd_lambda) * fd_lambda(1) from the "
          f"fake-degree edge of the SAME Molien series {'CONFIRMED' if ok else 'FAILED'} "
          f"at S_3, S_4. Binding signed-dims and Jones-Markov weights are two "
          f"specialisations of one bigraded M_nu(u,t).")

    try:
        from witness_base import WitnessBuilder
    except Exception:
        return 0 if ok else 1
    w = WitnessBuilder("molien-binding-signed-dimension", engine="sympy")
    w.set_description(
        "bean qou-3quc (Molien->binding hook): the PROVED binding signed dimensions "
        "Delta_lambda = (-1)^{n(lambda)} dim V_lambda are read off the SAME "
        "Webster-Williamson S_n Molien series M_nu(u,t) that gives the Jones-Markov "
        "weights -- at the fake-degree edge t=0: n(lambda) = u-valuation of "
        "fd_lambda(u)=numer M_nu(u,0), dim V_lambda = fd_lambda(1). Weights live at "
        "(u=q^2, t=qz/(q^2-qz-1)); binding signed-dims live at (u, t=0). The whole "
        "B = Sum y_lambda chi^lambda Delta_lambda is one bigraded Molien object read "
        "at two corners. Exact sympy at S_3, S_4. Nothing wired."
    )
    w.set_audit_only("docs/audits/2026-08-29-molien-jones-markov-n3-identification.md")
    w.add_data("delta_from_molien", "Delta_lambda = (-1)^(u-val fd_lambda) * fd_lambda(1)")
    w.add_data("fake_degree_edge", "fd_lambda(u) = numerator of M_nu(u, t=0)")
    w.add_data("free_parameters", 0)
    w.add_assertion("s3_delta_from_fake_degree", 1 if ok3 else 0, 1,
                    source="(-1)^(u-val) fd(1) == (-1)^n(lambda) dim, exact sympy S_3")
    w.add_assertion("s4_delta_from_fake_degree", 1 if ok4 else 0, 1,
                    source="(-1)^(u-val) fd(1) == (-1)^n(lambda) dim, exact sympy S_4")
    # q0Anchor DECLARED, not defaulted. `resolve_q0_anchor` returns "proton" for
    # any stem absent from the manifest -- the runtime DEFAULT, not evidence -- so
    # an undeclared witness goes out asserting a pin it never used, and
    # `q0_anchor_ratchet --strict` counts it as unstamped. Declared 2026-08-29,
    # bean `qou-6u53`, on an import-cone trace plus the absence of any q_0 value
    # in the payload.
    out = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-independent: q_0 is unreachable from this producer's entire import "
            "cone. Signed dimensions are Wedderburn/Springer counts, not substrate "
            "evaluations."
        ),
    })
    print(f"witness -> {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
