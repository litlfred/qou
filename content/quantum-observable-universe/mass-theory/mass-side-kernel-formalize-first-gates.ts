import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-side-kernel-formalize-first-gates",
  title:
    "Mass-side $\\S 4$ formalize-first gates as parametric Lean classes — `MassSideKernel` bundles anchor-stability, q=1 shadow (open gap), and direction sanity for any `linking_weight` candidate $w(q)$; mirrors the Q_$\\beta$ `BarEvenKernel` typeclass from PR #1893",
  lean: {
    ref: "qou:QOU.Mass.MassSideKernelFormalize.MassSideKernel",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-bar-even-kernel-typeclass",
    "prop:q-beta-radius-of-convergence-gate",
    "prop:q-beta-q-eq-one-shadow-gate",
    "prop:q-beta-direction-sanity-gate",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  tags: [
    "mass-theory",
    "linking-weight",
    "structural",
    "formalize-first",
    "parametric-typeclass",
    "kernel-invariant",
    "no-fit",
  ],
});
