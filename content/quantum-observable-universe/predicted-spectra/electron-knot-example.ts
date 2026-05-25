import { example } from "../../schema/builders";

export default example({
  label: "ex:electron-knot-concrete",
  title: "The electron as the trefoil knot on $\\Sigma_4$",
  interprets: "def:electron-knot",
  uses: ["def:electron-knot", "ex:brings-surface-concrete", "ex:topological-mass-trefoil"],
  tags: ["electron", "trefoil", "knot", "example"],
});
