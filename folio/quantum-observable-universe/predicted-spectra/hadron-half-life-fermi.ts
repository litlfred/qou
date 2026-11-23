import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Two-term ruling (owner card, 2026-11-21 13:30Z; ledger docs/coordination/owner-rulings.md): the two-term Lagrangian trace covers the beta-decay half-life rate. Open computation 2 now names W_2 = t_1 + c_em t_2." },
    { kind: "status", date: "2026-09-04", body: "Open computation 2 (the weak vertex form factor) is now derived: $\\mathcal{W}(q) = q^2(q^{12}+q^8-1)/(q^2+1)^2$ under the canonical Markov trace (Lean `QOU.Braiding.WeakVertexT35.weakVertexTrace_eq`, witness `weak-vertex-t35-trace`). The item is re-scoped to what remains open — wiring $|\\mathcal{W}|^2$ into the half-life tables in place of $s^2$ and measuring the heavy-nucleus residual — rather than removed. Beans `qou-egvf`, `qou-4x7c`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The electron mass is $m_e = 3\\mathfrak{E}_{\\times}(q) \\cdot \\mu_0$ ([building blocks](#rem:building-block-knots))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This is now derived: $\\mathcal{W}(q) = q^2(q^{12} + q^8 - 1)/(q^2+1)^2$ under the canonical trace, with $\\mathcal{W}(q_0) \\approx 1.1875$ and $\\mathcal{W}(1) = 1/4$ ([verification](#ex:hadron-half-life-verification))." },
  ],
  interprets: "prop:hadron-half-life",
  label: "rem:hadron-half-life-fermi",
  title: "Fermi-constant relation, $q$-dependence, and parameter count",
  uses: ["prop:hadron-half-life", "prop:em-coupling-projection"],
});
