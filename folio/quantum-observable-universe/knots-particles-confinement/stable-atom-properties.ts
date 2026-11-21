import { remark } from "../../schema/builders";

/**
 * Derived properties of the stable-atom ILP condition: pointwise
 * (fixed-$q$) independence of neighborhood, the strict-strengthening
 * relation to the LP relaxation, and the confinement-filtration scope.
 */
export default remark({
  label: "rem:stable-atom-properties",
  title: "Properties of ILP stability",
  interprets: "def:stable-atom",
  uses: [
    "def:stable-atom",
    "def:confinement-level",
    "prop:mass-endomorphism-tower",
  ],
  tags: [
    "stability",
    "ilp",
    "lp-dual",
    "frobenius-positivity",
    "confinement",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-29",
      body:
        "**Names a different proton stabiliser than " +
        "`rem:categorical-proton-properties` does.** This block says the ILP " +
        "search adjoining $\\{\\sigma_0, \\sigma_1, L_+, L_-\\}$ finds " +
        "*\"the unique integer solution $\\sigma_0 \\to \\sigma_0$ (2 gluon " +
        "crossings)\"*; `categorical-proton-properties` says *\"a single Hopf " +
        "link $L_- = \\sigma_1\\sigma_0$ is the minimum additional " +
        "structure capable of restoring stability\"*. The crossing **count** " +
        "agrees at two; the **operator** does not. Recorded, not " +
        "adjudicated — neither block cites a computation for its choice, and " +
        "no producer in the corpus enumerates the search. Bean `qou-vtlj`; " +
        "adjudication belongs to `qou-bg3w`.",
    },
    {
      kind: "caveat",
      date: "2026-08-29",
      body:
        "**The $N_\\ell = 84$ figure this chapter relies on is unsourced.** " +
        "`rem:ilp-solution-count-unwrap` reports 84 feasible ILP solutions " +
        "for the proton's 9-crossing element. Neither that block nor " +
        "`prop:stable-atom-decidable` declares a `computation:`; the one " +
        "named source, `docs/audits/2026-05-27-mass-formula-uniqueness-" +
        "argument.md` §C5, cites `mass-endomorphism.witness.json`, which " +
        "exists but contains **zero** fields equal to 84 and **zero** keys " +
        "naming ilp/solution/feasible/count/gluon (its subject is a $\\Phi_q$ " +
        "tower endomorphism recording a 407 % error). The only ILP-counting " +
        "code in the corpus is a deprecated magic-number heuristic capped at " +
        "3. This does **not** claim 84 is wrong — an exhaustive enumeration " +
        "may have been run and recorded by hand — only that nothing now " +
        "reproduces it, so it cannot be checked. Probe: " +
        "`qbeta_nl84_provenance_probe.py`.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The proton derivation in [mass-endomorphism-tower](#prop:mass-endomorphism-tower) shows that the $9$-crossing element $\\mathcal{B}_3 \\times \\Delta_3(\\mathfrak{u}\\mathfrak{u}\\mathfrak{d})$ violates Frobenius positivity (it is LP-infeasible at integer values). An ILP search adjoining $\\{\\sigma_0, \\sigma_1, L_+, L_-\\}$ finds the unique integer solution $\\sigma_0 \\to \\sigma_0$ ($2$ gluon crossings) that restores stability." },
  ],
});
