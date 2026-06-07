import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:double-magic-delta-i-bound",
  title:
    "Conjecture: Empirical double-magic isotopes satisfy $|\\Delta i| \\leq 1$ across Bring shell indices",
  lean: {
    ref: "qou:QOU.Interactions.DoubleMagicDeltaI.DeltaIBoundConjecture",
    validation: "not_checked",
  },
  uses: [
    "prop:diagrammatic-double-magic-lr-fusion",
    "prop:torus-knot-shell-binding",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/optimised_magic_verifier.py",
    witness:
      "folio-assistant/computations/optimised-magic-verifier.witness.json",
    status: "verified",
  },
  cites: [
    "mathas1999",
    "kassel1995",
  ],
  tags: [
    "tier:E",
    "double-magic",
    "lr-fusion",
    "bring-shell",
    "delta-i",
    "compatibility",
    "open-problem",
    "axiom-class",
  ],
});
