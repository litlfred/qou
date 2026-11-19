import { table } from "../../schema/builders";
export default table({
  label: "tbl:chi-v3-closed-form-proof-table-data",
  title: "Closed-form algebraic identities for the symmetric-representation difference $\\chi_{(3)}(\\mathcal{B}_n) - \\chi_{(3)}(\\mathcal{B}_p)$",
  caption: "Three sorry-free Lean theorems establishing the $\\chi_{V_3}$ neutron-proton difference in factored and polynomial forms.",
  uses: ["rem:chi-v3-closed-form-proof"],
  tags: ["chi-V3", "lean-theorems", "closed-form"],
});
