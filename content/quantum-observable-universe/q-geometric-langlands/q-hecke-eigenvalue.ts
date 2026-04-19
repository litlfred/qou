import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-hecke-eigenvalue",
  lean: {
    decl: "QOU.QGeometricLanglands.Stubs.q_hecke_eigenvalue",
    file: "QOU/QGeometricLanglands/Stubs.lean",
    validation: "not_checked",
  },
  title: "$q$-Hecke eigenvalues from the fibre functor",
  uses: [
    "def:q-hecke-eigensheaf",
    "def:q-hecke-operator",
    "rem:fibre-functor-rigidity",
  ],
  proofs: ["prf:q-hecke-eigenvalue"],
  tags: ["geometric-langlands", "hecke-algebra", "fiber-functor"],
});
