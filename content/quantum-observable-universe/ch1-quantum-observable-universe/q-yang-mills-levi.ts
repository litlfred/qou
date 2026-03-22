import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-yang-mills-levi",
  title: "$q$-Weighted Yang--Mills--Levi functional",
  lean: { decl: "QOU.QYangMillsLevi", validation: "not_checked" },
  status: "stated",
  uses: ["ex:c-quantum-observable-universe", "ex:instanton", "def:substrate-parameter"],
  tags: ["yang-mills", "functional"],
});
