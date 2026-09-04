#!/usr/bin/env python3
"""milnor_recursion_capcup_weight_probe.py — the corrected cap-cup weight (μ⁻¹, not μ) and the
trace-level reformulation of the single open identity (★★) in the ∀A deficit recursion (qou-v7ro).

Context. `milnor_recursion_forall_A_reduction_probe` reduced the recursion D_{A+1}=-h²(h²+2)D_A to
the single identity (★★)  qtr_{A+1}(W e_A W⁻¹ e_A) = [2]^{A+1}(1-u) + u[2]·qtr_A(ρ(w_A)),
W = ρ(w_A)⊗1, u = q²+q⁻² = h²+2 — three of the four qtr-terms being A-independent ∀A. The audit
doc flagged that the *reduction of (★★)'s LHS to a partial-closure of strand A* had used the wrong
contraction weight. This probe pins the correct one and the exact level at which the identity lives.

Verified here (exact ℚ(q), zero float64):

 (W1) The clean TL sub-lemma is  ptr_{μ⁻¹}(e) = 1  (identity), NOT ptr_μ(e).
      ptr_μ(e) = diag(q⁻², q²) is a nontrivial diagonal — the earlier μ-weighted reduction was wrong.
      (μ = diag(q,1/q) is the quantum-trace weight; e = q - R the TL generator; ptr over one strand.)

 (R1) Index reduction (holds ∀A, pure linear algebra):
        qtr_A( W₀ · (F⊗1) ) = qtr_{A-1}( P · F ),   P := ptr_μ(W₀),  F := ptr_{μ⁻¹}(W₀⁻¹),
      W₀ = ρ(w_A) on A strands, P,F on A-1 strands.  (Contract the strand-A index of qtr_A: the W₀
      factor carries weight μ ⇒ P; F already carries μ⁻¹.)

 (R2) With that, (★★) is EQUIVALENT to the trace identity (verified A=3,4):
        (†'')  qtr_{A-1}(P·F) = [2]^{A+1}(1-u) + u[2]·qtr_{A-1}(P).

 (R3) (†'') is a GENUINE TRACE identity — the tempting matrix form
        P·F ?= [2]²(1-u)·1 + u[2]·P
      is FALSE at A=3,4 (cancellation happens only after qtr_{A-1}). This tells the next agent NOT to
      look for a matrix identity: the ∀A proof must be a trace/Brunnian argument, not linear algebra.

 (R4) No affine collapse: P = ptr_μ(ρ(w_A)) is NOT in span{1, ρ(w_{A-1}), ρ(w_{A-1})⁻¹} (A=4). The
      one-strand partial closure of a Brunnian braid does not reduce to a scalar × identity, which is
      exactly why (†'') is Brunnian-specific yet still open.

Status: the ∀A recursion is proven modulo (†''); (†'') is verified A=3,4 and OPEN ∀A. No Lean
`BrunnianDeficitRecursion` instance is created — the honest open state is preserved. Scope (a).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from a4_brunnian_deficit_closed_form import band_comm, band_word_to_sigma, A01, A12, A23  # noqa: E402

q = sp.symbols("q", positive=True)
h = q - 1 / q
I2 = sp.eye(2)
R = sp.Matrix([[q, 0, 0, 0], [0, q - 1 / q, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]])
mu = sp.diag(q, 1 / q)
mu_inv = sp.diag(1 / q, q)
two = q + 1 / q
u = q ** 2 + 1 / q ** 2
e4 = sp.Matrix(sp.cancel(q * sp.eye(4) - R))  # TL generator e = q - R, e² = [2]e


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def op_on(n, i, M2):
    return kron(*(([I2] * i) + [M2] + ([I2] * (n - (i + 2)))))


def word_matrix(n, word):
    M = sp.eye(2 ** n)
    for (s, g) in word:
        Rg = op_on(n, g, R)
        M = M * (Rg if s > 0 else Rg.inv())
    return sp.Matrix(sp.cancel(M))


def qtr(n, X):
    return sp.cancel(sp.expand((kron(*([mu] * n)) * X).trace()))


def ptr_last(n, X, w):
    """partial trace over the LAST strand with diagonal weight w=diag(w0,w1)."""
    d = 2 ** (n - 1)
    out = sp.zeros(d, d)
    for a in range(d):
        for b in range(d):
            out[a, b] = w[0, 0] * X[2 * a, 2 * b] + w[1, 1] * X[2 * a + 1, 2 * b + 1]
    return sp.Matrix(sp.cancel(out))


def is_zero_mat(M):
    return all(sp.simplify(sp.cancel(x)) == 0 for x in M)


def main():
    res = {"convention": "spin-1/2, R Hecke, qtr mu=diag(q,1/q); u=q^2+q^-2=h^2+2; e=q-R"}

    # (W1) cap-cup weight sub-lemma
    p_muinv = ptr_last(2, e4, mu_inv)
    p_mu = ptr_last(2, e4, mu)
    res["W1_ptr_muinv_e_eq_I"] = bool(is_zero_mat(p_muinv - sp.eye(2)))
    res["W1_ptr_mu_e"] = str(sp.cancel(p_mu).tolist())
    res["W1_ptr_mu_e_ne_I"] = bool(not is_zero_mat(p_mu - sp.eye(2)))

    words = {3: band_comm(A01, A12), 4: band_comm(band_comm(A01, A12), A23)}
    per = {}
    for A in (3, 4):
        W0 = word_matrix(A, band_word_to_sigma(words[A]))
        W0inv = sp.Matrix(sp.cancel(W0.inv()))
        P = ptr_last(A, W0, mu)          # weight mu  (strand-A index of the W0 factor)
        F = ptr_last(A, W0inv, mu_inv)   # weight mu^{-1} (the corrected cap-cup contraction)
        d = 2 ** (A - 1)
        qP = qtr(A - 1, P)               # = qtr_A(W0)

        # (R1) index reduction: qtr_A(W0·(F⊗1)) == qtr_{A-1}(P·F)
        lhs_full = qtr(A, sp.Matrix(sp.cancel(W0 * kron(F, I2))))
        r1 = sp.simplify(lhs_full - qtr(A - 1, sp.Matrix(sp.cancel(P * F)))) == 0

        # (R2) the trace identity (†'')
        rhs = sp.cancel(two ** (A + 1) * (1 - u) + u * two * qP)
        r2 = sp.simplify(qtr(A - 1, sp.Matrix(sp.cancel(P * F))) - rhs) == 0

        # (R3) matrix version is FALSE
        cand = sp.cancel(two ** 2 * (1 - u)) * sp.eye(d) + sp.cancel(u * two) * P
        mat_true = is_zero_mat(sp.Matrix(sp.cancel(P * F - cand)))

        # control: with the WRONG weight (mu) for F, (†'') fails
        Fmu = ptr_last(A, W0inv, mu)
        r2_mu = sp.simplify(qtr(A, sp.Matrix(sp.cancel(W0 * kron(Fmu, I2)))) - rhs) == 0

        per[A] = {
            "R1_index_reduction": bool(r1),
            "R2_trace_identity_muinv": bool(r2),
            "R3_matrix_version_holds": bool(mat_true),   # expected False
            "control_R2_with_wrong_weight_mu": bool(r2_mu),  # expected False
        }

    # (R4) no affine collapse of P at A=4
    A = 4
    W0 = word_matrix(A, band_word_to_sigma(words[A]))
    P = ptr_last(A, W0, mu)
    wprev = word_matrix(A - 1, band_word_to_sigma(words[A - 1]))
    wprevi = sp.Matrix(sp.cancel(wprev.inv()))
    a, b, c = sp.symbols("a b c")
    eqs = [sp.Eq(P[r, r], a + b * wprev[r, r] + c * wprevi[r, r]) for r in range(3)]
    sol = sp.solve(eqs, [a, b, c], dict=True)
    if sol and all(sol[0].get(x) is not None for x in (a, b, c)):
        a0, b0, c0 = sol[0][a], sol[0][b], sol[0][c]
        affine = is_zero_mat(sp.Matrix(sp.cancel(P - (a0 * sp.eye(2 ** (A - 1)) + b0 * wprev + c0 * wprevi))))
    else:
        affine = False
    res["R4_P_affine_in_I_wprev_wprevinv_A4"] = bool(affine)  # expected False

    res["per_A"] = per
    all_ok = (
        res["W1_ptr_muinv_e_eq_I"] and res["W1_ptr_mu_e_ne_I"]
        and all(per[A]["R1_index_reduction"] for A in per)
        and all(per[A]["R2_trace_identity_muinv"] for A in per)
        and all(not per[A]["R3_matrix_version_holds"] for A in per)
        and all(not per[A]["control_R2_with_wrong_weight_mu"] for A in per)
        and not res["R4_P_affine_in_I_wprev_wprevinv_A4"]
    )
    res["all_verified"] = bool(all_ok)
    res["verdict"] = (
        "CAP-CUP WEIGHT CORRECTED + IDENTITY LEVEL PINNED: the clean TL sub-lemma is ptr_{μ⁻¹}(e)=1 "
        "(ptr_μ(e)=diag(q⁻²,q²) is nontrivial). The single open identity (★★) is equivalent, via the "
        "∀A index reduction qtr_A(W₀(F⊗1))=qtr_{A-1}(P·F) [P=ptr_μ(W₀), F=ptr_{μ⁻¹}(W₀⁻¹)], to the "
        "TRACE identity (†'') qtr_{A-1}(P·F)=[2]^{A+1}(1-u)+u[2]qtr_{A-1}(P) (verified A=3,4). This is a "
        "genuine trace identity — the matrix form P·F=[2]²(1-u)1+u[2]P is FALSE (A=3,4), and P does not "
        "collapse to an affine combination of {1,ρ(w_{A-1}),ρ(w_{A-1})⁻¹}. The ∀A proof of (†'') is OPEN; "
        "the wrong-weight (μ) control fails, confirming μ⁻¹ is the correct cap-cup contraction."
        if all_ok else
        "NOT fully verified — a claim came out unexpected; re-derive before reporting."
    )

    out = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. The stem IS "
            "declared physical_proton in "
            "computations/q0_anchor_manifest.json, and that declaration "
            "cannot stamp this witness: the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build(). Hence the declaration "
            "here, which is the only route that reaches the file."),
        "computation": "milnor-recursion-capcup-weight",
        "scriptFile": "milnor_recursion_capcup_weight_probe.py",
        "engine": "python-sympy-exact",
        "free_parameters": 0,
        "description": (
            "Corrects the cap-cup contraction weight (ptr_{μ⁻¹}(e)=1, not μ) and pins the single open "
            "identity (★★) in the ∀A Milnor deficit recursion to the trace level: (★★) ⟺ "
            "qtr_{A-1}(P·F)=[2]^{A+1}(1-u)+u[2]qtr_{A-1}(P) with P=ptr_μ(ρ(w_A)), F=ptr_{μ⁻¹}(ρ(w_A)⁻¹) "
            "(verified A=3,4). The matrix form is FALSE (trace-level only); P has no affine collapse. "
            "Exact ℚ(q), no float64. No Lean instance created; the recursion remains open ∀A modulo (†'')."
        ),
        "results": res,
    }
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    out["q0Anchor"] = _q0a
    if _q0v:
        out["q0Value"] = _q0v
    (HERE / "milnor-recursion-capcup-weight.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(res, indent=1))
    print("wrote milnor-recursion-capcup-weight.witness.json")
    assert res["all_verified"], "cap-cup weight / trace-level verification FAILED"


if __name__ == "__main__":
    main()
