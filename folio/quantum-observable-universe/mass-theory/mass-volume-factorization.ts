import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-volume-factorization",
  title:
    "Mass-volume factorization of the categorical mass endomorphism",
  tags: [
    "tier:S",
    "mass-endomorphism",
    "hyperbolic-volume",
    "density",
    "frobenius-packing",
    "jsj-decomposition",
    "categorical-action",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.MassVolumeFactorization",
    validation: "not_checked",
  },
  // `rem:frobenius-packing-density` removed 2026-08-15 to break an editorial
  // cycle. That remark declares `interprets: "conj:mass-volume-factorization"`
  // — it exists to interpret this conjecture — so requiring it here made the
  // conjecture a prerequisite of its own interpretation. `interprets` carries
  // the relation in the direction that is true.
  uses: [
    "prop:thurston-volume-additivity",
  ],
  cites: ["thurston1978", "murakami-murakami2001"],
  computation: {
    engine: "closed-form",
    script: "computations/d_density_derivation.py",
    witness: "computations/d-density-derivation.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `mass-theory/mass-volume-factorization.lean` " +
        "carries `volume : K → ℝ` (a hyperbolic volume) and `mass : K → ℝ` together in one factorisation. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
