import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mu-arch-continuum-limit",
  title:
    "Archimedean lift $\\mu_{\\mathrm{arch}}$: $\\tilde w_\\lambda$ converges to a Finster universal measure under joint Faddeev scaling",
  lean: {
    ref: "qou:QOU.Observations.MuArchContinuumLimit",
    validation: "not_checked",
  },
  uses: [
    "prop:algebraic-causal-action-structure",
    "conj:dilogarithm-archimedean-limit",
    "def:archimedean-realization-functor",
  ],
  cites: [
    "finster2021",
    "finster2024",
    "kerov1981",
    "biane1998",
    "feray2010",
  ],
  tags: [
    "causal-fermion-systems",
    "archimedean-realization",
    "asymptotic-plancherel",
    "kerov-vershik",
    "free-probability",
    "conjecture",
    "open-question",
  ],
});
