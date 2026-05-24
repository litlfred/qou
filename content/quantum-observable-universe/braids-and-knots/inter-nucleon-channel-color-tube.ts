import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:inter-nucleon-channel-color-tube",
  title: "Inter-nucleon Hecke channel assignment from Bring color-tube weighting",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.InterNucleonChannelColorTube",
    validation: "not_checked",
  },
  uses: [
    // Existing color-tube infrastructure (Bring's surface):
    "def:color-tube-coordinates",
    "def:color-tube-fibers",
    "def:color-tube-cubic",
    // Categorical class supplier (PR #1081 Task 3):
    "conj:s5-so3-fiber-action",
    // Hecke quadratic relating sigma / sigma^-1 / averaged:
    "def:hecke-algebra-h-n",
    // Existing knot-operator catalogue this block refines:
    "def:knot-operator-energy",
    "def:atom-knot-exists",
    // The proton/neutron quark-flavor sheets:
    "rem:categorical-proton",
    "rem:categorical-neutron",
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
