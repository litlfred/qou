import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "The q-Reeb-rotation-phase reading of the figure-eight eigenvalue on $V_{2,1}$, which connects to $\\mathrm{Vol}(4_1)$ and the muon anchor, is a genuinely framework-specific and novel conceptual idea. (Note that this connection is asserted conceptually rather than fully established in the formalization)." },
  ],
  label: "prop:figure-eight-reeb-rotation",
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
