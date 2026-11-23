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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is a\nformalize-first scaffold, not a derivation" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): No instance of the class is exhibited." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean class [`QOU.MassTheory.ComplexMassConstituent`](complex-mass-constituent-functional.lean)\ncarries this as two content fields, the winding-tower law and the light-doublet\nanchor, and the conditional theorem `charm_block_determined` shows the\ncharm block equals $\\mathrm{contRatio}(5)$ times the up block." },
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
