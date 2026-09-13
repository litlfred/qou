#!/usr/bin/env python3
"""One shared source for the `weight_family_note` the three Magnus Ω₂ sign
probes stamp into their witnesses (bean qou-q2q7, following qou-za3q).

WHY THIS IS A MODULE AND NOT THREE STRING LITERALS. It was three literals. All
three said the Wenzl re-weighting "leaves the sign of P_total unchanged", which
was read off the FIRST run of
`magnus_omega2_weight_family_robustness_probe.py` — a run whose triton source
witness predated the 2026-09-05 intra-nucleon ordering ruling (bean qou-hu1f).
Regenerating triton on the canonical borromean word flipped its Plancherel
P_total from -108.147 to +2.470, at which point the two weight families
disagree at A=3 and at A=4. Correcting a copy-pasted claim in three files is
how two of them stay wrong; there is now one copy, and the per-atom half of it
is computed from the run rather than asserted.

The cross-atom half IS asserted, because no single probe can measure it. Its
source is the robustness witness, which reads all three.
"""
from __future__ import annotations

#: Set by `magnus_omega2_weight_family_robustness_probe.py`, which is the only
#: thing that sees all three atoms at once. Kept here so a reader of any one
#: probe sees the cross-atom picture its own numbers cannot show.
CROSS_ATOM_FINDING = (
    "Across A = 2, 3, 4 the Plancherel arm runs -, +, + (one sign change, "
    "between deuteron and triton) and the Wenzl arm runs -, -, - (no sign "
    "change anywhere). The A-dependent sign change the programme targets is "
    "therefore exhibited by the Plancherel arm and NOT by the production "
    "Wenzl/Markov weight. Choosing the measure BECAUSE it yields the wanted "
    "sign would be fitting (AGENTS.md: selection against the target), so the "
    "honest reading is that under the production weight the sign change is "
    "not exhibited in A = 2, 3, 4. Which measure is the correct pairing for a "
    "Magnus Omega2 question is bean qou-za3q decision 1, still OPEN."
)


def weight_family_note(p_sign: int, p_wenzl_sign: int) -> str:
    """The `weight_family_note` for one atom, given its two measured signs.

    `p_sign` is the sign of the quantum-Plancherel-weighted P_total, and
    `p_wenzl_sign` that of the Wenzl-weighted P_total_wenzl, both as computed
    in THIS run. The agree/disagree clause is derived from them, so it cannot
    go stale the way the literal it replaced did.
    """
    agree = "AGREE" if p_sign == p_wenzl_sign else "DISAGREE"
    return (
        "The `y_lambda` column of `per_partition` holds the quantum Plancherel "
        "measure d_q(lambda)^2/[n]_q!, NOT the Wenzl y_lambda used by the "
        "production Markov trace. AGENTS.md forbids conflating y_lambda / "
        "w_lambda / w~_lambda, which are distinct at q != 1, and these two are "
        "not a rescaling of one another: the Wenzl weight carries the level "
        "r = 2 row cap (bean qou-fq0f) that zeroes every shape with >= 3 rows, "
        "and is a normalised Markov trace with tr(1) = 1 at every n, whereas "
        "Plancherel's tr(1) drifts from 11.1 to 6751.5 over n = 6 to 12. Both "
        "arms are computed here from the SAME per-partition tr(rho.Omega2): "
        f"P_total (Plancherel) and P_total_wenzl (headline). On this atom they "
        f"{agree} in sign. " + CROSS_ATOM_FINDING + " Measured in "
        "magnus_omega2_weight_family_robustness_probe.py; analysed in "
        "docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md."
    )
