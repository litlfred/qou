import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:figure-eight-reeb-rotation",
  proofs: ["prf:figure-eight-reeb-rotation"],
  title:
    "The figure-eight knot operator acts unitarily on $V_{(2,1)}$",
  lean: { ref: "qou:QOU.BraidsAndKnots.figure_eight_unitary_on_standard" },
  uses: [
    "prop:hoefsmit-binding-amplitude",
    "def:categorical-q-reeb-flow",
  ],
  cites: [
    "jones1987",
    "wenzl1988c",
    "kashaev1997",
  ],
  tags: [
    "figure-eight",
    "4_1",
    "reeb-flow",
    "unitary",
    "knot-operator",
    "volume-conjecture",
    "lepton-channel-rotation",
  ],
});
