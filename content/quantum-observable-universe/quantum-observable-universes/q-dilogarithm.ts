import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-dilogarithm",
  title: "$q$-Dilogarithm (iterated primitive, categorical)",
  tags: ["hopf-algebra", "dilogarithm", "pentagon-identity", "associator", "q-series"],
  lean: { ref: "qou:QOU.QDilogarithm",
    validation: "not_checked",
  },
  uses: [
    "def:q-logarithm",
    "prop:tannaka-krein-reconstruction",
  ],
});
