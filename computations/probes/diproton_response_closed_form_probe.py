#!/usr/bin/env python3
"""
qou-ales step 10 — the diproton trace-weighted response in CLOSED FORM, and the order
correction it forces: numerical + symbolic check of
`QOU/Mass/DiprotonResponseClosedForm.lean`.

Step 9 left exactly one quantity measured: the trace-weighted response

    r = tr(W.D)/tr(W),    D = (G^3 - 1)/h^2,   W = the two free 11-letter nucleon words.

This probe DERIVES it. It evaluates the convention-D Markov trace on H_6 EXACTLY over Q(q)
-- every letter of both nucleon words and of the bond, all four weight-support blocks, no
numerics and no anchor in the derivation itself -- and obtains

    r(q) = (q^2-1)^2 (q^4+q^2+1) R(q) / ((q^2+1) P(q))
    P(q) = q^18 - 3q^16 + 7q^14 - 8q^12 + 10q^10 - 9q^8 + 10q^6 - 6q^4 + 3q^2 - 1
    R(q) = q^10 - q^8 + 4q^6 - 4q^4 + 2q^2 - 1

THE CORRECTION. (q^2-1)^2 = q^2 h^2, so r ITSELF carries a factor h^2:

    r = h^2 c(q),   c(q) = q^2 (q^4+q^2+1) R(q) / ((q^2+1) P(q)),   c(q_0) = 0.5537297

hence the interface ratio is mu - 1 = h^2 r = h^4 c, and the binding magnitude is
Theta(h^4), NOT Theta(h^2) as step 9's headline said. Step 9's bracket theorem is correct
(r is a free hypothesis there); its stated ORDER was two powers too weak, and the reason is
exactly the clause step 9's own correction asserted -- that tr(W.D) "carries no such
cancellation". It does.

What this probe asserts:
  * the exact symbolic r equals the Lean closed form `respPP` (symbolic identity, 0);
  * r = h^2 c exactly (symbolic identity, 0) -- the order correction;
  * the free trace factorises as nucleonTrace(q)^2 (disjoint-union multiplicativity) and
    nucleonTrace equals the exact H_3 Markov trace of the single 11-letter element;
  * the derived ratio reproduces the step-3 witness ratio, READ from the committed file;
  * 0 < c <= 1 at the pin (the Lean proves both on the whole ray q >= 1);
  * the proved bracket contains |B|, and the derived ceiling alpha/100 bounds it;
  * per-block: the mixed response carries ONE factor (q^2-1); the second appears only after
    y-weighting. Three distinct orders, which is why a character-level check misleads.

## Precision
Exact sympy over Q(q) for the derivation; mpmath at 60 dps for every numerical evaluation.
No float64 anywhere. Nothing here reads AME2020, a CODATA binding value, or a census.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402
from markov_weights_symbolic import solve_y_lambda, tr_M_canonical  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)
STEP3_WITNESS = _ROOT / "computations/probes/gamma-gamma-h3-psd-selector-probe.witness.json"
BOND = "G^3"

# The Lean closed forms, transcribed from QOU/Mass/DiprotonResponseClosedForm.lean.
LEAN_P = (Q**18 - 3*Q**16 + 7*Q**14 - 8*Q**12 + 10*Q**10 - 9*Q**8 + 10*Q**6
          - 6*Q**4 + 3*Q**2 - 1)
LEAN_R = Q**10 - Q**8 + 4*Q**6 - 4*Q**4 + 2*Q**2 - 1
LEAN_RESP = (Q**2 - 1)**2 * (Q**4 + Q**2 + 1) * LEAN_R / ((Q**2 + 1) * LEAN_P)
LEAN_COEFF = Q**2 * (Q**4 + Q**2 + 1) * LEAN_R / ((Q**2 + 1) * LEAN_P)
LEAN_NUCLEON_TRACE = (Q**4 + 1) * LEAN_P / (4 * Q**9 * (Q**2 + 1)**2)


def nucleon_word(g0: int) -> list[tuple[int, str]]:
    """The canonical 11-letter proton element on generators (g0, g0+1), as ctypes.

    Identical to step 3's `nucleon_block("p", h, g0)` and, at g0 = 0, to
    `markov_weights_symbolic.atom_braid_word_3A_to_crossings(1, 0)`: beta_Bor
    = (sigma_0 sigma_1^-1)^3, then the three quark letters (one sigma, two
    colour-blind -h/2 averages), then the two gluon sigma_0 crossings.
    """
    g1 = g0 + 1
    w: list[tuple[int, str]] = []
    for _ in range(3):
        w += [(g0, "sigma"), (g1, "sigma_inv")]
    w += [(g0, "sigma"), (g0, "averaged"), (g1, "averaged")]
    w += [(g0, "sigma"), (g0, "sigma")]
    return w


def bond_word(m: int) -> list[tuple[int, str]]:
    """G^m = (sigma_2 sigma_3^-1)^m, the gamma-gamma interface bond of step 6."""
    return [(2, "sigma"), (3, "sigma_inv")] * m


def main() -> int:
    t0 = time.time()
    q = Q_MP
    qi = 1 / q
    h = q - qi
    h2 = h**2
    qv = sp.Rational(Q_50_DIGIT_STR)

    print(f"qou-ales step 10 probe — the diproton response in closed form "
          f"(proton pin, {DPS} dps)")
    print(f"  q_0 = {mp.nstr(q, 20)}   h^2 = {mp.nstr(h2, 20)}   h^4 = {mp.nstr(h2**2, 20)}")

    free = nucleon_word(0) + nucleon_word(3)
    bond = bond_word(3)
    print(f"  words: free = {len(free)} letters on generators (0,1)+(3,4); "
          f"bond = {len(bond)} letters on (2,3)")

    # ---- the exact derivation over Q(q) -------------------------------------------
    y6 = solve_y_lambda(6)
    support = [lam for lam in y6 if sp.cancel(y6[lam]) != 0]
    print(f"\n  convention-D weight support at H_6: {sorted(support, key=len)} "
          f"({len(support)} of {len(y6)} blocks)")
    chis: dict[tuple[str, tuple], sp.Expr] = {}
    tr: dict[str, sp.Expr] = {}
    for name, word in (("free", free), ("atom", free + bond)):
        total = sp.Integer(0)
        for lam in support:
            t1 = time.time()
            chi = sp.cancel(chi_lambda_symbolic(lam, word))
            chis[(name, lam)] = chi
            total += sp.cancel(y6[lam] * chi)
            print(f"    chi^{str(lam):<8} {name:<5} {time.time() - t1:6.1f}s")
        tr[name] = sp.cancel(sp.together(total))

    ratio_sym = sp.cancel(tr["atom"] / tr["free"])
    h2_sym = sp.cancel((Q - 1 / Q) ** 2)
    r_sym = sp.cancel((ratio_sym - 1) / h2_sym)
    print(f"\n  tr_M(free) = {sp.factor(tr['free'])}")
    print(f"  tr_M(atom) = {sp.factor(tr['atom'])}")
    print(f"  r(q)       = {sp.factor(r_sym)}")

    # ---- identities against the Lean closed forms ---------------------------------
    dev_resp = sp.simplify(r_sym - LEAN_RESP)
    dev_fact = sp.simplify(r_sym - h2_sym * LEAN_COEFF)
    dev_mult = sp.simplify(tr["free"] - LEAN_NUCLEON_TRACE**2)
    tr_p_sym = sp.cancel(tr_M_canonical(nucleon_word(0), 3)[0])
    dev_nucl = sp.simplify(tr_p_sym - LEAN_NUCLEON_TRACE)
    print(f"\n  r - respPP(q)                    = {dev_resp}   [Lean respPP]")
    print(f"  r - h^2 * responseCoeff(q)       = {dev_fact}   [Lean respPP_eq_hSq_mul_coeff]")
    print(f"  tr_M(free) - nucleonTrace^2      = {dev_mult}   [disjoint-union multiplicativity]")
    print(f"  tr_M,H3(p) - nucleonTrace        = {dev_nucl}   [Lean nucleonTrace]")

    # ---- the order of each per-block mixed response --------------------------------
    print("\n  per-block mixed response (chi_atom - chi_free)/h^2 — order in (q^2 - 1):")
    orders = {}
    for lam in sorted(support, key=len):
        resp = sp.cancel((chis[("atom", lam)] - chis[("free", lam)]) / h2_sym)
        if resp == 0:
            orders[lam] = None
            print(f"    {str(lam):<8} identically 0 (the bond acts as 1 on this block)")
            continue
        k = 0
        cur = sp.cancel(resp)
        while sp.simplify(sp.cancel(cur).subs(Q, 1)) == 0 and k < 6:
            cur = sp.cancel(cur / (Q**2 - 1))
            k += 1
        orders[lam] = k
        print(f"    {str(lam):<8} vanishes to order {k} in (q^2 - 1)")
    weighted_order = 0
    cur = sp.cancel(r_sym)
    while sp.simplify(sp.cancel(cur).subs(Q, 1)) == 0 and weighted_order < 6:
        cur = sp.cancel(cur / (Q**2 - 1))
        weighted_order += 1
    print(f"    y-weighted r vanishes to order {weighted_order} in (q^2 - 1) — "
          f"the extra power appears only after weighting")

    # ---- numerics at the pin -------------------------------------------------------
    # Evaluated twice, independently: once through sympy's exact rational substitution and
    # once through a direct mpmath transcription of the same closed form. The two agreeing is
    # a check on the transcription, not only on the arithmetic.
    def _P(x):
        return (x**18 - 3*x**16 + 7*x**14 - 8*x**12 + 10*x**10 - 9*x**8 + 10*x**6
                - 6*x**4 + 3*x**2 - 1)

    def _R(x):
        return x**10 - x**8 + 4*x**6 - 4*x**4 + 2*x**2 - 1

    c_mp = q**2 * (q**4 + q**2 + 1) * _R(q) / ((q**2 + 1) * _P(q))
    c_val = mp.mpf(str(sp.N(LEAN_COEFF.subs(Q, qv), DPS + 10)))
    dev_c_paths = abs(c_val - c_mp)
    r_val = h2 * c_val
    ratio_val = 1 + h2 * r_val
    print(f"\n  c via sympy-exact vs mpmath transcription: dev {mp.nstr(dev_c_paths, 3)}")
    print(f"\n  c(q_0)       = {mp.nstr(c_val, 20)}   (order one; 0 < c <= 1 proved for q >= 1)")
    print(f"  r(q_0)       = {mp.nstr(r_val, 20)}   = h^2 c")
    print(f"  mu - 1       = {mp.nstr(h2 * r_val, 20)}   = h^4 c")

    step3 = json.loads(STEP3_WITNESS.read_text())["data"]
    rows = {row["bond"]: row for row in step3["pp_binding"]}
    if BOND not in rows:
        print(f"  step-3 witness has no {BOND} row; bonds = {sorted(rows)}")
        return 1
    ratio_step3 = mp.mpf(rows[BOND]["ratio_atom_over_free"])
    B_step3 = mp.mpf(rows[BOND]["B_pp_MeV"])
    dev_ratio = abs(ratio_val - ratio_step3)
    print(f"  step-3 ratio = {mp.nstr(ratio_step3, 20)}   (dev {mp.nstr(dev_ratio, 3)})")

    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    hbar_q = 1 - qi
    c_q = 1 / (q - 1)
    alpha = me * c_q**2 * hbar_q / (1 - hbar_q**2)
    B = -alpha * mp.log(ratio_val)
    absB = abs(B)
    lower = alpha * (h2 * r_val) / (1 + h2 * r_val)
    upper = alpha * (h2 * r_val)
    ceiling = alpha / 100
    print(f"\n  alpha = E_0^full = {mp.nstr(alpha, 14)} MeV   [NOT the Q_beta base E_0^(N=0)]")
    print(f"  |B|              = {mp.nstr(absB * 1000, 12)} keV   "
          f"(step-3 {mp.nstr(abs(B_step3) * 1000, 12)} keV)")
    print(f"  proved bracket   = [{mp.nstr(lower * 1000, 10)}, {mp.nstr(upper * 1000, 10)}] keV")
    print(f"  derived ceiling  = alpha/100 = {mp.nstr(ceiling * 1000, 10)} keV "
          f"(h^4 <= 1/100 on 1 < q <= 23/20, c <= 1 for all q >= 1)")
    print(f"  step-9 ceiling   = alpha r/10 = {mp.nstr(alpha * r_val / 10 * 1000, 10)} keV "
          f"— needed a MEASURED r; the new one needs nothing")

    brackets = bool(lower <= absB <= upper)
    dev_B = abs(absB - abs(B_step3))
    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("diproton-response-closed-form-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales step 10: DERIVES the trace-weighted response r that step 9 carried as a "
        "measured hypothesis, by exact convention-D Markov-trace evaluation on H_6 over Q(q) "
        "with the two canonical 11-letter nucleon words and the gamma-gamma bond G^3. Result: "
        "r = (q^2-1)^2 (q^4+q^2+1) R / ((q^2+1) P) = h^2 c with c(q_0) = 0.5537297 order one, "
        "so mu - 1 = h^4 c and the binding magnitude is Theta(h^4) -- CORRECTING step 9's "
        "Theta(h^2) headline by two powers. Verifies the Lean closed forms respPP, "
        "responseCoeff and nucleonTrace as symbolic identities, the disjoint-union "
        "multiplicativity of the free trace, the reproduction of the step-3 witness ratio, and "
        "the derived ceiling alpha/100 which needs no measured input at all. Also records the "
        "three distinct orders (per-block mixed response, y-weighted response, ratio) that make "
        "a character-level order check misleading. No AME/CODATA binding value or census read.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1); two-row weight support at H_6)")
    w.add_parameter("dps", DPS)
    w.add_parameter("step3_witness", str(STEP3_WITNESS.relative_to(_ROOT)))
    w.add_parameter("bond", BOND)
    w.add_parameter("free_word_letters", len(free))
    w.add_parameter("alpha_register_name",
                    "E_0^full (tower-summed hadronic scale); NOT the Q_beta base E_0^(N=0)")
    w.add_data("weight_support", [list(lam) for lam in sorted(support, key=len)])
    w.add_data("tr_M_free_symbolic", sp.sstr(sp.factor(tr["free"])))
    w.add_data("tr_M_atom_symbolic", sp.sstr(sp.factor(tr["atom"])))
    w.add_data("response_r_symbolic", sp.sstr(sp.factor(r_sym)))
    w.add_data("response_coeff_symbolic", sp.sstr(sp.factor(sp.cancel(LEAN_COEFF))))
    w.add_data("nucleon_trace_symbolic", sp.sstr(sp.factor(sp.cancel(LEAN_NUCLEON_TRACE))))
    w.add_data("h_sq", fmt(h2))
    w.add_data("h_fourth", fmt(h2**2))
    w.add_data("response_coeff_at_q0", fmt(c_val))
    w.add_data("response_r_at_q0", fmt(r_val))
    w.add_data("ratio_atom_over_free", fmt(ratio_val))
    w.add_data("alpha_E0_full_MeV", fmt(alpha))
    w.add_data("abs_B_MeV", fmt(absB))
    w.add_data("proved_lower_MeV", fmt(lower))
    w.add_data("proved_upper_MeV", fmt(upper))
    w.add_data("derived_ceiling_alpha_over_100_MeV", fmt(ceiling))
    w.add_data("per_block_response_order_in_q_sq_minus_one",
               {str(lam): orders[lam] for lam in sorted(support, key=len)})
    w.add_data("weighted_response_order_in_q_sq_minus_one", weighted_order)
    w.add_assertion(name="exact_response_equals_lean_closed_form",
                    computed=sp.sstr(dev_resp), expected="0", tolerance="0",
                    source="Lean respPP vs exact H_6 convention-D Markov trace over Q(q)")
    w.add_assertion(name="response_factorises_as_h_sq_times_coeff",
                    computed=sp.sstr(dev_fact), expected="0", tolerance="0",
                    source="Lean respPP_eq_hSq_mul_coeff -- the Theta(h^4) correction")
    w.add_assertion(name="free_trace_is_square_of_nucleon_trace",
                    computed=sp.sstr(dev_mult), expected="0", tolerance="0",
                    source="disjoint-union multiplicativity of tr_M; Lean ResponseClosedForm.free_eq")
    w.add_assertion(name="nucleon_trace_matches_H3_closed_form",
                    computed=sp.sstr(dev_nucl), expected="0", tolerance="0",
                    source="Lean nucleonTrace vs tr_M_canonical(11-letter element, 3)")
    w.add_assertion(name="derived_ratio_reproduces_step3_witness",
                    computed=fmt(dev_ratio), expected="0", tolerance="1e-45",
                    source="step-3 witness pp_binding[G^3].ratio_atom_over_free (mpmath path)")
    w.add_assertion(name="log_law_reproduces_step3_B", computed=fmt(dev_B), expected="0",
                    tolerance="1e-9",
                    source="step-3 witness pp_binding[G^3].B_pp_MeV vs -alpha log(1 + h^4 c)")
    w.add_assertion(name="coeff_in_zero_one",
                    computed=str(int(0 < c_val <= 1)), expected="1", tolerance="0",
                    source="Lean responseCoeff_pos + responseCoeff_le_one (all q >= 1)")
    w.add_assertion(name="proved_bracket_contains_B", computed=str(int(brackets)),
                    expected="1", tolerance="0",
                    source="Lean binding_magnitude_fourth_order")
    w.add_assertion(name="derived_ceiling_bounds_B",
                    computed=str(int(absB <= ceiling)), expected="1", tolerance="0",
                    source="Lean binding_ceiling_on_interval: |B| <= alpha/100")
    w.add_data("coeff_two_path_dev", fmt(dev_c_paths))
    w.add_assertion(name="coeff_transcription_agrees_across_paths",
                    computed=fmt(dev_c_paths), expected="0", tolerance="1e-50",
                    source="sympy exact rational substitution vs direct mpmath transcription")
    w.add_assertion(name="weighted_response_gains_one_order_over_blocks",
                    computed=str(weighted_order), expected="2", tolerance="0",
                    source="per-block responses vanish to order 1 in (q^2-1); the sum to order 2")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
