import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "The Lean sketch theorem rested on an axiom that was false: it claimed M_d(R) is Baer-* for every field R with " +
        "every star structure. Over F_2 with the transpose, M_2(F_2) is not Baer-*. The axiom and theorem were removed; " +
        "the link points at the refutation. The prose claim needs a positive star (e.g. complex conjugation); open in Lean, bean qou-n2un.",
    },
  ],
  label: "prop:hecke-baer-star-generic",
  title:
    "Iwahori--Hecke algebra $H_n(q)$ is a Baer-*-ring at generic $q$",
  lean: {
    ref: "qou:QOU.BraidKnot.HeckeBaerStarGeneric.not_hecke_baer_star_generic_sketch",
    validation: "not_checked",
  },
  uses: [
    "rem:vc-as-depth-2-instance",
  ],
  cites: [],
  tags: [
    "baer-star",
    "hecke-algebra",
    "wedderburn",
    "bar-involution",
    "projection-generated",
    "annihilator-structure",
    "graded-mikusinski-foundation",
  ],
});
