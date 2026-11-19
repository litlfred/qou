import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:schur-weyl-mass-decomposition",
  label: "rem:bw-mass-decomposition-dictionary",
  title:
    "Empirical Bethe–Weizsäcker terms as Schur–Weyl strata",
  tags: [
    "bethe-weizsacker",
    "schur-weyl",
    "mass-formula",
    "dictionary",
    "nuclear-physics",
    "interpretation",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Crossing-count identities formalised in `QOU.MassTheory.CoulombFromCrossingCounts` and `QOU.MassTheory.CrossingCountAffine`; shell-closure selection principle tracked in `conj:homological-shell-condensation`.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_spin_orbit_shells_and_symmetry_probe.py",
    witness: "computations/probes/nuclear-spin-orbit-shells-and-symmetry.witness.json",
    status: "verified",
  },
});
