#!/usr/bin/env python3
"""4_1 AJ machinery vs Askey-Wilson three-term channel shape — bean cp4i.

Gated follow-up of docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md
(the one probe that survived the dialog assessment), run per the constraints
of docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md.
STRUCTURAL SHAPE TEST ONLY — exact sympy arithmetic, NO fit, no parameters.

The object: the figure-eight is the one knot where the strong AJ conjecture
is PROVED ([nguyen-tran-2021]) and the corpus already verifies the colored
Jones object (figure_eight_aj_operator.py, Habiro-Le form).  The proved AJ
machinery carries a canonical degree-index ladder — the Habiro cyclotomic
ladder — which is the knot-side analogue of the corpus's c_k channel ladders
(both are degree-index three-term candidates).  The 1jrh hypothesis needs a
three-term recurrence with a bar-EVEN multiplier A_k and an AW lower
coefficient B_k whose positivity drives the Casoratian sign test.  Question:
does the proved 4_1 ladder have that shape?

The structural identity this probe verifies exactly (then exploits):

    J_N(4_1; q) = sum_{k>=0} g_k(Lambda_N),   g_k(L) = prod_{j=1}^{k} (L - lam_j),
    Lambda_N = q^N + q^{-N},   lam_j = q^j + q^{-j},

i.e. the colored Jones is a single polynomial evaluated on the bar-even
variable Lambda_N, expanded in the Newton basis at the nodes lam_j with ALL
cyclotomic coefficients equal to 1 (the 4_1 signature; the sum terminates
at k = N-1 because Lambda_N = lam_N kills the j = N factor).  Consequences
tested:

  (1) the ladder multiplier A_k = Lambda - lam_{k+1} is bar-EVEN
      (lam(q) = lam(1/q)) — CONSISTENT with 1jrh's bar-even requirement;
  (2) the lower coefficient B_k is IDENTICALLY ZERO (Newton/interpolation
      ladder, first-order) — the ladder solution space is 1-dimensional and
      the Casoratian of any two solutions vanishes identically, so the
      proved knot side supplies NO Casoratian sign and NO (a,b,c,d)
      identification: the 1jrh gate STANDS;
  (3) the q-Hermite bottom of the AW scheme has C_n = 1 - q^n != 0 — the
      proved 4_1 ladder is NOT the q-Hermite bottom (scope (a): this
      identification, as-is, fails; it is the degenerate Newton boundary
      of the AW shape).

Correctness anchors: J_2 = V(4_1) Jones polynomial; Lambda-Newton form
matches the Habiro-Le double-Pochhammer form exactly for N = 1..9; bar
symmetry J_N(q) = J_N(1/q) re-derived structurally from the Lambda-form.

Audit-only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE / "substrate"))

import sympy as sp

q = sp.symbols("q")
Lam = sp.symbols("Lambda")  # bar-even spectral variable q^N + q^{-N}
s = sp.symbols("s")         # free seed for the second ladder solution

NMAX = 9
KMAX = 8


def qpoch(a, base, k):
    p = sp.Integer(1)
    for j in range(k):
        p *= (1 - a * base**j)
    return p


def colored_jones_habiro_le(N: int):
    """J_N(4_1;q) — Habiro-Le double Pochhammer (same as figure_eight_aj_operator)."""
    total = sp.Integer(0)
    for k in range(0, N):
        total += q**(N * k) * qpoch(q**(-N - 1), q**(-1), k) * qpoch(q**(-N + 1), q, k)
    return sp.expand(sp.simplify(total))


def lam(j: int):
    return q**j + q**(-j)


def g_poly(k: int):
    """Newton-basis element g_k(Lambda) = prod_{j=1}^k (Lambda - lam_j)."""
    p = sp.Integer(1)
    for j in range(1, k + 1):
        p *= (Lam - lam(j))
    return sp.expand(p)


def colored_jones_lambda_form(N: int, kmax: int | None = None):
    """J_N via the Lambda-Newton form, truncated at kmax (default N-1)."""
    if kmax is None:
        kmax = N - 1
    LamN = q**N + q**(-N)
    total = sp.Integer(0)
    for k in range(0, kmax + 1):
        total += g_poly(k).subs(Lam, LamN)
    return sp.expand(sp.simplify(total))


def main() -> int:
    t0 = time.time()
    print("\n  4_1 AJ machinery vs AW three-term channel shape (bean cp4i)\n")

    # --- anchor: J_2 = Jones polynomial of 4_1 --------------------------------
    J = {N: colored_jones_habiro_le(N) for N in range(1, NMAX + 1)}
    jones_4_1 = sp.expand(q**(-2) - q**(-1) + 1 - q + q**2)
    anchor_ok = sp.simplify(J[2] - jones_4_1) == 0
    print(f"  [anchor] J_2 == V(4_1)?  {anchor_ok}")
    assert anchor_ok

    # --- (0) Lambda-Newton form == Habiro-Le form, exactly --------------------
    newton_ok = {}
    for N in range(1, NMAX + 1):
        diff = sp.simplify(J[N] - colored_jones_lambda_form(N))
        newton_ok[N] = (diff == 0)
    all_newton = all(newton_ok.values())
    print(f"  [identity] J_N == sum_k prod_j (Lambda_N - lam_j), N=1..{NMAX}?  {all_newton}")
    assert all_newton

    # termination: extending the sum past k=N-1 changes nothing
    # (the j=N factor is Lambda_N - lam_N = 0)
    trunc_ok = all(
        sp.simplify(colored_jones_lambda_form(N, kmax=N + 2) - J[N]) == 0
        for N in range(2, 7)
    )
    print(f"  [termination] sum stable for kmax > N-1 (Lambda_N = lam_N)?  {trunc_ok}")
    assert trunc_ok

    # bar symmetry now STRUCTURAL: Lambda_N and every lam_j are bar-even
    bar_ok = all(sp.simplify(J[N] - J[N].subs(q, 1 / q)) == 0 for N in range(1, NMAX + 1))
    print(f"  [bar] J_N(q) == J_N(1/q) (manifest from the Lambda-form)?  {bar_ok}")
    assert bar_ok

    # --- (1) ladder multiplier A_k = Lambda - lam_{k+1} is bar-EVEN ----------
    mult_bar_even = all(
        sp.simplify(lam(k + 1) - lam(k + 1).subs(q, 1 / q)) == 0 for k in range(KMAX)
    )
    print(f"  [1jrh parity] multiplier A_k = Lambda - lam_(k+1) bar-even, k<{KMAX}?  {mult_bar_even}")
    assert mult_bar_even

    # --- (2) lower coefficient B_k == 0: Newton ladder is FIRST-order ---------
    # normal form g_{k+1} = A_k g_k + B_k g_{k-1}: verify with B_k = 0 exactly
    bzero_ok = all(
        sp.expand(g_poly(k + 1) - (Lam - lam(k + 1)) * g_poly(k)) == 0
        for k in range(KMAX)
    )
    print(f"  [shape] g_(k+1) == (Lambda - lam_(k+1)) g_k  (B_k == 0), k<{KMAX}?  {bzero_ok}")
    assert bzero_ok

    # Casoratian consequence: any two ladder solutions are proportional,
    # W_k = u_k v_{k+1} - u_{k+1} v_k == 0 identically
    u = {0: sp.Integer(1)}
    v = {0: s}
    for k in range(KMAX):
        u[k + 1] = sp.expand((Lam - lam(k + 1)) * u[k])
        v[k + 1] = sp.expand((Lam - lam(k + 1)) * v[k])
    casoratian_zero = all(
        sp.expand(u[k] * v[k + 1] - u[k + 1] * v[k]) == 0 for k in range(KMAX)
    )
    print(f"  [Casoratian] W_k == 0 identically (1-dim solution space)?  {casoratian_zero}")
    assert casoratian_zero

    # --- (3) contrast: the q-Hermite bottom has C_n != 0 ----------------------
    # continuous q-Hermite: 2x H_n = H_{n+1} + (1 - q^n) H_{n-1}; C_n = 1 - q^n
    qhermite_cn_nonzero = all(sp.simplify(1 - q**n) != 0 for n in range(1, 7))
    print(f"  [contrast] q-Hermite bottom C_n = 1 - q^n != 0 for n=1..6?  {qhermite_cn_nonzero}")
    assert qhermite_cn_nonzero

    elapsed = time.time() - t0
    verdict = (
        "DEGENERATE-AW: the proved 4_1 cyclotomic (Habiro/Newton) ladder has a "
        "bar-EVEN multiplier A_k = Lambda - lam_(k+1) (consistent with 1jrh's "
        "requirement) but IDENTICALLY ZERO lower coefficient B_k — the Newton-"
        "interpolation boundary of the AW three-term shape, NOT the q-Hermite "
        "bottom (whose C_n = 1 - q^n != 0). Scope (a): the knot-side proved AJ "
        "structure, as-is, supplies no Casoratian sign and no (a,b,c,d) "
        "identification; the 1jrh gate (measure c3^even first) STANDS."
    )
    print(f"\n  VERDICT: {verdict}\n  ({elapsed:.1f}s)")

    payload = {
        "description": (
            "4_1 AJ machinery vs Askey-Wilson three-term channel shape (bean cp4i): "
            "exact Lambda-Newton (Habiro cyclotomic) form of J_N(4_1), ladder "
            "multiplier bar-parity, B_k == 0 degeneracy, Casoratian consequence, "
            "q-Hermite-bottom contrast. Structural shape test only, no fit."
        ),
        "computation": "aj_operator_aw_shape_probe",
        "audit_only": True,
        "bean": "cp4i",
        "context": {
            "gated_by": "docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md",
            "origin": "docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md",
            "strong_aj_proved_for_4_1": "[nguyen-tran-2021]",
            "colored_jones_object": "computations/figure_eight_aj_operator.py",
        },
        "checks": {
            "jones_anchor_ok": bool(anchor_ok),
            "lambda_newton_form_ok_N": {str(N): bool(v_) for N, v_ in newton_ok.items()},
            "termination_stable": bool(trunc_ok),
            "bar_symmetry_structural": bool(bar_ok),
            "multiplier_bar_even": bool(mult_bar_even),
            "lower_coefficient_identically_zero": bool(bzero_ok),
            "casoratian_identically_zero": bool(casoratian_zero),
            "q_hermite_bottom_Cn_nonzero": bool(qhermite_cn_nonzero),
        },
        "structural_identity": (
            "J_N(4_1;q) = sum_{k=0}^{N-1} prod_{j=1}^{k} (Lambda_N - lam_j), "
            "Lambda_N = q^N + q^{-N}, lam_j = q^j + q^{-j}; all Habiro cyclotomic "
            "coefficients equal 1; termination via Lambda_N = lam_N"
        ),
        "tier": "structural-exact (all checks exact sympy identities; no fit, no parameters)",
        "verdict": verdict,
        "scope": "(a) scope-limited: constrains this identification as-is, not the AW ingredient",
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "aj-operator-aw-shape-probe", payload,
        script_path=__file__, engine="sympy",
        engine_version=sp.__version__, start_time=t0,
    ).save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
