import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:confinement-level",
  label: "rem:ilp-solution-count-unwrap",
  title:
    "ILP solution count determines unwrap depth via confinement level",
  tags: [
    "ilp",
    "solution-count",
    "unwrap-depth",
    "confinement",
    "computational-shortcut",
  ],
  uses: ["prop:stable-atom-decidable"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-29",
      body:
        "**$N_\\ell = 84$ is an unsourced figure.** This block reports that " +
        "the proton's 9-crossing element admits 84 feasible ILP solutions. " +
        "Nothing in the corpus computes it. This block declares no " +
        "`computation:`, nor does `prop:stable-atom-decidable`, which it " +
        "uses. The one named source, " +
        "`docs/audits/2026-05-27-mass-formula-uniqueness-argument.md` §C5, " +
        "cites `mass-endomorphism.witness.json` — a file that exists but " +
        "contains **zero** fields equal to 84 and **zero** keys naming " +
        "ilp/solution/feasible/count/gluon, and whose subject is a $\\Phi_q$ " +
        "tower endomorphism recording a 407 % error against CODATA. The only " +
        "ILP-counting code in the corpus is a deprecated magic-number " +
        "heuristic capped at 3, orphaned. " +
        "This is **not** a claim that 84 is wrong: an exhaustive enumeration " +
        "may have been run and recorded by hand. It is a statement that the " +
        "figure cannot presently be checked, so a computation disagreeing " +
        "with it cannot be interpreted either. Two independent readings of " +
        "the quantity were tried on branch `qou-vtlj` and neither reproduces " +
        "it. Probe: `qbeta_nl84_provenance_probe.py` (4/4).",
    },
  ],
});
