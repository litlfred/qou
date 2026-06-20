import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-mass-trace",
  title: "Mass via the Markov trace of the Hecke mass element",
  tags: [
    "hecke-algebra",
    "mass",
    "markov-trace",
    "fibre-functor",
    "topological-decomposition",
  ],
  lean: { ref: "qou:QOU.Braiding.hecke_mass_trace",
    validation: "not_checked",
  },
  uses: ["def:hecke-mass-element"],
  // Production wiring of the proved mass = Markov-trace bridge: the canonical
  // mass table computes |tr_M(Φ_mass(β))| per atom via the canonical Markov
  // trace (compute_tr_m_canonical → Rust MPFR kernel), realising the
  // proposition's |tr_M(Φ_mass)| object in production. The categorical FORM
  // (m = |tr_M|) is the proved content; the archimedean MeV evaluation for
  // composites relies on the documented vol-density / Borromean machinery
  // (see docs/audits/2026-06-20-wire-proved-mass-binding-into-production.md).
  computation: {
    engine: "python",
    script: "computations/canonical_mass_table_extended.py",
    witness: "computations/canonical-mass-table-extended.witness.json",
    status: "verified",
    requires: ["pyhecke_native"],
  },
});
