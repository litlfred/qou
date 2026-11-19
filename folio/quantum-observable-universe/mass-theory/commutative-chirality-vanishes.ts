import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:commutative-chirality-vanishes",
  title: "Chirality term vanishes in the commutative QOU limit",
  lean: {
    ref: "qou:QOU.WedderburnMass.commutative_chirality_vanishes",
    validation: "not_checked",
  },
  uses: ["rem:commutative-crossing-energy"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/commutative_chirality_vanishes_probe.py",
    witness: "computations/probes/commutative-chirality-vanishes-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
