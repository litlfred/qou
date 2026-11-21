import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:figure-eight-reeb-rotation",
  label: "rem:figure-eight-reeb-theta-value",
  title:
    "The q-Reeb angle at the substrate: $\\theta(q_0)\\approx 117.09^\\circ$, $\\theta(1)=2\\pi/3$",
  lean: { ref: "qou:QOU.BraidsAndKnots.figure_eight_classical_reeb" },
  uses: ["prop:figure-eight-reeb-rotation"],
  cites: ["jones1987", "kashaev1997"],
  tags: [
    "figure-eight",
    "reeb-flow",
    "q-reeb-angle",
    "substrate-value",
    "amphichirality",
    "c3-bar-odd",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The unit-modulus property $|\\lambda_{4_1}| = 1$, the classical anchor $\\theta(1) = 2\\pi/3$ (primitive cube root of unity), the two trace identities, the bound $\\mathrm{tr} \\geq -2$, and $\\theta = 0$ at the golden ratio are established in the Lean file." },
  ],
});
