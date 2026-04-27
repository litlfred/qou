import { example } from "../../schema/builders";

export default example({
  interprets: "thm:weight-decomposition-exists",
  label: "ex:weight-decomposition-su2",
  title:
    "Constructive weight decomposition for $\\mathrm{SU}(2)$",
  tags: ["su2", "weight-decomposition", "constructive", "peter-weyl"],
  uses: [
    "thm:weight-decomposition-exists",
    "ex:maximal-torus-su2",
  ],
});
