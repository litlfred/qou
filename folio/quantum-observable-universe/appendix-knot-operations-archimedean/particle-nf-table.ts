import { remark } from "../../schema/builders";

export default remark({
  label: "rem:particle-nf-table",
  title: "Particle normal forms in $H_3(q)$",
  tags: ["hecke", "normal-form", "particle-dictionary", "appendix"],
  uses: ["def:hecke-normal-form"],
  interprets: "rem:knot-particle-dictionary",
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
