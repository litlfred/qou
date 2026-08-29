#!/usr/bin/env python3
"""molien_jones_markov_n3_identification_probe.py — the Jones-Markov weights ARE
Webster-Williamson Molien series (n=3), exact. (beans qou-sf1t, qou-3quc.)

Resolves the 2026-08-21 Molien lead's items 4/2 (and the weight-level half of 1)
for n=3, and supplies the CORRECT normaliser that the 2026-08-22 refutation of
`y_lambda = f^lambda q^{-kappa}/[n]_q!` was missing.

## The two independently-computed objects

1. Webster-Williamson S_3 Molien series (arxiv-0911.4494v2 sec 6): with the
   reflection rep h (2-dim standard), E = Sym*(h*) (x) /\*(h*),
       M_nu(u,t) = sum_{i,j} u^i t^j dim Hom_{S3}(V_nu, Sym^i h* (x) /\^j h*)
   computed here by Molien: (1/6) sum_g chi_nu(g) det(1+t g)/det(1-u g).
2. Jones-Markov weights y_lambda(z) of the H_3(q) Markov trace, from the exact
   6-dim regular-rep character solve (qbeta_net_trace_invariance_probe machinery).

These share no inputs, so any match is an identity, not a tautology.

## The derivation (no fit)

Eliminate the weight variable t from the two Molien ratios M_sign/M_triv,
M_std/M_triv -> a Molien CONIC F(R1,R2,u)=0. Demand the three y_lambda ratios lie
on it: an OVERDETERMINED system (3 coefficients in z, one unknown u). Its ONLY
solution is the monomial u = q^2 (and its bar u = q^-2). At u=q^2 the weight
variable is forced t = q z/(q^2 - q z - 1), and then

    y_lambda = M_nu(u=q^2, t) * Z,     Z = (q^2 - q z - 1)^2

with ONE common perfect-square normaliser Z -- the Poincare/Molien shape the
lead predicted, NOT [n]_q!. Everything exact in Q(q,z).

Scope: n=3 only. General n (qou-3quc) is open; this is one strong data point.
Lean: QOU/QBeta/MolienJonesMarkovN3.lean (sorry-free, ring). Nothing wired.

-- Ref: [webster-williamson-2014-markov] arXiv:0911.4494 (geometry of Markov traces)
-- Ref: docs/audits/2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md
-- Ref: docs/audits/2026-08-22-ylambda-closed-form-refuted-and-a-float-trap.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, N, LEFT, basis_vec, reg_char, length, q, h,
)


def main() -> int:
    u, t, z = sp.symbols("u t z")

    # ---- (1) Webster-Williamson S_3 Molien series M_nu(u,t) ----
    # standard rep eigenvalues per class; (size, chi_triv, chi_sign, chi_std)
    classes = [
        (1, 1, 1, 2, (1 + t) ** 2, (1 - u) ** 2),
        (3, 1, -1, 0, (1 + t) * (1 - t), (1 - u) * (1 + u)),
        (2, 1, 1, -1, 1 - t + t ** 2, 1 + u + u ** 2),
    ]

    def M(idx):
        s = sum(c[0] * c[1 + idx] * c[4] / c[5] for c in classes)
        return sp.simplify(s / 6)

    Mtriv, Msign, Mstd = M(0), M(1), M(2)

    # ---- (2) Jones-Markov y_lambda(z) from the H_3 Markov trace ----
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]
    TR = [sp.Integer(1), z, z, z ** 2, z ** 2, z * (h * z + 1)]
    yv = sp.symbols("y0 y1 y2")
    sol = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)), TR[i])
                    for i in range(N)], yv, dict=True)[0]
    y3, y21, y111 = [sp.simplify(sol[yv[k]]) for k in range(3)]

    # ---- derivation: eliminate t, demand y ratios on the Molien conic, solve u ----
    R1, R2 = sp.symbols("R1 R2")
    r1 = Msign / Mtriv
    r2 = sp.simplify(Mstd / Mtriv)
    FM = sp.factor(sp.resultant(sp.Poly(sp.numer(sp.together(R1 - r1)), t),
                                sp.Poly(sp.numer(sp.together(R2 - r2)), t)))
    conic = [f for f, _ in sp.factor_list(FM)[1] if f.has(R1) or f.has(R2)][0]
    sub = sp.together(conic.subs({R1: y111 / y3, R2: y21 / y3}))
    p = sp.Poly(sp.expand(sp.numer(sub)), z)
    usols = sp.solve([sp.Eq(cf, 0) for cf in p.all_coeffs()], u, dict=True)
    usol_set = {sp.simplify(s[u]) for s in usols}

    # ---- verify the full identification at u=q^2 ----
    tspec = q * z / (q ** 2 - q * z - 1)
    Zexpected = (q ** 2 - q * z - 1) ** 2
    checks = {}
    Zs = []
    for nm, (Mnu, ynu) in {"(3)": (Mtriv, y3), "(1^3)": (Msign, y111),
                           "(2,1)": (Mstd, y21)}.items():
        Mval = Mnu.subs({u: q ** 2, t: tspec})
        Z = sp.simplify(ynu / Mval)
        Zs.append(Z)
        checks[f"y_{nm} = M_nu * Z"] = sp.simplify(ynu - Mval * Zexpected) == 0

    common_Z = all(sp.simplify(Zs[0] - Zk) == 0 for Zk in Zs[1:])
    Z_is_square = sp.simplify(Zs[0] - Zexpected) == 0
    forced = usol_set == {q ** 2, q ** (-2)} or usol_set == {q ** 2, 1 / q ** 2}

    print("Molien conic F(R1,R2,u) =", sp.expand(conic))
    print("u forced by the overdetermined system:", usol_set)
    print("common normaliser Z:", sp.factor(Zs[0]))
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print(f"  [{'PASS' if common_Z else 'FAIL'}] single common normaliser")
    print(f"  [{'PASS' if Z_is_square else 'FAIL'}] Z = (q^2 - q z - 1)^2 (perfect square)")
    print(f"  [{'PASS' if forced else 'FAIL'}] specialisation u=q^2 is forced (not fitted)")

    ok = all(checks.values()) and common_Z and Z_is_square and forced

    # ---- witness ----
    try:
        from witness_base import WitnessBuilder
    except Exception:
        print("(witness_base unavailable — printing only)")
        return 0 if ok else 1
    w = WitnessBuilder("molien-jones-markov-n3-identification", engine="sympy")
    w.set_description(
        "beans qou-sf1t/qou-3quc: the Jones-Markov weights y_lambda ARE the "
        "Webster-Williamson S_3 Molien series M_nu at the FORCED specialisation "
        "u=q^2, t=qz/(q^2-qz-1), with one common perfect-square normaliser "
        "Z=(q^2-qz-1)^2 (the Poincare/Molien shape, NOT [n]_q!). u=q^2 is the "
        "unique solution of an overdetermined elimination (3 z-coeffs, 1 unknown) "
        "-> a derivation, not a fit. Resolves the 2026-08-21 lead's items 4/2 and "
        "the weight-level half of item 1 for n=3; general n (qou-3quc) open. "
        "Exact Q(q,z); Lean QOU/QBeta/MolienJonesMarkovN3.lean sorry-free. Nothing wired."
    )
    w.set_audit_only("docs/audits/2026-08-29-molien-jones-markov-n3-identification.md")
    w.add_data("molien_conic", str(sp.expand(conic)))
    w.add_data("u_forced", str(sorted(map(str, usol_set))))
    w.add_data("t_specialisation", "q*z/(q^2 - q*z - 1)")
    w.add_data("normaliser_Z", "(q^2 - q*z - 1)^2")
    w.add_data("scope", "n=3 only; general n (qou-3quc) open")
    w.add_data("free_parameters", 0)
    for k, v in checks.items():
        w.add_assertion(k.replace(" ", "_"), 1 if v else 0, 1, source="exact Q(q,z)")
    w.add_assertion("specialisation_u_eq_qsq_is_forced", 1 if forced else 0, 1,
                    source="unique solution of the overdetermined conic system")
    w.add_assertion("normaliser_is_perfect_square", 1 if Z_is_square else 0, 1,
                    source="Z = (q^2 - q z - 1)^2")
    # q0Anchor DECLARED, not defaulted. `resolve_q0_anchor` returns "proton" for
    # any stem absent from the manifest -- the runtime DEFAULT, not evidence -- so
    # an undeclared witness goes out asserting a pin it never used, and
    # `q0_anchor_ratchet --strict` counts it as unstamped. Declared 2026-08-29,
    # bean `qou-6u53`, on an import-cone trace plus the absence of any q_0 value
    # in the payload.
    out = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-independent: everything is exact in Q(q,z), as this file's own "
            "docstring states. q_0 is reachable through an imported probe but is "
            "never evaluated at; no q_0 value reaches the payload."
        ),
    })
    print(f"witness -> {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
