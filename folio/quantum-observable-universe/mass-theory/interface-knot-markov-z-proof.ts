import { proof } from "../../schema/builders";

export default proof({
  label: "prf:interface-knot-markov-z",
  title: "Proof of interface knot markov z",
  uses: ["prop:interface-knot-markov-z"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/probes/pn_interface_bar_structure_probe.py.",
    },
    {
      kind: "note",
      date: "2026-10-10",
      body: "The verification table replaces one measured at the excised convention-C weight z = √q/(q+1) (bean qou-7xpx). Producer: computations/probes/interface_knot_markov_z_convention_d_probe.py.",
    },
  ],
  computation: {
    engine: "sympy",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/probes/pn-interface-bar-structure.witness.json",
      "computations/probes/interface-knot-markov-z-convention-d.witness.json",
      "computations/markov/markov-pipeline-cross-validation.witness.json",
    ],
    status: "verified",
  },
});
