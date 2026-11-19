import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:mass-identity",
  title: "Two-Term Categorical Lagrangian Trace and nucleon mass anchor",
  uses: [
    "prop:mass-identity-exists",
    "prop:mass-identity-unique",
    "thm:knot-mass-formula-unified",
    "prop:borromean-markov-trace-closed-form",
    "prop:em-coupling-bring-zero-mode",
    "prop:neutron-proton-splitting",
    "alg:bring-brane",
  ],
  cites: ["martelli2016"],
  tags: [
    "mba",
    "step-9a",
    "mass-identity",
    "two-term-lagrangian",
    "muon-anchor",
    "canonical-chain",
  ],
});
