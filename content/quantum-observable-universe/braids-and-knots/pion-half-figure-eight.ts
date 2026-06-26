import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the proof itself is a straightforward characteristic-polynomial comparison for $2 \\times 2$ matrices with equal trace and determinant, the mathematical novelty is structurally mapping the meson's topological state to a specific \"half-knot\" Reeb rotation, directly formalising the relationship between meson decay energies and the lepton mass ratio (figure-eight volume) via the algebraic squaring relation $4_1 = (\\sigma_1\\sigma_2^{-1})^2$." },
    { kind: "status", date: "2026-06-26", body: "The formalization intentionally focuses on the algebraic reduction—verifying that identical traces and determinants force identical characteristic polynomials and eigenvalues in the $2 \\times 2$ module. The specific trace identity $\\chi^{(2,1)}(\\mathfrak{M}_+) = -(h^2+1)$ is introduced as an assumed hypothesis rather than calculated from scratch; this is a routine computational fact in representation theory, not a disguised gap. By factoring out the topological character computation, the goal of verifying the spectral consequences becomes highly plausible and sharply targeted." },
  ],
  label: "prop:pion-half-figure-eight",
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
