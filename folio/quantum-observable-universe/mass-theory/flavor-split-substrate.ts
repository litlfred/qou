import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:flavor-split-substrate",
  lean: { ref: "qou:QOU.HadronicMass.flavor_split_substrate",
    validation: "not_checked",
  },
  title: "Closed and factored forms of the substrate flavor split",
  tags: ["flavor-split", "u-d-splitting", "substrate-only", "no-fit",
         "hecke-substrate-atoms", "categorical-derivation"],
  uses: [
    "lem:pair-skein-mass-formula",
  ],
  computation: {
    engine: "python",
    script: "computations/probes/flavor_split_substrate_probe.py",
    witness: "computations/probes/flavor-split-substrate-probe.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
  proofs: ["prf:flavor-split-substrate"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the cross-chapter reading-order drain (L4; the block moved from observations to mass-theory and this sentence would now point ahead): A companion proposition ([Substrate-pure derivation of the dressed-quark mass splitting](#prop:flavor-dressed-mass-from-substrate-split)) recovers the dressed-mass difference $\\mu_{\\mathfrak{d}} - \\mu_{\\mathfrak{u}} \\approx 1.288\\,\\text{MeV}$, conditional on `conj:flavor-split-substrate-mass`." },
  ],
});
