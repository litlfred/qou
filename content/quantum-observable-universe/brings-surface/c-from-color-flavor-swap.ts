import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:c-from-color-flavor-swap",
  title:
    "Charge conjugation $C$ as the color-sheet flavor-swap $u \\leftrightarrow \\bar u$, $d \\leftrightarrow \\bar d$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.CFromColorFlavorSwap",
    validation: "not_checked",
  },
  uses: [
    "prop:inter-nucleon-channel-color-tube",
    "prop:cpt-orbit-closure-density",
    "def:bar-involution",
  ],
  cites: [
    "kashiwara1991",
    "khovanov-lauda2009",
    "wigner1937",
  ],
  tags: [
    "charge-conjugation",
    "color-tube",
    "duality-d6",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
