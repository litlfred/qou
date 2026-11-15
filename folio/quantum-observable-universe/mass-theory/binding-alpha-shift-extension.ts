import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-alpha-shift-extension",
  title: "Binding A≥3 via per-rep Reeb phase at a force-carrier torus knot",
  cites: ["jones1987", "wenzl1988"],
  uses: [],
  defines: [],
  tags: ["normalization", "no-fitting", "uniqueness", "binding", "alpha-shift"],
  lean: { ref: "qou:QOU.BraidKnot.binding_unique_via_alpha_shift" },
  authorNotes: [
    {
      kind: "status",
      body: "This proposition is **proved conditional on the\n`BindingPerRepReebPhase` + `BindingForceCarrierKnot` class\ninstances**.  The per-rep Reeb phase axiom is the substrate identity\n(audit-confirmed); the force-carrier knot identification per A is\nthe genuine open math.  Sorry-free Lean conditional on both classes.\n\nCloses the $A\\ge3$ binding entry in\n[`docs/uniqueness-theorems-backlog.md`](../../../docs/uniqueness-theorems-backlog.md)\nas a structurally identified item, parallel to the meson + lepton\nα_shift specialisations.",
    },
    {
      kind: "note",
      body: "Provenance: the deuteron T(2, 3) candidate identification in the Phase-3 status table was pursued in PR #1485 (the table cell formerly read \"open (#1485)\").",
    },
  ],
});
