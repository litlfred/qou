import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-operations",
  title: "Hecke algebra $H_3(q)$ operation dictionary",
  tags: ["hecke", "operation-dictionary", "appendix", "normal-form"],
  uses: ["rem:particle-nf-table"],
  interprets: "rem:knot-particle-dictionary",
  computation: {
    engine: "python",
    script: "folio-assistant/computations/basis_knot_tables.py",
    witness: "folio-assistant/computations/basis-knot-tables.witness.json",
    status: "verified",
  },
});
