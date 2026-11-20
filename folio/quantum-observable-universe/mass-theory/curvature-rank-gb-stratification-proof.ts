import { proof } from "../../schema/builders";

export default proof({
  label: "prf:curvature-rank-gb-stratification",
  title: "Proof of curvature rank gb stratification",
  uses: ["prop:curvature-rank-gb-stratification"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > degree $0$, and cannot stratify anything. Proved as\n> `QOU.BraidKnot.WordFiltration.map_pow_eq_bot`." },
  ],
});
