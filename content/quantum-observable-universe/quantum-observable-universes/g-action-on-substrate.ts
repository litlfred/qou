import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:g-action-on-substrate",
  title:
    "Categorical $G = \\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$ action on the Frobenius–Hopf substrate",
  lean: { ref: "qou:QOU.QuantumObservableUniverses.GActionOnSubstrate", validation: "stub" },
  uses: [
    "def:frobenius-hopf-substrate",
    "def:categorical-action",
    "rem:hecke-algebra-from-braiding",
  ],
  tags: [
    "tier:S",
    "g-action",
    "electroweak",
    "frobenius-hopf-substrate",
    "g-equivariance",
    "categorical-higgs",
    "n-sym",
    "open-problem",
  ],
  // The witness below provides the q_0 numerical anchor cited via
  // :val[q_0] in the body — it does NOT verify this conjecture
  // (which is tagged `open-problem`). Status reflects the
  // conjecture's open status, not the witness script's correctness.
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
    status: "not_run",
  },
  authorNotes: [
    {
      kind: "status",
      body: "**Open at the closure level.** The four axioms above are a\n**concrete framework extension** that takes the QOU substrate\nfrom \"$\\mathbf{Rep}(\\mathrm{SU}_q(2))$-equivariant\" to\n\"$G \\times \\mathbf{Rep}(\\mathrm{SU}_q(2))$-equivariant\", entailing\nthe closed form $\\mathcal{N}_{\\rm sym}(q) = [2]_q \\cdot [4]_q^2 \\cdot\n[6]_q$ that matches CODATA-derived target to 1.81%. Each factor is\n**categorically derived**, not fitted.\n\nThe remaining 1.81% is a SINGLE missing categorical input (one of\nthe three sources above); identifying it would close the audit\nflag NV-1 entirely.\n\n**To promote to `proposition`:**\n1. Resolve the 1.81% residual via one of the three open routes\n2. Provide the unique-existence argument for the four axioms\n3. Author the Lean formalization",
    },
  ],
});
