import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "The Lean `QHeatEquation.unique_solution` proves a weaker statement: two `QHeatEquation` structures with the same q-Laplacian image `dq_u` have the same time derivative `dt_u`. It does not formalise the initial-value uniqueness stated in the .md. Statement and proof rewritten 2026-11-21 (round-trip audit pass 2, C01): the space, the operator and the notion of solution are now explicit, and the old reliance on semisimplicity is removed." },
  ],
  label: "prop:q-heat-equation-unique",
  title: "Uniqueness of solutions of the $q$-heat equation",
  lean: { ref: "qou:QOU.QHeatEquation.unique_solution",
    validation: "not_checked",
  },
  uses: ["prop:q-heat-equation-exists"],
  proofs: ["prf:q-heat-equation-unique"],
  tags: ["uniqueness", "q-heat-equation"],
});
