import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:archimedean-remainder-exponential-decay",
  title:
    "Exponential decay of the archimedean brane-tower truncation remainder",
  lean: {
    ref: "qou:QOU.Interactions.ArchimedeanRemainderExponentialDecay",
    validation: "not_checked",
  },
  uses: [
    "prop:neutron-qvalue-symbolic",
  ],
  cites: [
    "jones1985",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/c_k_beta_decay_witness.py",
    witness: "computations/c-k-beta-decay-bound.witness.json",
    status: "verified",
  },
  tags: [
    "tier:primary-conjecture",
    "q-beta",
    "brane-tower",
    "truncation-remainder",
    "exponential-decay",
    "archimedean",
    "beta-decay",
  ],
});
