import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-oper",
  lean: { ref: "qou:QOU.QOper", validation: "not_checked" },
  title: "$q$-Oper",
  uses: [
    "def:q-flat-connection",
    "def:q-langlands-dual",
  ],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "oper", "q-deformation"],
});
