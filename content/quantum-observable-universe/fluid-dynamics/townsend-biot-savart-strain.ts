import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  interprets: "conj:levi-degeneracy",
  label: "rem:townsend-biot-savart-strain",
  title:
    "Townsend evolution under Biot--Savart strain: the first-order flattening $\\kappa \\to 0$",
  uses: ["rem:hyperbolic-overlap-saturation"],
  cites: ["townsend1951", "saffman1992", "moffatt1994"],
  tags: [
    "townsend",
    "biot-savart",
    "vortex-core",
    "levi-form",
    "strain",
    "fluid-dynamics",
    "navier-stokes",
    "millennium-problem",
  ],
});
