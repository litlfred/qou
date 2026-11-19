import { proof } from "../../schema/builders";

export default proof({
  label: "prf:parallel-fibre-noninteraction",
  title: "Proof of parallel fibre noninteraction",
  uses: ["prop:parallel-fibre-noninteraction"],
  authorNotes: [
    { kind: "note", body: "The Lean sibling proves all four properties over a generic commutative ring $R$; factorisation is definitional and commutativity uses only `propext`." },
  ],
});
