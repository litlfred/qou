import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-from-braid-mirror",
  title:
    "Parity $P$ as mirror reflection of the braid diagram (writhe sign flip)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PFromBraidMirror",
    validation: "not_checked",
  },
  uses: [
    "prop:cpt-d6-d7-d8-closure",
    "def:bar-involution",
    "conj:cpt-orbit-closure-density",
    "prop:chirality-writhe-ribbon-derivation",
  ],
  cites: [
    "kassel1995",
    "jones1987",
    "kauffman1991",
  ],
  tags: [
    "tier:S",
    "parity",
    "duality-d7",
    "braid-mirror",
    "writhe",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
