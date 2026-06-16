#!/usr/bin/env python3
"""qbeta_ck_sseries_operator_match_probe.py — DECISIVE test of whether
exact CONSTANT c_k exist (Hoefsmit Stage B, path 1).

⚠ STATUS: WIP SCAFFOLD — does NOT yet run to a trustworthy result.
Two blockers found on the 2026-06-16 attempt (see
docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md §"Empirical"):

  BLOCKER 1 (object). The operator object used here, Q_beta(q) =
    E_0(q) * tau_M(T_beta)(q) with E_0 = 1/(q(q-1)), DIVERGES at q=1
    (E_0 pole), but the true Q_beta(1) = 2*m_e is FINITE. So this is the
    WRONG object: the canonical Q_beta = |Delta(net)(q)| * E_0(q) needs
    the GB-reduced Delta(net)(q) carrying a (q-1) ZERO to cancel the E_0
    pole. free-neutron-decay.witness.json has only NUMERIC net coeffs at
    q0 — Delta(net)(q) as a symbolic q-function must be produced by
    free-neutron-decay.py::reduce_verbose run with a SYMBOLIC q.
    => the c_2 gate would FAIL with the placeholder object below.

  BLOCKER 2 (performance). Full sympy series to order s^{2*KC+3} with
    sqrt(q)/cos/log TIMES OUT (>9 min at KC=8). Switch to a NUMERIC
    mpmath s-Taylor (high-precision finite differences or mp.taylor of
    the regularised R) + numeric triangular solve; keep the c_2 = -1
    gate as the correctness check.

To complete: (a) wire Delta(net)(q) symbolic from the GB reducer,
(b) numeric mpmath s-series, (c) re-run; PASS the c_2 gate before
trusting c_3..c_8; check the next-order residual for constant-c_k
consistency (nonzero => c_k are q-dependent, kernel needed).

--- original design (the math is right; the object + perf need the
above fixes) ---

Strategy (avoids the singular u-reversion of PR #1840): expand the
operator ladder ratio R(q) and u(q) BOTH as exact power series in
s = q - 1, then match

    log R(s)  =  sum_{k>=2} c_k * u(s)^k

order-by-order in s.  u(s) ~ (sqrt3/2) s^2 + ... starts at s^2, so c_2
first appears at s^4, c_3 at s^6, ..., c_k at s^{2k}.  No q->u inversion
(no sqrt branch); the match is a linear triangular solve in s-orders.

GATE (recipe Stage 3, critical): c_2 MUST come out = -1 (proved,
Taylor-exact, PR #1786).  If the gate FAILS the operator/normalisation
convention is wrong -> we report that and STOP (no trusting c_4..c_8).
If it PASSES we read c_3..c_8 as the first unbiased operator values and
test whether the match is CONSISTENT (constant c_k exist) by checking
the residual at the next s-order.

No production wiring. auditOnly.
"""
from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import json  # noqa: E402
import ast  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent


def hoefsmit_blocks(q):
    s0_3 = sp.Matrix([[q]]); s1_3 = sp.Matrix([[q]])
    s0_111 = sp.Matrix([[-1/q]]); s1_111 = sp.Matrix([[-1/q]])
    b = sp.sqrt(q**4 + q**2 + 1)/(q**2 + 1)
    s0_21 = sp.Matrix([[q, 0], [0, -1/q]])
    s1_21 = sp.Matrix([[-1/(q*(q**2+1)), b], [b, q**3/(q**2+1)]])
    return {"(3)": (s0_3, s1_3), "(2,1)": (s0_21, s1_21),
            "(1,1,1)": (s0_111, s1_111)}


def nf_basis_mats(s0, s1):
    eye = sp.eye(s0.rows)
    return [eye, s0, s1, s0*s1, s1*s0, s0*s1*s0]


def load_y_lambda(q):
    r = sp.sqrt(q)
    with open(_pb.witness_path("y-lambda-cyclotomic-factor.witness.json", HERE)) as f:
        data = json.load(f)
    n3 = data["results"]["3"]
    out = {}
    for part_str, info in n3.items():
        expr = sp.sympify(info["y_polynomial"]["polynomial_q"], locals={"r": r})
        part = tuple(ast.literal_eval(part_str))
        lab = {(3,): "(3)", (2, 1): "(2,1)", (1, 1, 1): "(1,1,1)"}.get(part)
        if lab:
            out[lab] = expr
    return out


def main() -> int:
    q = sp.Symbol("q", positive=True)
    KC = 8                      # highest c_k
    SORD = 2*KC + 3             # s-series order

    print("="*78)
    print(" Hoefsmit Stage B — exact s-series operator c_k match (c_2 gate)")
    print("="*78)

    # exact A_i(q)
    blocks = hoefsmit_blocks(q)
    y_lam = load_y_lambda(q)
    chi = {lab: [sp.trace(m) for m in nf_basis_mats(s0, s1)]
           for lab, (s0, s1) in blocks.items()}
    A = [sp.simplify(sum(y_lam[lab]*chi[lab][i] for lab in blocks)) for i in range(6)]

    # q0 (live proton anchor)
    from codata_constants import M_E_MEV  # noqa
    q0_str = json.load(open(_pb.witness_path("q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"]
    q0 = sp.Float(q0_str, 50)
    A_q0 = [a.subs(q, q0) for a in A]
    normsq0 = sum(a**2 for a in A_q0)
    # g(q) = (A(q).A(q0))/||A(q0)||^2  -> operator trace shape, g(q0)=1
    g = sum(A[i]*A_q0[i] for i in range(6))/normsq0

    # substrate scalars
    h = q - 1/q
    z = 1/(sp.sqrt(q) + 1/sp.sqrt(q))
    hbar = (q - 1)/q
    b = sp.sqrt(q**4 + q**2 + 1)/(q**2 + 1)
    alpha = (z - 1)*h/2
    u = b*hbar**2
    alpha_eff = alpha - u/2
    E0 = 1/(q*(q - 1))            # m_e cancels in R
    QA_over_me = (2*q + 1 - q**2)*(q + 1)/(2*q**3)   # substrate branch

    # Q_beta(q) ~ E0 * g  ;  R = Q_beta/[Q_A cos(alpha_eff)]
    R_raw = (E0*g)/(QA_over_me*sp.cos(alpha_eff))

    # series in s = q-1
    s = sp.Symbol("s")
    print("  expanding R(s), u(s) in s = q-1 (this is the slow step)...")
    R_s = sp.series(R_raw.subs(q, 1 + s), s, 0, SORD).removeO()
    u_s = sp.series(u.subs(q, 1 + s), s, 0, SORD).removeO()
    # normalise R(s->0) -> 1
    R0 = sp.limit(R_raw.subs(q, 1 + s), s, 0)
    print(f"  R(q->1) (pre-norm) = {sp.nsimplify(R0) if R0.is_number else R0}")
    R_s = sp.series((R_raw/R0).subs(q, 1 + s), s, 0, SORD).removeO()

    # log R and u^k as s-series
    logR = sp.series(sp.log(R_s), s, 0, SORD).removeO()
    u_pows = {}
    acc = sp.Integer(1)
    for k in range(1, KC + 1):
        acc = sp.expand(sp.series(acc*u_s, s, 0, SORD).removeO())
        u_pows[k] = acc
    # leading s-power of u^k is 2k (u ~ s^2). c_k first enters log R at s^{2k}.
    # log(prod(1+c_k u^k)) = sum_m P_m where the s-expansion mixes; solve
    # triangularly: at order s^{2k}, the new unknown is c_k (since u^j for
    # j<k contribute via products of lower c's already known, and log
    # cross-terms c_i c_j appear at s^{2(i+j)} > s^{2k} for i,j>=2... but
    # c_2^? at s^8 etc). Do an exact order-by-order solve.
    c = {}
    # Build symbolic target: logR_target(s) = sum_k c_k u_pows[k] - (1/2)(...)
    # Easiest robust route: define F(s) = sum_k C_k * u_pows[k] with C_k
    # sympy symbols, expand log(prod(1+C_k u^k)) to SORD, equate to logR,
    # solve order by order at s^{2k}.
    Csym = {k: sp.Symbol(f"C{k}") for k in range(2, KC + 1)}
    prod = sp.Integer(1)
    for k in range(2, KC + 1):
        prod = sp.expand(sp.series(prod*(1 + Csym[k]*u_pows[k]), s, 0, SORD).removeO())
    logprod = sp.series(sp.log(prod), s, 0, SORD).removeO()
    diff = sp.expand(logR - logprod)
    solved = {}
    gate_ok = None
    consistent = True
    for k in range(2, KC + 1):
        order = 2*k
        coeff_eq = diff.coeff(s, order)
        coeff_eq = coeff_eq.subs(solved)
        sol = sp.solve(sp.Eq(coeff_eq, 0), Csym[k])
        if not sol:
            print(f"  c_{k}: NO solution at s^{order} (over-determined?)")
            consistent = False
            break
        ck = sp.nsimplify(sol[0], rational=False)
        ck_val = complex(sp.N(sol[0], 30))
        solved[Csym[k]] = sol[0]
        c[k] = ck_val
        print(f"  c_{k} (from s^{order}) = {sp.N(sol[0], 12)}")
        if k == 2:
            gate_ok = abs(ck_val.real - (-1.0)) < 1e-6 and abs(ck_val.imag) < 1e-9
            print(f"    GATE c_2 == -1 ? {'PASS ✓' if gate_ok else 'FAIL ✗'}")
            if not gate_ok:
                print("    -> convention/normalisation wrong; c_3.. NOT trustworthy.")
    # consistency: residual at s^{2*KC+1}/s^{2*KC+2} after all c_k solved
    resid = sp.expand(diff.subs(solved))
    resid_next = None
    for extra in (2*KC + 1, 2*KC + 2):
        cc = resid.coeff(s, extra)
        if cc != 0:
            resid_next = (extra, complex(sp.N(cc, 20)))
            break

    print()
    print(f"  c_2 gate: {'PASS' if gate_ok else 'FAIL'}")
    print(f"  c_k solved: {sorted(c)}")
    if resid_next:
        print(f"  residual at s^{resid_next[0]} = {resid_next[1]:.3e} "
              f"(nonzero -> constant-c_k match is APPROXIMATE, c_k are q-dependent)")
    print()

    wb = WitnessBuilder("qbeta-ck-sseries-operator-match", engine="sympy")
    wb.set_description(
        "Hoefsmit Stage B path-1 attempt: exact s=q-1 series match of the "
        "min-L2 T_beta operator ladder R=Q_beta/[Q_A cos(alpha_eff)] against "
        "prod(1+c_k u^k). c_2=-1 gate. Tests whether constant c_4..c_8 exist."
    )
    wb.add_data("c2_gate_pass", bool(gate_ok) if gate_ok is not None else False)
    wb.add_data("c_k", {str(k): [v.real, v.imag] for k, v in c.items()})
    wb.add_data("residual_next_order",
                None if resid_next is None else
                {"s_order": resid_next[0], "value_re": resid_next[1].real,
                 "value_im": resid_next[1].imag})
    wb.add_data("constant_ck_consistent", bool(consistent and resid_next is None))
    wb.add_assertion(
        "c2_gate", computed=1 if gate_ok else 0, expected=1, tolerance=0,
        source="operator s-series match must reproduce proved c_2 = -1",
    )
    wb.save()
    print("  Witness: qbeta-ck-sseries-operator-match.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
