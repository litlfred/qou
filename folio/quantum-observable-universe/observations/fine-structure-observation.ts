import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fine-structure-observation",
  title: "Fine structure constant: CODATA comparison",
  interprets: "prop:em-coupling-projection",
  tags: [
    "fine-structure-constant",
    "electromagnetic",
    "CODATA",
    "observation",
    "coupling",
    "q-integer",
  ],
  uses: [
    "sec:mass-predictions-data",
    "rem:half-life-as-q-probe",
    "rem:mass-comparison-table",
  ],
  // The +0.313 ppb figure and the 137.035999127 fixed point come from the
  // Schwinger cubic, not from this block's own arithmetic; pinned so the
  // numbers are traceable rather than transcribed. The companion q-inversion
  // (q_alpha = 1.10997858..., 0.245 ppb from the proton pin, 11.8 ppb from the
  // muon pin) is alpha-em-anchor-preference.witness.json.
  computation: {
    engine: "python",
    script: "computations/alpha_em_schwinger_ladder_probe.py",
    witness: [
      "computations/alpha-em-schwinger-ladder.witness.json",
      "computations/alpha-em-anchor-preference.witness.json",
      "computations/probes/the_em_coupling_projection_block_cites_a_producer_that_leaves_no_witness_probe.witness.json",
      "computations/per-observable-100x-status.witness.json",
      "computations/probes/substrate_consistency_window_q_from_alpha_em_probe.witness.json",
    ],
    status: "verified",
  },
});
