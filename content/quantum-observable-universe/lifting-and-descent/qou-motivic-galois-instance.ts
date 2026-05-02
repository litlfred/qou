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
    "def:habiro-ring",
    "def:motivic-substrate",
    "prop:full-pole-structure-mass-trace",
  ],
  cites: ["habiro2002", "yekutieli2010", "tate1967"],
  lean: {
    ref: "qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar",
    validation: "not_checked",
  },
});
