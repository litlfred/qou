import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body:
        "Matrix-block step proved for a positive star: `baerStarRing_matrix_rclike` shows M_n(k) with the conjugate " +
        "transpose is Baer-* for every RCLike field k (R or C), using the orthogonal projection onto the complement of the " +
        "column span. Sorry-free; axioms propext, Classical.choice, Quot.sound. The proposition itself is still open: it " +
        "also needs a *-isomorphism from H_n(q) onto a sum of matrix blocks that carries the bar involution to the " +
        "conjugate transpose, which is not formalised. Beans qou-n2un, qou-jgp2.",
    },
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
  // rem:vc-as-depth-2-instance dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the statement or proof. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: [],
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
