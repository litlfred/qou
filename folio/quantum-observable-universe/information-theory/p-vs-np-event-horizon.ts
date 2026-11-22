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
  cites: ["arxiv-1301.4504v4"],
  uses: [
    "rem:hawking-radiation",
    "def:big-bang-state",
  ],
});
