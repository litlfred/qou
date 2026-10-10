import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:single-volume-irrationality",
  title: "Irrationality of a single hyperbolic knot volume",
  lean: { ref: "qou:QOU.Archimedean.SingleVolumeIrrationality", validation: "stub" },
  tags: [
    "tier:famous",
    "irrationality",
    "hyperbolic-volume",
    "bloch-wigner",
    "clausen-function",
    "open-problem",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/Archimedean/SingleVolumeIrrationality.lean` " +
        "states irrationality of a hyperbolic volume — a transcendence statement about a real number. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
