import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "The proved facts are elementary, consisting of a ring-level observation regarding the bar-symmetry of $[2]_q(1-h^2 \\alpha)$. The mathematical novelty and interesting framework content lie in the fibre-vs-observable framing and the realization that $\\zeta_4=0$ is dual to the $\\mathfrak{Q}_\\beta$ pole." },
  ],
  label: "prop:alpha-em-habiro-bar-involution",
  title:
    "The $\\alpha_{EM}$ Habiro element $[2]_q(1-h^2\\alpha)$ is a " +
    "bar-involution fixed point, with $H(1)=2$, $H(-1)=-2$",
  lean: {
    ref: "qou:QOU.BraidKnot.alphaEmHabiro_bar_invariant",
  },
  uses: [],
  cites: [
    "jones1987",
    "kassel1995",
  ],
  computation: {
    engine: "sympy",
    script:
      "computations/alpha/alpha_em_q_difference_fourier.py",
    witness:
      "computations/alpha/alpha-em-q-difference-fourier.witness.json",
    status: "verified",
  },
  tags: [
    "alpha-em",
    "habiro",
    "bar-involution",
    "q-difference",
    "root-of-unity",
    "fibre-level",
    "categorical-derivation",
  ],
});
