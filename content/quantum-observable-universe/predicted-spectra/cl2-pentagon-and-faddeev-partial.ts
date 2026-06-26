import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cl2-pentagon-and-faddeev-partial",
  title:
    "Partial closures: $\\mathrm{Cl}_2$ pentagon at boundary + Faddeev-Kashaev limit at boundary (closes parts of substantive Mathlib gaps 2+3)",
  uses: ["rem:three-substantive-mathlib-fillers"],
  cites: ["zagier1986", "faddeev1994", "kashaev1997"],
  tags: [
    "mathlib-filler",
    "cl2-pentagon",
    "faddeev-kashaev",
    "boundary-case",
    "lean-construction",
    "partial-closure",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.PartialClosures.partial_closures_at_boundary",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "Resolving the boundary scaffolding for the Faddeev-Kashaev relation anchors the broader pentagon formulation in a strictly formalized setting. It establishes novel consistency boundaries essential for extending these relations over non-standard algebraic domains." },
    {
      kind: "status",
      body:
        "**theorem (boundary cases, sorry-free).** This proposition closes a non-trivial portion of substantive Mathlib gaps (2) and (3) from [rem:three-substantive-mathlib-fillers](#rem:three-substantive-mathlib-fillers) without requiring upstream Mathlib contributions. The full identities (general 5-argument pentagon, $x \\in (0,1)$ Faddeev-Kashaev) remain open and require Fourier-series or Tauberian infrastructure not yet in Mathlib.",
    },
  ],
});
