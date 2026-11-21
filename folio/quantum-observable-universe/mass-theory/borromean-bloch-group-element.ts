import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borromean-bloch-group-element",
  title:
    "Borromean rings represent a non-trivial element of $K_3(\\mathbb{C})$ / Bloch group with regulator $r_2 = 8G$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.BorromeanBlochGroupElement",
    validation: "not_checked",
  },
  uses: [
    "prop:vol-through-tau",
    "rem:vol-as-motivic-period",
    "conj:binding-scale-catalan",
    "conj:dilogarithm-archimedean-limit",
  ],
  cites: [
    "arxiv-2304.12545v1",
    "kirillov1995",
    "bloch2000",
    "neumann-zagier1985",
    "suslin1991",
    "zagier1986",
    "kashaev1997",
    "kegel2024",
  ],
  tags: [
    "bloch-group",
    "k-theory",
    "duality-d16",
    "borromean",
    "regulator",
    "k3-c",
    "motivic-period",
    "h4-closure-route",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "quantum-dilogarithm",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean axiomatisation (sketch)\n\n```lean\nclass BorromeanBlochGroupElement\n    (M : Type*) [BrCategory M] [QuantumDilogarithm M] where\n  /-- The Bloch-group element of the Borromean complement. -/\n  borromean_bloch_class : BlochGroup (Complex)\n  /-- It equals 8 · [i], the ζ₄ (octahedral) class. -/\n  borromean_bloch_eq_eight_xi :\n    borromean_bloch_class = 8 • bloch_symbol Complex.I\n  /-- The Beilinson regulator of the class equals 8G. -/\n  regulator_eq_eight_G : r_2 borromean_bloch_class = 8 * catalan_G\n  /-- The order-h² regulator correction equals -6G. -/\n  regulator_h2_correction : r_2_h2_correction borromean_bloch_class = -6 * catalan_G\n  /-- Equivalently, the h^4 Markov-trace coefficient = -3/4. -/\n  borromean_h4_coefficient_from_regulator :\n    markov_trace_h4_coefficient borromean_complement = -3/4\n```\n\n2. Closing the conjecture needs an instance of the class above, and the\n   `borromean_h4_coefficient_from_regulator` proof (which would\n   import a Bloch-Suslin lemma from Mathlib once available; per\n   `lean_loogle` search, $K_3$ formalisation is currently partial in\n   Mathlib)." },
  ],
});
