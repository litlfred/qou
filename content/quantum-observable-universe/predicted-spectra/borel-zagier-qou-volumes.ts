import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borel-zagier-qou-volumes",
  title:
    "Rational linear independence of QOU hyperbolic volumes (Borel--Zagier)",
  lean: { ref: "qou:QOU.Archimedean.BorelZagierQouVolumes", validation: "stub" },
  tags: [
    "tier:famous",
    "borel-regulator",
    "zagier-conjecture",
    "linear-independence",
    "hyperbolic-volume",
    "K-theory",
    "open-problem",
  ],
  uses: ["conj:single-volume-irrationality"],
  cites: ["borel1986", "borel1974"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/Archimedean/BorelZagierQouVolumes.lean` " +
        "states ℚ-linear independence of the hyperbolic volumes `vol(4₁)`, `vol(5₂)`, `vol(𝓑)` — a transcendence statement about real numbers. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
