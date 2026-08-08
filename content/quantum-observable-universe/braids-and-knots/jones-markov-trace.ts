import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:jones-markov-trace",
  lean: { ref: "qou:QOU.Braiding.JonesMarkovTrace",
    validation: "not_checked",
  },
  title: "Existence and non-degeneracy of the Markov trace (Jones, 1987)",
  tags: ["hecke-algebra", "markov-trace", "jones-polynomial", "external-proof"],
  uses: ["prop:braid-action-tensor", "prop:braiding-eigenvalue-extraction"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body: "**A false attribution was corrected here.** The block asserted that $\\mathrm{tr}_M(\\rho_n(\\beta))$ computes the Jones polynomial of the closure up to framing, while axiom 3 stipulates $z = 1/(q^{1/2}+q^{-1/2})$. That value is convention **C** of the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md), whose three-row weight $y_{(1^3)}$ is non-zero; the Jones polynomial is convention **D** ($y_{(1^3)} = 0$, $z = q^3/(q^2+1)$). The two functionals differ on an explicit braid — 195.82 ppm on $\\beta_{\\mathrm{Bor}}$, with $D \\neq C$ Lean-proved — so they cannot both compute that closure's Jones polynomial. The statement now names the family member selected by $z$. The stipulated $z$ itself was **not** changed: this block and `rem:markov-axioms-primitive` are the corpus's two C pins and are registered together in the registry, so any future move to D must change both, and that move is the reserved owner decision of bean `qou-3qrv`.",
      see: "docs/audits/2026-08-08-markov-axioms-naming-vs-z-value.md",
    },
  ],
});
