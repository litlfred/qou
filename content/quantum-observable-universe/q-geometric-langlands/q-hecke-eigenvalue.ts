import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-hecke-eigenvalue",
  lean: { ref: "qou:QOU.q_hecke_eigenvalue", validation: "not_checked" },
  title: "$q$-Hecke eigenvalues from the fibre functor",
  uses: [
    "def:q-hecke-eigensheaf",
    "rem:fibre-functor-rigidity",
  ],
  proofs: ["prf:q-hecke-eigenvalue"],
  tags: ["geometric-langlands", "hecke-algebra", "fiber-functor"],
});
