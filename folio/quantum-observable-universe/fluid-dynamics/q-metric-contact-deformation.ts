import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-metric-contact-deformation",
  title:
    "$q$-deformation as a contact metric change (Miranda picture)",
  // rem:reeb-contact-universal-computer stays a dependency: it lives in
  // `quantum-observable-universes` (chapter 2) while this block is in
  // `fluid-dynamics` (chapter 18), so it points BACKWARD across sixteen
  // chapters. The reader passed it long ago -- an ordinary prerequisite, not
  // a preview.
  uses: ["rem:reeb-contact-universal-computer"],
  // This block is the chapter overview (§0). It names results developed
  // across §3-§6 to lay out the picture; it does not depend on them, and a
  // reader is not expected to jump. Recorded as forward pointers rather than
  // dependencies -- see the `overview-source` rows of
  // docs/audits/uses-edge-rejections.json for why these are not `uses[]`.
  foreshadows: [
    "def:ns-obstruction",
    "prop:core-levi-form",
    "rem:hyperbolic-overlap-saturation",
    "rem:townsend-biot-savart-strain",
    // Reclassified from a dependency: same-chapter, pos 9 -> 95, and the
    // prose names it as the programme this chapter builds toward rather than
    // as something the reader needs first. This retires one of
    // fluid-dynamics' twelve pre-existing forward edges by classifying it
    // correctly. NOTE: never write a closing square bracket inside a comment
    // in this array — the manifest parsers match it non-greedily and stop at
    // the first one, silently dropping every entry after this point.
    "rem:q-ns-research-programme",
    "thm:q-ns-wellposedness",
  ],
  cites: ["cardona2021"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped after owner ruling Q1 ($\\varTheta = f\\,\\xi^\\flat$, " +
        "2026-10-13).** Withdrawn sentences, verbatim: \"The Levi form " +
        "condition number isolates this contact degeneracy; it is the exact " +
        "metric property that the $q$-deformation corrects. The quantum pressure " +
        "term acts as an isotropic buffer preventing the Levi eigenvalues from " +
        "crossing zero.\"; programme item 2, \"The Levi degeneracy conjecture " +
        "isolates whether a given vortex collision targets the metric-Riemannian " +
        "(regular) limit, where the contact form dies and the flow flattens, or " +
        "the contact (blowup) limit, where the metric isolates non-degenerate " +
        "dynamics. The Biot–Savart and hyperbolic overlap remarks frame these " +
        "regimes explicitly as ODEs.\"; and the closing clause \"or triggers a " +
        "contact-degenerate singularity\". Reason: in dimension 3 the Levi datum " +
        "is the scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$ (no eigenvalues, no " +
        "condition number), the blow-up branch (A) of `conj:levi-degeneracy` is " +
        "withdrawn, and the Townsend ODEs describe core shape, not Levi data. " +
        "Item 2 is restated on the surviving branch (B). The regime table is " +
        "untouched and was not re-examined here. Bean `qou-fm7s`.",
    },
  ],
  tags: [
    "q-deformation",
    "contact-geometry",
    "metric-change",
    "reeb",
    "miranda",
    "fluid-dynamics",
  ],
});
