import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-pairing-exists",
  title: "Existence of the Frobenius pairing",
  lean: { ref: "qou:QOU.FrobeniusHopfData.frobeniusForm_exists",
    validation: "not_checked",
  },
  uses: ["def:frobenius-pairing"],
  proofs: ["prf:frobenius-pairing-exists"],
  tags: ["existence", "frobenius-pairing", "quantum-universe"],
});
