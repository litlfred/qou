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
});
