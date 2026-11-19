import { remark } from "../../../schema/builders";

/**
 * Rewritten 2026-08-21 (bean qou-6y28). The original imported `Block` from
 * "../../../../../schema/block-schema" — five levels up, which leaves the
 * repository entirely, so the path has never resolved. It also exported
 * only a NAMED const, and the pipeline reads `default`, so even a working
 * import would have yielded an invisible block. Live since 1b60cb2fa2
 * (2026-08-03).
 *
 * `interprets` is set because this is a `remark` and an uninterpreted
 * remark is a dangling remark (AGENTS.md §3a). The original recorded the
 * same target under `uses`, which for a remark is the weaker relation.
 *
 * NOT wired into the chapter manifest — see the sibling note in
 * qbeta-toroidal-harmonics-basis.ts. This one is a numerical probe whose
 * AME-residual claims have never been reviewed.
 */
export default remark({
  label: "rem:wigner-su4-alpha-cluster-probe",
  title: "Numerical probe: SU(4) alpha-cluster capacity and AME residuals",
  interprets: "conj:wigner-su4-from-spin-isospin",
  tags: ["nuclear-physics", "su4", "alpha-cluster", "audit", "numerical-probe"],
  computation: {
    engine: "numpy",
    script: "computations/probes/the_alpha_spike_is_an_inverted_stagger_probe.py",
    witness: "computations/probes/the_alpha_spike_is_an_inverted_stagger_probe.witness.json",
    status: "verified",
  },
});
