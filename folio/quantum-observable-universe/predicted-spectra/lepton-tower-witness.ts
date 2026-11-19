import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:lepton-continuant-recurrence",
  label: "rem:lepton-tower-witness",
  title:
    "Numerical witness: NF tower for $T_{2,n}$, $n = 0 \\ldots 9$",
  tags: [
    "lepton",
    "witness",
    "computation",
    "continuant",
    "normal-form",
    "tau-lepton-nf",
  ],
  uses: ["prop:lepton-continuant-recurrence"],
  computation: {
    engine: "python",
    script: "computations/tau-lepton-nf.py",
    witness: "computations/tau-lepton-nf.witness.json",
    status: "verified",
  },
});
