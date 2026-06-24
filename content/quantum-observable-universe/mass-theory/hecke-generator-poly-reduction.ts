import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-generator-poly-reduction",
  proofs: ["prf:hecke-generator-poly-reduction"],
  title: "Single-generator Hecke polynomial reduction",
  tags: [
    "hecke-algebra",
    "markov-trace",
    "transfer-matrix",
    "cayley-hamilton",
    "binding",
  ],
  lean: {
    ref: "qou:QOU.Braiding.hecke_gen_poly_reduction",
    validation: "not_checked",
  },
  uses: ["def:hecke-normal-form"],
});
