"""Lever-1 fibre kernel, Stage 4: is S(m)=Σ_{λ⊢m} dim_q(λ) q-HOLONOMIC of order 3?

Stage 3 (lever1_qholonomic_kernel_fit) ruled out a small-bidegree ORDER-2 q-holonomic
recurrence (held-out-falsified). This stage raises the q-shift order to 3:

    Σ_{j=0}^{3} P_j(q, q^m)·S(m-j) = 0,                                     (★₃)

with P_j bar-symmetric Laurent polynomials in (q, X:=q^m). Order-3 is the next falsifiable
rung: the classical involution sequence is order-2 holonomic, so if the q-deformation needs
order 3 that is itself a structural fact about the fibre kernel R.

METHOD (same honest guess-and-verify as Stage 3): compute S(0..NMAX) exactly; fit the ansatz
coefficients on m=ORDER..MFIT by collecting q-power constraints; take the nullspace; VERIFY each
nullspace recurrence on the HELD-OUT m=MFIT+1..NMAX. A held-out-verified solution at honest
(over-determined) bidegree is a genuine certificate; an under-determined nullspace that fails
held-out is an overfit artifact. No fit.

Order-2 is re-run first as a regression sanity check (must reproduce the Stage-3 negative).
"""
import json, os, sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp

# Shared, cached Young-diagram / symmetric quantum-dimension machinery (bean z3a2; PR #2952).
# Replaces the formerly inline qint/qfact/partitions/hooks/dim_q/S — same symbolic results.
from young_qdim import q, S  # noqa: E402


NMAX = 11         # compute S(0..11); order-3 needs more held-out room
print(f"Computing S(0..{NMAX}) symbolically (this is the slow step) ...", flush=True)
Sm = {}
for m in range(0, NMAX + 1):
    Sm[m] = sp.cancel(sp.expand(sp.together(S(m))))
    print(f"    S({m}) done", flush=True)


def build_and_test(ORDER, A, B, MFIT, HELDOUT):
    """Σ_{j=0..ORDER} P_j(q,q^m) S(m-j) = 0, P_j = Σ c_{jab} q^a X^b, X=q^m, b∈[-B,B].
    Fit on m=ORDER..MFIT, verify nullspace recurrences on HELDOUT. Returns
    (certified, n_unknowns, n_constraints, nullspace_dim)."""
    coeffs, syms = {}, []
    for j in range(ORDER + 1):
        for a in range(-A, A + 1):
            for b in range(-B, B + 1):
                s = sp.Symbol(f"c_{j}_{a}_{b}")
                coeffs[(j, a, b)] = s
                syms.append(s)

    def Pj_at(j, m):
        return sp.Add(*[coeffs[(j, a, b)] * q**(a + m * b)
                        for a in range(-A, A + 1) for b in range(-B, B + 1)])

    def eq_at(m):
        return sp.expand(sp.Add(*[Pj_at(j, m) * Sm[m - j] for j in range(ORDER + 1)]))

    rows = []
    for m in range(ORDER, MFIT + 1):
        p = sp.Poly(sp.expand(eq_at(m) * q**60), q)   # shift clears negative q-powers
        for c in p.all_coeffs():
            if sp.expand(c) != 0:
                rows.append(sp.expand(c))
    if not rows:
        return [], len(syms), 0, 0
    M = sp.Matrix([[sp.diff(r, s) for s in syms] for r in rows])
    ns = M.nullspace()
    certified = []
    for vec in ns:
        sol = {syms[k]: vec[k] for k in range(len(syms))}

        def Pj_sol(j, m):
            return sp.Add(*[sol[coeffs[(j, a, b)]] * q**(a + m * b)
                            for a in range(-A, A + 1) for b in range(-B, B + 1)])
        ok = True
        for m in HELDOUT:
            resid = sp.cancel(sp.Add(*[Pj_sol(j, m) * Sm[m - j] for j in range(ORDER + 1)]))
            if sp.simplify(resid) != 0:
                ok = False
                break
        if ok:
            X = sp.Symbol("X")
            Pj = {j: sp.factor(sp.Add(*[sol[coeffs[(j, a, b)]] * q**a * X**b
                                        for a in range(-A, A + 1) for b in range(-B, B + 1)]))
                  for j in range(ORDER + 1)}
            certified.append(Pj)
    return certified, len(syms), M.rows, len(ns)


def run_order(ORDER, MFIT, HELDOUT, bidegrees):
    print(f"\n=== ORDER {ORDER}: fit m={ORDER}..{MFIT}, held-out {HELDOUT} ===", flush=True)
    attempts, certified_final = [], None
    for (A, B) in bidegrees:
        print(f"  ansatz q-deg ±{A}, X-deg {B} ...", flush=True)
        cert, nu, nc, nsd = build_and_test(ORDER, A, B, MFIT, HELDOUT)
        attempts.append({"A": A, "B": B, "unknowns": nu, "constraints": nc,
                         "fit_nullspace_dim": nsd, "n_certified": len(cert)})
        print(f"    unknowns={nu} constraints={nc} fit_nullspace_dim={nsd} "
              f"certified={len(cert)}", flush=True)
        if cert:
            X = sp.Symbol("X")
            certified_final = {"A": A, "B": B,
                               "recurrence": {str(j): str(cert[0][j]) for j in cert[0]}}
            break
    return attempts, certified_final


# Order-2 regression sanity (must stay negative), then the order-3 test.
o2_attempts, o2_cert = run_order(2, 7, [8, 9, 10, 11],
                                 [(1, 1), (2, 2), (3, 3)])
o3_attempts, o3_cert = run_order(3, 8, [9, 10, 11],
                                 [(1, 1), (2, 1), (2, 2), (3, 2), (3, 3)])

if o3_cert:
    verdict = (
        f"ORDER-3 q-HOLONOMIC RECURRENCE CERTIFIED at q-deg ±{o3_cert['A']}, X-deg {o3_cert['B']}. "
        "The fibre kernel R is a THIRD-order q-difference operator (the binding period needs one "
        "more q-shift than the classical order-2 involution recursion). Fit on m=3..8, predicts "
        "the held-out m=9,10,11. This is the explicit lever-1 operator; order-2 failed (Stage 3) "
        "because the true order is 3. No fit (held-out falsified)."
    )
elif o2_cert:
    verdict = "UNEXPECTED: order-2 certified here though Stage 3 was negative — investigate."
else:
    verdict = (
        "ORDER-3 ALSO NEGATIVE (scope-limited (a)). No order-2 OR order-3 q-holonomic recurrence "
        "up to q-deg ±3, X-deg 3 predicts the held-out m. The binding period S(m)=Σ dim_q(λ) is "
        "not q-holonomic of small order/bidegree at all — consistent with the Q_β c_k ladder, "
        "which likewise admits no low-order (q-)holonomic recurrence (ck-dk-canonical-registry; "
        "2026-06-04 holonomic-c11 verdict). The kernel is genuinely high-complexity in the Habiro "
        "ring; the cyclotomic (q-1)²·Φ_d tower (Stage 1) is the structural handle, not a finite "
        "q-difference operator of small order. Does NOT refute the Habiro class; rules out "
        "low-order q-holonomicity for BOTH rungs."
    )

witness = {
    "computation": "lever1_qholonomic_order3_fit",
    "description": (
        "Stage 4: raises the q-shift order to 3 for the binding period S(m)=Σ_{λ⊢m} dim_q(λ), "
        "Σ_{j=0..3} P_j(q,q^m) S(m-j)=0, bar-symmetric bounded-bidegree guess-and-verify with "
        "held-out falsification (order-2 re-run as regression). Follows the order-2 negative "
        "(Stage 3)."
    ),
    "discipline": (
        "no fit; sympy symbolic exact in q to S(11); held-out m never used in the fit; "
        "(a)/(b)-scoped per AGENTS.md."
    ),
    "auditOnly": "docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md",
    "results": {
        "order2_regression": {"attempts": o2_attempts, "certified": o2_cert},
        "order3": {"attempts": o3_attempts, "certified": o3_cert},
    },
    "certified_order3": o3_cert is not None,
    "verdict": verdict,
}
out = os.path.join("computations", "substrate", "lever1-qholonomic-order3-fit.witness.json")
with open(out, "w") as f:
    json.dump(witness, f, indent=2)

print(f"\n  order-3 certified: {o3_cert is not None}")
if o3_cert:
    for j, P in o3_cert["recurrence"].items():
        print(f"    P{j}(q,X) = {P}")
print(f"\n  VERDICT: {verdict}")
print(f"\nwitness -> {out}")
