import { definition } from "../../schema/builders";

export default definition({
  label: "def:computational-horizon",
  title: "Computational horizon",
  tags: [
    "computational-horizon",
    "jet-horizon",
    "P-vs-NP",
    "complexity",
    "information-barrier",
    "turing-machine",
    "planck-step",
  ],
  lean: { ref: "qou:QOU.ComputationalHorizon",
    validation: "not_checked",
  },
  uses: [
    "def:jet-horizon",
    "rem:skein-turing-machine",
    "def:information-speed-of-light",
  ],
});
