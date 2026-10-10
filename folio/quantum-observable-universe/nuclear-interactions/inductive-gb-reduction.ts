import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:inductive-gb-reduction",
  title: "Inductive Gröbner--Shirshov reduction",
  tags: [
    "groebner-shirshov",
    "inductive",
    "normal-form",
    "hecke-algebra",
  ],
  lean: { ref: "qou:QOU.Interactions.inductiveGBReduction",
    validation: "not_checked",
  },
  uses: ["def:derived-atom"],
});
