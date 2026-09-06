import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      date: "2026-09-06",
      body:
        "**The categorical half was an axiom that asserted nothing, and is " +
        "now a one-line theorem.** `chart_glue_from_spectrum` stood as an " +
        "`axiom` for `∃ κ : R, κ = ↑bed.lam_sym⁻¹` -- an existential whose " +
        "witness is named in its own body, so `⟨_, rfl⟩` closes it for any " +
        "`R` and any eigenvalue data. Its docstring called it *\"the wall -- " +
        "the categorical model of `O_q(P¹)` is not in Mathlib\"*. The wall is " +
        "real; the statement was never standing at it, because nothing in " +
        "the type mentions a chart, a transition map, or `P_q(V)`. The " +
        "categorical interpretation lived entirely in the prose. Deleting " +
        "the axiom removes an unearned dependency and changes no " +
        "downstream truth value -- `spectral_chart_correspondence` still " +
        "holds -- but the gap it appeared to bridge is now visible rather " +
        "than papered over.",
      see: "docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md",
    },
  ],
  label: "prop:spectral-chart-correspondence",
  title:
    "Spectral--chart correspondence: Hecke eigenspaces realise the chart-glue of $\\mathbb{P}_q(V)$",
  cites: ["kassel1995", "woronowicz1988"],
  tags: [
    "braiding",
    "eigenvalue",
    "affine-chart",
    "projective-line",
    "substrate-parameter",
    "categorical",
  ],
  lean: { ref: "qou:QOU.spectral_chart_correspondence",
    validation: "not_checked",
  },
  uses: [],
});
