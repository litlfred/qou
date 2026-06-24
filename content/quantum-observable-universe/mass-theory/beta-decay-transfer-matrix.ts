import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:beta-decay-transfer-matrix",
  proofs: ["prf:beta-decay-transfer-matrix"],
  title:
    "Beta decay as a universal matrix-valued polynomial in $q$",
  tags: [
    "beta-decay",
    "transfer-matrix",
    "polynomial",
    "q-deformed",
    "skein",
    "hecke",
    "universal",
    "matrix",
  ],
  lean: { ref: "qou:QOU.Archimedean.beta_decay_transfer_matrix",
    validation: "not_checked",
  },
  uses: ["prop:skein-polynomial-transfer-matrix"],
});
