import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:inductive-gb-reduction",
  proofs: ["prf:inductive-gb-reduction"],
  title: "Inductive Gröbner--Shirshov reduction (polynomial scaling)",
  tags: [
    "groebner-shirshov",
    "inductive",
    "polynomial-scaling",
    "normal-form",
    "hecke-algebra",
  ],
  lean: { ref: "qou:QOU.Interactions.inductiveGBReduction",
    validation: "not_checked",
  },
  uses: ["def:derived-atom"],
});
