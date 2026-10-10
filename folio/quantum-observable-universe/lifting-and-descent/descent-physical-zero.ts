import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-physical-zero",
  title: "Physical implications of a $0$-dimensional base",
  tags: ["descent", "mass", "lepton", "primordial"],
  uses: [
    "def:mass-identity",
    "rem:betti-numbers-brane",
  ],
});
