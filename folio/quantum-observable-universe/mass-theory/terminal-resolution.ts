import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body:
        "**Restated (issue #8893).** This block used to read *\"the hadronic " +
        "masses are determined without free parameters\"* over a table whose " +
        "proton, neutron, deuteron and binding rows equalled CODATA. Its Lean " +
        "sibling set the substrate parameter to `1.1097` and the QOU masses to " +
        "the CODATA values, then proved each matched itself. The proton and " +
        "neutron rows took the mean nucleon mass as an input through " +
        "$\\bar\\mu \\approx M_N/3$, and the deuteron and binding rows were not " +
        "derived anywhere. The statement now gives only what the pair Skein " +
        "formula determines: the splitting identity, and the invertibility of " +
        "the nucleon map. Invertibility is the reason the old table could not " +
        "test anything.",
    },
    {
      kind: "note",
      body:
        "Lean sibling over a generic field (AGENTS.md §7c). The square root is " +
        "avoided by writing $q = s^2$.",
    },
  ],
  label: "prop:terminal-resolution",
  lean: { ref: "qou:QOU.MassTheory.PairSkeinNucleon.terminal_resolution",
    validation: "not_checked",
  },
  title: "Nucleon masses under the pair Skein formula",
  uses: [
    "lem:pair-skein-mass-formula",
  ],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic", "pair-skein", "convention-c"],
});
