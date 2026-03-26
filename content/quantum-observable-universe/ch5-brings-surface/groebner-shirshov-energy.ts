import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:groebner-shirshov-energy",
  title:
    "Energy as a Gröbner--Shirshov invariant of the nuclear braid",
  tags: [
    "groebner-shirshov",
    "hecke-algebra",
    "energy",
    "braid-word",
    "normal-form",
    "division-algorithm",
    "topological-invariant",
  ],
  lean: {
    decl: "QOU.Descartes.groebner_shirshov_energy",
    validation: "not_checked",
  },
  uses: [
    "prop:nuclear-groebner-reduction",
    "def:skein-binding-lagrangian",
    "def:braid-group",
    "unital-groebner-bases:def:admissible-system",
    "unital-groebner-bases:def:groebner-basis",
    "unital-groebner-bases:def:division-algorithm",
    "unital-groebner-bases:thm:main-theorem",
  ],
});
