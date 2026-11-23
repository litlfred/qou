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
    "prop:reeb-operations-per-planck",
    "def:planck-time",
    "rem:julia-set-reeb",
    "rem:golden-ratio-degeneration",
    "rem:operational-entropy-self-consistency",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Gravitational self-consistency forces this formula, without fitting ([operational entropy is forced by self-consistency](#rem:operational-entropy-self-consistency))." },
  ],
});
