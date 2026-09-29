import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-physical",
  title: "Physical implications of a $1$-dimensional base",
  tags: ["descent", "vortex", "mass", "lepton"],
  uses: [
    "def:mass-identity",
    "rem:betti-numbers-brane",
  ],
  cites: [
    "yekutieli2015",
  ],
});
