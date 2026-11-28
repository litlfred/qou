import { remark } from "../../schema/builders";

export default remark({
  label: "rem:p-vs-np-event-horizon",
  title: "Analogy between black-hole jet horizons and computational witness verification",
  interprets: "conj:p-vs-np-boundary",
  uses: [
    "conj:p-vs-np-boundary",
    "quantum-observable-universe:def:jet-horizon",
  ],
  cites: ["arxiv-1301.4504v4"],
  tags: ["P-vs-NP", "event-horizon", "jet-horizon", "dictionary"],
});
