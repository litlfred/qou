import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:inductive-gb-reduction",
  title: "Inductive Gröbner--Shirshov reduction (polynomial scaling)",
  tags: [
    "groebner-shirshov",
    "inductive",
    "polynomial-scaling",
    "normal-form",
    "hecke-algebra",
  ],
  lean: {
    decl: "QOU.Interactions.inductiveGBReduction",
    validation: "not_checked",
  },
  uses: [
    "def:nuclear-groebner-reduction",
    "def:derived-atom",
  ],
});
