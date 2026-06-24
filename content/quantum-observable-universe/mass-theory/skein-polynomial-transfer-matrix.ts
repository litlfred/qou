import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-polynomial-transfer-matrix",
  proofs: ["prf:skein-polynomial-transfer-matrix"],
  title:
    "The nuclear Skein polynomial as a transfer matrix product in $q$",
  tags: [
    "skein-polynomial",
    "transfer-matrix",
    "polynomial",
    "jones-polynomial",
    "hecke-algebra",
    "nuclear",
    "q-variable",
    "factored-form",
  ],
  lean: { ref: "qou:QOU.Archimedean.skein_polynomial_transfer_matrix",
    validation: "not_checked",
  },
  uses: ["thm:markov-trace-factorization"],
});
