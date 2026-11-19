import { proof } from "../../schema/builders";

export default proof({
  label: "prf:baryon-product-from-alt",
  title: "Proof of baryon product from alt",
  uses: ["prop:baryon-product-from-alt"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/probes/bring-cubic-monodromy-probe.witness.json.",
    },
  ],
});
