import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-dual-space-derivation",
  title:
    "Chirality $a_K = \\prod_{pn} (1 + \\mathrm{sign}\\cdot h)$ from symmetric-channel trace duality",
  lean: {
    ref: "qou:QOU.BraidKnot.chirality_dual_space_derivation",
    validation: "not_checked",
  },
  uses: ["prop:chirality-writhe-ribbon-derivation"],
  tags: [
    "chirality",
    "dual-space",
    "wedderburn",
    "symmetric-channel",
    "per-crossing",
    "term-5",
    "derivation",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
