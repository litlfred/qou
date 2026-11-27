import { table } from "../../schema/builders";
export default table({ label: "tbl:braid-group-n-strand-table1-data", title: "Table 1 from rem:braid-group-n-strand", uses: ["rem:braid-group-n-strand"], tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): | Lean object | Role |\n|---|---|\n| `TypedCrossing n` | A single typed crossing: generator index $i \\in \\mathrm{Fin}(n-1)$ + sign $\\pm 1$ |\n| `BraidWord n` | List of typed crossings (the empty word is the identity braid) |\n| `BraidWord.writhe` | Net signed crossing count (algebraic) |\n| `closureN` | Markov closure to a `Link`, **opaque at general $n$**, concrete at $n=2$ via `closure2` |\n| `HeckeQuotient n q` | Class encoding the Hecke quadratic relation $\\sigma_i^2 = (q - q^{-1})\\sigma_i + 1$ |\n| `MarkovTraceN n q` | Generalised Markov-trace axioms M1-M4 (Jones 1985), inherits the 2-strand `MarkovTraceAxioms` |" },
  ],
});
