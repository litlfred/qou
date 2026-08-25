import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:h2o-bond-angle-shift",
  title: "Bent angle as a quadratic-well shift",
  lean: {
    ref: "qou:QOU.Molecular.bond_angle_shift",
    validation: "not_checked",
  },
  uses: ["def:h2o-molecular-braid"],
  tags: ["water", "H2O", "bond-angle", "quadratic", "harmonic", "lone-pair"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The `ℝ` of `h2o-bond-angle-shift.lean` are a **bond angle and a " +
        "bending stiffness**: `bond_angle_shift (a θ₀ s θ : ℝ) (ha : 0 < a)` " +
        "locates the minimum of the harmonic bending energy `a(θ-θ₀)² + " +
        "(2as)·θ` at `θ₀ - s`, and the block's content is the water " +
        "molecule's `109.5° → 104.5°` reduction, with the file's own " +
        "docstring recording that \"the magnitude `s = b/(2a)` is the " +
        "compute/experimental input\". A continuous physical angle is `ℝ` by " +
        "meaning, as the photon-polarisation parameters of " +
        "`confinement-universality` and the time parameter of " +
        "`q-heat-equation` are, so the block sits on the archimedean side of " +
        "the §7c wall by construction.",
    },
  ],
});
