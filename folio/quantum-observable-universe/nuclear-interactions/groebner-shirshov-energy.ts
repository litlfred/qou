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
  lean: { ref: "qou:QOU.Archimedean.groebner_shirshov_energy",
    validation: "not_checked",
  },
  uses: ["unital-groebner-bases:thm:main-theorem"],
});
