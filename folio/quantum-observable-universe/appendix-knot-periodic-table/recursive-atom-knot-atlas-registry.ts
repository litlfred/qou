import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-registry",
  title:
    "Atlas registry — canonical braid closures, confinement levels $\\ell = 0\\text{--}3$, and 3,558-nuclide synthesis",
  interprets: "prop:recursive-atom-knot-atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
    "prop:confinement-sdp",
    "prop:fermion-boson-knot-link",
  ],
  cites: ["wenzl1988"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_wave3_periodic_table_synthesis_probe.py",
    witness: [
      "computations/q-pinning-50-digit.witness.json",
      "computations/probes/h4-fulltwist-alpha-and-carbon12-groebner.witness.json",
      "computations/probes/second-order-gpmt-h12-carbon12-and-o16.witness.json",
      "computations/probes/nuclear-pairing-hoyle-and-actinide-deformation.witness.json",
      "computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json",
      "computations/catalan-binding.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "atlas",
    "registry",
    "atom-knot",
    "particle-registry",
    "q0",
    "braid-word",
    "markov-closure",
    "hyperbolic-knot",
    "per-element",
    "appendix",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body:
        "Consolidated to the zero-fitting Wave-3 3D simplicial + GPMT + Mayer-Jensen + Temperley-Lieb synthesis (`nuclear_wave3_periodic_table_synthesis_probe.py`), replacing the retired L4 Q-CLT per-Z dump that stopped at Z = 99.",
    },
  ],
});
