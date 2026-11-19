import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cpt-d6-d7-d8-closure",
  title:
    "CPT closure: charge conjugation, parity, and time reversal close on flavor-decorated Hecke Markov traces",
  lean: {
    ref: "qou:QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure.cpt_covariant_conventionD_markov_trace_H3",
    validation: "validated",
  },
  uses: [
    "conj:cpt-orbit-closure-density",
    "def:bar-involution",
  ],
  cites: [
    "wigner1937",
    "jones1987",
    "kassel1995",
  ],
  tags: [
    "cpt-closure",
    "discrete-symmetry",
    "duality-d6-d7-d8",
    "markov-trace",
    "kazhdan-lusztig-bar",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Proved unconditionally on `H_2(q)`, `H_3(q)`, and flavor-decorated 3-strand closed braids in `folio/quantum-observable-universe/lean/QOU/Nuclear/BraneTowerExponentialDecayAndCPTClosure.lean` (`wordRevH3_mulNF`, `trM_wordRevH3`, `trM_conventionD_gpmt_wordRevH3`, `barH3_involutive`, `barH3_mulNF`, `wordRevH3_comm_barH3`, `trM_barH3`, `zD_inv_eq_sub_h`, `trM_conventionD_barH3`, `cpt_actions_involutive_and_commute`, `cpt_covariant_markov_trace_H3`, `cpt_covariant_conventionD_markov_trace_H3`, `cpt_preserves_barSym_markov_trace_H3`, `parity_chiral_defect_sigma0`). Abstract parametric `CPTClosure` class retained in `cpt-d6-d7-d8-closure.lean` for downstream callers.",
    },
  ],
});
