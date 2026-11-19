import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-residue-sum-equivalence",
  authorNotes: [
    {
      kind: "note",
      body: "Computational cross-validation witness: markov-pipeline-cross-validation.witness.json.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Witness-certified axiom removed from Lean (owner decision, bean " +
        "`qou-uabo`).** The Lean sibling no longer carries " +
        "`protonExample_archimedean_agreement_axiom` or the `protonExample` " +
        "instance. That axiom equated an opaque integer polynomial evaluated " +
        /* <!-- literal-source: retired axiom decimal quoted in removal history note --> */
        "at `√q₀` with the decimal `2.1225825095` read from a Python witness, " +
        "i.e. it put a witness-certified number into a formal premise. The " +
        "proton identity " +
        "stays open in `conj:gs-archimedean-agreement-residue` (no instance); " +
        "the cross-pipeline numerical agreement stays in this block's table.",
    },
  ],
  title:
    "Habiro completion ≡ Gröbner–Shirshov residue spectral sum (equivalence)",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroResidueSumEquivalence",
    validation: "not_checked",
  },
  uses: ["prop:full-pole-structure-mass-trace"],
  cites: ["habiro2004", "jones1987"],
  tags: [
    "habiro-ring",
    "cyclotomic-completion",
    "markov-trace",
    "residue",
    "spectral-sequence",
    "equivalence",
    "computational-witness",
  ],
  computation: {
    engine: "python",
    script: "computations/markov/markov_pipeline_cross_validator.py",
    witness: "computations/markov/markov-pipeline-cross-validation.witness.json",
    status: "verified",
  },
});
