import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:golden-ratio-degeneration",
  label: "rem:golden-ratio-transport",
  title:
    "Parallel transport of a golden-ratio parallelogram to $q_{\\mathrm{gold}}$",
  tags: [
    "golden-ratio",
    "parallel-transport",
    "q-connection",
    "elliptic-curve",
    "information-theory",
    "degeneration",
  ],
  uses: [
    "rem:golden-ratio-degeneration",
    "prop:descartes-elliptic-curve",
    "def:categorical-q-connection",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "ex:q-reeb-flow",
    "prop:local-substrate-q",
  ],
});
