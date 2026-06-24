import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:three-halves-structural-factor",
  lean: {
    ref: "qou:QOU.BraidKnot.ThreeHalvesStructuralFactor.three_halves_factor_eq_q_brackets",
    validation: "not_checked",
  },
  title:
    "Lepton-tower closure structural identities — muon (3+h²)/(2+h²) = [3]_q·[2]_q/[4]_q and tau [6]_q = [2]_q·[3]_q·(1+h²) — proved over generic [Field R] via field_simp; ring.",
  uses: [
    "prop:lepton-bring-surface-h3-3channel",
  ],
  proofs: ["prf:three-halves-structural-factor"],
  cites: [],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**proposition (sorry-free).** Five algebraic identities in h = q − q⁻¹ " +
        "and the symmetric q-integers [n]_q, all proved via `field_simp; ring`. " +
        "Muon set (PR #1127): three_plus_h_sq_eq_bracket3, " +
        "two_plus_h_sq_times_bracket2_eq_bracket4, three_halves_factor_eq_q_brackets. " +
        "Tau set (PR #1253): bracket6_eq_bracket2_bracket3_times_one_plus_h_sq, " +
        "bracket5_bracket3_div_bracket6. Numerically cross-checked at canonical " +
        "q_0 to ≤ 1e-40 via `tau_amphichiral_sdp_probe.py` witness (3 of 4 " +
        "assertions). Consumed (by docstring narrative) from " +
        "`conj-lepton-tower-h-n-plus-1-branching.lean`.",
    },
  ],
  tags: [
    "lepton",
    "mass-tower",
    "q-bracket",
    "structural-identity",
    "phase-3",
    "lean-proved",
  ],
});
