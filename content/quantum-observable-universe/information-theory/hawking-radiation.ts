import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hawking-radiation",
  title: "Hawking radiation as degree $\\geq 1$ leakage",
  tags: [
    "hawking-radiation", "jet-horizon", "event-horizon",
    "black-hole", "thermal-radiation",
  ],
  interprets: "def:jet-horizon",
  uses: [
    "def:jet-horizon",
    "def:operational-entropy",
  ],
  cites: ["hawking1975", "bekenstein1973"],
});
