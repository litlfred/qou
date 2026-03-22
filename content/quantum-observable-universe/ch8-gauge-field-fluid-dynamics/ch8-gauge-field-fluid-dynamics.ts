import { chapter, section } from "../../schema/builders";
export default chapter({
  number: 8,
  title: "Gauge Field Fluid Dynamics",
  label: "chap:gauge-fluid",
  sections: [
    section({
      title: "Fluid Dynamics of the Brane",
      label: "sec:brane-fluid",
      blocks: ["brane-fluid"],
    }),
    section({
      title: "Geodesics as Stable Vortex Points",
      label: "sec:geodesic-vortices",
      blocks: ["geodesic-vortices"],
    }),
    section({
      title: "Braid Operators in the Fluid Picture",
      label: "sec:braid-fluid",
      blocks: ["braid-fluid"],
    }),
    section({
      title: "$q$-Parameter, Planck Limit, and Reynolds Number",
      label: "sec:planck-reynolds",
      blocks: ["planck-reynolds"],
    }),
  ],
});
