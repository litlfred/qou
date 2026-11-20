#!/usr/bin/env python3
"""
qou-ales step 9 — the gamma-gamma-selected diproton binding is second order in the
deformation: numerical check of `QOU/Mass/DiprotonSecondOrder.lean` at the proton pin.

The Lean file proves, from step 4's cube identity V^3 - 1 = h^2 ((2+h^2) V + 1) and the
log law of step 8, that with scale alpha > 0, deformation h != 0 and relative response
r > 0 the binding B = -alpha log(1 + h^2 r) has magnitude bracketed by

    alpha h^2 r / (1 + h^2 r)   <=   |B|   <=   alpha h^2 r,

so |B| = Theta(h^2) -- second order, with no constant chosen anywhere. It also proves
that h^2 <= 1/10 (which 1 < q <= 23/20 forces) caps the magnitude at alpha r / 10.

This probe does NOT re-derive any of that and asserts no new physical value. It checks
that the proved bracket actually contains the step-3 measurement, and how tight it is:

  * the interface ratio is READ from the step-3 witness
    (`gamma-gamma-h6-psd-selector-probe.witness.json`, the `G^3` row of `pp_binding`),
    not hardcoded;
  * the relative response r = (ratio - 1)/h^2 is derived from it;
  * |B| recomputed from the log law agrees with the step-3 `B_pp_MeV` for that row;
  * the two proved bounds bracket |B|, and the bracket width is reported;
  * the interval hypotheses hold at the pin (h^2 <= 1/10) and the alpha r / 10 ceiling
    is evaluated.

The scale alpha = E_0^full = m_e c_q^2 hbar_q / (1 - hbar_q^2) is recomputed here from
CODATA m_e and the pin, exactly as the step-3 producer does; it is the register's
tower-summed hadronic scale, NOT the Q_beta base E_0^(N=0).

## Precision
mpmath at 60 dps end to end; q_0 is the proton pin `Q_50_DIGIT_STR`. Nothing here reads
AME2020, a CODATA *binding* value, or a census.
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
STEP3_WITNESS = _ROOT / "computations/probes/gamma-gamma-h3-psd-selector-probe.witness.json"
BOND = "G^3"


def main() -> int:
    t0 = time.time()
    q = Q_MP
    qi = 1 / q
    h = q - qi
    h2 = h ** 2

    # alpha = E_0^full, recomputed as the step-3 producer does (register name; NOT E_0^(N=0))
    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    hbar_q = 1 - qi
    c_q = 1 / (q - 1)
    alpha = me * c_q ** 2 * hbar_q / (1 - hbar_q ** 2)

    print(f"qou-ales step 9 probe — diproton magnitude is Theta(h^2) (proton pin, {DPS} dps)")
    print(f"  q_0   = {mp.nstr(q, 20)}")
    print(f"  h^2   = {mp.nstr(h2, 20)}")
    print(f"  alpha = E_0^full = {mp.nstr(alpha, 14)} MeV")

    # the ratio is READ from the step-3 witness, not hardcoded
    step3 = json.loads(STEP3_WITNESS.read_text())["data"]
    rows = {r["bond"]: r for r in step3["pp_binding"]}
    if BOND not in rows:
        print(f"  step-3 witness has no {BOND} row; bonds = {sorted(rows)}")
        return 1
    row = rows[BOND]
    ratio = mp.mpf(row["ratio_atom_over_free"])
    B_step3 = mp.mpf(row["B_pp_MeV"])
    print(f"\n  step-3 witness, bond {BOND}: ratio = {mp.nstr(ratio, 20)}, "
          f"B_pp = {mp.nstr(B_step3, 12)} MeV")

    # the relative response, derived from the ratio
    r = (ratio - 1) / h2
    print(f"  r = (ratio - 1)/h^2 = {mp.nstr(r, 14)}   (order 10^-2, so h^2 r is order 10^-3)")

    # |B| from the log law, and the two proved bounds
    B = -alpha * mp.log(1 + h2 * r)
    absB = abs(B)
    lower = alpha * (h2 * r) / (1 + h2 * r)
    upper = alpha * (h2 * r)
    dev_vs_step3 = abs(absB - abs(B_step3))
    print(f"\n  |B| via the log law   = {mp.nstr(absB * 1000, 10)} keV")
    print(f"  |B| step-3 witness    = {mp.nstr(abs(B_step3) * 1000, 10)} keV   "
          f"(dev {mp.nstr(dev_vs_step3, 3)} MeV)")
    print(f"  proved LOWER bound    = {mp.nstr(lower * 1000, 10)} keV   "
          f"[alpha h^2 r/(1 + h^2 r)]")
    print(f"  proved UPPER bound    = {mp.nstr(upper * 1000, 10)} keV   [alpha h^2 r]")
    brackets = bool(lower <= absB <= upper)
    width = upper - lower
    rel_width = width / absB
    print(f"  bracket contains |B|  = {brackets};  width = {mp.nstr(width * 1000, 4)} keV "
          f"({mp.nstr(rel_width * 100, 3)} % of |B|)")

    # the interval ceiling
    in_interval = bool(h2 <= mp.mpf(1) / 10)
    ceiling = alpha * r / 10
    print(f"\n  h^2 <= 1/10 (i.e. 1 < q <= 23/20) = {in_interval}")
    print(f"  proved ceiling alpha r / 10        = {mp.nstr(ceiling * 1000, 10)} keV "
          f"-- keV scale from the interval alone")

    # first order would be alpha * h * r: the contrast that makes "second order" content
    first_order = alpha * h * r
    print(f"\n  for contrast, a FIRST-order magnitude alpha h r would be "
          f"{mp.nstr(first_order * 1000, 8)} keV "
          f"({mp.nstr(first_order / absB, 5)} x larger) -- the h^2 is what buys the keV")

    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("diproton-second-order-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales step 9: checks QOU/Mass/DiprotonSecondOrder.lean at the proton pin. The Lean "
        "proves |B| = Theta(h^2) for B = -alpha log(1 + h^2 r), bracketed by alpha h^2 r/(1+h^2 r) "
        "and alpha h^2 r, with the h^2 forced by step 4's cube identity rather than assumed. This "
        "probe reads the interface ratio from the step-3 witness (G^3 row), derives the relative "
        "response r, and verifies the bracket contains the measured |B| and how tight it is; it "
        "also evaluates the alpha r/10 ceiling that h^2 <= 1/10 gives. No new physical value is "
        "asserted; r remains the measurement. No AME/CODATA binding value or census is read.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (two-row truncation; ratio read from the step-3 H_6 witness)")
    w.add_parameter("dps", DPS)
    w.add_parameter("step3_witness", str(STEP3_WITNESS.relative_to(_ROOT)))
    w.add_parameter("bond", BOND)
    w.add_parameter("alpha_register_name",
                    "E_0^full (tower-summed hadronic scale); NOT the Q_beta base E_0^(N=0)")
    w.add_data("h_sq", fmt(h2))
    w.add_data("alpha_E0_full_MeV", fmt(alpha))
    w.add_data("ratio_atom_over_free", fmt(ratio))
    w.add_data("relative_response_r", fmt(r))
    w.add_data("abs_B_MeV", fmt(absB))
    w.add_data("proved_lower_MeV", fmt(lower))
    w.add_data("proved_upper_MeV", fmt(upper))
    w.add_data("bracket_width_MeV", fmt(width))
    w.add_data("bracket_rel_width", fmt(rel_width))
    w.add_data("ceiling_alpha_r_over_10_MeV", fmt(ceiling))
    w.add_data("first_order_contrast_MeV", fmt(first_order))
    w.add_assertion(name="log_law_reproduces_step3_B", computed=fmt(dev_vs_step3), expected="0",
                    tolerance="1e-9",
                    source="step-3 witness pp_binding[G^3].B_pp_MeV vs -alpha log(1 + h^2 r)")
    w.add_assertion(name="proved_bracket_contains_measured_B", computed=str(int(brackets)),
                    expected="1", tolerance="0",
                    source="Lean binding_magnitude_second_order")
    w.add_assertion(name="bracket_is_tight_below_one_percent",
                    computed=str(int(rel_width < mp.mpf("0.01"))), expected="1", tolerance="0",
                    source="width/|B| recorded in data as bracket_rel_width")
    w.add_assertion(name="pin_inside_h_sq_interval", computed=str(int(in_interval)), expected="1",
                    tolerance="0", source="Lean bound_on_q_interval via h_sq_le_of_q_le")
    w.add_assertion(name="ceiling_bounds_measured_B",
                    computed=str(int(absB <= ceiling)), expected="1", tolerance="0",
                    source="Lean bound_at_small_h_sq: |B| <= alpha r / 10")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
