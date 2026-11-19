import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-resolvent",
  title: "$q$-Resolvent",
  tags: ["resolvent", "q-laplacian", "spectral", "hopf-algebra"],
  lean: { ref: "qou:QOU.QResolvent",
    validation: "not_checked",
  },
  uses: ["def:q-exponential"],
});
