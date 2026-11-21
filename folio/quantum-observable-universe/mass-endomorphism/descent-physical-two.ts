import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-physical-two",
  title: "Physical implications of a $2$-dimensional base",
  tags: ["descent", "vortex", "mass", "lepton", "surface", "central"],
  uses: [
    "def:mass-identity",
    "rem:betti-numbers-brane",
    "prop:euler-char-stability",
  ],
  cites: [
    "yekutieli2015",
  ],
});
