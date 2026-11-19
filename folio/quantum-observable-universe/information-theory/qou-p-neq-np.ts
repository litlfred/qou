import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-p-neq-np",
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q \\in \\mathbb{G}_m$",
  lean: { ref: "qou:QOU.Information.QouPNeqNp", validation: "stub" },
  tags: [
    "tier:famous",
    "P-vs-NP",
    "Gm-torsion",
    "obstruction",
    "millennium-problem",
    "substrate-parameter",
    "computational-horizon",
  ],
  uses: [
    "conj:p-vs-np-boundary",
    "ex:chi-minus-six-derivation",
    "prf:qou-obstruction-reduction",
  ],
  cites: ["jaeger1990", "aharonov2009", "freedman2003", "cook1971"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "Earlier drafts stated the G_m-torsion dichotomy backwards.",
    },
    {
      kind: "note",
      body: "Lean formalisation: `QouPNeqNp` (`qou_implies_p_neq_np`, `PNeqNPInQOU`) carries faithfulness as a class hypothesis rather than an axiom or instance. Companion modules: `ObstructionGenericity` (`obstruction_vanishing_locus_finite`, `obstruction_nonvanishing_locus_infinite`); `PNeqNpEquivalence` (`ResidueFaithfulness`, `sound_of_residual_ne_zero`, `equivalence_collapse`, `chi_mod_vanishes_iff`, `nontorsion_of_one_lt`, `counting_sep_of_decision_sep`, `JonesComplexityCitations`, `counting_faithfulness`, `faithfulness_of_transfer`, `WenzlGeneric`, `wenzlGeneric_of_one_lt`, `counting_faithfulness_of_one_lt`, `WenzlCriterion`); `WenzlSchurElement` (`schurElement_ne_zero`, `SchurElementCriterion`, `semisimple_of_substrate`, `tl_numerator_eq_zero_iff`, `schurElement_tl_eq_zero_iff`, `substrate_avoids_tl_locus`); `QOU.Information.qou_physical_intractability_unconditional` (`superPoly_two_pow`); and `QOU.Information.SkeinObservationSystem` (`PolyObservable`).",
    },
  ],
});
