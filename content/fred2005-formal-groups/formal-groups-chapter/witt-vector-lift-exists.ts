import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:witt-vector-lift-exists",
  title: "Existence of Witt vector lift",
  lean: { ref: "fred2005:Fred2005.witt_vector_lift_exists",
    validation: "not_checked",
  },
  tags: ["witt-vector", "existence", "lift"],
  uses: [
    "def:commutative-formal-group",
    "def:skewed-poisson-structure",
    "def:witt-vector-lift",
    "thm:skew-poisson-integrates",
  ],
  cites: ["fred2005"],
});
