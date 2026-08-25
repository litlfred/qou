import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-quantity-map",
  title:
    "Categorical quantity map: mass, Q-value, decay rate, density",
  interprets: "def:categorical-action",
  tags: [
    "mass",
    "q-value",
    "decay-rate",
    "density",
    "functional-map",
  ],
  uses: [
    "def:categorical-action",
  ],
});
