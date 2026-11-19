import { conjecture } from "../../schema/builders";

/**
 * Complex-mass constituent functional (formalize-first scaffold).
 *
 * Generalizes the real volume mass reading in two ways: (1) real volume
 * Vol(K) -> complex volume Vol(K) + i*CS(K) (Chern-Simons the imaginary
 * partner already used for alpha_EM), physical mass = real part, imaginary
 * part = confinement/instability scale; (2) per-knot scalar -> spectrum of a
 * single complex-mass functional 𝔐 on the composite's Hecke module, quark
 * masses = real parts of its Frobenius-block projections, with the
 * generation blocks tied by the fixed Morgan-Voyce continuant ratio
 * (no per-flavour tuning) and the light doublet as the single anchor.
 *
 * PRIMARY conjecture, OPEN: the Lean class carries the winding-tower law +
 * light-doublet anchor as content fields and has NO instance; the sorry-free
 * conditional theorem charm_block_determined shows the scaffold is
 * non-degenerate (charm block determined by the up block via contRatio(5)).
 * Subgoal-2 research; anti-fit discipline gates how it may be closed.
 */
export default conjecture({
  label: "conj:complex-mass-constituent-functional",
  title: "Complex-mass constituent functional",
  uses: ["def:flavor-dressing-functor", "rem:chern-simons-as-knot-invariant"],
  lean: { ref: "qou:QOU.MassTheory.ComplexMassConstituent" },
  computation: {
    engine: "python",
    script: "computations/charm_mass_tower_probe.py",
    witness: "computations/charm-mass-tower.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      body: "Status: OPEN (primary conjecture / Subgoal-2 formalize-first scaffold). Anti-fit discipline: M must be derived from the Frobenius pairing tr_M = sum_lambda y_lambda chi_lambda rather than inverted from empirical quark-mass anchors.",
    },
    {
      kind: "caveat",
      date: "2026-08-02",
      body:
        "Derive-then-check negative: the plain-continuant-ratio reading " +
        "`contRatio = b_n/b_{n-2}` is scope-(a) refuted at the substrate as " +
        "the sole hierarchy mechanism — it gives a nearly geometric " +
        "~5.85x-per-generation ladder that matches neither the current-mass " +
        "(mc/mu~577, undershoot ~100x) nor the constituent-mass (~4.46, " +
        "overshoot ~30%) charm/light hierarchy. See " +
        "`docs/audits/2026-08-02-charm-mass-tower-negative.md`. The Lean " +
        "class does NOT assert that identification; a viable `contRatio` must " +
        "be steeper than the continuant ratio or carried by the complex-volume " +
        "/ Chern-Simons imaginary part. `m_c` remains open.",
    },
  ],
});
