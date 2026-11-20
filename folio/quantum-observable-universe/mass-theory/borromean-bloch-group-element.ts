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
    "bloch2000",
    "neumann-zagier1985",
    "suslin1991",
    "zagier1986",
    "kashaev1997",
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
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): sketched as `class BorromeanBlochGroupElement (M) [BrCategory M] [QuantumDilogarithm M]` with fields `borromean_bloch_class`, `borromean_bloch_eq_eight_xi`, `regulator_eq_eight_G`, `regulator_h2_correction`, `borromean_h4_coefficient_from_regulator`.",
    },
  ],
});
