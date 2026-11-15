#!/usr/bin/env python3
"""qbeta_d_frame_terminus_probe.py — three-place decomposition at the z = z_D
representative plus explicit 1-parameter free-y_{(1^3)} sweep (qou-vuaj).

BEAN `qou-cds1` / `qou-vuaj`.

WHAT CHANGED (qou-vuaj warrant correction).
An earlier version of this probe asserted that the two-row cap y_{(1^3)} = 0 is
DERIVED for the decay channel by `QOU/BraidsAndKnots/FibreDimensionForcesTL.lean`
and cited bean `qou-n1dj` as resolved. That cross-channel transfer was
unwarranted:

  1. `FibreDimensionForcesTL.lean` is explicitly MASS-SCOPED: its module header
     states "Read strictly as a theorem about the mass fibre... This file says
     nothing about the decay channel", grounding dim V = 2 in the two-eigenvalue
     structure of the mass operator (`lem:feynman-eigenbasis-decomposition`).
  2. Bean `qou-n1dj` is status `todo` and is likewise scoped to the mass fibre.
  3. On the decay side, `QOU/QBeta/DecayFibreBarParity.lean` proves:
       * `threeRow_undetermined_by_decay`: because chi^{(2,1)}(Delta_S) = 0 and
         chi^{(1^3)}(Delta_S) = -chi^{(3)}(Delta_S), the decay trace pairing
         depends on the Wedderburn weights ONLY through g = y_{(3)} - y_{(1^3)}.
         For EVERY prescribed g and EVERY free t = y_{(1^3)}, there is a unique
         normalised triple
           y_{(3)} = g + t,  y_{(2,1)} = (1 - g - 2t)/2,  y_{(1^3)} = t
         satisfying y_{(3)} - y_{(1^3)} = g and y_{(3)} + 2 y_{(2,1)} + y_{(1^3)} = 1.
       * `cap_member_of_family`: the two-row cap t = y_{(1^3)} = 0 is the t = 0
         representative of this 1-parameter family (selected in the decay
         channel by the Convention-D ruling z = z_D, NOT forced by the decay
         observable or by the mass-fibre theorem).

THE DECOMPOSITION. Q_beta = K * g * chi, evaluated both at the Convention-D
two-row representative z = z_D (t = y_{(1^3)} = 0) and across the 1-parameter
free-y_{(1^3)} family:

  g     the block-weight pairing g = y_{(3)} - y_{(1^3)}.
        * At the two-row representative z = z_D (t = y_{(1^3)} = 0):
          g(z_D) = y_{(3)}(z_D) = (q^4+1)/(q^2+1)^2 = 0.5054042265 against
          g_required = 0.8891258104 -- short by 1.7592369905.
        * Slice B1 (fixed y_{(2,1)} = y_{(2,1)}(z_D) = q^2/(q^2+1)^2, free
          t = y_{(1^3)} >= 0): normalisation y_{(3)} + y_{(1^3)} = g(z_D) gives
          g(t) = y_{(3)}(t) - t = g(z_D) - 2t <= g(z_D) < g_required for all
          t >= 0. Non-negative y_{(1^3)} at fixed y_{(2,1)}(z_D) moves g in the
          WRONG direction; reaching g_required along this slice requires
          negative weight t_req = (g(z_D) - g_required)/2 = -0.1918607920 < 0.
        * Slice B2 (the 1-parameter Ocneanu Markov curve y_lambda(z)):
          on the Ocneanu curve, g(z) = y_{(3)}(z) - y_{(1^3)}(z) = (2*q*z - q^2 + 1)/(q^2 + 1)
          is strictly increasing in z. Weight positivity (y_{(3)}, y_{(2,1)}, y_{(1^3)} >= 0)
          together with non-triviality (y_{(2,1)}(z) > 0, i.e. z != q) restricts z
          to (-1/q, z_D], because y_{(1^3)}(z) = q^2(z - q)(q^2 z + z - q^3)/((q^2+1)(q^4+q^2+1))
          is strictly negative on (z_D, q). At z_required = 0.9985003026 in (z_D, q),
          y_{(1^3)}(z_required) = -0.0141306962 < 0 (violating positivity). Thus on
          the entire non-negative nontrivial Ocneanu family, max g(z) = g(z_D) = 0.5054042265
          (attained at t = y_{(1^3)} = 0)!
        * Slice B3 (general central trace on the 2-simplex y_{(3)} + 2 y_{(2,1)} + y_{(1^3)} = 1,
          abandoning the Ocneanu Markov relation):
          by `threeRow_undetermined_by_decay`, g = g_required is attainable on the
          non-negative 2-simplex along y_{(3)} = g_required + t,
          y_{(2,1)} = (1 - g_required - 2t)/2, y_{(1^3)} = t for
          t in [0, (1 - g_required)/2] = [0, 0.0554370948], which requires
          abandoning BOTH z = z_D and the single-parameter Ocneanu Markov trace
          and introducing unpinned free parameters.
  chi   the decay element's block characters. Delta_S has (c, 0, -c)
        (Lean-proved: chi^(2,1)(Delta_S) = 0 exactly). At the z = z_D
        representative, reaching the required pairing via an element with
        non-zero (2,1) character would need a_(2,1)/a_(3) = 1.5516573513.
  K     the trace -> MeV scale, outside the Hecke trace entirely.

🛑 SYMBOL COLLISION — this `K` is NOT the `K(delta)` of entries 10c/12/16.
Two different objects carry the letter in this arc, and their verdicts differ:

  * THIS `K` — the trace -> MeV scale, OUTSIDE the Hecke trace entirely.
    Verdict NEGATIVE (enumerated 2026-08-29, nothing parameter-free within
    6.31 %).
  * `K(delta)` — the multiplicative constant in the N=1 factor
    `F = cos(a - delta/2) * K(delta)`, subject to `K(0) = 1`. Verdict FREE
    (entry 12: bar-parity is vacuous on it), then filtered but not determined
    (entry 16). Numerically it is ~1; this one is a MeV-scale factor.

A reader who takes "K is closed, enumerated negative" from here and applies it
to `K(delta)` closes a question that is open; one who takes "K is free" from
entry 12 and applies it here re-opens a question that is enumerated. Same class
as the `alpha_eff` overload this arc already flags, and as the `markovZ` /
`markovZC` / `markovZc` overload in AGENTS.md.


VERDICT ACROSS THE THREE LEGS.

  g   At the Convention-D representative z = z_D (t = y_{(1^3)} = 0),
      g(z_D) = 0.5054042265 vs g_required = 0.8891258104. Varying t = y_{(1^3)} >= 0
      at fixed y_{(2,1)}(z_D) strictly decreases g(t) = g(z_D) - 2t further below
      g_required; reaching g_required on the full simplex requires abandoning
      z = z_D and introducing a free parameter undetermined by the decay channel.
  chi 1.5516573513 matches no declared form. Nearest are [3]_q/[2]_q at 2.45 %
      and 3/2 at 3.33 % -- neither isolated, both basket-distance. AND SEARCHING
      FOR AN ELEMENT THAT HITS IT WOULD BE A FIT: the decay element is supposed
      to be DERIVED from the nucleon content, not selected to close a number.
      The ratio is recorded as a TARGET for a future derivation to be checked
      against, never as a criterion to search on.
  K   already enumerated by
      `qbeta_d_frame_admissible_base_correction_search_probe` (2026-08-29):
      no parameter-free object comes within 6.31 % on the tr_M base.

SO: at the Convention-D representative z = z_D (and across the fixed-y_{(2,1)}(z_D)
non-negative t = y_{(1^3)} >= 0 sweep), no parameter-free closure of the
convention-D Q_beta exists in any of the three legs. Scope-(a) -- this is an
enumeration over declared classes, not a proved impossibility.

WHAT IS NOT CLAIMED. That the framework is wrong, that D is wrong, or that no
closure exists. Only that the four correction classes already closed
(2026-08-29 corrections, Step 8 additive/cos, the z=1 wall, Step 9 block
re-weighting) are now joined by the remaining three legs at z = z_D, so the
closure is not findable by any enumeration this corpus has run.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 60

F_REQ_TRM = mp.mpf("1.75923699054610623")


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    q = q_at(55)
    y3D = (q ** 4 + 1) / (q ** 2 + 1) ** 2
    y21D = q ** 2 / (q ** 2 + 1) ** 2
    g_req = y3D * F_REQ_TRM
    check("normalisation y_3 + 2 y_21 = 1 at z_D (two-row representative t = 0)",
          abs(y3D + 2 * y21D - 1) < mp.mpf(10) ** -45)

    # Free t = y_{(1^3)} analysis (QOU.QBeta.DecayFibreBarParity):
    # Slice B1: fixed y_{(2,1)} = y21D, varying t = y_{(1^3)} >= 0.
    # Normalisation y_3(t) + 2*y21D + t = 1 => y_3(t) = y3D - t => g(t) = y3D - 2t.
    t_req_fixed_y21 = (y3D - g_req) / 2
    g_max_fixed_y21_nonneg = y3D
    g_min_fixed_y21_nonneg = -y3D
    fixed_y21_nonneg_cannot_reach = bool(
        g_max_fixed_y21_nonneg < g_req and t_req_fixed_y21 < 0
    )
    check(
        "fixed y_21(z_D) non-negative t = y_(1^3) >= 0 cannot reach g_required (g(t) = g(z_D) - 2t)",
        fixed_y21_nonneg_cannot_reach,
        f"max g(t >= 0) = {mp.nstr(g_max_fixed_y21_nonneg, 12)} < {mp.nstr(g_req, 12)}; "
        f"t_req = {mp.nstr(t_req_fixed_y21, 12)} < 0",
    )

    # Slice B2: Ocneanu 1-parameter Markov curve y_lambda(z) and full 2-simplex
    # (threeRow_undetermined_by_decay):
    t_simplex_max_at_g_req = (1 - g_req) / 2
    # On the Ocneanu curve, g(z) = y_3(z) - y_{1^3}(z) = (2*q*z - q^2 + 1)/(q^2 + 1):
    z_req_ocneanu = ((q ** 2 + 1) * g_req + q ** 2 - 1) / (2 * q)
    denom_3 = (q ** 2 + 1) * (q ** 4 + q ** 2 + 1)
    y3_zreq = (q * z_req_ocneanu + 1) * (q ** 3 * z_req_ocneanu + q * z_req_ocneanu + 1) / denom_3
    y21_zreq = q * (q - z_req_ocneanu) * (q * z_req_ocneanu + 1) / (q ** 4 + q ** 2 + 1)
    y111_zreq = q ** 2 * (z_req_ocneanu - q) * (q ** 2 * z_req_ocneanu + z_req_ocneanu - q ** 3) / denom_3
    check(
        "Ocneanu z_required reproduces g_required = y_3(z_req) - y_(1^3)(z_req) but has y_(1^3)(z_req) < 0",
        abs((y3_zreq - y111_zreq) - g_req) < mp.mpf(10) ** -45
        and abs((y3_zreq + 2 * y21_zreq + y111_zreq) - 1) < mp.mpf(10) ** -45
        and y111_zreq < 0
        and t_simplex_max_at_g_req > 0,
        f"z_req = {mp.nstr(z_req_ocneanu, 12)}, y_(1^3)(z_req) = {mp.nstr(y111_zreq, 12)} < 0; "
        f"2-simplex t in [0, {mp.nstr(t_simplex_max_at_g_req, 12)}]",
    )

    sweep_grid_fixed_y21 = []
    for frac in ("0", "0.05", "0.10", "0.25", "0.50", "1.0"):
        t_val = mp.mpf(frac) * y3D
        y3_val = y3D - t_val
        g_val = y3_val - t_val
        sweep_grid_fixed_y21.append({
            "t_over_y3_zD": frac,
            "t_y111": mp.nstr(t_val, 20),
            "y_3": mp.nstr(y3_val, 20),
            "y_21": mp.nstr(y21D, 20),
            "g_pairing": mp.nstr(g_val, 20),
            "shortfall_vs_g_required": mp.nstr(g_req / g_val, 15) if g_val != 0 else "inf",
        })

    a21_over_c = (g_req - y3D) / y21D
    print(f"\n[1] the three legs (and free-y_(1^3) sweep, qou-vuaj)")
    print(f"    g   = y_(3)(z_D)      = {mp.nstr(y3D, 14)}   (t = y_(1^3) = 0 representative at z = z_D)")
    print(f"          required          {mp.nstr(g_req, 14)}   short by "
          f"{mp.nstr(F_REQ_TRM, 10)}")
    print(f"          fixed-y_21(z_D)   g(t) = g(z_D) - 2t <= {mp.nstr(y3D, 14)} for all t >= 0 "
          f"(t_req = {mp.nstr(t_req_fixed_y21, 10)} < 0)")
    print(f"          full-simplex      g = g_req on t in [0, {mp.nstr(t_simplex_max_at_g_req, 10)}] "
          f"(abandons z = z_D; Ocneanu z_req = {mp.nstr(z_req_ocneanu, 10)})")
    print(f"    chi = a_(2,1)/a_(3)   = {mp.nstr(a21_over_c, 14)}   would be needed at z_D")
    print(f"    K   = trace -> MeV    enumerated 2026-08-29: nothing within 6.31 %")

    # DECLARED before evaluating, and the point is that none of them lands
    CANDS = {
        "[2]_q": q + 1 / q,
        "[3]_q": q ** 2 + 1 + 1 / q ** 2,
        "[3]_q/[2]_q": (q ** 2 + 1 + 1 / q ** 2) / (q + 1 / q),
        "h = q - 1/q": q - 1 / q,
        "1/z_D": (q ** 2 + 1) / q ** 3,
        "q^2": q ** 2,
        "3/2": mp.mpf(3) / 2,
        "2 - 1/q": 2 - 1 / q,
        "[2]_q - h/2": q + 1 / q - (q - 1 / q) / 2,
    }
    ranked = sorted(((abs(v - a21_over_c) / a21_over_c, k, v) for k, v in CANDS.items()))
    print(f"\n[2] nearest DECLARED forms to the needed character ratio")
    for rel, k, v in ranked[:4]:
        print(f"    {k:<14} {mp.nstr(v, 12):>16}   rel {mp.nstr(rel * 100, 5)} %")
    best, second = ranked[0], ranked[1]
    isolated = second[0] > 10 * best[0]
    check("the needed character ratio matches NO declared form (not isolated)",
          not (isolated and best[0] < mp.mpf("1e-3")),
          f"nearest {best[1]} at {mp.nstr(best[0] * 100, 4)} %, "
          f"next {second[1]} at {mp.nstr(second[0] * 100, 4)} % -> isolated={isolated}")

    verdict = (
        "SCOPE-(a) TERMINUS (conditional on the Convention-D z = z_D representative, "
        "plus explicit 1-parameter free-y_{(1^3)} sweep per qou-vuaj). "
        "Warrant correction: QOU/BraidsAndKnots/FibreDimensionForcesTL.lean is "
        "explicitly mass-scoped (lem:feynman-eigenbasis-decomposition) and bean "
        "qou-n1dj is todo; on the decay side, "
        "QOU.QBeta.DecayFibreBarParity.threeRow_undetermined_by_decay proves the "
        "decay trace pairing depends on the weights only through g = y_{(3)} - y_{(1^3)}, "
        "leaving t = y_{(1^3)} undetermined by the decay channel alone, with "
        "t = 0 (`cap_member_of_family`) the two-row representative selected by the "
        "Convention-D ruling z = z_D. "
        "At the z = z_D (t = 0) representative, g(z_D) = 0.5054042265 against a "
        "required 0.8891258104. Across the 1-parameter family at fixed y_{(2,1)}(z_D), "
        "g(t) = g(z_D) - 2t <= 0.5054042265 for all t = y_{(1^3)} >= 0, so non-negative "
        "3-row weight moves g in the wrong direction (reaching g_required at fixed "
        "y_{(2,1)}(z_D) would require negative weight t = -0.1918607920). On the "
        "1-parameter Ocneanu Markov curve y_lambda(z), reaching g_required requires "
        "z_required = 0.9985003026 in (z_D, q), where y_{(1^3)}(z_required) = -0.0141306962 < 0 "
        "(violating weight positivity); across the entire non-negative nontrivial Ocneanu "
        "region z in (-1/q, z_D] where y_{(1^3)}(z) >= 0, g(z) <= g(z_D) = 0.5054042265. "
        "Only by abandoning both z = z_D and the Ocneanu Markov relation for the general "
        "2-simplex y_{(3)} = g_required + t, y_{(2,1)} = (1 - g_required - 2t)/2, "
        "y_{(1^3)} = t with t in [0, 0.0554370948] is g_required reachable with "
        "non-negative weights, at the cost of unpinned free parameters. "
        "The other two legs at z = z_D remain measured-negative: the character ratio "
        "an element would need, 1.5516573513, matches no declared form (nearest "
        "[3]_q/[2]_q at 2.45 %, next 3/2 at 3.33 % -- basket distance, not isolation), "
        "and the trace->MeV scale was enumerated on 2026-08-29 with nothing within "
        "6.31 %. NOT a proved impossibility: this is an enumeration over declared "
        "classes, and a DERIVED (not searched) decay element with the right character "
        "ratio would still close it.")
    print(f"\n[3] {verdict}")

    wb = WitnessBuilder("qbeta-d-frame-terminus", engine="mpmath")
    wb.set_description(
        "Three-place decomposition of the missing convention-D Q_beta factor at the "
        "z = z_D two-row representative (y_{(1^3)} = 0) together with the qou-vuaj "
        "warrant correction (citing QOU.QBeta.DecayFibreBarParity.threeRow_undetermined_by_decay "
        "and cap_member_of_family rather than the mass-scoped FibreDimensionForcesTL.lean) "
        "and an explicit 1-parameter sweep over free t = y_{(1^3)}. Records the needed "
        "character ratio as a target for a future DERIVATION, explicitly not as a "
        "search criterion.")
    wb.add_data("g_forced", mp.nstr(y3D, 20))
    wb.add_data("g_required", mp.nstr(g_req, 20))
    wb.add_data("shortfall_factor", mp.nstr(F_REQ_TRM, 20))
    wb.add_data("needed_character_ratio_a21_over_a3", mp.nstr(a21_over_c, 20))
    wb.add_data("nearest_declared", {k: mp.nstr(rel * 100, 6) for rel, k, _ in ranked[:5]})
    wb.add_data("warrant_correction_qou_vuaj", {
        "mass_channel_theorem": "QOU/BraidsAndKnots/FibreDimensionForcesTL.lean",
        "mass_channel_scope": (
            "Explicitly mass-scoped via lem:feynman-eigenbasis-decomposition "
            "(2-eigenvalue mass operator => dim V_mass = 2 => Lambda^3_q V_mass = 0). "
            "Does NOT prove dim V_decay = 2 or force y_{(1^3)} = 0 in the decay channel; "
            "bean qou-n1dj is status todo."
        ),
        "decay_channel_theorem": (
            "QOU.QBeta.DecayFibreBarParity.threeRow_undetermined_by_decay + "
            "QOU.QBeta.DecayFibreBarParity.cap_member_of_family"
        ),
        "decay_channel_scope": (
            "Because chi^{(2,1)}(Delta_S) = 0 and chi^{(1^3)}(Delta_S) = -chi^{(3)}(Delta_S), "
            "the decay trace pairing depends on the weights only through g = y_{(3)} - y_{(1^3)}. "
            "Setting t = y_{(1^3)} = 0 (`cap_member_of_family`) is the two-row representative "
            "selected by the Convention-D ruling z = z_D, not forced by the decay observable."
        ),
    })
    wb.add_data("free_y111_family_analysis", {
        "parameter": "t = y_{(1^3)}",
        "lean_warrant": "QOU.QBeta.DecayFibreBarParity.threeRow_undetermined_by_decay",
        "slice_B1_fixed_y21_at_zD": {
            "y_21_fixed": mp.nstr(y21D, 20),
            "formula": "y_{(3)}(t) = g(z_D) - t, g(t) = y_{(3)}(t) - t = g(z_D) - 2t",
            "admissible_nonneg_t_interval": ["0", mp.nstr(y3D, 20)],
            "g_range_on_nonneg_t": [mp.nstr(g_min_fixed_y21_nonneg, 20), mp.nstr(g_max_fixed_y21_nonneg, 20)],
            "t_required_for_g_required": mp.nstr(t_req_fixed_y21, 20),
            "nonneg_t_reaches_g_required": not fixed_y21_nonneg_cannot_reach,
            "conclusion": (
                "At fixed y_{(2,1)}(z_D), increasing t = y_{(1^3)} >= 0 strictly decreases "
                "g(t) = g(z_D) - 2t away from g_required; reaching g_required requires "
                "t = -0.19186079197006352147 < 0 (violating positivity)."
            ),
            "sweep_grid": sweep_grid_fixed_y21,
        },
        "slice_B2_full_simplex_abandoning_zD": {
            "formula": "y_{(3)} = g + t, y_{(2,1)} = (1 - g - 2t)/2, y_{(1^3)} = t",
            "t_interval_for_g_required_on_simplex": ["0", mp.nstr(t_simplex_max_at_g_req, 20)],
            "ocneanu_z_required": mp.nstr(z_req_ocneanu, 20),
            "ocneanu_weights_at_z_required": {
                "y_3": mp.nstr(y3_zreq, 20),
                "y_21": mp.nstr(y21_zreq, 20),
                "y_111": mp.nstr(y111_zreq, 20),
            },
            "conclusion": (
                "On the 1-parameter Ocneanu Markov curve, reaching g = g_required requires "
                "z_required = 0.998500302563 in (z_D, q), where y_{(1^3)}(z_required) = -0.0141306962 < 0 "
                "(violating weight positivity); across the entire non-negative nontrivial "
                "Ocneanu region z in (-1/q, z_D] where y_{(1^3)}(z) >= 0, g(z) <= g(z_D) = 0.5054042265. "
                "Reaching g = g_required with non-negative weights requires abandoning both "
                "z = z_D and the Ocneanu Markov trace relation for the general 2-simplex "
                "segment t in [0, 0.0554370948], which introduces unpinned free parameters."
            ),
        },
    })
    wb.add_data("legs", {
        "g (block weights)": (
            "REPRESENTATIVE-PINNED AT z_D (g(z_D) = 0.5054042265 at t = y_{(1^3)} = 0; "
            "at fixed y_{(2,1)}(z_D), free t >= 0 gives g(t) = g(z_D) - 2t <= g(z_D); "
            "reaching g_required = 0.8891258104 requires abandoning z = z_D)"
        ),
        "chi (element characters)": "NEGATIVE — needed ratio matches no declared form",
        "K (trace->MeV scale)": "NEGATIVE — enumerated 2026-08-29, nothing within 6.31%",
    })
    wb.add_data("not_claimed",
                "that the framework or convention D is wrong, or that no closure "
                "exists; only that none is findable by any enumeration this corpus "
                "has run")
    wb.add_data("free_parameters", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) enumeration over declared classes, NOT a proved impossibility")
    wb.add_data("q0Anchor", "proton")
    wb.add_data("q0Value", mp.nstr(q, 50))
    for c in checks:
        wb.add_assertion(c["name"],
                         computed=mp.mpf(1) if c["passed"] else mp.mpf(0),
                         expected=mp.mpf(1), tolerance=mp.mpf("0.5"), unit="bool")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
