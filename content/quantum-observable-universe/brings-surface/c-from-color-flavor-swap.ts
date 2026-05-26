import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:c-from-color-flavor-swap",
  title:
    "Charge conjugation $C$ as the color-sheet flavor-swap $u \\leftrightarrow \\bar u$, $d \\leftrightarrow \\bar d$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.CFromColorFlavorSwap",
    validation: "not_checked",
  },
  uses: [
    // The just-merged color-tube channel-assignment conjecture
    // (PR #1111) supplies the framework for flavor-content on color
    // sheets:
    "conj:inter-nucleon-channel-color-tube",
    // The existing color-tube infrastructure on Bring's surface:
    "def:color-tube-coordinates",
    "def:color-tube-fibers",
    // The CPT composite that this block decomposes:
    "prop:cpt-orbit-closure-density",
    // The categorical proton/neutron sheets:
    "def:categorical-proton",
    "def:categorical-neutron",
    // Bar-involution is the framework's existing duality; this
    // block disentangles C from CPT:
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
