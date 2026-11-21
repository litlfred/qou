import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body:
        "**Moved to convention D (issue #8923).** The statement used the " +
        "convention-C normaliser $1/(q^{1/2}+q^{-1/2})$. It now uses the " +
        "canonical frame $z = q^3/(q^2+1)$: $\\mathcal{S}_{ab} = " +
        "(q^2\\mu_a + q^{-2}\\mu_b)/[2]_q$, the splitting coefficient is " +
        "$[4]_q/[2]_q^2$, and the bijection is unchanged. Lean: " +
        "`terminal_resolution_conventionD`, sorry-free over a generic field.",
    },
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
        "Lean sibling over a generic field (AGENTS.md §7c). The convention-C " +
        "theorems are kept, written in $s$ with $q = s^2$; the convention-D " +
        "theorems reuse them at $s := q$.",
    },
  ],
  label: "prop:terminal-resolution",
  lean: { ref: "qou:QOU.MassTheory.PairSkeinNucleon.terminal_resolution_conventionD",
    validation: "not_checked",
  },
  title: "Nucleon masses under the pair Skein formula",
  uses: [
    "lem:pair-skein-mass-formula",
  ],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic", "pair-skein", "convention-d"],
});
