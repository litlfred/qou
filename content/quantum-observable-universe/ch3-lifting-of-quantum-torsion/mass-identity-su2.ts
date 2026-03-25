import { example } from "../../schema/builders";

export default example({
  label: "ex:mass-identity-su2",
  title: "Mass identity for $\\mathrm{SU}(2)$",
  tags: ["su2", "mass", "frobenius", "trace"],
  uses: ["def:mass-identity", "ex:recursive-brane-tower-su2"],
});
