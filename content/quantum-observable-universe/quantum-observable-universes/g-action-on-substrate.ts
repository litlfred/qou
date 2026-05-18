import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:g-action-on-substrate",
  title:
    "Categorical $G = \\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$ action on the Frobenius–Hopf substrate",
  uses: [
    "def:frobenius-hopf-substrate",
    "def:rigid-monoidal-category",
    "def:categorical-action",
    "rem:hecke-algebra-from-braiding",
    "conj:categorical-higgs-idempotent",
  ],
  tags: [
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
});
