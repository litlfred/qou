import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bar-self-dual-confinement-band",
  title: "Proof of bar self dual confinement band",
  uses: ["prop:bar-self-dual-confinement-band"],
  computation: {
    engine: "sympy",
    script: "computations/qbeta/qbeta_bar_parity_of_the_decay_trace_probe.py",
    witness: "computations/qbeta/qbeta-bar-parity-of-the-decay-trace.witness.json",
    status: "verified",
  },
});
