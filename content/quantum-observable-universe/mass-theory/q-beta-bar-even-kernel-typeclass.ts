import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-bar-even-kernel-typeclass",
  title:
    "$Q_\\beta$ formalize-first unified typeclass — `BarEvenKernel` bundles all four $\\S 4$ invariants (bar-even, radius-of-convergence, q=1 shadow, direction sanity) into one parametric Lean typeclass so any future kernel candidate $F(q)$ becomes a single class-instance attempt",
  lean: {
    ref: "qou:QOU.QBeta.BarEvenKernelTypeclass.BarEvenKernel",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-radius-of-convergence-gate",
    "prop:q-beta-q-eq-one-shadow-gate",
    "prop:q-beta-direction-sanity-gate",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "formalize-first",
    "unified-typeclass",
    "kernel-invariant",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "status",
      body:
        "**Theorem (this proposition).** Sorry-free Lean class definition " +
        "(`q-beta-bar-even-kernel-typeclass.lean`) with three lifting lemmas " +
        "(`bar_even_kernel_implies_q_one_shadow`, " +
        "`bar_even_kernel_implies_direction_sanity`, " +
        "`bar_even_kernel_implies_radius_of_convergence`). Pure Lean " +
        "infrastructure; no sympy probe — the structural content is captured " +
        "by the type definitions.",
    },
  ],
});
