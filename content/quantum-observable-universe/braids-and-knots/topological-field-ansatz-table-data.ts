import { table } from "../../schema/builders";
export default table({
  label: "tbl:topological-field-ansatz-table-data",
  title: "Particle-to-knot axiomatic assignments",
  caption: "Eight particles/fields mapped to their topological identities (knot types) and QOU geometric roles.",
  uses: ["rem:topological-field-ansatz"],
  tags: ["knot-particle", "dictionary", "axiomatic"],
});
