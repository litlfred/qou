import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-dilogarithm",
  title: "$q$-Dilogarithm",
  tags: ["hopf-algebra", "dilogarithm", "pentagon-identity", "associator", "q-series"],
  lean: { ref: "qou:QOU.QDilogarithm",
    validation: "not_checked",
  },
  uses: ["def:q-logarithm"],
});
