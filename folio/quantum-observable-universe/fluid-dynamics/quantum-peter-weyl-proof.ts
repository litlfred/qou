import { proof } from "../../schema/builders";

export default proof({
  label: "prf:quantum-peter-weyl",
  title: "Proof of quantum peter weyl",
  uses: ["thm:quantum-peter-weyl"],
  authorNotes: [
    {
      kind: "note",
      body: "Step 1 snake identities correspond to `pairing_snake_left` and `pairing_snake_right`.",
    },
  ],
});
