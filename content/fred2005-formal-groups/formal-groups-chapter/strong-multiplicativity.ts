import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:strong-multiplicativity",
  title: "Strong multiplicativity",
  lean: { ref: "fred2005:Fred2005.strong_multiplicativity_holds",
    validation: "not_checked",
  },
  tags: ["strong-multiplicativity", "frobenius", "comultiplication"],
  uses: [
    "def:non-commutative-formal-group",
    "def:grobner-shirshov-basis",
  ],
  cites: ["fred2005"],
});
