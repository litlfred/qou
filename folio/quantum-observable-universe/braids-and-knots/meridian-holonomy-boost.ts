import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meridian-holonomy-boost",
  title:
    "Meridian holonomy is a boost: $\\mathrm{barEven}(q)^2 - \\mathrm{barOdd}(q)^2 = 4$",
  lean: { ref: "qou:QOU.Knot.CuspShapeBarParity.holonomy_hyperbola" },
  uses: ["prop:cusp-shape-bar-parity"],
  tags: [
    "meridian",
    "holonomy",
    "boost",
    "rapidity",
    "bar-parity",
    "hyperbolic-rotation",
    "cusp-shape",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): All three identities are formalized over a generic field: `holonomy_hyperbola`, `barEven_mul`, `barOdd_mul`." },
  ],
});
