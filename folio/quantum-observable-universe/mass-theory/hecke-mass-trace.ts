import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hecke-mass-trace",
  title: "Mass via the Markov trace of the Hecke mass element",
  tags: [
    "hecke-algebra",
    "mass",
    "markov-trace",
    "fibre-functor",
    "topological-decomposition",
  ],
  lean: { ref: "qou:QOU.Braiding.HeckeMassTraceContext",
    validation: "not_checked",
  },
  uses: [
    // def:mass-identity is NOT listed although the statement names it (the
    // categorical mass it equates with the trace norm): it is reached
    // through def:hecke-mass-element, which now declares it directly.
    "def:hecke-mass-element",
    // The decomposition the proposition descends to H_n(R, q).
    "conj:topological-mass",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "Demoted from `prop:hecke-mass-trace` (owner ruling 1(a), 2026-11-20, PR #8526 comment 7041693067; bean qou-tm3c). The block cites the topological decomposition of mass, which became [conj:topological-mass](#conj:topological-mass) in #8555. The argument [rem:hecke-mass-trace-sketch](#rem:hecke-mass-trace-sketch) also asserts, without proof, that the fibre functor preserves the norm. The trace-level split $\\mathrm{tr}_M(\\Phi_{\\mathrm{mass}}) = \\mathrm{tr}_M(\\Phi^{\\mathrm{desc}}) + \\sum_i \\mathrm{tr}_M(\\Phi^{\\mathrm{trans}}_i)$ needs only linearity of $\\mathrm{tr}_M$ once the element splits. It is proved in `QOU.Braiding.trace_split_of_phi_split`.",
    },
  ],
  // Production wiring of the conjectured mass = Markov-trace bridge: the
  // canonical mass table computes |tr_M(Φ_mass(β))| per atom via the canonical
  // Markov trace (compute_tr_m_canonical → Rust MPFR kernel), realising the
  // |tr_M(Φ_mass)| object in production. The categorical FORM (m = |tr_M|) is
  // the conjecture, not a proved result (owner ruling 2026-11-20, bean
  // qou-tm3c); the archimedean MeV evaluation for
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
