import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:braiding-induced-ordering",
  title:
    "Degree-lexicographic well-ordering on braid words",
  tags: [
    "braiding",
    "well-ordering",
    "admissible-system",
    "hecke-algebra",
    "arrow-of-time",
    "temporal",
    "groebner",
  ],
  lean: { ref: "qou:QOU.braiding_induced_ordering_holds",
    validation: "not_checked",
  },
  uses: [
    "prop:braid-action-tensor",
    "def:braid-group",
    "rem:hecke-algebra-from-braiding",
    "unital-groebner-bases:def:admissible-system",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Restricting $\\prec_c$ to reduced positive monomials, or to the $n!$ standard basis of the Iwahori--Hecke algebra $H_n(q)$, gives a well-founded order on those subsets." },
  ],
});
