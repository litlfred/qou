import { proof } from "../../schema/builders";

export default proof({
  label: "prf:interface-knot-markov-z",
  title: "Proof of interface knot markov z",
  uses: ["prop:interface-knot-markov-z"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-10-10",
      body: "The verification table replaces one measured at the excised convention-C weight z = √q/(q+1) (bean qou-7xpx). Producer: computations/probes/interface_knot_markov_z_convention_d_probe.py.",
    },
  ],
});
