import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-groebner-reduction",
  title:
    "Unique nuclear normal form via Gröbner reduction in $H_n(q)$",
  tags: [
    "groebner-basis",
    "hecke-algebra",
    "braid-word",
    "normal-form",
    "nuclear",
    "skein-relation",
    "temperley-lieb",
    "admissible-system",
  ],
  lean: { ref: "qou:QOU.Descartes.nuclear_groebner_reduction",
    validation: "not_checked",
  },
  uses: [
    "prop:braiding-eigenvalue-extraction",
    "rem:hecke-algebra-from-braiding",
    "unital-groebner-bases:def:groebner-basis",
    "unital-groebner-bases:def:division-algorithm",
    "unital-groebner-bases:def:admissible-system",
  ],
});
