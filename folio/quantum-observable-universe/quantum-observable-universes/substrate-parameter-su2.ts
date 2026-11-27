import { example } from "../../schema/builders";

export default example({
  interprets: "def:aether-parameter",
  label: "ex:aether-parameter-su2",
  renamedFrom: ["ex:substrate-parameter-su2"],
  title: "Aether parameter for $\\mathrm{SU}(2)$",
  tags: ["su2", "substrate-parameter", "deformation", "chern-simons"],
  uses: ["def:aether-parameter", "ex:quantum-universe-su2"],
});
