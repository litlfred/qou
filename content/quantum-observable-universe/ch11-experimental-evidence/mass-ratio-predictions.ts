import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-ratio-predictions",
  title: "Theoretical mass ratios from the mass identity",
  uses: ["def:mass-identity", "def:recursive-brane-tower"],
  tags: ["mass", "prediction", "observation"],
});
