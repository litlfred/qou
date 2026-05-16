import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-plancherel-asymptotic-skeleton",
  title:
    "Asymptotic skeleton of the q-Plancherel measure $\\tilde w_\\lambda$ — convergence on a continuous Young-diagram space",
  lean: {
    ref: "qou:QOU.Observations.QPlancherelAsymptoticSkeleton",
    validation: "not_checked",
  },
  uses: [
    "prop:wedderburn-weight-canonical",
    "prop:plancherel-term-7-formulation",
  ],
  cites: [
    "kerov1981",
    "biane1998",
    "feray2010",
  ],
  tags: [
    "causal-fermion-systems",
    "plancherel",
    "asymptotic-plancherel",
    "kerov-vershik",
    "wedderburn-weight",
    "thoma-simplex",
    "partly-established",
  ],
});
