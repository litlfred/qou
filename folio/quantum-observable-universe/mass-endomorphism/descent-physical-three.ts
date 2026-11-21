import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-physical-three",
  title: "Physical implications of a $3$-dimensional base",
  tags: ["descent", "vortex", "mass", "lepton", "knot", "non-abelian"],
  uses: [
    "def:mass-identity",
    "rem:betti-numbers-brane",
    "prop:euler-char-stability",
  ],
  cites: [
    "yekutieli2015",
  ],
});
