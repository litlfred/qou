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
    "conj:diagrammatic-double-magic-lr-fusion",
    "prop:torus-knot-shell-binding",
  ],
  computation: {
    engine: "python",
    script: "computations/optimised_magic_verifier.py",
    witness:
      "computations/optimised-magic-verifier.witness.json",
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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The conjecture is axiomatised as a Lean class. The algebraic-primality verifier ([`sdp-primality-verifier-spec.md`](../../../computations/sdp-primality-verifier-spec.md)). Empirical tests on small-$n$ pairs via `optimised_magic_verifier.py` measure an approximate $16\\times$ speedup." },
  ],
});
