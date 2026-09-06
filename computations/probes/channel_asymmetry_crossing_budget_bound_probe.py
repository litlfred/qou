#!/usr/bin/env python3
"""The two-nucleon channel asymmetry is capped by the CROSSING BUDGET, and the
budget is forced to 9 by the 3-strands-per-nucleon layout.

STATUS: class bound (scope-(b) CONDITIONAL on two cited facts, stated below as
H1/H2 -- neither is derived here).  No fit, no search, no selection.  Exact
integer arithmetic for the budget; mpmath only for the reported target ratio.

-----------------------------------------------------------------------------
WHY THIS EXISTS

Bean `qou-brng`, arc `bk-crossing-mass-binding`.  Nature's two-nucleon binding
channel asymmetry is

    R_nature = B(3S1, T=0) / B(1S0, T=1) = 2.224566 / 0.066 = 33.7055

Four routes to it have closed, each excluding ONE object:

  * `isospin_channel_R_is_one_everywhere_probe` -- a single crossing gives
    R = 1 EXACTLY in every rep at every dimension (minimal polynomial:
    spec(rho(sigma)) subset {q, -1/q}).
  * `block_transposition_lift_probe` -- the 9-crossing block transposition
    Delta_{3,3} gives a discrete asymmetry set with ceiling 9.  Its own words:
    "over all 11 blocks of H_6, for THIS operator, the ceiling is 9."
  * `markov_trace_family_rank_probe` / `ocneanuFamily_finrank_le` -- the
    Ocneanu/Markov trace family has rank n, so trace subtraction cannot
    isolate a Wedderburn block.
  * `two_nucleon_linking_matrix_channel_blind_probe` -- the linking class is
    I_3-valued hence channel-blind (scope-(b)).

Those are four point-exclusions and a stated residue.  What none of them does
is BOUND THE CLASS: the ceiling 9 was scoped to Delta_{3,3} specifically.  This
probe asks the class question -- what is the largest asymmetry ANY braid
carrier on the physical strand layout can produce? -- and finds that 9 is not
an accident of that operator but the forced budget.

-----------------------------------------------------------------------------
THE TWO CITED FACTS (H1, H2 -- neither derived here)

(H1) QUANTISATION WITH A CROSSING CAP.  In the seminormal reps of H_n(q), the
     log-modulus of every eigenvalue of a braid word `w` is an integer multiple
     of log q,

         log|lambda| = k * log q,      k in Z,     |k| <= c(w)

     where `c(w)` is the crossing count of `w`, and the extremes are ATTAINED.
     Measured in `block_transposition_lift_probe`: k integral to 1.8e-22 at
     90 dps, and its line 148 -- "a 9-crossing word must give k = +9 and
     k = -9.  Both hit exactly."  The cap direction is elementary: each
     generator contributes one factor of modulus q^{+-1}, so a c-crossing word
     cannot exceed q^{+-c}.

(H2) THE STRAND LAYOUT IS FORCED.  Each nucleon carries exactly s = 3 strands.
     This is not chosen: `QOU.Mass.StrandLayoutForcesChain` / bean `qou-gwr9`
     ("The chain bond set is FORCED by the 3-strands-per-nucleon layout, not
     chosen").

-----------------------------------------------------------------------------
THE ARGUMENT (three lines, given H1/H2)

A two-nucleon channel operator is an exchange of the two nucleon blocks.  With
s strands per nucleon, exchanging the blocks crosses each strand of one nucleon
past each strand of the other EXACTLY ONCE:

    c_inter = s * s = 9          (s = 3 by H2; this IS Delta_{3,3})

By H1 the channel log-moduli are k_T * log q with |k_T| <= c_inter, and a
non-degenerate channel has |k| >= 1.  Hence

    R = |k_0 / k_1| <= c_inter / 1 = 9

so the achievable asymmetry is capped at the crossing budget.  Nature needs
33.7055 > 9.  Inverting: reaching R_nature needs c >= ceil(33.7055) = 34
inter-nucleon crossings, i.e. s >= ceil(sqrt(34)) = 6 strands per nucleon --
contradicting the forced s = 3.

This EXPLAINS the ceiling 9 rather than merely recording it: 9 is s^2, not a
property of one operator.

-----------------------------------------------------------------------------
SCOPE -- what this does and does NOT exclude

EXCLUDES (scope-(b), given H1+H2): any SINGLE block-exchange braid carrier on
the forced 3-strand layout, in every representation and dimension.  The four
prior point-exclusions become corollaries of one budget.

Does NOT exclude:
  * REPEATED exchanges.  Delta^m has c = 9m and would lift the cap.  The
    physical carrier is the MINIMAL braid representing the two-nucleon link
    (owner ruling 2026-08-29: canonical braid closure), so m = 1; if a
    derivation ever justifies m >= 4, this bound does not apply to it.  Stated
    as a limitation, not waved away.
  * NON-braid carriers.  A channel object that is not a braid word in the
    nucleon strands is untouched by H1.
  * Any claim that the binding gap is closed.  It is not.

NO FIT: nothing is tuned.  s, c and the k-cap are integers; R_nature is an
experimental input used only for comparison, never to select anything.

-- Ref: probes/block_transposition_lift_probe.py (H1, ceiling 9, k integrality);
probes/isospin_channel_R_is_one_everywhere_probe.py (R=1 for a single crossing);
QOU/Mass/StrandLayoutForcesChain.lean + bean qou-gwr9 (H2, s=3 forced);
probes/two_nucleon_linking_matrix_channel_blind_probe.py (linking class dead);
docs/audits/2026-09-03-two-mubars-selector-vs-magnitude.md (the stated residue).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

set_compute_dps()

# Experimental comparison point (input only; never used to select anything).
B_DEUTERON_MEV = AME_B_DEUTERON_MEV_VALIDATION     # 3S1, T=0, bound
B_NP_1S0_MEV = mp.mpf("0.066")          # 1S0, T=1, virtual state

STRANDS_PER_NUCLEON = 3                 # H2: forced (qou-gwr9)


def main() -> int:
    t0 = time.monotonic()

    s = STRANDS_PER_NUCLEON
    c_inter = s * s                      # each strand of A crosses each of B once
    k_min_nondegenerate = 1              # a channel with k = 0 has |lambda| = 1
    r_max = mp.mpf(c_inter) / k_min_nondegenerate

    r_nature = B_DEUTERON_MEV / B_NP_1S0_MEV
    excluded = r_nature > r_max

    # Inversion: what budget / layout would be required?
    c_required = int(mp.ceil(r_nature))
    s_required = int(mp.ceil(mp.sqrt(mp.mpf(c_required))))

    verdict = (
        f"CAPPED. With s={s} strands per nucleon (H2, forced), a single "
        f"two-nucleon block exchange has c={c_inter} inter-nucleon crossings "
        f"(=s^2, which IS Delta_{{{s},{s}}}). By H1 the channel log-moduli are "
        f"k*log q with |k|<=c, so the achievable asymmetry is R<={int(r_max)}. "
        f"Nature needs R={mp.nstr(r_nature, 6)}, so the single-block-exchange "
        f"braid class is EXCLUDED (scope-(b), given H1+H2). Reaching R_nature "
        f"would need c>={c_required} inter-nucleon crossings, i.e. s>={s_required} "
        f"strands per nucleon, contradicting the forced s={s}. This EXPLAINS the "
        f"ceiling 9 reported for Delta_{{3,3}}: 9 is s^2, not a property of that "
        f"one operator. Does NOT exclude repeated exchanges (Delta^m, c=9m; the "
        f"minimal carrier is m=1 by the 2026-08-29 owner ruling) or non-braid "
        f"carriers. Does NOT close the binding gap."
    )

    result = {
        "hypotheses_cited_not_derived": {
            "H1": "log|lambda| = k*log q, k integer, |k| <= c(w), extremes attained "
                  "(block_transposition_lift_probe; k integral to 1.8e-22 at 90 dps)",
            "H2": "s = 3 strands per nucleon is FORCED (StrandLayoutForcesChain / qou-gwr9)",
        },
        "budget": {
            "strands_per_nucleon_s": s,
            "inter_nucleon_crossings_c": c_inter,
            "identification": "c = s^2 = Delta_{3,3}, the block transposition",
            "k_min_nondegenerate": k_min_nondegenerate,
            "R_max_achievable": int(r_max),
        },
        "comparison": {
            "B_3S1_T0_MeV": mp.nstr(B_DEUTERON_MEV, 7),
            "B_1S0_T1_MeV": mp.nstr(B_NP_1S0_MEV, 4),
            "R_nature": mp.nstr(r_nature, 8),
            "excluded": bool(excluded),
            "margin_factor": mp.nstr(r_nature / r_max, 5),
        },
        "inversion": {
            "crossings_required": c_required,
            "strands_per_nucleon_required": s_required,
            "contradicts_forced_layout": bool(s_required > s),
        },
        "verdict": verdict,
    }
    payload = {
        "computation": "channel-asymmetry-crossing-budget-bound",
        "description": ("Class bound on the two-nucleon channel asymmetry: the "
                        "crossing budget c = s^2 = 9 forced by the 3-strand layout "
                        "caps R <= 9 against nature's 33.7, lifting the per-operator "
                        "ceiling-9 to the whole single-block-exchange braid class. "
                        "Audit-only; conditional on cited H1/H2; no fit."),
        "tier": "exploratory (class bound; scope-(b) given H1+H2)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "channel-asymmetry-crossing-budget-bound", payload,
        script_path=__file__, engine="python+mpmath",
        engine_version=f"python {platform.python_version()} + mpmath {mp.__version__}",
        output_dir=str(_HERE), start_time=t0,
    )
    # This compared `str(c_inter)` to `str(s * s)` while `c_inter = s * s` is
    # its own definition four lines up — a tautology, not a check (bean
    # `qou-t0wm`). Pinned to the literal instead, matching how the sibling
    # assertion below writes `expected="9"`.
    #
    # BE CLEAR ABOUT WHAT CARRIES THE FALSIFIABILITY: it is the PIN, not the
    # enumeration. `len(_inter_pairs)` is s^2 by construction and is here only
    # to exercise the pair-set the budget is a count OF. What can actually
    # fail is `STRANDS_PER_NUCLEON` moving off the value H2 forces (qou-gwr9)
    # without this bound being revisited — which is the regression that
    # matters, since every conclusion below rides on c_inter = 9.
    _inter_pairs = [(_i, _j) for _i in range(s) for _j in range(s)]
    wb.add_assertion("budget_is_s_squared",
                     computed=str(len(_inter_pairs)), expected="9",
                     source="s = STRANDS_PER_NUCLEON = 3, forced by H2 "
                            "(qou-gwr9); budget = s^2 = Delta_{3,3}")
    wb.add_assertion("ceiling_matches_reported_delta33_ceiling",
                     computed=str(int(r_max)), expected="9")
    wb.add_assertion("nature_exceeds_budget",
                     computed=str(bool(excluded)), expected="True")
    wb.add_assertion("required_layout_contradicts_forced",
                     computed=str(s_required > s), expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== channel asymmetry: the crossing-budget class bound ===")
    print(f"  s = {s} strands/nucleon (FORCED, H2)")
    print(f"  c_inter = s^2 = {c_inter}   -> this IS Delta_{{{s},{s}}}")
    print(f"  R_max  = c/1 = {int(r_max)}")
    print(f"  R_nature = {mp.nstr(r_nature, 8)}   ({mp.nstr(r_nature/r_max,4)}x over budget)")
    print(f"  to reach nature: c >= {c_required}  =>  s >= {s_required}  "
          f"(contradicts forced s={s})")
    print("  " + verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
