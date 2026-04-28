import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-exponential",
  title: "$q$-Exponential (grouplike)",
  tags: ["hopf-algebra", "grouplike", "q-exponential", "reeb-flow"],
  lean: { ref: "qou:QOU.QExponential",
    validation: "not_checked",
  },
  uses: ["def:categorical-laplace", "def:habiro-ring"],
});
