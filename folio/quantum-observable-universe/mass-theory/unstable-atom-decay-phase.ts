import { remark } from "../../schema/builders";

/**
 * Decay-channel selection, the phase-boundary shadow-price condition,
 * and the phase-interior interpolation shortcut for an unstable atom.
 */
export default remark({
  label: "rem:unstable-atom-decay-phase",
  title: "Decay channel, phase boundary, and phase-interior shortcut",
  interprets: "def:unstable-atom",
  uses: [
    "def:unstable-atom",
    "def:stable-atom",
    "prop:mass-endomorphism-tower",
  ],
  tags: [
    "decay",
    "phase-boundary",
    "ilp",
    "shadow-price",
  ],
});
