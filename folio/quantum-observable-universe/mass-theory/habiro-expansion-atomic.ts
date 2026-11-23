import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:habiro-expansion-atomic",
  title: "Atomic-braid Habiro expansion: integrality and termination",
  uses: ["prop:full-pole-structure-mass-trace"],
  tags: [
    "habiro-ring",
    "cyclotomic-expansion",
    "markov-trace",
    "atomic-braid",
    "integrality",
    "termination",
  ],
  cites: ["habiro2002", "kassel1995", "jones1987", "garoufalidis-kashaev-descendants2023"],
  lean: {
    ref: "qou:QOU.BraidKnot.habiro_expansion_atomic",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/probes/habiro_expansion_atomic_probe.py",
    witness: "computations/probes/habiro-expansion-atomic-probe.witness.json",
    status: "verified",
  },
});
