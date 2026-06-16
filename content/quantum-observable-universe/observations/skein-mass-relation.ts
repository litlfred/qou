import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:topological-mass-formula",
  label: "rem:skein-mass-relation",
  title: "$q$-Deformed Skein Relation (Observation)",
  uses: [
    "rem:skein-decomposition",
    "thm:weight-decomposition-exists",
    "thm:categorical-reeb-exists",
    "thm:substrate-parameter-exists",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: ["mass", "skein"],
});
