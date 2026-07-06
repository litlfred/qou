import { definition } from "../../schema/builders";

export default definition({
  label: "def:qou-motivic-galois-instance",
  title:
    "QOU $\\mathrm{MotivicGaloisCharacter}$ instance via Habiro $\\to \\mathrm{Frob}_p$",
  tags: [
    "motivic-galois",
    "frobenius",
    "habiro",
    "qou-substrate",
    "instance",
    "axiom",
  ],
  uses: [
    "def:motivic-galois-character",
  ],
  cites: ["habiro2002", "yekutieli2010", "tate1967"],
  computation: {
    engine: "python",
    script: "computations/probes/habiro_frobenius_probe.py",
    witness:
      "computations/probes/habiro-frobenius-probe.witness.json",
    status: "verified",
  },
  lean: {
    ref: "qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar",
    validation: "not_checked",
  },
});
