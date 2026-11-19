import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:algebraic-geometric-dilog-equivalence",
  title:
    "Algebraic-geometric dilogarithm equivalence: $\\Phi_n(x; q)$ poles map to ideal-tetrahedron cusps",
  lean: {
    ref: "qou:QOU.QPochhammer.algebraic_geometric_equivalence",
    validation: "not_checked",
  },
  uses: [
    "conj:dilogarithm-archimedean-limit",
    "conj:binding-qbeta-complex-volume",
    "prop:phi-b-unitary-bar-odd",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "neumann-zagier1985",
    "thurston1978",
    "zagier1986",
  ],
  tags: [
    "q-pochhammer",
    "dilogarithm",
    "bloch-wigner",
    "kashaev",
    "phi-q",
    "algebraic-geometric",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: computations/q-pochhammer-seed.witness.json, computations/snappy-cusp-seeding.witness.json (snappy_cusp_seeding.py).",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_pochhammer_seed.py",
    witness: [
      "computations/q-pochhammer-seed.witness.json",
      "computations/snappy-cusp-seeding.witness.json",
      "computations/qbeta/qbeta-c3-muon-anchor-codata-edition-attribution.witness.json",
      "computations/qbeta/qbeta-c3-geometric-channel-q0star.witness.json",
    ],
    status: "verified",
  },
});
