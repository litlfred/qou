import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:qou-obstruction-reduction",
  label: "rem:qou-obstruction-millennium-specializations",
  title:
    "RH, NS and BSD as specializations of the single obstruction class",
  uses: [
    "thm:qou-obstruction-reduction",
    "tbl:qou-obstruction-reduction-table4-data",
    "conj:qou-p-neq-np",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-15",
      body:
        "Proportionality was stated here as a **consequence** of `dim HH² = 1`, " +
        "contradicting `conj:qou-p-neq-np`, which calls it \"part of the " +
        "conjecture, not a consequence of it\". The latter is correct: " +
        "one-dimensionality of the target constrains the class, not the images " +
        "of three different restriction maps into three different groups. " +
        "Corrected, and the disagreement between restrictions is now stated " +
        "concretely (level-2 vanishes at χ(A) = −6 while the resolution-tree " +
        "residue does not), with the machine-checked refutation of the " +
        "single-verdict reading in `QOU.Information.ObstructionVerdictCap`.",
    },
  ],
});
