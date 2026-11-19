import { proof } from "../../schema/builders";

export default proof({
  label: "prf:lepton-continuant-recurrence",
  title: "Proof of lepton continuant recurrence",
  uses: ["prop:lepton-continuant-recurrence"],
  computation: {
    engine: "python+mpmath",
    script: "computations/substrate/frakV_askey_wilson_recurrence_tie_probe.py",
    witness: "computations/substrate/frakV-askey-wilson-recurrence-tie-probe.witness.json",
    status: "verified",
  },
});
