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
    {
      kind: "status",
      date: "2026-11-16",
      body: "Proved mathematical content under rem:q-beta-direction-sanity-gate (issue #8094). The threshold and the target are parameters; the value 10 and the CODATA target stay in the remark. Sorry-free sibling .lean over any linearly ordered field, lean-direct exit 0.",
    },
  ],
});
