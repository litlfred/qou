import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:order-of-magnitude-screen",
  title:
    "The order-of-magnitude screen $\\mathrm{Scr}_\\lambda(t,x)$: monotone in the threshold, multiplicative, conditional rejection, finite-ladder bound, and the threshold-free direction obstruction",
  lean: {
    ref: "qou:QOU.MassCore.OrderOfMagnitudeScreen.not_screen_pow_of_le",
  },
  uses: [],
  tags: ["q-beta", "formalize-first", "direction-sanity", "screen", "no-fit"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): These are the mathematical facts under the screening rule [$\\mathfrak{Q}_\\beta$ order-of-magnitude gate](#rem:q-beta-direction-sanity-gate). The rule fixes $\\lambda=10$ and a target built from a measured value; neither is part of this statement." },
    {
      kind: "status",
      date: "2026-11-16",
      body: "Proved mathematical content under rem:q-beta-direction-sanity-gate (issue #8094). The threshold and the target are parameters; the value 10 and the CODATA target stay in the remark. Sorry-free sibling .lean over any linearly ordered field, lean-direct exit 0.",
    },
  ],
});
