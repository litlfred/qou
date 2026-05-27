import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:inter-nucleon-channel-color-tube",
  title: "Inter-nucleon Hecke channel assignment from Bring color-tube weighting",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.InterNucleonChannelColorTube",
    validation: "not_checked",
  },
  uses: [
    // Existing color-tube infrastructure (Bring's surface):
    "def:color-tube-coordinates",
    "def:color-tube-fibers",
    "rem:color-tube-cubic",
    // Hecke quadratic relating sigma / sigma^-1 / averaged:
    "def:hecke-normal-form",
    // Existing knot-operator catalogue this block refines:
    "def:knot-operator-energy",
    "prop:atom-knot-exists",
    // The proton/neutron quark-flavor sheets:
    "def:categorical-proton",
    "def:categorical-neutron",
    // The categorical class supplier `conj:s5-so3-fiber-action`
    // (PR #1081 Task 3) is cited in the narrative cross-reference
    // only — it has not yet landed as a content block, so it is
    // not in `uses[]` (validation would fail).  Once PR #1081
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
