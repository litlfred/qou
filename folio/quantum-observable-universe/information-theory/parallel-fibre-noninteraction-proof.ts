import { proof } from "../../schema/builders";

export default proof({
  label: "prf:parallel-fibre-noninteraction",
  title: "Proof of parallel fibre noninteraction",
  uses: ["prop:parallel-fibre-noninteraction"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling proves all four properties over a generic commutative ring $R$. The factorisation is definitional. Commutativity uses only $\\mathrm{propext}$." },
  ],
});
