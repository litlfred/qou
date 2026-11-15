import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-prefix-gb-filtration",
  title:
    "Jet-level prefix formula via Gröbner–Shirshov filtration (candidate Term 6)",
  lean: {
    ref: "qou:QOU.BraidKnot.jet_prefix_gb_filtration",
    validation: "not_checked",
  },
  uses: [
    "conj:confinement-grading-correspondence",
  ],
  tags: [
    "jet-level",
    "prefix-formula",
    "gb-filtration",
    "groebner-shirshov",
    "term-6",
    "open-problem",
  ],
});
