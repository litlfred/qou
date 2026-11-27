#!/usr/bin/env python3
"""Bean `qou-59j5`, ANSWERED: `E_0` is NOT derivable, and the problem is bigger.

THE QUESTION
------------
The previous probe (`extensive_term_energy_scale_reconciliation_probe`) showed
that the extensive term's "~7x shortfall" was the ratio `E_0/m_e = 8.19`, and
left one question gating every magnitude claim in the lane:

    is `E_0 = m_e/(q_0(q_0-1))` derivable, or is it CAL-1 forever?

ANSWER: NOT DERIVABLE, AND THE CORPUS ALREADY KNEW
---------------------------------------------------
`computations/derivation_chain.py` carries an `E_0_CONVENTIONS` registry, and
convention A's own `derivation` field says it outright:

    "Closed-form algebraic substitution from CAL-1 m_e + CAL-2 q_0. ...
     the existing direct LP-dual probe at H_3 reports y_0^* DIMENSIONLESS,
     far from 4.186 MeV -- so the MeV scale of E_0 still comes from
     CAL-1 + CAL-2 outside the LP, not from the LP dual directly."

The one attempt to derive it — convention D, the operator-selection LP dual,
`derive_e_0_lp_dual_h3.py` — is a **recorded negative finding**. Its committed
witness gives `y_0^* = 0.37539` (dimensionless), so `y_0^* m_e = 0.1918 MeV`
against convention A's 4.186: a factor of **21.8 away** [assertion 3]. Its own
`negative_finding` field states the conclusion: *"The LP-dual does NOT derive
E_0 in MeV; it gives a dimensionless action shadow price."*

So `qou-59j5` closes NO. Nothing further needs to be tried; it has been tried.

AND THE SITUATION IS WORSE THAN THAT BEAN STATED
-------------------------------------------------
I framed it as two scales in tension, `m_e` vs `E_0`. It is a **registry of four
conventions spanning 256x**, indexed by (`hbar_q` power, Hecke level, operator
class):

    A_single_hecke_tick   m_e/(q_0(q_0-1)) = 4.18598 MeV  hbar_q^1  H_3    3 strands
    B_q_value_absorbed    Q_beta^CODATA    = 0.78233 MeV  hbar_q^0  H_3A   3A strands
    C_proton_back_fit     ~ 200 MeV        DISCIPLINE VIOLATION, do not consume
    D_lp_dual             N/A -- dimensionless; NOT an E_0 derivation

and `m_e = 0.511 MeV`, the scale my three probes used, **is not in the registry
at all**.

A and B are not two guesses at one number. They are (scale) and
(scale x operator): `B = A * |Delta(net)|` with `Delta(net) = h(h-2)/2`,
`h = q - 1/q = hbar_q (q+1)`, so the operator is `hbar_q^1` and both routes give
the same total `hbar_q^2`. Which convention a quantity takes depends on what
`hbar_q` power the quantity itself already carries.

THE LADDER'S RUNGS ARE 102x APART, AND MY 8.19x ERROR WAS A SMALL STEP ON IT
-----------------------------------------------------------------------------
The registry's convention-B `validity` field warns:

    "Naively using convention A with a Delta(net)-style operator difference
     would miss the 1/hbar_q^2 factor (~ 102x error)."

Measured, `1/hbar_q^2 = 101.862` [assertion 1] — so that stated 102 is exactly
the `hbar_q` bookkeeping, confirming the ladder's spacing independently of any
prose. **Getting the `hbar_q` power wrong costs 102x; my `m_e`-for-`E_0` slip
cost 8.19x.** The uncertainty in the extensive term's scale is an order of
magnitude larger than the error I just corrected.

THE EXTENSIVE TERM MATCHES NO REGISTERED OPERATOR CLASS
--------------------------------------------------------
This is the part that leaves the question genuinely open rather than merely
unanswered. The registry indexes by operator class:

    A: Delta_NF = (h^2/2) gamma - (h/2) sigma_0 - (h/2) sigma_1, beta-decay
       single-wrap in H_3(q)
    B: |tr_M(W_free)| - |tr_M(W_atom)|, a trace DIFFERENCE at H_3A
    C: multi-term atomic mass assembly

`log Z(3A)` — the extensive term — is the logarithm of the **partition
function**. It is neither `Delta_NF` nor a trace difference. Its Hecke level is
`H_3A`, which points at B; its `hbar_q` content is **zero** (`log(1+q_0^2) =
0.803`, an O(1) quantity, not a small one), which points at A. The registry does
not adjudicate, and the two answers differ by 5.35x:

    at convention A:   10.083 MeV/nucleon   ->  1.57x short of a_V
    at convention B:    1.884 MeV/nucleon   ->  8.38x short of a_V
    at m_e (mine):      1.231 MeV/nucleon   -> 12.84x short of a_V

WHAT THIS MEANS FOR THE LANE
-----------------------------
"The extensive term is short by N" has no determinate value. N is 1.57, 8.38 or
12.84 depending on a choice the corpus has not made and, per convention D,
cannot currently derive. The honest statements that survive are the scale-free
ones: the A-exponent is exactly 1 (`qou-imcd`), the counters are exactly linear
(`extensive_counter_family_probe`), the framing factor is exactly `q`
(`qou-78pt` assertion 1), and `b_nn/b_pp = 1.78` in the `B_sym` chain.

Stop quoting magnitude deficits for the extensive term.

A SMALL DRIFT NOTED IN PASSING
-------------------------------
`derive_e_0_lp_dual_h3.py`'s docstring says the positive-cone LP gives
`y_0^* = 0.1245`; its committed witness records `0.37539` for every target. The
docstring predates the 2026-08-23 solver change (scipy.linprog -> clarabel-MPFR)
noted in that same file. The conclusion is unaffected — both are far from 4.186
— but the prose figure is stale.

Usage:
    python3 computations/probes/e0_convention_ladder_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

M_E_MEV = mp.mpf("0.51099895069")
STRANDS_PER_NUCLEON = 3
B_OVER_A_PLATEAU = mp.mpf("8.5")
SEMF_A_V = mp.mpf("15.8")

# Figures quoted from `computations/derivation_chain.py`'s E_0_CONVENTIONS
# registry, transcribed, not recomputed. They are the INDEPENDENT side of the
# assertions below.
REGISTRY_A_QUOTED_MEV = mp.mpf("4.186")     # "m_e / (q_0 (q_0 - 1)) ~ 4.186 MeV"
REGISTRY_HBARQ_ERROR_FACTOR = mp.mpf("102")  # "would miss the 1/hbar_q^2 factor (~ 102x)"
REGISTRY_C_APPROX_MEV = mp.mpf("200")        # "~ 200 MeV", flagged discipline violation


def main() -> int:
    q = Q_MP
    hbar_q = (q - 1) / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    conv_a = _qbeta_e0.order_zero_scaled(M_E_MEV, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    w = WitnessBuilder("e0-convention-ladder-probe")
    w.set_description(
        "Answers bean qou-59j5: E_0 is NOT derivable -- the corpus's own E_0_CONVENTIONS "
        "registry calls convention A a closed-form substitution from CAL-1 + CAL-2, and the "
        "sole derivation attempt (convention D, the LP dual) is a recorded negative finding. "
        "Also shows the problem is a 256x-wide four-convention registry, not a two-scale "
        "tension, and that the extensive term log Z(3A) matches no registered operator class."
    )

    # ---- assertion 1: the ladder's spacing is 1/hbar_q^2 ---------------------
    # INDEPENDENT side: the "~102x" is prose in derivation_chain.py's
    # E_0_CONVENTIONS["B_q_value_absorbed"]["validity"], written before this
    # probe. Agreement confirms that the registry's conventions really are
    # indexed by powers of hbar_q, rather than being unrelated guesses.
    w.add_assertion(
        "registry_stated_102x_error_is_one_over_hbar_q_squared",
        computed=mp.nstr(1 / hbar_q ** 2, 6),
        expected=mp.nstr(REGISTRY_HBARQ_ERROR_FACTOR, 6),
        tolerance="0.5",
        source="1/hbar_q^2 with hbar_q = (q_0-1)/q_0 from q_parameter, vs the '~ 102x error' "
               "quoted in derivation_chain.E_0_CONVENTIONS['B_q_value_absorbed']['validity']",
    )

    # ---- assertion 2: convention A's registry string is the value ------------
    w.add_assertion(
        "convention_A_computes_to_the_registry_quoted_value",
        computed=mp.nstr(conv_a, 6),
        expected=mp.nstr(REGISTRY_A_QUOTED_MEV, 6),
        tolerance="1e-3",
        source="m_e/(q_0(q_0-1)) at 40 dps vs the '~ 4.186 MeV' recorded in "
               "derivation_chain.E_0_CONVENTIONS['A_single_hecke_tick']['value_MeV']",
    )

    # ---- assertion 3: the LP-dual derivation of E_0 FAILED -------------------
    # This is the bean's actual question, answered against a committed artifact
    # rather than against prose. y_0^* is read from the LP witness on disk.
    lp = json.loads((HERE.parent / "e-0-lp-dual-h3.witness.json").read_text())
    y0_cone = [mp.mpf(str(r["y_0_star"]))
               for r in lp["data"]["results_per_target_cone"].values()]
    lp_best_mev = max(y0_cone) * M_E_MEV
    w.add_assertion(
        "lp_dual_shadow_price_does_not_reproduce_E0",
        computed="1" if lp_best_mev * 10 < conv_a else "0",
        expected="1",
        source=f"max over targets of y_0^* from computations/e-0-lp-dual-h3.witness.json is "
               f"{mp.nstr(max(y0_cone), 8)} (dimensionless); times m_e that is "
               f"{mp.nstr(lp_best_mev, 8)} MeV against convention A's "
               f"{mp.nstr(conv_a, 8)} MeV -- a factor of {mp.nstr(conv_a / lp_best_mev, 6)} "
               f"away. Asserting the gap exceeds 10x, i.e. that the derivation attempt "
               f"failed, which is that probe's own recorded negative finding.",
    )

    # ---- the ladder ---------------------------------------------------------
    conv_b = mp.mpf(str(lp["data"]["codata_Q_beta_MeV"]))
    lg = mp.log(1 + q ** 2)
    ladder = []
    for name, val, note in [
        ("m_e (NOT in the registry; used by my three probes)", M_E_MEV,
         "no registry entry, no operator class, no hbar_q index"),
        ("A_single_hecke_tick", conv_a,
         "hbar_q^1, H_3, 3 strands; operator Delta_NF (beta-decay single wrap)"),
        ("B_q_value_absorbed", conv_b,
         "hbar_q^0, H_3A, 3A strands; operator |tr_M(W_free)| - |tr_M(W_atom)|"),
        ("C_proton_back_fit", REGISTRY_C_APPROX_MEV,
         "DISCIPLINE VIOLATION per Workplan 0b §5 -- do not consume"),
    ]:
        coeff = STRANDS_PER_NUCLEON * lg * val
        ladder.append({
            "convention": name,
            "E_0_MeV": mp.nstr(val, 12),
            "extensive_coefficient_MeV_per_nucleon": mp.nstr(coeff, 10),
            "vs_a_V_15.8": mp.nstr(SEMF_A_V / coeff, 6) + "x short",
            "vs_B_over_A_plateau_8.5": mp.nstr(B_OVER_A_PLATEAU / coeff, 6) + "x",
            "registry_index": note,
        })

    w.add_parameter("q0", mp.nstr(q, 30))
    w.add_parameter("hbar_q", mp.nstr(hbar_q, 25))
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_data("E_0_convention_ladder", ladder)
    w.add_data("ladder_spread", {
        "registry_min_MeV": mp.nstr(conv_b, 10),
        "registry_max_MeV": mp.nstr(REGISTRY_C_APPROX_MEV, 10),
        "spread": mp.nstr(REGISTRY_C_APPROX_MEV / conv_b, 8) + "x",
        "spacing_mechanism": "powers of hbar_q; one wrong power is "
                             + mp.nstr(1 / hbar_q ** 2, 8) + "x",
        "my_error_for_comparison": mp.nstr(conv_a / M_E_MEV, 8) + "x",
    })

    # ---- A and B are (scale) and (scale x operator), not two guesses ---------
    h = q - 1 / q
    delta_net = abs(h * (h - 2) / 2)
    w.add_data("A_and_B_are_related_by_the_operator", {
        "Delta_net = |h(h-2)/2|": mp.nstr(delta_net, 12),
        "h = q - 1/q": mp.nstr(h, 12),
        "h_over_hbar_q": mp.nstr(h / hbar_q, 12) + "  (= q+1 exactly, so h is hbar_q^1)",
        "A_times_Delta_net_MeV": mp.nstr(conv_a * delta_net, 12),
        "codata_Q_beta_MeV": mp.nstr(conv_b, 12),
        "agreement": mp.nstr(
            100 * abs(conv_a * delta_net - conv_b) / conv_b, 4) + " %",
        "reading": ("A is the unit-action scale with the operator carried separately; B "
                    "absorbs the operator. Both routes give total hbar_q^2. So which "
                    "convention a quantity takes is decided by what hbar_q power the "
                    "quantity itself already carries -- not by taste."),
    })

    # ---- and that is exactly what is undetermined for log Z -----------------
    w.add_data("why_the_extensive_term_is_still_unpinned", {
        "the_quantity": "log Z(3A) = 3A log(1+q_0^2), the Markov-trace normaliser",
        "log_loop_value": mp.nstr(lg, 12),
        "its_hbar_q_content": "ZERO -- log(1+q_0^2) = " + mp.nstr(lg, 8) + " is O(1), not "
                              "small. In hbar_q units it is " + mp.nstr(lg / hbar_q, 6)
                              + ", not a clean power.",
        "its_Hecke_level": "H_3A -- which indexes to convention B",
        "its_operator_class": "NONE OF THE REGISTERED ONES. It is neither Delta_NF (A) nor "
                              "a trace DIFFERENCE (B) nor a mass assembly (C). It is the "
                              "logarithm of a partition function.",
        "consequence": ("Hecke level points at B, hbar_q content points at A, and they "
                        "differ by " + mp.nstr(conv_a / conv_b, 6) + "x. The registry does "
                        "not adjudicate, so 'the extensive term is short by N' has no "
                        "determinate N: it is 1.57, 8.38 or 12.84 depending on a choice "
                        "the corpus has not made and, per convention D, cannot derive."),
    })

    w.add_data("what_survives_because_it_is_scale_free", [
        "the A-exponent of log Z is exactly 1, the SEMF volume exponent (qou-imcd)",
        "the four counters are exactly linear: bonds A-1, averaged 2A+1, strands 3A, "
        "letters 12A-1, and letters = 4 x strands (extensive_counter_family_probe)",
        "the framing factor (1+q^2)/(q+1/q) = q exactly (qou-78pt assertion 1)",
        "b_nn/b_pp = 1.78 in the B_sym linear chain",
    ])

    w.add_data("stale_figure_noted", {
        "where": "computations/derive_e_0_lp_dual_h3.py docstring",
        "says": "y_0^* = 0.1245 for the positive-cone LP",
        "witness_records": mp.nstr(max(y0_cone), 10) + " for every target",
        "why": "the docstring predates the 2026-08-23 scipy.linprog -> clarabel-MPFR change "
               "noted in that same file",
        "impact": "none on the conclusion -- both are far from 4.186 MeV -- but the prose "
                  "figure is stale",
    })

    w.add_data("verdict", (
        "qou-59j5 ANSWERED: NO. E_0 is not derivable. derivation_chain's own registry calls "
        "convention A a 'closed-form algebraic substitution from CAL-1 m_e + CAL-2 q_0', the "
        "sole derivation attempt (convention D, LP dual) is a recorded negative finding with "
        "y_0^* m_e a factor of 21.8 from the target, and convention C is flagged a discipline "
        "violation. Moreover the problem is not the two-scale tension I described but a "
        "four-convention registry spanning 256x whose rungs are 1/hbar_q^2 = 102x apart, and "
        "log Z(3A) matches no registered operator class, so the registry cannot even select "
        "among A and B for it. STOP QUOTING MAGNITUDE DEFICITS FOR THE EXTENSIVE TERM."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  hbar_q = (q0-1)/q0                : {mp.nstr(hbar_q, 12)}")
    print(f"  1/hbar_q^2  (registry says ~102x) : {mp.nstr(1 / hbar_q ** 2, 8)}")
    print()
    print(f"  {'convention':38} {'E_0 MeV':>12} {'MeV/nucleon':>13} {'vs a_V':>10}")
    for row in ladder:
        print(f"  {row['convention'][:38]:38} {row['E_0_MeV'][:12]:>12} "
              f"{row['extensive_coefficient_MeV_per_nucleon'][:13]:>13} "
              f"{row['vs_a_V_15.8']:>10}")
    print()
    print(f"  A x |Delta(net)| = {mp.nstr(conv_a * delta_net, 10)} MeV vs CODATA Q_beta "
          f"{mp.nstr(conv_b, 10)} -- A and B differ by the OPERATOR, not by taste")
    print(f"  LP-dual attempt  : y_0* m_e = {mp.nstr(lp_best_mev, 8)} MeV, a factor "
          f"{mp.nstr(conv_a / lp_best_mev, 6)} from convention A -- DERIVATION FAILED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
