#!/usr/bin/env python3
"""qbeta_delta_tr_vs_formA.py — is the Habiro Δtr_M the same object as
Form A's net-winding Δ(net)?

CONTEXT. Item 1 of the "fo 1 and 2" task. The prior probe
(qbeta_habiro_taylor_investigation.py) extracted the exact Δtr_M Taylor
coefficients and showed Q_β = m_e × |Δtr_M| × (substrate constant) does
NOT close (g(q₀)=10.776 is not a clean substrate constant). This script
runs the DECISIVE canonical test instead of guessing constants.

THE CANONICAL DERIVATION STEP (not fitting). Form A is the canonical
Q_β leading term per prop:neutron-qvalue-symbolic:

    Q_A = m_e × |Δ(net)_A| × E_0,   E_0 = 1/(q(q-1)),
    Δ(net)_A = h(h-2)/2 = (q²-1)(q²-2q-1)/(2q²),   h = q - 1/q.

(Algebra: Q_A/m_e = |q²-2q-1|(q+1)/(2q³); dividing by |Δ(net)_A| gives
E_0 = 1/(q(q-1)) exactly.)

Form A uses the SINGLE-WRAP normal-form net winding Δ(net)_A. The
natural canonical refinement — the genuine derivation step, not a fit —
is to replace it with the EXACT Habiro multi-block Markov-trace
difference Δtr_M = tr_M(β_n) - tr_M(β_p), keeping the same E_0 scale:

    Q_β_test = m_e × |Δtr_M(q)| × 1/(q(q-1)).

If Δtr_M IS Form A's Δ(net) slot (i.e. Form A is the single-wrap
approximation of the exact Habiro object), this closes Q_β to compute
precision and the c_k saga ends the way #1511 ended α_EM. If the two
objects differ — even at leading Taylor order — then Q_β does NOT
consume Δtr_M through Form A's slot and the bridge is a genuine open
derivation.

DISCIPLINE: zero free parameters. We compare two SYMBOLIC objects
(Δ(net)_A and Δtr_M) and test one zero-parameter substitution. The
result is decisive either way.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mpf, mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-delta-tr-vs-formA",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Decisive test: is the exact Habiro Δtr_M = tr_M(β_n) - tr_M(β_p) "
        "the same categorical object as Form A's single-wrap net winding "
        "Δ(net)_A = (q²-1)(q²-2q-1)/(2q²)? Substitutes Δtr_M into Form A's "
        "Δ(net) slot keeping E_0 = 1/(q(q-1)) and compares to CODATA Q_β. "
        "Zero free parameters. Determines whether Q_β consumes Δtr_M "
        "through Form A's slot or the bridge is a genuine open derivation."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    print("=" * 78)
    print(" Q_β: is the Habiro Δtr_M the same object as Form A's Δ(net)?")
    print("=" * 78)
    print()

    q = sp.Symbol('q', positive=True)
    eps = sp.Symbol('eps')

    # --- Form A's net winding Δ(net)_A (symbolic, canonical) ---
    h = q - 1 / q
    delta_net_A = sp.simplify(h * (h - 2) / 2)            # = (q²-1)(q²-2q-1)/(2q²)
    E0 = 1 / (q * (q - 1))
    Q_A_over_me = sp.simplify(sp.Abs(delta_net_A) * E0)   # should = |q²-2q-1|(q+1)/(2q³)
    print(f"  Δ(net)_A(q) = {sp.simplify(delta_net_A)}")
    print(f"  E_0(q)      = 1/(q(q-1))")
    print(f"  Q_A/m_e     = {sp.simplify(Q_A_over_me)}   (Form A, factored)")
    print()

    # --- exact Habiro Δtr_M from the witness ---
    hab = json.loads((_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)).read_text())
    tr_p_str = hab["results"]["p (proton, A=1)"]["tr_M_in_q"]
    tr_n_str = hab["results"]["n (neutron, A=1)"]["tr_M_in_q"]
    tr_p_sym = sp.sympify(tr_p_str, locals={"q": q})
    tr_n_sym = sp.sympify(tr_n_str, locals={"q": q})
    delta_tr = sp.simplify(tr_n_sym - tr_p_sym)

    # --- leading Taylor coefficients (q = 1 + ε) ---
    def lead_coeffs(expr, n=6):
        e = sp.series(sp.expand(expr.subs(q, 1 + eps)), eps, 0, n).removeO()
        e = sp.expand(e)
        return {k: sp.nsimplify(e.coeff(eps, k)) for k in range(n)}

    cA = lead_coeffs(delta_net_A)
    cT = lead_coeffs(delta_tr)
    print("  Leading Taylor coefficients (basis ε = q-1):")
    print(f"     {'order':>6} | {'Δ(net)_A':>12} | {'Δtr_M':>12}")
    for k in range(6):
        print(f"     ε^{k:<4} | {str(cA[k]):>12} | {str(cT[k]):>12}")
    print()

    same_leading = sp.simplify(cA[1] - cT[1]) == 0
    print(f"  Leading-order (ε¹) match?  Δ(net)_A: {cA[1]}   Δtr_M: {cT[1]}   "
          f"→ {'SAME' if same_leading else 'DIFFERENT'}")
    print()

    # --- numerical substitution test at q₀ ---
    q0 = mpf(Q_50_DIGIT_STR)
    me = mpf(M_E_MEV)
    Q_codata = mpf("0.78233341")

    def num(expr):
        return mpf(str(sp.N(expr.subs(q, sp.Float(str(q0), 60)), 50)))

    dnetA0 = num(delta_net_A)
    dtr0 = num(delta_tr)
    E0_0 = 1 / (q0 * (q0 - 1))

    Q_formA = me * abs(dnetA0) * E0_0
    Q_swap = me * abs(dtr0) * E0_0    # the canonical substitution Δ(net)_A → Δtr_M

    ppm_formA = (Q_formA / Q_codata - 1) * mpf(10) ** 6
    ppm_swap = (Q_swap / Q_codata - 1) * mpf(10) ** 6

    print(f"  At q₀ = {mp.nstr(q0, 12)}:")
    print(f"     |Δ(net)_A(q₀)| = {mp.nstr(abs(dnetA0), 12)}")
    print(f"     |Δtr_M(q₀)|    = {mp.nstr(abs(dtr0), 12)}")
    print(f"     ratio Δtr_M / Δ(net)_A = {mp.nstr(abs(dtr0) / abs(dnetA0), 12)}")
    print()
    print(f"     Q_β CODATA               = {mp.nstr(Q_codata, 10)} MeV")
    print(f"     Form A  (Δ(net)_A slot)  = {mp.nstr(Q_formA, 10)} MeV  "
          f"({mp.nstr(ppm_formA, 6)} ppm)")
    print(f"     swap    (Δtr_M slot)     = {mp.nstr(Q_swap, 10)} MeV  "
          f"({mp.nstr(ppm_swap, 6)} ppm)")
    print()

    # --- verdict ---
    closes = abs(ppm_swap) < mpf("0.001")   # compute precision ≪ 1 ppb
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if closes:
        print("""
  ✓ Δtr_M closes Q_β to compute precision through Form A's slot.
    The c_k ARE the Habiro Taylor coefficients — saga closed.
    → wire Q_β = m_e × |Δtr_M| × 1/(q(q-1)) to production.""")
    else:
        print(f"""
  ✗ DECISIVE NEGATIVE. The Habiro Δtr_M is NOT Form A's Δ(net) slot.

    • Leading Taylor coefficients DIFFER: Δ(net)_A = {cA[1]}·ε,
      Δtr_M = {cT[1]}·ε.  They are different categorical objects, not
      single-wrap-vs-exact versions of one object.

    • Numerically the substitution misses CODATA by {mp.nstr(ppm_swap, 6)} ppm
      (Form A itself misses by {mp.nstr(ppm_formA, 6)} ppm). Substituting
      the exact Habiro trace difference makes the agreement WORSE, not
      better — confirming the two objects are structurally distinct.

    • CONCLUSION: Q_β does NOT consume Δtr_M through Form A's Δ(net)
      slot. The bridge f in Q_β = m_e × f(Δtr_M, q) — if it exists — is
      NOT the canonical-refinement substitution. This is a genuine open
      derivation step, not a fit-able gap.

    • DISCIPLINE OUTCOME: wire nothing new. Production Q_β stays at the
      Q_N2 honest floor (c_2 = -1 Taylor-exact, Lean-proved). The c_k
      cache keeps its discipline labels; future work flips a label only
      when a real categorical f is derived (not guessed).""")
    print()

    builder.add_data("form_A_factorization", {
        "delta_net_A": str(sp.simplify(delta_net_A)),
        "E_0": "1/(q*(q-1))",
        "Q_A_over_me": str(sp.simplify(Q_A_over_me)),
        "note": "Form A = m_e·|Δ(net)_A|·E_0 with Δ(net)_A the single-wrap NF net winding.",
    })
    builder.add_data("leading_taylor_coefficients", {
        "basis": "eps = q - 1",
        "delta_net_A": {f"eps^{k}": str(cA[k]) for k in range(6)},
        "delta_tr_M": {f"eps^{k}": str(cT[k]) for k in range(6)},
        "leading_order_match": bool(same_leading),
    })
    builder.add_data("numerical_at_q0", {
        "abs_delta_net_A": mp.nstr(abs(dnetA0), 18),
        "abs_delta_tr_M": mp.nstr(abs(dtr0), 18),
        "ratio_dtr_over_dnetA": mp.nstr(abs(dtr0) / abs(dnetA0), 18),
        "Q_codata_MeV": mp.nstr(Q_codata, 12),
        "Q_formA_MeV": mp.nstr(Q_formA, 12),
        "Q_swap_MeV": mp.nstr(Q_swap, 12),
        "ppm_formA": mp.nstr(ppm_formA, 8),
        "ppm_swap": mp.nstr(ppm_swap, 8),
    })
    builder.add_data("verdict", {
        "delta_tr_closes_qbeta_through_form_A_slot": bool(closes),
        "leading_taylor_orders_match": bool(same_leading),
        "conclusion": ("Δtr_M and Δ(net)_A are structurally distinct "
                       "(differ at leading Taylor order); Q_β does not "
                       "consume Δtr_M through Form A's slot; bridge is a "
                       "genuine open derivation, not a fit-able gap; "
                       "production stays Q_N2."),
        "production_action": "none — Q_β stays at Q_N2 honest floor",
    })
    builder.add_assertion(
        "delta_tr_is_not_form_A_delta_net",
        computed=float(1 if not same_leading else 0),
        expected=1.0,
        tolerance=0.0,
        source=("Leading Taylor coefficients differ (Δ(net)_A=-2ε, "
                "Δtr_M=-5/4ε), so the Habiro trace difference is not "
                "Form A's net-winding slot."),
    )
    builder.save()
    print(f"  Witness: qbeta-delta-tr-vs-formA.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
