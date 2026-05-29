import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:p-from-braid-mirror",
  title:
    "Parity $P$ as mirror reflection of the braid diagram (writhe sign flip)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PFromBraidMirror",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
    "prop:cpt-orbit-closure-density",
    "prop:chirality-writhe-ribbon-derivation",
  ],
  cites: [
    "kassel1995",
    "jones1987",
    "kauffman1991",
  ],
  tags: [
    "parity",
    "duality-d7",
    "braid-mirror",
    "writhe",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
