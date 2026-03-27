import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:knot-particle-generation",
  label: "rem:knot-formula-table",
  title: "Topological knot formulas for fundamental and composite particles",
  tags: [
    "knot",
    "formula",
    "notation",
    "particle",
    "hadron",
    "nucleus",
    "generation",
  ],
  uses: [
    "def:knot-particle-generation",
    "prop:torus-knot-generators",
    "thm:embeddability-closure",
    "def:hadron",
    "rem:hadron-operations",
    "prop:skein-generation",
    "rem:knot-particle-dictionary",
    "prop:terminal-resolution",
    "def:color-tube-coordinates",
  ],
});
