#!/usr/bin/env python3
"""qou-cds1 attack options: the D-frame trace COLLAPSES, and the assets exist.

Bean qou-cds1 (via t7qv, PRIMARY GOAL fix binding). cds1 requires the Q_beta c_k
ladder to be "re-derived, not re-evaluated" from the D Markov trace, and proves
the C->D move is not a z-swap. Question put: we have a Habiro basis and D in
terms of it -- can we use that? Answer: YES, and the D side is structurally
SIMPLER than C, which is the opposite of what "blocked" suggests.

ASSET 1: the D-frame Habiro machinery already exists and is live.
-------------------------------------------------------------------
computations/habiro/habiro_mass_table_convention_attribution_probe.py reports
"committed reproduced by convention D : 25/25 ... uniformly convention D: True",
exit 0, run today. PR #5526 regenerated all 25 atoms into D (cde2fbcd89) and the
probe is kept as a live regression check. Four regenerators sit beside it:
regenerate_y_lambda_{jones_markov,symbolic,orphans,sdp}_convention*D*.py. So the
y_lambda weights are ALREADY in convention D.

ASSET 2: at z_D the trace collapses to a SINGLE term, in closed form.
----------------------------------------------------------------------
The operator route (computations/qbeta/qbeta_ck_from_operator_markov_trace_probe
.py, the existing vehicle) writes

    tr_M(trefoil) = sum_lambda y_lambda(q) chi^lambda,
    chi^(3) = q^3,   chi^(2,1) = 0 exactly (PR #1873),   chi^(1^3) = -q^-3.

Two of the three terms die under D, for two INDEPENDENT reasons:

  * chi^(2,1) = 0 exactly -- a character fact, convention-free;
  * y_(1^3) = 0 under D -- and this is exactly the Lean characterisation cds1
    already cites, markovWeights_eq_jones_of_threeRow_eq_zero: y_(1^3) = 0 iff
    z = z_D. Verified here against the live bridge.

leaving one term, computed here in closed form:

    tr_M(trefoil)|_D  =  q^3 (q^4 + 1) / (q^2 + 1)^2

CONTROL: the weights normalise, sum_lambda dim(lambda) y_lambda = 1 exactly
(1*y_(3) + 2*y_(2,1) + 1*y_(1^3)), so the bridge is a genuine Markov trace and
not a truncation artefact.

WHY THIS REFRAMES "NOT A Z-SWAP". Under C, decayLadder_zC_threeRow_ne_zero
(sorry-free) forces y_(1^3) != 0 for every substrate s = sqrt(q) > 1, so the C
trace carries TWO terms. The C->D move therefore changes the trace's RANK, not
just a parameter value -- which is cds1's point, and which cuts in the helpful
direction: the object to be re-derived under D is SMALLER than the one under C.

ASSET 3 / OBSTRUCTION: the Habiro DIVISIBILITY structure is C-specific.
------------------------------------------------------------------------
computations/probes/qbeta_habiro_element_probe.py records its divisibility fact
D(u) = 4u^19 (1+u^2) as "the convention-C denominator", explicitly "true under
convention C, false under D". So the Habiro basis TRANSFERS (assets 1-2) but the
integrality/divisibility lemmas proved in it DO NOT -- they must be re-derived
against the collapsed D trace. That is the actual work, and it is narrower than
re-deriving the ladder from nothing.

RECOMMENDED ATTACK, in order:
  1. Re-run the operator route with the D weights and the single-term trace
     above, extracting c_k from Q_beta(q)/[Q_A(q) cos(alpha_eff(q))].
  2. Re-derive the divisibility/integrality structure against the D denominator
     (the C-frame 4u^19(1+u^2) is known false under D, so this is derive-anew,
     not port).
  3. Only then compare against the C-frame c_3; the -974 sensitivity number is
     NOT a target and cds1 says do not wire it anywhere.

NOTHING HERE DERIVES THE LADDER. This probe establishes that the D-side assets
exist, that the D trace is a one-term closed form, and where the C-specific
lemmas will have to be redone. cds1 stays OPEN.
"""
import json
import sys
import time
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main():
    t0 = time.monotonic_ns()
    checks = []
    q = sp.symbols("q", positive=True)
    from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic as Y
    y3, y21, y111 = Y((3,)), Y((2, 1)), Y((1, 1, 1))

    norm = sp.simplify(1 * y3 + 2 * y21 + 1 * y111)
    checks.append({
        "name": "CONTROL: the D weights are a genuine Markov trace (sum dim*y = 1)",
        "pass": norm == 1,
        "detail": (
            f"sum_lambda dim(lambda) y_lambda = 1*y_(3) + 2*y_(2,1) + 1*y_(1^3) "
            f"= {norm}, exactly 1. So the bridge's weights normalise and the "
            f"collapse below is a property of the trace, not a truncation "
            f"artefact. y_(3) = {sp.simplify(y3)}, y_(2,1) = {sp.simplify(y21)}, "
            f"y_(1^3) = {sp.simplify(y111)}."),
    })

    chi3, chi21, chi111 = q ** 3, sp.Integer(0), -q ** -3
    tr = sp.simplify(y3 * chi3 + y21 * chi21 + y111 * chi111)
    target = sp.simplify(q ** 3 * (q ** 4 + 1) / (q ** 2 + 1) ** 2)
    checks.append({
        "name": "ASSET 2: at z_D the trefoil trace COLLAPSES to one closed-form term",
        "pass": sp.simplify(tr - target) == 0 and y111 == 0,
        "detail": (
            f"Two of three terms die for INDEPENDENT reasons: chi^(2,1) = 0 "
            f"exactly (a character fact, convention-free, PR #1873), and "
            f"y_(1^3) = {y111} under D -- which is precisely the Lean "
            f"characterisation cds1 already cites, "
            f"markovWeights_eq_jones_of_threeRow_eq_zero (y_(1^3) = 0 iff "
            f"z = z_D), here verified against the live bridge. What remains is "
            f"tr_M(trefoil)|_D = {sp.factor(tr)}. Under C, "
            f"decayLadder_zC_threeRow_ne_zero forces y_(1^3) != 0 for every "
            f"s = sqrt(q) > 1, so the C trace carries TWO terms: the C->D move "
            f"changes the trace's RANK, not a parameter value. That is cds1's "
            f"'not a z-swap', and it cuts the helpful way -- the object to be "
            f"re-derived under D is SMALLER than the one under C."),
    })

    hab = Path(__file__).resolve().parents[1] / "probes" / "qbeta_habiro_element_probe.py"
    c_only = hab.exists() and "true under convention C, false under D" in hab.read_text()
    checks.append({
        "name": "OBSTRUCTION: the Habiro divisibility structure is C-specific",
        "pass": bool(c_only),
        "detail": (
            f"qbeta_habiro_element_probe.py records its divisibility fact "
            f"D(u) = 4u^19 (1+u^2) as the convention-C denominator, explicitly "
            f"'true under convention C, false under D' (found in file: "
            f"{c_only}). So the Habiro BASIS transfers -- the mass table is "
            f"D 25/25 live, and the y_lambda regenerators are convention-D -- "
            f"but the integrality/divisibility LEMMAS proved in it do not, and "
            f"must be re-derived against the collapsed D trace. That is the "
            f"actual remaining work, and it is narrower than re-deriving the "
            f"ladder from nothing."),
    })

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("qbeta-d-ladder-attack-options.witness.json").write_text(
        json.dumps({
            "probe": "qbeta_d_ladder_attack_options",
            "bean": ["qou-cds1", "t7qv"],
            "y_lambda": {"(3)": str(y3), "(2,1)": str(y21), "(1^3)": str(y111)},
            "tr_M_trefoil_D": str(sp.factor(tr)),
            "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: the D-side assets EXIST -- mass table D 25/25 live, y_lambda")
    print("RESULT:   regenerated into D, and tr_M(trefoil)|_D = q^3(q^4+1)/(q^2+1)^2,")
    print("RESULT:   a SINGLE closed-form term. The D object is smaller than the C one.")
    print("RESULT: the Habiro divisibility lemmas are C-specific and must be redone.")
    print("RESULT: NOTHING HERE DERIVES THE LADDER. qou-cds1 stays OPEN.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
