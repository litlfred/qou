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
  lean: {
    decl: "QOU.Descartes.nuclear_groebner_reduction",
    validation: "not_checked",
  },
  uses: [
    "def:stable-nucleus",
    "def:skein-binding-lagrangian",
    "def:braid-group",
    "rem:skein-crossing-asymmetry",
    "conj:shell-threading-energy",
    "unital-groebner-bases:def:admissible-system",
    "unital-groebner-bases:def:groebner-basis",
    "unital-groebner-bases:def:division-algorithm",
  ],
});
