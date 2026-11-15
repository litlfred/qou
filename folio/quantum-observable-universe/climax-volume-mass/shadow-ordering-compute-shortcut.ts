import { remark } from "../../schema/builders";

export default remark({
  label: "rem:shadow-ordering-compute-shortcut",
  title: "Computational shortcut from local constancy",
  interprets: "def:local-shadow-ordering",
  uses: [
    "def:local-shadow-ordering",
    "def:unstable-atom",
    "prop:phase-boundary-variety",
    "prop:confinement-local-constancy",
  ],
  tags: [
    "computational-shortcut",
    "local-constancy",
    "phase-boundary",
    "interpolation",
  ],
});
