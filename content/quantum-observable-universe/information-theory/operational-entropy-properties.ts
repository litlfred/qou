import { remark } from "../../schema/builders";

export default remark({
  label: "rem:operational-entropy-properties",
  interprets: "def:operational-entropy",
  title: "Hausdorff dimension, self-consistency, and regimes of $\\eta_q$",
  tags: [
    "information-theory",
    "metric-entropy",
    "julia-set",
    "hausdorff-dimension",
    "manning-mccluskey",
    "golden-ratio",
  ],
  uses: [
    "def:operational-entropy",
    "def:gravitational-constant",
    "prop:reeb-operations-per-planck",
    "def:planck-time",
    "rem:julia-set-reeb",
    "rem:golden-ratio-degeneration",
  ],
});
