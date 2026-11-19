import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "The Lean link previously pointed at `substrate_self_duality`, a wrapper around an axiom that was false: " +
        "`SelfDualPairingData` has no counit or snake laws, so `selfDualityMorphism` need not be an isomorphism " +
        "(counterexample in `Type`: A = Bool, Δ b = (true, b)). The axiom and wrapper were removed; the refutation is " +
        "`not_selfDualityMorphism_isIso_unconstrained`. The theorem as stated in prose (for a genuine Frobenius " +
        "algebra) is not yet formalised; bean `qou-n2un`.",
    },
  ],
  label: "thm:substrate-self-duality",
  title: "Self-duality of the algebraic aether",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.SelfDualPairingData",
    validation: "not_checked",
  },
  uses: ["def:rigid-dualizing-complex"],
  cites: ["yekutieli2015", "kock2004",
    "yekutieli2010",
  ],
  tags: ["self-duality", "frobenius", "dualizing-complex"],
});
