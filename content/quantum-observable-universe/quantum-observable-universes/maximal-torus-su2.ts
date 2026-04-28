import { example } from "../../schema/builders";

export default example({
  interprets: "def:maximal-torus",
  label: "ex:maximal-torus-su2",
  title: "Maximal torus for $\\mathrm{SU}(2)$",
  lean: { ref: "qou:QOU.Examples.su2MaximalTorus", validation: "not_checked" },
  uses: ["def:maximal-torus", "ex:spin-labels-su2"],
  tags: ["su2", "torus"],
});
