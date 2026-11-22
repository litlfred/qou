import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:descent-cocycle-deviation",
  lean: { ref: "qou:QOU.LiftingDescent.descent_cocycle_deviation",
    validation: "not_checked",
  },
  title: "Cocycle deviation recursion at level $n+1$ (hypothesis)",
  tags: ["cocycle", "yekutieli-triple", "central-extension", "cech-cohomology"],
  uses: ["def:yekutieli-triple"],
  proofs: ["prf:descent-cocycle-deviation"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "**Statement restated 2026-11-22 to what the Lean proves (owner ruling, round-trip pass 3).** The Lean theorem's body is `ctx.claim_cocycle_deviation n i j k`: the recursion is a field of `DescentCocycleContext` and the theorem returns it. So the statement is now the recursion stated as a hypothesis, with no derived content. The former statement also asserted a twisted Čech 2-cocycle equation `d(g) = a_ij · g · a_jk⁻¹` and a class in H²(M, O_M^×); the audit found that equation ill-formed (`d` of a 2-cochain is a 3-cochain, but the right side is indexed by a triple), and the Lean only carries it as a second field (`claim_cech_cocycle`) that nothing uses. Both were dropped. Whether this block should stay a lemma is open. Found by the blind round-trip audit (docs/audits/2026-11-22-roundtrip-blind-audit-pass3.md, block P15).",
    },
  ],
});
