import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:isovector-chiral-residue",
  title: "Binding isovector coefficient as the $W_\\lambda$ chiral residue (conditional)",
  uses: [
    "prop:mirror-baseline-cancellation",
    "prop:chirality-residue-mass-term",
    "rem:archimedean-chirality",
  ],
  lean: {
    ref: "qou:QOU.BraidsAndKnots.BraidKnot.binding_isovector_mirror_from_chiral",
  },
  tags: [
    "delta-lambda",
    "isovector",
    "chirality",
    "bring-surface",
    "conditional",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Relocated intact from `appendix-mass-binding-algorithms/mba-sidecar-isovector-chiral-residue` to Chapter 12 (`nuclear-interactions`) under `qou-mba8`, preserving label `prop:isovector-chiral-residue`. Consequence: once chiral weight $\\kappa$ is fixed by `BWVacuumRowIsHecke`, the mirror slope $b = 4\\kappa$ is parameter-free and unfitted.",
    },
  ],
});
