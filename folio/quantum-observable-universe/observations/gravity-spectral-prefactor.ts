import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gravity-spectral-prefactor",
  title:
    "Catalan's $G$ as the universal-residue prefactor of the unified mass formula",
  lean: {
    ref: "qou:QOU.Observations.gravity_spectral_prefactor",
    validation: "not_checked",
  },
  uses: ["prop:confinement-categorical"],
  tags: [
    "catalan-constant",
    "borromean-volume",
    "universal-residue",
    "plancherel",
    "macroscopic-stratum",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "deprecated",
      date: "2026-09-14",
      body:
        "**The Newton reading is withdrawn.** This block previously stated " +
        "$G$ to be Newton's gravitational constant in Planck units " +
        "($G_{\\mathrm{Planck}} = 1$), asserting the same formula " +
        "$\\alpha = m_e \\cdot 8G$ that " +
        "[`conj:binding-scale-catalan`](../mass-theory/binding-scale-catalan.md) " +
        "states with $G$ = Catalan's constant. The two readings give " +
        "$3.744459659941610$ MeV and $4.087991605520000$ MeV; the corpus's own " +
        "quoted value is $3.7445$ MeV, so the Catalan reading is the one " +
        "every consuming block uses, and the Newton reading was a glyph " +
        "collision rather than a second result. Newton's constant does not " +
        "appear anywhere in this repository: there is no witness, no producer, " +
        "and no CODATA comparison.",
      see: "conj:binding-scale-catalan",
    },
    {
      kind: "note",
      date: "2026-09-14",
      body:
        "The three critical `da-*` verdicts standing against this block since " +
        "2026-07-07 (`da-hidden-dof`, `da-empirical-fragility`, " +
        "`da-physical-implausibility`) read \"the factor of 8 appears " +
        "fitted\". Under the Catalan reading the 8 is **derived**: " +
        "$\\mathrm{Vol}(\\mathcal{B}_3)$ decomposes into two regular ideal " +
        "octahedra of volume $4G$ each. The watcher was right that " +
        "\"Newton's $G$, times 8\" was unmotivated, and the motivation it " +
        "could not see is hyperbolic geometry rather than a fit. Re-queue " +
        "those three criteria against this revision.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/catalan_binding.py",
    witness: [
      "computations/catalan-binding.witness.json",
      "computations/probes/pentagon-rt-torus-knot-higgs-probe.witness.json",
    ],
    status: "verified",
  },
});
