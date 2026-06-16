import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:rigid-monoidal-structural-gap-invariance",
  title:
    "Convention-independence of the structural gap: the brane-tower factors through the rigid monoidal Markov trace on the Type-B-folded Hecke category",
  lean: {
    ref: "qou:QOU.BraidKnot.RigidMonoidalStructuralGapInvariance",
    validation: "not_checked",
  },
  uses: [
    "prop:spin-involution-lp-dual-invariance",
    "conj:brane-tower-z-habiro",
  ],
  computation: {
    engine: "python",
    script: "computations/rigid_monoidal_gap_invariance_check.py",
    witness: "computations/rigid-monoidal-gap-invariance.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-12",
      body: [
        "Witness producer re-pointed from `lp-duality-check.py` to `rigid_monoidal_gap_invariance_check.py`.",
        "",
        "The prior producer asserted tr_M(s0 s1 s0) = z^3 via an invalid Markov-move chain (the M2 peel requires the maximal generator to appear exactly once; in s1 s0 s1 it appears twice), contradicting the corrected pyhecke `TR_M[5] = h z^2 + z` (fix commit be773569; 2026-05-19 deprecated-scripts catalog). Its upstream witnesses (`confinement-lp.witness.json`, `breit-wheeler-nucleon-nf.witness.json`) were retired to `_deprecated/`.",
        "",
        "The replacement probe verifies the proposition's convention-invariance claim directly: two structurally independent fully-symbolic routes (NF-algebra right-multiplication table vs Markov-axiom derivation) agree symbolically and at q_0 to 1e-40, including the corrected h z^2 + z trace, with a regression guard asserting the superseded z^3 value is detectably distinct.",
      ].join("\n"),
    },
  ],
  tags: [
    "rigid-monoidal",
    "type-b-folding",
    "kashiwara-crystal",
    "structural-gap",
    "convention-invariance",
    "categorical-unification",
  ],
});
