import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "status", date: "2026-09-04", body: "Open computation 2 (the weak vertex form factor) is now derived: $\\mathcal{W}(q) = q^2(q^{12}+q^8-1)/(q^2+1)^2$ under the canonical Markov trace (Lean `QOU.Braiding.WeakVertexT35.weakVertexTrace_eq`, witness `weak-vertex-t35-trace`). The item is re-scoped to what remains open — wiring $|\\mathcal{W}|^2$ into the half-life tables in place of $s^2$ and measuring the heavy-nucleus residual — rather than removed. Beans `qou-egvf`, `qou-4x7c`." },
    { kind: "note", date: "2026-11-19", body: "Formalization provenance moved from prose: the Gram constant $\\kappa$ in the conjectural Chern–Simons correction (`rem:em-coupling-chern-simons`) was carried as an unproved Lean `sorry`." },
  ],
  interprets: "prop:hadron-half-life",
  label: "rem:hadron-half-life-fermi",
  title: "Fermi-constant relation, $q$-dependence, and parameter count",
  uses: ["prop:hadron-half-life", "prop:em-coupling-projection"],
});
