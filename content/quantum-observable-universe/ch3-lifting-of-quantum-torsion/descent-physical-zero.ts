import { remark } from "../../schema/builders";

export default remark({
  label: "rem:descent-physical-zero",
  title: "Physical implications of a $0$-dimensional base",
  tags: ["descent", "mass", "lepton", "primordial"],
  uses: [
    "def:mass-identity",
    "rem:betti-numbers-brane",
  ],
});
