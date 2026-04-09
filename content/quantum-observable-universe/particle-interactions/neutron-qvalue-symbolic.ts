import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:neutron-qvalue-symbolic",
  title: "Symbolic $Q$-value of free neutron decay",
  uses: [
    "def:typed-crossing-operator",
    "rem:calibration-inputs",
    "rem:energy-scale-planck",
    "prop:categorical-mass-markov",
  ],
  tags: [
    "beta-decay",
    "q-value",
    "symbolic",
    "neutron",
    "typed-crossing",
    "prediction",
  ],
});
