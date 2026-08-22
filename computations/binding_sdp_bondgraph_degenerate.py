#!/usr/bin/env python3
"""
binding_sdp_bondgraph_degenerate.py — the SDP-active-set route to the bond graph
is DEGENERATE (live-confirmed): neither the ad-hoc chain nor the SDP derives it.

Owner steer (2026-07-11): "k < A−1 should not be case by case" → derive the bond
graph from the confinement / operator-selection SDP dual active set instead.

Tested: the canonical H₃ operator-selection LP-dual (NF basis {γ,σ₀,σ₁,L₊,L₋,e⁻},
Frobenius Gram G_ij, costs t_i = tr_M(b_i), various demands). RESULT — degenerate
at every target: y0* = 0, active_set = {γ} (identity only). Structural reason
(corpus-established, he3_pairknot_composite_lp_probe.py + audit
2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md): a free / single nucleon
has W_free = W_atom, so there is NO binding constraint to select against; the pair
(H₆) LP is intractable / also degenerate. So a direct operator-selection LP-dual
does NOT isolate a bond graph at any tractable level.

Conclusion (honest, both routes fail):
  • ad-hoc chain (`k < A−1`, atom_braid_word_3A): a placeholder, undercounts
    coordination (Part 8);
  • SDP-active-set: DEGENERATE (this probe).
⇒ the bond graph M_n(K) (coordination / which pairs bond) is a genuine OPEN
  GEOMETRIC input — it needs a categorical / geometric coordination construction
  (the owner-gated s5-so3 keystone territory), not an LP. What IS derivable is the
  per-bond-TYPE strength L_pp/L_pn/L_nn = log(tr_M^full/tr_M^atom) (bond traces)
  and the Milnor M_n of a GIVEN graph (Part 7) — not the graph itself.

EXPLORATORY — no production wiring, no fitted constant, no tier change.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md §Part 9
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "pyhecke" / "python"))


def main() -> int:
    print("=== SDP-active-set bond graph: DEGENERACY test (H₃ operator-selection LP-dual) ===\n")
    try:
        import numpy as np
        from pyhecke import gram as G
        from lp_dual_solver import solve_operator_selection_lp
    except Exception as e:
        print(f"(pyhecke/LP unavailable: {e}) — verdict from corpus (he3 probe + 2026-06-18 audit): DEGENERATE.")
        return 0

    t = np.array(G.TR_M, dtype=float)
    Gm = np.array(G.G, dtype=float)
    print(f"NF basis: {G.NF_NAMES}")
    print(f"t_i = tr_M(b_i): {np.round(t, 4).tolist()}\n")
    all_deg = True
    # The full dual is kept, not just the verdict. It used to be computed here
    # and discarded: the witness recorded `sdp_bondgraph_degenerate = 1` and
    # none of the numbers behind it, which is the case
    # `lp_dual_witness_validator.py` exists for — "solves the primal but never
    # reports the dual, losing the principled binding-energy interpretation".
    # For a witness whose whole claim IS about the duals, that left the claim
    # unauditable. Bean `qou/augu`.
    duals = []
    for lbl, ntar in [("|tr_M(proton)|≈0.66", 0.6614), ("identity 1.0", 1.0),
                      ("Σ t_i", float(t.sum()))]:
        r = solve_operator_selection_lp(t, Gm, ntar).to_dict()
        deg = abs(r["y0_star"]) < 1e-9 or len(r["active_set"]) <= 1
        all_deg &= deg
        duals.append({"n_target_label": lbl, "n_target": repr(float(ntar)),
                      "degenerate": bool(deg), **r})
        print(f"  n_target={lbl:<20} y0*={r['y0_star']:+.6f}  active_set={r['active_set']}  "
              f"{'DEGENERATE' if deg else 'non-degen'}")

    print(f"\nVERDICT: {'DEGENERATE at every target' if all_deg else 'NON-degenerate (unexpected!)'}.")
    print("  A free/single nucleon has W_free=W_atom ⇒ no binding constraint ⇒ empty active set.")
    print("  Neither the ad-hoc chain (k<A−1) nor the SDP-active-set derives the bond graph.")
    print("  ⇒ the coordination/topology M_n(K) is an OPEN GEOMETRIC input (s5-so3 keystone),")
    print("     not an LP output. Derivable: per-bond-type strength (tr_M ratios) + Milnor M_n")
    print("     of a GIVEN graph — not the graph itself.")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("binding-sdp-bondgraph-degenerate", engine="scipy-lp")
        wb.set_description(
            "EXPLORATORY: the SDP-active-set route to the nuclear bond graph is degenerate "
            "(H₃ operator-selection LP-dual: y0*=0, only identity active, at every demand). "
            "A free nucleon has W_free=W_atom (no binding constraint). Neither the ad-hoc "
            "chain (k<A−1) nor the SDP derives the bond graph; coordination M_n(K) is an open "
            "geometric input (s5-so3). Corpus: he3_pairknot_composite_lp_probe + 2026-06-18 audit.")
        wb.add_assertion(
            name="sdp_bondgraph_degenerate",
            computed=str(int(all_deg)), expected="1", tolerance=0,
            source=("H₃ operator-selection LP-dual degenerate (y0*=0, active={γ}) at every "
                    "target; free nucleon W_free=W_atom. Bond graph not SDP-derivable."))
        # Per-target duals, so the verdict above can be checked rather than
        # taken. Also hoisted to the top level under the canonical field names
        # the LP-dual contract asks for (AGENTS.md §LP / SDP duals — first-class
        # infra), which is what `lp_dual_witness_validator.py` walks.
        wb.add_data("lp_duals_per_target", duals)
        for key in ("y0_star", "y_star", "active_set", "primal_obj",
                    "dual_obj", "duality_gap"):
            wb.add_data(key, [d[key] for d in duals])
        wb.add_caveat(
            "y0_star = 0 with active_set = {0} at every target is the "
            "t = G e_0 signature: the basis contains the identity, so "
            "t_j = tr_M(b_j) = tr_M(b_0 b_j) = G_0j and (0, e_0) is dual "
            "feasible with objective 0 — the objective is bounded below by "
            "one of its own constraints. See `dualCertificateExists_of_cost_"
            "eq_gram_row` and bean qou/augu. It is a structural identity, "
            "not a solver artefact, and it is why this route cannot derive "
            "the bond graph.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
