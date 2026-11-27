#!/usr/bin/env python3
"""
qou-ales step 4 — the gamma-gamma vertex is the q-deformed 3-cycle: numerical
cross-check of `QOU/Mass/GammaGammaVertexOrder.lean` against the step-3 witness.

The Lean file proves, from the Hoefsmit relations alone, that the (2,1)-image
V of the pair-production vertex sigma_0 sigma_1^-1 has det V = 1 and
tr V = -1 - h^2 (h = q - 1/q), so by Cayley-Hamilton

    V^k = alpha_k V + beta_k 1,   alpha_{k+1} = t alpha_k + beta_k,
                                  beta_{k+1}  = -alpha_k,   t = tr V,

and on the reals V^k is symmetric iff alpha_k = 0 iff V^k = +-1. Also
V^3 = (2h^2 + h^4) V + (1 + h^2) 1, so V^3 = 1 iff h = 0: the k = 3 survivor
of step 3 is the q-deformation of the 3-cycle s_0 s_1 of S_3.

This probe does NOT re-derive any of that. It checks that the numbers the
theorems predict at the proton pin are the numbers the step-3 probe measured
and recorded in `gamma-gamma-h3-psd-selector-probe.witness.json`:

  * det V = 1, tr V = -1 - h^2 to working precision;
  * the closed-form Chebyshev traces chi_k (Lean trace_vtx_pow_1..5) equal
    the witness column `h3_candidates[k].chi_21` for k = 0..5, and equal the
    directly computed tr(V^k);
  * V^3 - 1 = h^2 ((2 + h^2) V + 1) entrywise;
  * the interval hypotheses of the Lean sign lemmas hold at the pin
    (1 < q_0 <= 23/20, 0 < h^2 <= 1/10) and alpha_k != 0 for k = 1..5;
  * the sign pattern (-,-,+,-,-) of chi_1..chi_5.

Informational only (no claim, no assertion): theta/pi with 2 cos theta = tr V,
the distance of 3 theta from 2 pi, and min_k |alpha_k| for k <= 60 — the
question "is some V^k scalar?" is theta/pi in Q, which is not decided here.

## Precision
mpmath at 60 dps end to end; q_0 is the proton pin `Q_50_DIGIT_STR`; the
Hoefsmit data is the closed form a = h/(1-q^4), a' = h/(1-q^-4),
b = sqrt(a a' + 1) exactly as in the Lean definitions. Nothing here reads
AME2020, CODATA masses beyond the pin, or a census.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "computations/substrate", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")
STEP3_WITNESS = _ROOT / "computations/probes/gamma-gamma-h3-psd-selector-probe.witness.json"


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matpow(A, k):
    M = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]
    for _ in range(k):
        M = matmul(M, A)
    return M


def lin(t, k):
    """(alpha_k, beta_k) of the Lean `lin` recurrence."""
    a, b = mp.mpf(0), mp.mpf(1)
    for _ in range(k):
        a, b = t * a + b, -a
    return a, b


def chi_closed(k, x):
    """Lean trace_vtx_pow_1..5 with x = h^2 (k = 0 is the dimension 2)."""
    return {
        0: mp.mpf(2),
        1: -1 - x,
        2: x**2 + 2 * x - 1,
        3: 2 - 3 * x**2 - x**3,
        4: x**4 + 4 * x**3 + 2 * x**2 - 4 * x - 1,
        5: -x**5 - 5 * x**4 - 5 * x**3 + 5 * x**2 + 5 * x - 1,
    }[k]


def main() -> int:
    t0 = time.time()
    mp.mp.dps = DPS
    q = Q_MP
    qi = 1 / q
    h = q - qi
    x = h**2

    # Hoefsmit (2,1) data, closed form (Lean hoefsmitA / hoefsmitA' / hoefsmitB)
    a = h / (1 - q**4)
    ap = h / (1 - q**-4)
    b = mp.sqrt(a * ap + 1)
    # V = sigma_0 * (sigma_1 - h 1)  (Lean stdImage_vertex_entries)
    V = [[q * (a - h), q * b], [-qi * b, -qi * (ap - h)]]

    detV = V[0][0] * V[1][1] - V[0][1] * V[1][0]
    trV = V[0][0] + V[1][1]
    t = -1 - x
    dev_det = abs(detV - 1)
    dev_tr = abs(trV - t)
    print(f"q0 = {mp.nstr(q, 20)}   h = {mp.nstr(h, 20)}   h^2 = {mp.nstr(x, 20)}")
    print(f"det V - 1 = {mp.nstr(dev_det, 5)}   tr V - (-1 - h^2) = {mp.nstr(dev_tr, 5)}")

    # Chebyshev traces vs direct powers vs the step-3 witness
    wit = json.loads(STEP3_WITNESS.read_text())
    rows = wit["data"]["h3_candidates"]
    chi_wit = {int(r["k"]): mp.mpf(r["chi_21"]) for r in rows}
    dev_closed_vs_direct = mp.mpf(0)
    dev_closed_vs_witness = mp.mpf(0)
    table = []
    for k in range(0, 6):
        Vk = matpow(V, k)
        tr_direct = Vk[0][0] + Vk[1][1]
        tr_closed = chi_closed(k, x)
        alpha, beta = lin(t, k)
        d1 = abs(tr_closed - tr_direct)
        d2 = abs(tr_closed - chi_wit[k]) if k in chi_wit else None
        dev_closed_vs_direct = max(dev_closed_vs_direct, d1)
        if d2 is not None:
            dev_closed_vs_witness = max(dev_closed_vs_witness, d2)
        # the lin decomposition itself, entrywise
        lin_dev = max(abs(Vk[i][j] - (alpha * V[i][j] + (beta if i == j else 0)))
                      for i in range(2) for j in range(2))
        table.append({"k": k, "chi_closed": fmt(tr_closed), "chi_direct": fmt(tr_direct),
                      "chi_witness_step3": fmt(chi_wit[k]) if k in chi_wit else None,
                      "alpha_k": fmt(alpha), "beta_k": fmt(beta),
                      "lin_decomposition_dev": fmt(lin_dev),
                      "sign": "+" if tr_closed > 0 else "-"})
        print(f"  k={k}: chi = {mp.nstr(tr_closed, 12):>16}   witness = "
              f"{mp.nstr(chi_wit[k], 12) if k in chi_wit else 'n/a':>16}   "
              f"alpha_k = {mp.nstr(alpha, 10):>14}   lin dev = {mp.nstr(lin_dev, 3)}")
    print(f"max |closed - direct| = {mp.nstr(dev_closed_vs_direct, 5)}   "
          f"max |closed - step-3 witness| = {mp.nstr(dev_closed_vs_witness, 5)}")

    # V^3 - 1 = h^2 ((2 + h^2) V + 1)
    V3 = matpow(V, 3)
    dev_cube = max(abs((V3[i][j] - (1 if i == j else 0))
                       - x * ((2 + x) * V[i][j] + (1 if i == j else 0)))
                   for i in range(2) for j in range(2))
    dist_cube = mp.sqrt(sum((V3[i][j] - (1 if i == j else 0))**2 for i in range(2) for j in range(2)))
    print(f"|V^3 - 1 - h^2((2+h^2)V + 1)|_max = {mp.nstr(dev_cube, 5)}   "
          f"|V^3 - 1|_F = {mp.nstr(dist_cube, 10)}")

    # interval hypotheses and the alpha_k != 0 / sign pattern facts
    in_q_interval = (1 < q) and (q <= mp.mpf(23) / 20)
    in_x_interval = (0 < x) and (x <= mp.mpf(1) / 10)
    alphas = [lin(t, k)[0] for k in range(1, 6)]
    min_abs_alpha_5 = min(abs(al) for al in alphas)
    signs = "".join("+" if chi_closed(k, x) > 0 else "-" for k in range(1, 6))
    print(f"1 < q0 <= 23/20: {in_q_interval}   0 < h^2 <= 1/10: {in_x_interval}   "
          f"min_{{k<=5}} |alpha_k| = {mp.nstr(min_abs_alpha_5, 8)}   signs(1..5) = {signs}")

    # informational: theta/pi, 3 theta vs 2 pi, closest approach to scalar for k <= 60
    cos_theta = trV / 2
    theta = mp.acos(cos_theta)
    theta_over_pi = theta / mp.pi
    three_theta_minus_2pi_deg = (3 * theta - 2 * mp.pi) * 180 / mp.pi
    best_k, best_abs = None, None
    for k in range(1, 61):
        al = abs(lin(t, k)[0])
        if best_abs is None or al < best_abs:
            best_k, best_abs = k, al
    print(f"theta/pi = {mp.nstr(theta_over_pi, 15)}   3 theta - 2 pi = {mp.nstr(three_theta_minus_2pi_deg, 6)} deg   "
          f"min_{{k<=60}} |alpha_k| = {mp.nstr(best_abs, 6)} at k = {best_k}   (informational)")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gamma-gamma-vertex-order-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales step 4: numerical cross-check of QOU/Mass/GammaGammaVertexOrder.lean at "
        "the proton pin. The (2,1)-image V of the gamma-gamma vertex has det 1 and trace "
        "-1-h^2; V^k = alpha_k V + beta_k 1 (Chebyshev/Cayley-Hamilton); the closed-form "
        "traces chi_1..chi_5 reproduce the step-3 witness column chi_21; V^3 - 1 = "
        "h^2((2+h^2)V + 1) (the q-deformed 3-cycle); the Lean interval hypotheses "
        "(1 < q <= 23/20, 0 < h^2 <= 1/10) hold at the pin and alpha_k != 0 for k <= 5. "
        "Informational: theta/pi and the closest approach of V^k to a scalar for k <= 60. "
        "No AME/CODATA binding value read; no census."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (Hoefsmit (2,1) block; Markov parameter not used here)")
    w.add_parameter("dps", DPS)
    w.add_parameter("tolerance", fmt(TOL))
    w.add_parameter("step3_witness", str(STEP3_WITNESS.relative_to(_ROOT)))
    w.add_data("h", fmt(h))
    w.add_data("h_sq", fmt(x))
    w.add_data("trace_V", fmt(trV))
    w.add_data("det_V", fmt(detV))
    w.add_data("chebyshev_table", table)
    w.add_data("V3_minus_1_frobenius", fmt(dist_cube))
    w.add_data("theta_over_pi", fmt(theta_over_pi))
    w.add_data("three_theta_minus_2pi_deg", fmt(three_theta_minus_2pi_deg))
    w.add_data("closest_scalar_approach_k_le_60", {"k": best_k, "abs_alpha_k": fmt(best_abs)})
    w.add_data("signs_chi_1_to_5", signs)
    w.add_assertion(name="det_V_is_one", computed=fmt(dev_det), expected="0", tolerance="1e-50",
                    source="Lean vtx_det")
    w.add_assertion(name="trace_V_is_minus_one_minus_h_sq", computed=fmt(dev_tr), expected="0",
                    tolerance="1e-50", source="Lean vtx_trace")
    w.add_assertion(name="chebyshev_closed_forms_match_direct_powers",
                    computed=fmt(dev_closed_vs_direct), expected="0", tolerance="1e-50",
                    source="Lean trace_vtx_pow_one..five via pow_eq_lin")
    w.add_assertion(name="chebyshev_closed_forms_match_step3_witness",
                    computed=fmt(dev_closed_vs_witness), expected="0", tolerance="1e-40",
                    source="gamma-gamma-h3-psd-selector-probe.witness.json h3_candidates[k].chi_21")
    w.add_assertion(name="vertex_cube_is_q_deformed_identity", computed=fmt(dev_cube),
                    expected="0", tolerance="1e-50", source="Lean vtx_three_sub_one")
    w.add_assertion(name="pin_inside_lean_interval",
                    computed=str(int(in_q_interval and in_x_interval)), expected="1", tolerance="0",
                    source="Lean h_sq_le_of_q_le: 1 < q <= 23/20 => h^2 <= 1/10")
    w.add_data("min_abs_alpha_k_le_5", fmt(min_abs_alpha_5))
    w.add_assertion(name="alpha_k_nonzero_k_le_5",
                    computed=str(int(min_abs_alpha_5 > mp.mpf("1e-3"))), expected="1",
                    tolerance="0", source="Lean lin_ne_zero_of_small (min |alpha_k| recorded in data)")
    w.add_assertion(name="sign_pattern_chi_1_to_5", computed=signs, expected="--+--", tolerance="0",
                    source="Lean chi_signs_of_small")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
