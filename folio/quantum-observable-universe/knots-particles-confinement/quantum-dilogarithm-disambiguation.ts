import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-dilogarithm-disambiguation",
  title:
    "Quantum dilogarithm disambiguation: $\\Phi_q$ (product form) vs $-\\mathrm{Li}_2^q(-z)$ (Kashaev integration limit)",
  lean: {
    ref: "qou:QOU.BraidKnot.QuantumDilogarithm",
    validation: "not_checked",
  },
  uses: [
  ],
  cites: [],
  tags: [
    "quantum-dilogarithm",
    "kashaev-limit",
    "anti-regression",
    "li2q",
    "phi_q",
    "disambiguation",
    "structural-discipline",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing.** The block's content is a *refutation*: \`¬ (∀ q z : ℝ, phi_q q z = − li2_q q (−z))\`, i.e. that the Faddeev quantum dilogarithm \`Φ_q\` and the symmetric \`q\`-dilogarithm \`Li₂^q\` are **not** related by that sign flip. Both are analytic functions of a real argument, \`towerTerm\` takes an absolute value \`|V|\`, and a disambiguation between two analytic functions has no meaning over a generic commutative ring — there is nothing there to disambiguate. This block sits on the observable side of the wall by construction.`,
    },
  ],
});
