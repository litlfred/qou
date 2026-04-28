import { definition } from "../../schema/builders";

export default definition({
  label: "def:hyperelliptic-quintic",
  lean: { ref: "qou:QOU.HyperellipticQuintic", validation: "not_checked" },
  title: "The hyperelliptic quintic $\\mathcal{X}_5 \\colon y^2 = x^5 - 1$",
  tags: ["hyperelliptic", "genus-2", "bolza", "roots-of-unity"],
  uses: ["prop:lagrange-resolvent-transform"],
});
