import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-23",
      body:
        "Hypothesis made explicit (issue #9179): the statement needs a finite projective, symmetric " +
        "Frobenius algebra. A Frobenius form that is not symmetric gives $\\omega_A \\simeq {}_1A_\\nu$, " +
        "twisted by the Nakayama automorphism, not $A$. A finite Hopf algebra is symmetric only when it is " +
        "unimodular and $S^2$ is inner (Lorenz 2011). Sweedler's algebra is Frobenius and not symmetric.",
    },
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
  title: "Self-duality of the algebraic layer",
  lean: { ref: "qou:QOU.Core.AlgebraicSubstrate.SelfDualPairingData",
    validation: "not_checked",
  },
  uses: ["def:rigid-dualizing-complex"],
  cites: ["yekutieli2015", "kock2004", "lorenz2011",
    "yekutieli2010",
  ],
  tags: ["self-duality", "frobenius", "dualizing-complex"],
});
