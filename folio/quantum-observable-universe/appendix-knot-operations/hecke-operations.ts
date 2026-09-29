import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-operations",
  title: "Hecke algebra $H_3(q)$ operation dictionary",
  tags: ["hecke", "operation-dictionary", "appendix", "normal-form"],
  uses: ["rem:particle-nf-table"],
  interprets: "rem:knot-particle-dictionary",
  computation: {
    engine: "python",
    script: "computations/basis_knot_tables.py",
    witness: "computations/basis-knot-tables.witness.json",
    status: "verified",
  },
});
