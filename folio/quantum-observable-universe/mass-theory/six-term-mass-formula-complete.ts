import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:six-term-mass-formula-complete",
  title:
    "Six-term mass formula: derivation + computation index",
  lean: {
    ref: "qou:QOU.BraidKnot.six_term_mass_formula_complete",
    validation: "not_checked",
  },
  uses: [
    "conj:terms-2-6-higher-operations",
    "prop:chirality-writhe-ribbon-derivation",
  ],
  computation: {
    engine: "sympy",
    script: "computations/term6_residues_at_roots.py",
    witness: "computations/term6-residues-at-roots.witness.json",
    consumers: [
      "computations/term6_habiro_residue_mpfr_50dps_bridge.py",
    ],
    status: "verified",
  },
  tags: [
    "mass-formula",
    "six-term",
    "master-index",
    "completeness",
    "derivation-status",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
