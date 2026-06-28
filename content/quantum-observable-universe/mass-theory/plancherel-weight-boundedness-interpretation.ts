import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:plancherel-weight-boundedness",
  label: "rem:plancherel-weight-boundedness-interpretation",
  title: "The q-deformed weight $\\widetilde{w}_\\lambda$ is not a probability measure",
  uses: ["prop:plancherel-weight-boundedness"],
});
