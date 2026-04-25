import { definition } from "../../schema/builders";

export default definition({
  label: "def:jet-stratified-reduction",
  title: "Jet-stratified Gröbner--Shirshov reduction",
  lean: { ref: "ugb:UGB.GrobnerShirshov.jet_stratified_correct",
    validation: "not_checked",
  },
  tags: [
    "groebner-basis",
    "jet-tower",
    "algorithm",
    "complexity",
    "descended",
    "transient",
  ],
  uses: [
    "def:division-algorithm",
    "def:groebner-basis",
    "def:admissible-system",
    "thm:buchberger",
    "unital-groebner-bases:cor:pbw",
  ],
});
