import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:braiding-eigenvalue-extraction",
  title:
    "Extraction of $q$ from the braiding eigenvalues",
  cites: ["kassel1995", "woronowicz1988"],
  tags: [
    "braiding",
    "eigenvalue",
    "substrate-parameter",
    "hecke-algebra",
    "categorical",
  ],
  lean: {
    decl: "QOU.braiding_eigenvalue_extraction",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "prop:tannaka-krein-reconstruction",
    "thm:su2-emergence",
  ],
});
