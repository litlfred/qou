import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-local-system",
  lean: { ref: "qou:QOU.QLocalSystem", validation: "not_checked" },
  title: "$q$-Local system",
  uses: [
    "def:categorical-q-connection",
    "def:substrate-parameter",
    "def:q-flat-connection",
    "prop:categorical-dq-squared",
    "rem:kummer-filtration-obstruction",
  ],
  tags: ["geometric-langlands", "local-system", "q-deformation"],
});
