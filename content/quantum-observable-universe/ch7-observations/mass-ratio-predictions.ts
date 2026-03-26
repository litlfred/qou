import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-ratio-predictions",
  title: "Theoretical mass ratios from the mass identity",
  uses: ["prop:topological-mass-formula", "def:mass-identity", "def:recursive-brane-tower"],
  tags: ["mass", "prediction", "observation"],
});
