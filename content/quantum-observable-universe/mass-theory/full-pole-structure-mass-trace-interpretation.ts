import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:full-pole-structure-mass-trace",
  label: "rem:full-pole-structure-mass-trace-interpretation",
  title: "The Mittag-Leffler residue sum as a heuristic shadow of the Habiro expansion",
  uses: ["prop:full-pole-structure-mass-trace", "prop:gb-residue-spectral-sum"],
});
