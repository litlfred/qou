import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-chromaticity",
  title:
    "Three colors and $q$-chromaticity: why negative coefficients require confinement",
  interprets: "rem:force-knot-identification",
  tags: [
    "color",
    "chromaticity",
    "confinement",
    "skein",
    "negativity",
    "color-tube",
    "strong-force",
    "primaries",
  ],
  uses: [
    "rem:force-knot-identification",
    "rem:unmapped-torus-knots",
    "rem:color-tube-interpretation",
    "rem:chirality-trefoil",
    "def:color-tube-coordinates",
    "prop:torus-knot-generators",
    "thm:embeddability-closure",
    "prop:local-substrate-q",
  ],
  cites: ["feynman1963"],
});
