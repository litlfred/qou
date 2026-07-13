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
});
