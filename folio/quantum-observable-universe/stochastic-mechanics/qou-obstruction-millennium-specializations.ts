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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which is proved outright ([`collatz_obstruction_link.lean`](../lean/QOU/AlgebraicSubstrate/collatz_obstruction_link.lean)),\n\nis therefore refuted by the framework's own arithmetic, machine-checked in [`ObstructionVerdictCap`](../lean/QOU/Information/ObstructionVerdictCap.lean)." },
    {
      kind: "refined-framing",
      date: "2026-08-15",
      body:
        "Proportionality was stated here as a **consequence** of `dim HH² = 1`, " +
        "contradicting `conj:qou-p-neq-np`, which calls it \"part of the " +
        "conjecture, not a consequence of it\". The latter is correct: " +
        "one-dimensionality is a property of the **source** HH² ≅ k (the " +
        "common domain of the three restriction maps), so it pins each image " +
        "within its own target but cannot make images in three different " +
        "groups proportional to each other — that is not well-typed. " +
        "Corrected, and the disagreement between restrictions is now stated " +
        "concretely (level-2 vanishes at χ(A) = −6 while the resolution-tree " +
        "residue does not), with the machine-checked refutation of the " +
        "single-verdict reading in `QOU.Information.ObstructionVerdictCap`.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , and the corpus's own statement elsewhere is the correct one: the proportionality of the evaluations \"is part of the conjecture, not a consequence of it\" ([$\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q$](#conj:qou-p-neq-np))" },
  ],
});
