import { remark } from "../../schema/builders";

export default remark({
  label: "rem:color-confinement-observation",
  title:
    "Color confinement as $q$-chromaticity: the Feynman negativity constraint",
  interprets: "rem:q-chromaticity",
  tags: [
    "color",
    "confinement",
    "chromaticity",
    "observation",
    "QCD",
    "skein",
    "negativity",
  ],
  uses: ["rem:q-chromaticity"],
  cites: ["feynman1963"],
});
