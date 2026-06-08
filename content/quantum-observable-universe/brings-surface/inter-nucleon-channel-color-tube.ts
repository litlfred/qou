import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:inter-nucleon-channel-color-tube",
  title: "Inter-nucleon Hecke channel assignment from Bring color-tube weighting",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.InterNucleonChannelColorTube",
    validation: "not_checked",
  },
  // Note: the s5-so3-fibre-action conjecture is cited in the narrative
  // only — it is not yet a content block, so it is omitted from uses[]
  // (an unresolved ref would fail validation). Add it here once the
  // block exists.
  uses: [
    "def:color-tube-fibers",
    "def:hecke-normal-form",
    "prop:atom-knot-exists",
  ],
  cites: [
    "kashaev1997",
    "faddeev1996",
    "ohtsuki2002",
    "khovanov-lauda2009",
    "kashiwara1991",
  ],
  tags: [
    "tier:keystone",
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
