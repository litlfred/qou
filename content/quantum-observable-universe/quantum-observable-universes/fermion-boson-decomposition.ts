import { definition } from "../../schema/builders";

export default definition({
  label: "def:fermion-boson-decomposition",
  title: "Fermion--Boson decomposition",
  tags: ["fermion", "boson", "particle"],
  lean: { ref: "qou:QOU.Fermion",
    validation: "leanok",
  },
  uses: ["def:q-harmonic-form"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/fermion-boson-decomposition-0.svg", blockIndex: 0, hash: "e2cd03af6567" },
    { mime: "image/svg+xml", url: "rendered/fermion-boson-decomposition-1.svg", blockIndex: 1, hash: "468ace28c05e" },
  ],

  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `quantum-observable-universes/fermion-boson-decomposition.lean` " +
        "imports `Mathlib.Analysis.SpecialFunctions.Pow.Real` and `Mathlib.Topology.*` — the decomposition is analytic, not merely additive. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
