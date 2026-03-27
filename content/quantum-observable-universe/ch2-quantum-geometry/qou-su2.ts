import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-observable-universe",
  label: "ex:qou-su2",
  title: "$\\mathrm{SU}(2)$ is observable",
  lean: { decl: "QOU.Examples.su2Observable" },
  tags: ["su2", "observable"],
  uses: ["def:quantum-observable-universe", "ex:rigid-monoidal-vect", "ex:quantum-universe-su2"],
});
