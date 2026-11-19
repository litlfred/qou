import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-local-system",
  label: "rem:q-local-system",
  title: "From monodromy to $q$-monodromy",
  uses: ["def:q-local-system", "prop:categorical-dq-squared", "rem:kummer-filtration-obstruction"],
  tags: ["geometric-langlands", "monodromy"],
});
