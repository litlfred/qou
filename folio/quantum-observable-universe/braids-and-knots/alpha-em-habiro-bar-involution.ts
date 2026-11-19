import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:alpha-em-habiro-bar-involution",
  title:
    "The $\\alpha_{EM}$ Habiro element $[2]_q(1-h^2\\alpha)$ is a bar-involution fixed point, with $H(1)=2$, $H(-1)=-2$",
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
