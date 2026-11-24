import { table } from "../../schema/builders";
export default table({
  label: "tbl:knot-operator-basis-table-table2-data",
  title: "Data table 2 from rem:knot-operator-basis-table",
  uses: ["rem:knot-operator-basis-table"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Owner ruling 2026-11-21 (docs/coordination/owner-rulings.md): the electron is σ₀σ₁σ₀ ∈ B₃, whose closure is the Hopf link. The operator was named T_{2,3} (trefoil) until then; it is renamed T_{2,2}^{(3)}. The word σ₀σ₁σ₀ and every entry are unchanged." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The full symbolic values of the elided entries are recorded in the computation witness `photon-operator-table.witness.json`." },
  ],
});
