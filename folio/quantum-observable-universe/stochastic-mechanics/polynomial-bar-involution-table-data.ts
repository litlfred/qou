import { table } from "../../schema/builders";
export default table({
  label: "tbl:polynomial-bar-involution-table-data",
  title: "Ring-homomorphism and monomial parity identities of the polynomial bar involution $p(X) \\mapsto p(-X)$",
  uses: ["prop:polynomial-bar-involution"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "Lean declarations: `barPoly_X`, `barPoly_neg_X`, `barPoly_C`, `barPoly_add`, `barPoly_mul`, `barPoly_one`, `barPoly_zero`, `barPoly_involutive`, `barPoly_X_pow_two`, `barPoly_X_pow`.",
    },
  ],
});
