import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-central-idempotent",
  title:
    "Explicit central primitive idempotents $e_\\lambda$ via Murphy elements",
  lean: {
    ref: "qou:QOU.BraidKnot.ExplicitCentralIdempotent.explicit_central_idempotent_via_murphy",
    validation: "not_checked",
  },
  uses: [
    "prop:jucys-murphy-central-elements-qou",
    "prop:hecke-baer-star-generic",
    // conj:bring-figure-eight-depth-2-witness removed from uses[]
    // (2026-06-01 detangler Bucket-A): referenced only as numerical
    // corroboration ("verified numerically in (…)"), not a dependency
    // the idempotent construction builds on. Prose link retained.
  ],
  cites: [],
  tags: [
    "central-idempotent",
    "murphy-elements",
    "lagrange-interpolation",
    "hecke-algebra",
    "explicit-formula",
    "computability",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/explicit_central_idempotent_probe.py",
    witness: "computations/probes/explicit-central-idempotent-probe.witness.json",
    status: "verified",
  },
});
