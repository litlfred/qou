import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-resolvent",
  title: "$q$-Resolvent (categorical)",
  tags: ["resolvent", "q-laplacian", "spectral", "hopf-algebra"],
  lean: {
    decl: "QOU.QResolvent",
    validation: "not_checked",
  },
  uses: [
    "def:q-heat-equation",
    "def:categorical-laplace",
    "def:q-exponential",
  ],
});
