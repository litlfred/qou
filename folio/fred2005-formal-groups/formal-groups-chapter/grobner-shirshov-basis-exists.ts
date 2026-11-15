import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:grobner-shirshov-basis-exists",
  title: "Existence of Groebner--Shirshov basis",
  lean: { ref: "fred2005:Fred2005.grobner_shirshov_basis_exists",
    validation: "not_checked",
  },
  tags: ["groebner-shirshov", "existence", "flat-deformation"],
  uses: [
    "def:non-commutative-formal-group",
    "def:grobner-shirshov-basis",
  ],
  cites: ["fred2005"],
});
