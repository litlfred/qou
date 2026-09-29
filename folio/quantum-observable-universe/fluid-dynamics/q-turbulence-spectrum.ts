import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-turbulence-spectrum",
  lean: { ref: "qou:QOU.FluidDynamics.q_turbulence_spectrum", validation: "not_checked" },
  title: "$q$-deformed energy cascade and modified Kolmogorov spectrum",
  uses: [
    // A hypothesis of the statement, named in its first clause and used again
    // for the cascade-depth bound. It reaches the substrate parameter, the
    // block's other prose citation, so that one stays undeclared.
    "rem:planck-reynolds",
  ],
  tags: ["turbulence", "kolmogorov", "energy-cascade", "fluid-dynamics", "prediction"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-14",
      body:
        "**Claim (iii) restructured — file now sorry-free (bean `qou-octr`).** " +
        "The flat cascade-depth statement was *refutable as written* " +
        "(`finite_cascade_depth_unconstrained_false`: the context class never " +
        "related `N_modes` to `Re_q`), so its `sorry` could never be discharged " +
        "and was removed. The dissipation-cutoff hypothesis " +
        "`q^N_modes ≤ Re_q^{3/4}` is now an explicit class " +
        "(`QTurbulenceCascadeModel`), and the depth bound is derived from it " +
        "sorry-free (`finite_cascade_depth_of_cutoff`); the resolving theorem " +
        "`q_turbulence_spectrum` is conditional on that class per §3b-cond. " +
        "Verified lean-direct exit 0.",
    },
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/FluidDynamics/q_turbulence_spectrum.lean` uses " +
        "`Real.log`, `Real.rpow`. These are real-analytic constructs with " +
        "no generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
