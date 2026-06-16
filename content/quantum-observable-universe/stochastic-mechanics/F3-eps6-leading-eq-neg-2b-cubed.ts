import { remark } from "../../schema/builders";

export default remark({
  label: "rem:F3-eps6-leading-eq-neg-2b-cubed",
  title:
    "Lean exact-arithmetic lemma: the ε^6 leading coefficient of (F_3 − 1) at q=1+ε equals exactly −2·b(1)³ = −3√3/4 (closed proof, no sorry)",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  uses: ["prop:q-beta-c3-hopf-three-fold-markov"],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "exact-arithmetic",
    "hopf-jones",
    "epsilon-expansion",
    "class-discharge",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probe_q_beta_cat_per_factor_decomposition.py",
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "Lean stub: **closed**, no `sorry`s. Provable by Mathlib `Real.sqrt_sq` +\n`ring`. Companion to `rem:markov-axioms-primitive` in the categorical-chain\nLean infrastructure.",
    },
  ],
});
