import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-flat-connection",
  lean: { ref: "qou:QOU.QFlatConnection", validation: "not_checked" },
  title: "$q$-Flat connection",
  uses: ["def:q-local-system"],
  tags: ["geometric-langlands", "connection", "q-deformation"],
});
