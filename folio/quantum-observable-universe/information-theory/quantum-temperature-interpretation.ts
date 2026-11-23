import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-temperature",
  label: "rem:quantum-temperature-interpretation",
  title: "Temperature as tick rate and surface quantity",
  tags: [
    "temperature",
    "reeb-flow",
    "holographic",
    "non-abelian-stokes",
    "classical-limit",
  ],
  uses: ["def:quantum-temperature"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-23",
      body:
        "The second principle previously said non-degeneracy of the Frobenius pairing makes internal degrees of freedom fully determined by boundary data (a holographic principle). Non-degeneracy gives no such bound, and since the 2026-11-22 ruling (owner-rulings row 104) the pairing is not carried by the tower levels above n = 0. The sentence is rescoped to what is proved.",
    },
  ],
});
