import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:inter-nucleon-channel-color-tube",
  title: "Inter-nucleon Hecke channel assignment from Bring color-tube weighting",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.InterNucleonChannelColorTube",
    validation: "not_checked",
  },
  uses: [
    "def:color-tube-fibers",
    "def:hecke-normal-form",
    "prop:atom-knot-exists",
    "def:categorical-neutron",
  ]` (validation would fail).  Once PR #1081
    // creates the block, add it here and promote this conjecture
    // to a `proposition` with §3b-cond conditional-class banner.
  ],
  cites: [
    "kashaev1997",
    "faddeev1996",
    "ohtsuki2002",
    "khovanov-lauda2009",
    "kashiwara1991",
  ],
  tags: [
    "color-tube",
    "channel-assignment",
    "inter-nucleon",
    "bring-surface",
    "s5-so3-fiber",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
