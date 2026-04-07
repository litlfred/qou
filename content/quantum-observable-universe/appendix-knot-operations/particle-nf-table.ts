import { remark } from "../../schema/builders";

export default remark({
  label: "rem:particle-nf-table",
  title: "Particle normal forms in $H_3(q)$",
  tags: ["hecke", "normal-form", "particle-dictionary", "appendix"],
  uses: ["rem:knot-particle-dictionary", "def:hecke-normal-form"],
  interprets: "rem:knot-particle-dictionary",
});
