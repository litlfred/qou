import { table } from "../../schema/builders";

/**
 * Reader-facing summary of Eightfold Way and first-generation Standard Model
 * multiplet derivation status (bean qou-intr). Grounded in
 * docs/audits/2026-11-27-8fold-sm-derivation-status.md,
 * QOU/EightfoldWay/NeutralLeptonFixesCharges.lean,
 * QOU/EightfoldWay/FermiPairWedge.lean,
 * QOU/EightfoldWay/StrandSlotSeparatesGen1.lean,
 * QOU/StandardModel/EvenStrandGeneration.lean, and
 * QOU/BringsSurface/EssentialSeparatingLeptonCount.lean.
 */
export default table({
  label: "tbl:intro-eightfold-status",
  title: "Derivation status of the Eightfold Way and first-generation multiplet structure",
  uses: [
    "chap:eightfold-way",
    "app:standard-model",
    "prop:neutral-lepton-fixes-charges",
    "prop:fermi-pair-wedge",
    "prop:even-strand-generation",
    "prop:strand-slot-separates-gen1",
  ],
  tags: ["introduction", "eightfold-way", "standard-model", "summary-table"],
});
