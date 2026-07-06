import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:plancherel-weight-boundedness",
  label: "rem:plancherel-weight-boundedness-interpretation",
  title: "The q-deformed weight $\\widetilde{w}_\\lambda$, and significance for mass-tower computations",
  uses: [
    "prop:plancherel-weight-boundedness",
    "prop:plancherel-term-7-formulation",
    "rem:mass-formula-validation",
  ],
});
