import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-event-horizon",
  title:
    "P versus NP through the event horizon: information loss and computational irreversibility",
  interprets: "conj:p-vs-np-boundary",
  tags: [
    "P-vs-NP",
    "event-horizon",
    "information-loss",
    "hawking-radiation",
    "computational-irreversibility",
    "planck-step",
    "turing-machine",
    "information-flow",
  ],
  uses: [
    "conj:p-vs-np-boundary",
    "def:computational-horizon",
    "def:jet-horizon",
    "rem:hawking-radiation",
    "rem:skein-turing-machine",
    "def:operational-entropy",
    "prop:information-speed-of-light",
    "rem:jet-planck-steps",
    "def:big-bang-state",
  ],
});
