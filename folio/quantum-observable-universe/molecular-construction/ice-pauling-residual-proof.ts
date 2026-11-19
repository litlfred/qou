import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ice-pauling-residual",
  title: "Proof of ice pauling residual",
  uses: ["prop:ice-pauling-residual"],
  authorNotes: [
    {
      kind: "status",
      body: "Lean sibling proves C(4,2) = 6 and C(4,2) * (1/2)^2 = 3/2 over Q.",
    },
  ],
});
