import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:strangelet-crossing-energy",
  label: "rem:strangelet-witten-stability",
  title:
    "Witten's strange matter hypothesis as a crossing-energy inequality",
  tags: [
    "strangelet",
    "witten",
    "strange-quark-matter",
    "stability",
    "ground-state",
    "genus",
  ],
  uses: [
    "prop:strangelet-crossing-energy",
    "rem:golden-ratio-degeneration",
  ],
  cites: [
    "witten1984",
  ],
});
