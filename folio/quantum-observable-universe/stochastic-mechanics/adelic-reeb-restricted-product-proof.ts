import { proof } from "../../schema/builders";

export default proof({
  label: "prf:adelic-reeb-restricted-product",
  title: "Proof of adelic reeb restricted product",
  uses: ["prop:adelic-reeb-restricted-product"],
  authorNotes: [
    {
      kind: "status",
      body: "Formalised in `adelic-reeb-restricted-product.lean` (`adelic_reeb_order_additive`, `adelic_reeb_squeeze_local_to_global` via `Finset.sum_lt_sum` over `AddCommGroup` + `LinearOrder` + `IsOrderedCancelAddMonoid`).",
    },
  ],
});
