import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-graded-markov-trace-existence",
  title:
    "Existence of the graded Markov trace on the GS filtration (categorical existence)",
  lean: {
    ref: "qou:QOU.IwahoriHecke.MarkovTrace.GradedMarkovTraceExistence",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:graded-markov-trace-from-gs-filtration",
    "thm:jones-markov-trace",
  ],
  computation: {
    engine: "python",
    script: "computations/markov/markov_pipeline_cross_validator.py",
    witness:
      "computations/markov/markov-pipeline-cross-validation.witness.json",
    status: "verified",
    // Round trip, 2026-08-23 (bean `qou-bm4i`): "verified" -> "failed" -> back.
    // The witness genuinely did not all-pass, but the failure was staleness on
    // BOTH sides of the cross-validation, not a mathematical disagreement:
    // markov_substrate_realizer's witness was 7 weeks old and carried a MUON
    // q_0 at ~12 digits, term6's went through `float(complex(sp.N(...)))` on a
    // float64 `q_parameter.Q`. With both producers on `Q_50_DIGIT_STR` and mpf
    // end to end they agree byte-for-byte at 60 digits, rel_diff exactly 0.
  },
  tags: [
    "tier:keystone",
    "gs-filtration",
    "spectral-sequence",
    "graded-trace",
    "markov-trace",
    "noncomputable-opaque",
    "closure-tier-b",
    "phase-2-sprint-4-discharge",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean encoding.** In `gb-residue-spectral-sum.lean`, this is encoded as the abstract class field `gradedTrace : Fin levelBound → ℝ` on `GBResidueSpectralSum`. Each atomic instance supplies its per-level values. Constructing a fully verifiable `def` requires Mathlib infrastructure for filtered algebras and remains tracked downstream.\n\n\n\nPromoting the formal Lean counterpart to a theorem requires formalising $\\mathrm{ConfinementLevel}$, constructing" },
  ],
});
