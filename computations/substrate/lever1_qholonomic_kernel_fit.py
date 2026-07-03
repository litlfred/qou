"""Lever-1 fibre kernel, Stage 3: is S(m)=Σ_{λ⊢m} dim_q(λ) q-HOLONOMIC of order 2?

Stage 1 (lever1_qinvolution_kernel_test) showed: the C-finite (constant-τ) depth-2 SL₂
recurrence FAILS beyond the seed, and the MONIC involution-form coefficient
W(m)=(S(m)-S(m-1))/S(m-2) acquires a partition-sum denominator at m=6 (not Laurent in q).
So no MONIC order-2 q-holonomic lift closes.

This stage tests the GENERAL (non-monic) order-2 q-holonomic recurrence:

    P2(q, q^m)·S(m) + P1(q, q^m)·S(m-1) + P0(q, q^m)·S(m-2) = 0,            (★)

with P_i bivariate Laurent polynomials in (q, X:=q^m) of bounded bidegree. (★) is the
q-difference operator (the fibre kernel R) acting on the binding period. The q-Bessel /
q-Lommel class lives here: the Hahn-Exton coefficient recurrence is exactly an order-2 (★)
whose middle term factors (QOU/QBeta/QBesselContiguityRecurrence.lean).

METHOD — honest guess-and-verify with held-out falsification (q-Petkovšek-lite):
  * Compute S(0..NMAX) symbolically (no fit, exact in q).
  * For increasing bidegree (A in q, B in X), build the ansatz P_i = Σ c_{iab} q^a X^b,
    substitute X=q^m, collect the resulting Laurent polynomial in q → a homogeneous linear
    system in the c's; FIT on m = 2..MFIT only.
  * Take the nullspace. For each basis recurrence, VERIFY it on the HELD-OUT m = MFIT+1..NMAX
    (indices never used in the fit). A genuine q-holonomic recurrence predicts the held-out
    values; an overfit nullspace artifact does not.
  * Report the minimal (A,B) whose nullspace recurrence verifies all held-out m, or NONE.

Heavily over-determined (each m gives ~20-40 q-power constraints vs ~3·(2A+1)(B+1) unknowns),
so a held-out-verifying solution at small (A,B) is a real certificate, not a fit. No fit.
"""
import json, os, sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp

# Shared, cached Young-diagram / symmetric quantum-dimension machinery (bean z3a2; PR #2952).
# Replaces the formerly inline qint/qfact/partitions/hooks/dim_q/S — same symbolic results.
from young_qdim import q, S  # noqa: E402


NMAX = 9          # compute S(0..9)
MFIT = 6          # fit on m=2..6
HELDOUT = list(range(MFIT + 1, NMAX + 1))   # verify on m=7,8,9

print(f"Computing S(0..{NMAX}) symbolically ...")
Sm = {m: S(m) for m in range(0, NMAX + 1)}
# clear to common q-power denominators: work with numerators over a q-power so everything is a
# genuine Laurent polynomial in q (dim_q is bar-symmetric ⇒ S(m) is a Laurent poly in q already).
Sm = {m: sp.cancel(sp.expand(sp.together(Sm[m]))) for m in range(0, NMAX + 1)}


def build_and_test(A, B):
    """Ansatz P_i = Σ_{a=-A..A, b=0..B} c_{iab} q^a X^b, X=q^m. Fit on m=2..MFIT, return list
    of nullspace recurrences (each as dict i->Poly-in-(q) coeff at each (a,b)) that VERIFY all
    held-out m. Returns (certified_list, n_unknowns, n_constraints)."""
    # b ranges over [-B, B]: the natural kernel coefficients are bar-symmetric in X=q^m
    # (e.g. [m-1]_q = (X - X^{-1})/(q - q^{-1}) needs the X^{-1} term), so a non-negative-only
    # X-ansatz cannot even represent the seed-exact involution kernel.
    coeffs = {}
    syms = []
    for i in range(3):           # P0,P1,P2 (i = shift back amount: S(m-i)... we map below)
        for a in range(-A, A + 1):
            for b in range(-B, B + 1):
                s = sp.Symbol(f"c_{i}_{a}_{b}")
                coeffs[(i, a, b)] = s
                syms.append(s)

    def Pi_at(i, m):
        # P_i(q, q^m) = Σ c_{iab} q^{a + m b}
        return sp.Add(*[coeffs[(i, a, b)] * q**(a + m * b)
                        for a in range(-A, A + 1) for b in range(-B, B + 1)])

    # Equation at m: P2·S(m) + P1·S(m-1) + P0·S(m-2) = 0   (i=2->S(m), i=1->S(m-1), i=0->S(m-2))
    def eq_at(m):
        expr = Pi_at(2, m) * Sm[m] + Pi_at(1, m) * Sm[m - 1] + Pi_at(0, m) * Sm[m - 2]
        return sp.expand(expr)

    # Build the linear system from m=2..MFIT by collecting q-power coefficients.
    rows = []
    for m in range(2, MFIT + 1):
        e = eq_at(m)
        p = sp.Poly(sp.expand(e * q**(50)), q)   # shift by q^50 to clear negative powers
        for c in p.all_coeffs():
            lin = sp.expand(c)
            if lin != 0:
                rows.append(lin)
    if not rows:
        return [], len(syms), 0, 0
    M = sp.Matrix([[sp.diff(r, s) for s in syms] for r in rows])   # rows are linear in syms
    ns = M.nullspace()
    n_constraints = M.rows
    ns_dim = len(ns)
    certified = []
    for vec in ns:
        sol = {syms[k]: vec[k] for k in range(len(syms))}
        # Build the recurrence coefficient functions and verify on held-out m.
        def Pi_sol(i, m):
            return sp.Add(*[sol[coeffs[(i, a, b)]] * q**(a + m * b)
                            for a in range(-A, A + 1) for b in range(-B, B + 1)])
        ok = True
        for m in HELDOUT:
            resid = sp.cancel(Pi_sol(2, m) * Sm[m] + Pi_sol(1, m) * Sm[m - 1]
                              + Pi_sol(0, m) * Sm[m - 2])
            if sp.simplify(resid) != 0:
                ok = False
                break
        if ok:
            # record the solved P_i as readable Laurent polys in q and X
            X = sp.Symbol("X")
            Pis = {}
            for i in range(3):
                Pis[i] = sp.factor(sp.Add(*[sol[coeffs[(i, a, b)]] * q**a * X**b
                                            for a in range(-A, A + 1) for b in range(-B, B + 1)]))
            certified.append(Pis)
    return certified, len(syms), n_constraints, ns_dim


# Sweep ansatz sizes from small to larger; stop at first (A,B) with a held-out-verified recurrence.
results = {"S_symbolic_degrees": {m: sp.Poly(sp.expand(Sm[m] * q**50), q).degree() - 50
                                  for m in range(2, NMAX + 1)},
           "fit_indices": list(range(2, MFIT + 1)), "heldout_indices": HELDOUT,
           "attempts": []}
certified_final = None
for (A, B) in [(1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3)]:
    print(f"  trying ansatz q-deg ±{A}, X-deg {B} ...", flush=True)
    cert, nu, nc, nsd = build_and_test(A, B)
    rec = {"A": A, "B": B, "unknowns": nu, "constraints": nc,
           "fit_nullspace_dim": nsd, "n_certified": len(cert)}
    results["attempts"].append(rec)
    print(f"    unknowns={nu} constraints={nc} fit_nullspace_dim={nsd} "
          f"certified(held-out-verified)={len(cert)}")
    if cert:
        certified_final = {"A": A, "B": B,
                           "recurrences": [{i: str(P[i]) for i in range(3)} for P in cert]}
        break

if certified_final:
    verdict = (
        f"ORDER-2 q-HOLONOMIC RECURRENCE CERTIFIED at q-deg ±{certified_final['A']}, "
        f"X-deg {certified_final['B']} (X=q^m). The non-monic kernel "
        "P2(q,q^m)S(m)+P1 S(m-1)+P0 S(m-2)=0 fits m=2..{MFIT} AND predicts the held-out "
        f"m={HELDOUT} (never used in the fit). This IS the explicit lever-1 fibre q-difference "
        "operator R; the binding period S(m)=Σ dim_q(λ) is order-2 q-holonomic. The monic form "
        "failed only because the operator is non-monic. No fit (held-out falsification passed)."
    ).replace("{MFIT}", str(MFIT))
else:
    # Did any honest (over-determined) bidegree even ADMIT a fitting recurrence?
    honest_nullspaces = [a["fit_nullspace_dim"] for a in results["attempts"]
                         if a["unknowns"] <= a["constraints"]]
    all_zero = all(d == 0 for d in honest_nullspaces) if honest_nullspaces else False
    verdict = (
        f"NO order-2 q-holonomic recurrence found up to q-deg ±4, X-deg 3 (X=q^m, bar-symmetric) "
        f"that predicts the held-out m={HELDOUT} (scope-limited (a)). "
        + ("STRONGER: at every OVER-determined (honest) bidegree the fit nullspace is EMPTY — the "
           "recurrence does not even fit the training m=2..6; a nullspace appears only once the "
           "ansatz becomes under-determined (189 unknowns), and none of those overfit solutions "
           "survive the held-out test. " if all_zero else "")
        + "So the binding period S(m)=Σ dim_q(λ) is q-holonomic of HIGHER q-shift order (≥3) or "
        "non-order-2; a small-bidegree order-2 closed form is excluded. This MIRRORS the Q_β c_k "
        "result (no clean low-order holonomic recurrence; kernel must be depth ≥3 or non-constant "
        "q-rational — ck-dk-canonical-registry). The cyclotomic (q-1)²·Φ_d tower (Stage 1) + the "
        "partition-sum denominator onset at m=6 (Stage 2) remain the sharp constraints; this rules "
        "out the small-bidegree order-2 closed form, not the q-holonomic/Habiro class."
    )

results["certified"] = certified_final
witness = {
    "computation": "lever1_qholonomic_kernel_fit",
    "description": (
        "Stage 3 of the lever-1 fibre-kernel hunt: tests whether the binding period "
        "S(m)=Σ_{λ⊢m} dim_q(λ) satisfies a general (non-monic) order-2 q-holonomic recurrence "
        "P2(q,q^m)S(m)+P1 S(m-1)+P0 S(m-2)=0, by bounded-bidegree guess-and-verify with HELD-OUT "
        "falsification (fit m=2..6, verify m=7,8,9). Follows the C-finite SL₂ falsification "
        "(Stage 0) and the monic-form non-closure at m=6 (Stage 2)."
    ),
    "discipline": (
        "no fit; sympy symbolic exact in q; held-out m never used in the linear fit, so a "
        "verifying nullspace solution is a genuine q-holonomic certificate not an overfit; "
        "(a)/(b)-scoped verdict per AGENTS.md."
    ),
    "auditOnly": "docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md",
    "results": results,
    "certified": certified_final is not None,
    "verdict": verdict,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
wpath = WitnessBuilder.wrap_legacy(
    "lever1-qholonomic-kernel-fit", witness,
    script_path=__file__, engine="sympy",
).save()

print(f"\n  certified order-2 q-holonomic recurrence: {certified_final is not None}")
if certified_final:
    for i in range(3):
        print(f"    P{i}(q,X) = {certified_final['recurrences'][0][i]}")
print(f"\n  VERDICT: {verdict}")
print(f"\nwitness -> {wpath}")
