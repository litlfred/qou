import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-holonomy",
  lean: { ref: "qou:QOU.LiftingDescent.tm_descended_is_holonomy",
    validation: "not_checked",
  },
  title: "Descended term is the unknot-core holonomy",
  tags: ["holonomy", "ascent-embedding", "blow-up", "nonabelian-stokes"],
  uses: ["lem:topological-mass-eigenspace-decomp"],
  proofs: ["prf:topological-mass-holonomy"],
  cites: ["yekutieli2015"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-10-10",
      body:
        "**Lean scope (bean `tmvac`).** The Lean module " +
        "`lean/QOU/LiftingDescent/tm_descended_is_holonomy.lean` takes the multiplicative " +
        "integral with values in an arbitrary monoid (holonomies need not commute; the " +
        "blow-up product is ordered). Multiplicativity over the decomposition, naturality " +
        "under blow-down, collapse of the exceptional discs to points, and non-abelian " +
        "Stokes are explicit hypotheses; triviality of the exceptional-disc contributions " +
        "and the holonomy identity are derived from them. The earlier module assumed the " +
        "disc triviality directly.",
    },
  ],

});
