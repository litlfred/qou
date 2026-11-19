import { proof } from "../../schema/builders";

export default proof({
  label: "prf:h2o-bond-angle-shift",
  title: "Proof of h2o bond angle shift",
  uses: ["prop:h2o-bond-angle-shift"],
  authorNotes: [
    {
      kind: "status",
      body: "Lean sibling proves the quadratic-completion inequality over R.",
    },
  ],
});
