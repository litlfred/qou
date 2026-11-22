import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:habiro-residue-sum-equivalence",
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Cross-validation infrastructure.** The check is run by\nthe formal derivation; output witness\n`markov-pipeline-cross-validation.witness.json` records:\n\n- Per-atom assertion `tr_M_at_q0_archimedean[atom]` with a relative\n  tolerance proportional to `AGREEMENT_RTOL = 1e-9`.\n- Diagnostic fields `realizer_value`, `term6_value`, `abs_diff`,\n  `rel_diff` for each common atom.\n- Asymmetric atom coverage (atoms present in only one input pipeline).\n\nThe validator skips when one of its inputs is absent (forward\ncompatibility), and uses the standard `WitnessBuilder` so\nthe formal derivation automatically reruns it whenever either input\nwitness changes." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the Lean formalization does not take it as a premise" },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Witness-certified axiom removed from Lean (owner decision, bean " +
        "`qou-uabo`).** The Lean sibling no longer carries " +
        "`protonExample_archimedean_agreement_axiom` or the `protonExample` " +
        "instance. That axiom equated an opaque integer polynomial evaluated " +
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
});
