import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:mass-comparison-table",
  label: "rem:mass-formula-validation",
  title: "Mass formula validation: source classification and isotope coverage",
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-03",
      body:
        "**No producer regenerates this block's tables.** The `computation` " +
        "block was removed here: it declared `script: " +
        "computations/q_pinning_50_digit.py` at `status: \"verified\"`, and " +
        "that script solves for `q_0` to 50 digits — it cannot emit a mass " +
        "table, and no other producer for this block resolves. The " +
        "attribution was the defect; the numbers are carried from a prior " +
        "computation that is not recoverable from the corpus.",
      see: "bean qou-lvx7",
    },
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**Undetermined, and not to be written down as if it were:** whether " +
        "the 0.04 % figure is wrong, whether it is convention-C, or where it " +
        "came from. Absence of a producer is not evidence about a " +
        "convention. What *is* established is only that `status: " +
        "\"verified\"` was unsupported. Do **not** write a producer fitted to " +
        "reproduce 0.04 % — that manufactures provenance for a number of " +
        "unknown origin, which is worse than the missing producer.",
      see: "bean qou-lvx7",
    },
  ],
  tags: [
    "mass",
    "validation",
    "isotope",
    "CODATA",
    "AME2020",
    "certificate",
    "hecke-engine",
  ],
  uses: [
    "rem:mass-comparison-table",
  ],
  cites: [
    "kerov1996",
  ],
});
