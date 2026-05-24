import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-form-a-n1-symbolic",
  lean: {
    ref: "qou:QOU.Interactions.q_beta_form_a_n1_symbolic",
    validation: "not_checked",
  },
  title:
    "$Q_\\beta$ Form A at brane-tower depth $N = 1$: symbolic closed form (geometric-series lift)",
  uses: [
    "prop:neutron-qvalue-symbolic",
    "prop:q-beta-spectral-bridge",
    "conj:brane-tower-z-habiro",
    "conj:archimedean-remainder-exponential-decay",
  ],
  cites: [
    "habiro2002",
    "wenzl1988",
  ],
  tags: [
    "q-beta",
    "form-a",
    "brane-tower",
    "n-equals-1",
    "symbolic",
    "geometric-series",
    "negative-finding",
    "lift-formula",
  ],
});
