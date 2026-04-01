import { example } from "../../schema/builders";

export default example({
  interprets: "def:maximal-torus",
  label: "ex:maximal-torus-su2",
  title: "Maximal torus for $\\mathrm{SU}(2)$",
  lean: { decl: "QOU.Examples.su2MaximalTorus" },
  uses: ["def:maximal-torus", "ex:spin-labels-su2"],
  tags: ["su2", "torus"],
});
