import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-exponential",
  title: "$q$-Exponential (grouplike)",
  tags: ["hopf-algebra", "grouplike", "q-exponential", "reeb-flow"],
  lean: {
    decl: "QOU.QExponential",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-laplace",
    "rem:base-field-independence",
    "rem:adjoint-trace",
  ],
});
