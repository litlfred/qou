import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While using the Hecke relation and determinant constraint to relate braiding eigenvalues is standard algebraic manipulation (e.g., following Kassel), the mathematical novelty here is treating this extraction not as a definition of $q$, but as a rigorous proof that the macroscopic substrate parameter governing the fluid PDE is precisely and completely constrained by the microscopic categorical braiding of the observable universe." },
  ],
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
  lean: { ref: "qou:QOU.braiding_eigenvalue_extraction",
    validation: "not_checked",
  },
  uses: ["prop:tannaka-krein-reconstruction"],
});
