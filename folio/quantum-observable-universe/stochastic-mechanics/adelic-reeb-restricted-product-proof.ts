import { proof } from "../../schema/builders";

export default proof({
  label: "prf:adelic-reeb-restricted-product",
  title: "Proof of adelic reeb restricted product",
  uses: ["prop:adelic-reeb-restricted-product"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Proof.** Both parts are proved formally over the abstract value group\n$\\Gamma$ in\n[`adelic-reeb-restricted-product.lean`](adelic-reeb-restricted-product.lean).\n\nThe squeeze\n is `Finset.sum_lt_sum`: a finite sum of\n\n(formalised in Lean as a linearly ordered abelian group:\n`AddCommGroup` $+$ `LinearOrder` $+$ `IsOrderedCancelAddMonoid`)" },
  ],
});
