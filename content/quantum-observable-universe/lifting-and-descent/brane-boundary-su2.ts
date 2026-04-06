import { example } from "../../schema/builders";

export default example({
  interprets: "def:brane-boundary",
  label: "ex:brane-boundary-su2",
  title: "Brane boundary for $\\mathrm{SU}(2)$",
  tags: ["su2", "brane-boundary", "singular-set"],
  uses: ["def:brane-boundary", "ex:recursive-brane-tower-su2"],
});
