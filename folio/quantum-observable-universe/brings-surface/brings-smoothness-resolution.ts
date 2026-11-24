import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brings-smoothness-resolution",
  title:
    "Smoothness of the Bring's surface and intrinsic resolution of projection singularities",
  tags: ["brings-surface", "smooth", "resolution", "branch-point", "color"],
  lean: { ref: "qou:QOU.BringsSurface.BringsSurfaceRoot.brings_smoothness_resolution",
    validation: "not_checked",
  },
  uses: [
    "rem:color-bundles",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-23-free-prop-field-triviality-probe.lean` records that bare `Prop`-valued fields on `BringSurfaceSmoothness` were trivially inhabited by `⟨True, True, True⟩`.",
      see: "docs/audits/2026-08-23-free-prop-field-triviality-probe.lean",
    },
  ],
});
