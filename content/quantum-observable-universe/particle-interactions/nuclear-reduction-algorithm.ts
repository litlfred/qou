import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:nuclear-groebner-reduction",
  label: "rem:nuclear-reduction-algorithm",
  title: "Nuclear braid reduction algorithm",
  tags: [
    "algorithm",
    "groebner-shirshov",
    "hecke-algebra",
    "normal-form",
    "leitner-pawloski",
  ],
  uses: [
    "def:nuclear-groebner-reduction",
    "def:inductive-gb-reduction",
    "unital-groebner-bases:def:division-algorithm",
    "unital-groebner-bases:def:admissible-system",
  ],
});
