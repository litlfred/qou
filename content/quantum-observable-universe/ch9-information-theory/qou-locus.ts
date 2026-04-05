import { definition } from "../../schema/builders";

export default definition({
  label: "def:qou-locus",
  lean: { decl: "QOU.MotivicIntegration.QOULocus", validation: "not_checked" },
  title: "QOU locus and axiom filtration",
  uses: [
    "def:qo-moduli",
    "def:quantum-observable-universe",
  ],
  tags: ["motivic-integration", "qou-locus", "definable", "axiom-filtration"],
});
