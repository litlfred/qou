import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-observable-universe",
  label: "ex:qou-su2",
  title: "$\\mathrm{SU}(2)$ is observable",
  lean: { ref: "qou:QOU.Examples.su2Observable", validation: "not_checked" },
  tags: ["su2", "observable"],
  uses: [
    "def:quantum-observable-universe",
    "ex:quantum-universe-su2",
  ],
});
