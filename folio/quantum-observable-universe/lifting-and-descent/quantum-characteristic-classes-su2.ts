import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-characteristic-classes",
  label: "ex:quantum-characteristic-classes-su2",
  title: "Quantum characteristic classes for $\\mathrm{SU}(2)$",
  tags: ["su2", "obstruction", "cohomology", "chern-class"],
  uses: ["def:quantum-characteristic-classes", "ex:recursive-brane-tower-su2"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**🟧 OWNER RULING 2026-09-15 settles the symbol: `tr(id_A)` is the quantum dimension `dim_q(A)`, the Euler characteristic of an object IN THE QOU CATEGORY — so it is q-DEPENDENT.** Consequence for this block: `chi_eu(CP^1) = 2` is a **topological** Euler characteristic, a different object from the categorical trace, so it does not compete with `lem:brings-euler-characteristic`'s -6 as a value of one quantity. What remains open is that the two apply the same `prop:euler-char-stability` bridge to **different S** — `SU(2)/U(1) = CP^1` here, the generic fibre taken as Bring's `Sigma_4` there — so at most one describes the Descartes universe's state bundle. Register entry in `notation/notation-collisions.md`; bean `qou-2uf0`.",
    },
  ],
});
