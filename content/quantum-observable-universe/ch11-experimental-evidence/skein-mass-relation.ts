import { remark } from "../../schema/builders";

export default remark({
  label: "rem:skein-mass-relation",
  lean: {
    decl: "QOU.Experimental.skein_mass_relation",
    validation: "not_checked",
  },
  title: "$q$-Deformed Skein Relation (Observation)",
  uses: [
    "conj:topological-mass-formula",
    "rem:skein-decomposition",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "ex:c-quantum-observable-universe",
    "thm:weight-decomposition-exists",
    "thm:categorical-reeb-exists",
    "thm:substrate-parameter-exists",
  ],
  tags: ["mass", "skein"],
});
