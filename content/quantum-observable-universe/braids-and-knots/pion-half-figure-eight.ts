import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pion-half-figure-eight",
  proofs: ["prf:pion-half-figure-eight"],
  title:
    "The pion braid and $\\sigma_1\\sigma_2^{-1}$ have identical eigenvalue phases on $V_{(2,1)}$",
  lean: { ref: "qou:QOU.BraidsAndKnots.pion_eq_half_figure_eight_phase" },
  uses: ["prop:figure-eight-reeb-rotation"],
  cites: [
    "wenzl1988c",
    "jones1987",
  ],
  tags: [
    "pion",
    "figure-eight",
    "half-rotation",
    "reeb-flow",
    "eigenvalue-phase",
    "lepton-meson-bridge",
  ],
});
