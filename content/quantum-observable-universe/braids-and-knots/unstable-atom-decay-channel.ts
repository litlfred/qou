import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unstable-atom-decay-channel",
  title: "Unstable atom has a uniquely-determined decay channel",
  lean: {
    decl: "QOU.BraidKnot.UnstableAtom.decay_channel",
    validation: "not_checked",
  },
  uses: [
    "def:unstable-atom",
    "def:stable-atom",
    "def:knot-operator-energy",
  ],
  tags: ["decay", "instability", "ilp", "phase-boundary"],
});
