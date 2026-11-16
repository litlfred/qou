import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-pairing-unique",
  title: "Uniqueness of the Frobenius pairing",
  lean: { ref: "qou:QOU.FrobeniusHopfData.frobeniusForm_unique_of_schur",
    validation: "not_checked",
  },
  uses: ["prop:frobenius-pairing-exists"],
  proofs: ["prf:frobenius-pairing-unique"],
  tags: ["uniqueness", "frobenius-pairing", "quantum-universe"],
});
