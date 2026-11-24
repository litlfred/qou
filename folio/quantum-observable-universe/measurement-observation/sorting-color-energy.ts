import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sorting-color-energy",
  lean: { ref: "qou:QOU.BraidKnot.sorting_color_energy", validation: "not_checked" },
  title:
    "Sorting deposits energy $q + q^{-1}$ per crossing in the colour fibre",
  tags: [
    "sorting",
    "colour-fibre",
    "energy",
    "R-matrix",
    "adjoint",
    "symmetric",
    "antisymmetric",
    "observation",
  ],
  uses: ["rem:observation-braid"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` inhabits `SortingColorEnergyContext ℚ` on `Unit` with `sigma := id`.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
  ],
});
