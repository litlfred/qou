import { proposition } from "../../schema/builders";

export default proposition({
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
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`braids-and-knots/figure-eight-reeb-rotation.lean` uses " +
        "`Complex.*`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
