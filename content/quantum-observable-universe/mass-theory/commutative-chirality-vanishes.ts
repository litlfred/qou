import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:commutative-chirality-vanishes",
  title: "Chirality term vanishes in the commutative QOU limit",
  lean: {
    ref: "qou:QOU.WedderburnMass.commutative_chirality_vanishes",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-s-classification",
    "rem:commutative-crossing-energy",
  ],
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/commutative_chirality_vanishes_probe.py",
    witness: "folio-assistant/computations/commutative-chirality-vanishes-probe.witness.json",
    status: "verified",
  },
});
