import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:reeb-exceptional-divisor",
  label: "rem:julia-set-reeb",
  title: "Julia set of the Reeb flow on the exceptional divisor",
  tags: [
    "julia-set",
    "reeb",
    "exceptional-divisor",
    "golden-ratio",
    "hausdorff-dimension",
    "information-theory",
    "photon",
  ],
  uses: [
    "rem:reeb-exceptional-divisor",
    "rem:golden-ratio-degeneration",
  ],
});
