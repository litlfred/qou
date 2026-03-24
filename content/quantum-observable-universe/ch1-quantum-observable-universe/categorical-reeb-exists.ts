import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:categorical-reeb-exists",
  title: "Existence of the categorical Reeb derivation",
  lean: {
    decl: "QOU.CategoricalReeb.ofWeightDecomposition",
    validation: "not_checked",
  },
  uses: ["def:quantum-observable-universe", "def:maximal-torus", "def:weight-decomposition", "def:categorical-reeb"],
  tags: ["existence", "reeb", "derivation"],
});
