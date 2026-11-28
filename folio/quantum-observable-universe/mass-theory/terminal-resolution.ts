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
        "Lean sibling over a generic field (AGENTS.md §7c). Re-stated under " +
        "convention D on 2026-11-28 (owner ruling 2026-11-27): the pair Skein " +
        "mass is $(q^3\\mu_a + q^{-1}\\mu_b)/(q^2+1)$, so no square root " +
        "appears. The determinant is $3\\kappa^2$ with $\\kappa$ the sum of the " +
        "two crossing weights, the same shape as under the retired convention C.",
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
  tags: ["mass", "hadronic", "pair-skein"],
});
